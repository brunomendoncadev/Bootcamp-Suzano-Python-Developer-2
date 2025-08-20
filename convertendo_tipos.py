
#converter uma variavel de str(strings) para outra como numerico int,float ou inverso.

#---------------------------------------------
#INTEIRO PARA FLOAT
preco = 10
print(preco)
#>>> 10

preco = float(preco)
print(preco)
#>>> 10.0

preco = 10 / 2
print(preco)
#>>> 5.0  (obs quando for feito com / sempre vem tipo float)

#--------------------------------------------
#FLOAT PARA INTEIRO
preco = 10.30
print(preco)
#>>> 10.3

preco = int(preco)
print(preco)
#>>>10

#--------------------------------------------
#CONVERSAO POR DIVISAO

preco = 10
print(preco)
#>>>10

print(preco / 2)
#>>> 5.0   (feito com / vem com tipo float)

print(preco // 2)
#>>> 5   (feito com // vem com tipo int)

#--------------------------------------------

#NUMÉRICO PARA STRING??
# na realidade o codigo abaixar vai concatenar com a string

preco = 10.5
idade = 28

print (str(preco))
#>>>10.5

print(str(idade))
#>>>28

texto = f"idade {idade} preco {preco}"
print(texto)
#>>> idade 28 preco 10.5  (importante usar f"..."" para funcionar, ou seja paara concatenar o texto)

#------------------------------------------
# STRING PARA NÚMERO
preco = "10.50"
idade = "28"
print (float(preco))
#>>> 10.5

print(int(idade))
#>>> 28

#------------------------------------------

#   >>> print(type(str(10.10)))
#   <class 'str'>
#   >>> print(int(1.9788989898))
#   1   
#   >>> print(int("10"))
#   10  
#   >>> print(float(10.10))
#   10.1
#   >>> print(float(100))
#    100.0
#    >>> valor = 10
#   >>> valor_str = str(valor)
#    >>> print(type(valor))
#    <class 'int'>
#   >>> print(type(valor_str))
#   <class 'str'>
#   >>> 



