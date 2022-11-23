operacion = input("Choose an operation (sumar, restar, multiplicar) ")

num1 = int(input("elige el primer numero: "))
num2 = int(input("elige el segundo numero "))

def suma():
    sumar = num1 + num2
    print(str(num1) + "+" + str(num2) + "=" + str(sumar))

def res():
    restar = num1 - num2
    print(str(num1) + "-" + str(num2) + "=" + str(restar))

def multi():
    multiplicar = num1 * num2
    print(str(num1) + "*" + str(num2) + "*" + str(multiplicar))

if operacion == "sumar":
    suma()
elif operacion == "restar":
    res()
elif operacion == "multiplicar":
    multi()
else:
    print("elige una operacion")
    