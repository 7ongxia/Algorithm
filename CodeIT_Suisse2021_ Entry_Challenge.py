import json
from sys import argv
from datetime import datetime, timedelta


def get_next_time(roboRate, currentTime, endTime):
  # Set variables
  standardOrExtra = None
  nextWeek = currentTime
  nextTime = currentTime
  answer = None
  today = {
    'day': 'weekday',
    'time': 'night'
  }

  # Find next weekday or weekend
  if nextWeek.isoweekday() in set((6, 7)):
    nextWeek += timedelta(days = 8 - nextWeek.isoweekday())
    standardOrExtra = 'extraDay'
    today['day'] = 'weekend'
  else:
    nextWeek += timedelta((6-nextWeek.isoweekday()) % 8)
    standardOrExtra = 'standardDay'
  nextWeek = datetime.combine(nextWeek, datetime.min.time())

  # Find next day or night
  DayStart = datetime.strptime(roboRate[f"{standardOrExtra}"]['start'], '%H:%M:%S').time()
  DayEnd = datetime.strptime(roboRate[f"{standardOrExtra}"]['end'], '%H:%M:%S').time()
  if nextTime.time() < DayStart:
    nextTime = datetime.combine(nextTime, DayStart)
  elif nextTime.time() < DayEnd:
    nextTime = datetime.combine(nextTime, DayEnd)
    today['time'] = 'day'
  else:
    nextTime = datetime.combine(nextTime, DayStart)
    nextTime += timedelta(days = 1)
  
  # Get earlier one
  answer = nextTime
  if nextWeek < nextTime:
    answer = nextWeek
  if endTime < answer:
    answer = endTime
  return answer, today


# Find the next time to break
def get_next_break(currentTime, noBreakWorkTime):
  timeLeft = 8 * 60 - noBreakWorkTime
  currentTime += timedelta(minutes = timeLeft)
  
  return currentTime


if __name__ == '__main__':
  # command sample:
  # python3 main.py "{\"shift\": {\"start\": \"2038-01-01T20:15:00\",\"end\": \"2038-01-02T05:16:00\" }, \"roboRate\": {\"standardDay\": { \"start\": \"07:00:00\", \"end\": \"23:00:00\", \"value\": 20},\"standardNight\": { \"start\": \"23:00:00\", \"end\": \"07:00:00\", \"value\": 25},\"extraDay\": { \"start\": \"07:00:00\", \"end\": \"23:00:00\", \"value\": 30},\"extraNight\": { \"start\": \"23:00:00\", \"end\": \"07:00:00\", \"value\": 35}}}"

  # Get data from Json input
  try:
    temp = argv[1]
  except IndexError:
    print("@@@ Input(Json) for 'shift' and 'roboRate' is required @@@")
    exit()
  data = json.loads(argv[1])
  shift = data['shift']
  roboRate = data['roboRate']

  # Set variables
  currentTime = datetime.fromisoformat(shift['start'])
  endTime = datetime.fromisoformat(shift['end'])
  nextTime = None
  workTime = None
  timeInfo = None
  nextBreakTime = None
  hadBreak = None
  noBreakWorkTime = 0
  salary = 0

  # Calculate the rate
  while currentTime < endTime:
    hadBreak = False
    nextBreakTime = get_next_break(currentTime, noBreakWorkTime)
    nextTime, timeInfo = get_next_time(roboRate, currentTime, endTime)

    # Check whether the time is to break or not
    if nextBreakTime <= nextTime:
      nextTime = nextBreakTime
      hadBreak = True

    # Calculate the working time in a minute
    workTime = (nextTime - currentTime).seconds / 60
    noBreakWorkTime += workTime

    # Calculate cumulative working time
    if timeInfo['day'] == 'weekday':
      if timeInfo['time'] == 'day':
        salary += workTime * roboRate['standardDay']['value']
      else:
        salary += workTime * roboRate['standardNight']['value']
    else:
      if timeInfo['time'] == 'day':
        salary += workTime * roboRate['extraDay']['value']
      else:
        salary += workTime * roboRate['extraNight']['value']

    # Move current time
    currentTime = nextTime
    if hadBreak:
      noBreakWorkTime = 0
      currentTime += timedelta(hours = 1)

  # Output the expected value
  salary = int(salary)
  print(salary)