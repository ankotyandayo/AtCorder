x = int(input())
h = 21 if x < 60 else 22;
m = x % 60
print('{}:{:02}'.format(h, m))

# formatの:より後ろは書式,今回は2桁ってこと　:より前はインデックス

# https://atcoder.jp/contests/abc258/tasks/abc258_a