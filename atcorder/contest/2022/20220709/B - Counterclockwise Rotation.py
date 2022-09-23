import math
a,b,d= map(int, input().split())
d = math.radians(d)

print(a * math.cos(d) - b * math.sin(d),a * math.sin(d) + b * math.cos(d))



# 回転行列
#  (acosθ−bsinθ,asinθ+bcosθ) 


# https://atcoder.jp/contests/abc259/tasks/abc259_b
# もしかすると、こういうことですか？

# 例えば、円を中心点Ｃ(ａ，ｂ)、半径ｒとすると、
# 円の方程式は、(ｘ－ａ)^2＋(ｙ－ｂ)^2=ｒ^2なります。
# この円周上に点Pがあるとします。

# 点Ｃを通りｘ軸と平行な直線とCPの角度をθとすると、
# 点Ｐの座標値は、(ａ＋ｒ*cosθ，ｂ＋ｒ*sinθ)となります。