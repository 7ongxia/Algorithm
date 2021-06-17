n = int(input())
dp = [None, ["()"], None, None, None, None, None, None, None]

def generateParentheses(n):
    if dp[n]:
        return dp[n]

    answer = []

    for i in range(1, int(n/2)+1):
        aList = dp[i]
        if aList is None:
            aList = generateParentheses(i)
        bList = dp[n-i]
        if bList is None:
            bList = generateParentheses(n-i)

        for a in aList:
            for b in bList:
                answer.append(a+b)
                answer.append(b+a)

    patterns = dp[n-1]
    if patterns is None:
        patterns = generateParentheses(n-1)

    for pattern in patterns:
        answer.append("("+pattern+")")
    
    dp[n] = list(dict.fromkeys(answer))
    dp[n].sort()
    return dp[n]

print(generateParentheses(n))
