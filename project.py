print("----------그래프 자동 그리기----------")

some = input("도움말\n1)사용법\n2)제작자:")
if some == "1)" or "1":
  print("이차함수 및 일차함수: ex)x^2+2*x-3 \n 지수함수: ex)x^2 + exp(x) \n 로그함수: x^2 + log(x)")
elif some == "2)" or "2" :
  print("이유찬")

#%%
reqast = input("그리실 함수 식을 입력하세요: ")
reqast = reqast.replace("^","**")

from sympy import *
import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

x = sy.symbols('x')
fx = parse_expr(reqast)
plot(fx)
# x 값 범위 설정
x_vals = np.linspace(-100, 100, 1000)

# y 값 계산
y_vals = [fx.subs(x, val) for val in x_vals]

# %%
# 그래프 그리기
plt.plot(x_vals, y_vals)
plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of f(x)')
plt.grid(True)
plt.show()
#%%