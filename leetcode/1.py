def solve():
    target = int(input())
    n = int(input())
    coefficients = list(map(int, input().split()))
    total_sum = sum(coefficients)
    if (total_sum + target) % 2 != 0 or total_sum < target:
        return "0"
    k = (total_sum + target) // 2
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(k, coefficients[i] - 1, -1):
            dp[j] += dp[j - coefficients[i]]
    return f"{dp[k]}"


if __name__ == "__main__":
    t = int(input())
    for test_case in range(t):
        print(solve(), end="" if test_case == t - 1 else "\n")