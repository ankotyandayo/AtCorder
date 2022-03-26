import math


def lcm(x, y):
    return (x*y) // math.gcd(x, y)


N, K = map(int, input().split())
print(lcm(N, K))
# https: // atcoder.jp/contests/abc148/tasks/abc148_c
# 最小公倍数を求める

# 最大公約数 = greatest common divisor
# 最大公約数 = least common multiple
