X, K, D = map(int, input().split())

X = abs(X)

if 0 < X-K*D:
    print(abs(X-K*D))

else:
    move_count = K-X//D

    jump_before = X-D*(X//D)
    jump_after = jump_before-D

    if move_count % 2 == 0:
        print(abs(jump_before))
    else:
        print(abs(jump_after))


# https://atcoder.jp/contests/abc175/tasks/abc175_c
# 入力
# 6 2 4
# 出力
# 2
