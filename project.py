print("----------그래프 자동 그리기----------")

some = input("도움말\n1)사용법\n2)제작자")
if some == "1)" or "1":
  print("이차함수 및 일차함수: ex)x^2+2*x-3 \n 지수함수: ex)x^2 + exp(x) \n 로그함수: x^2 + log(x)")
elif some == "2)" or "2" :
  print("이유찬")

#%%
reqast = input("그리실 함수 식을 입력하세요: ")
reqast = reqast.replace("^","**")

from sympy import *
import sympy as sy

x = sy.symbols('x')
fx = parse_expr(reqast)
plot(fx)

# %%