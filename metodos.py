"""import math
co = float(input("Digite o Valor do catetoOposto:"))
ca = float(input("Digite o valor do catetoAdjacente:"))
hypo = math.hypot(co,ca)
print("O valor da Hipotenusa é {:.2f}".format(hypo))"""
import math
a = float(input("Digite o Angulo que Você deseja saber:"))
r = math.radians(a)
s = (math.sin(r))
c = (math.cos(r))
t = (math.tan(r))
print("O VAlor do Seno do angulo {0} é {1:.2f}\n".format(a,s))
print("O valor do cosseno do angulo {0} é {1:.2f}\n".format(a,c))
print("O valor da tangente do angulo {0} é {1:.2f}\n".format(a,t))