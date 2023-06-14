l1 = int(input("Valor do primeiro Lado:"))
l2 = int(input("Valor do segundo lado:"))
l3 = int(input("Valor do terceiro lado"))
if l1 == l2 == l3 :
    print(" Esse é um Triângulo    Equilátero")
elif l1 == l2 != l3 :
    print("Esse é um Triângulo    Isóscele")
elif l1 != l2 == l3 :
    print("Esse é um Triângulo    Isóscele")
else :
    print("Esse é um Triângulo    Escaleno")
