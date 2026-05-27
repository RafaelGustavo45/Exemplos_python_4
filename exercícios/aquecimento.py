# aquecimento.py - Execute e complete os comentários

# 1. Qual a diferença entre = e == ?
x = 5
print(x == 5)  # Retorna: _____ (tipo: _____)

# 2. O que este código imprime?
nota = 8
situacao = "" 

if nota >= 7:
  situacao = "Aprovado" 
else:
    situacao = "Reprovado"
    
print(situacao)  

# 3. Complete o loop para imprimir apenas números pares de 0 a 10:
for n in range(11):
    if (n < 10 and n%2== 0):  # sua condição aqui
        print(n)