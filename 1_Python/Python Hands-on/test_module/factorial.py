def factorial(num, memo={}):
    if num in memo:
        return memo[num]
    elif num == 1 or num == 0:
        memo[num] = 1
    else:
        memo[num] = num * factorial(num-1, memo)
    return memo[num]