a = int(input("Insira o Valor 1"))
o = input("Insira o Operador")
b = int(input("Insira o Valor 2"))

if o == "+":
    resul = a + b
if o == "-":
    resul = a - b
if o == "*":
    resul = a * b
if o == "/":
    resul = a / b

print(f"O resultado é: {resul}")