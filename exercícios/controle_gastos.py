# controlador_gastos_pratica.py

print("💰 CONTROLADOR DE GASTOS SEMANAL")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# 1. Coleta do limite
while True:
    limite_input = input("Limite semanal (R$): ").strip()

    # valida se é número
    if not is_number(limite_input):
        print("⚠️ Valor inválido. Digite um número.")
        continue

    # converte para float
    limite_semanal = float(limite_input)

    # valida se é maior que 0
    if limite_semanal <= 0:
        print("⚠️ O valor deve ser maior que 0.")
        continue

    break

print(f"✅ Limite definido: R$ {limite_semanal:.2f}")


# 2. Coleta de gastos
descricoes = []
valores = []

while True:
    desc = input("Descrição (ou 'fim'): ").strip().title()

    if desc.lower() == 'fim':
        break

    # valida o valor do gasto
    while True:
        valor_input = input("Valor (R$): ").strip()

        # verifica se é número
        if not is_number(valor_input):
            print("⚠️ Valor inválido. Digite um número.")
            continue

        # converte para float
        valor = float(valor_input)

        # verifica se é maior que 0
        if valor <= 0:
            print("⚠️ O valor deve ser maior que 0.")
            continue

        break

    # adiciona às listas
    descricoes.append(desc)
    valores.append(valor)


print("\n📋 Gastos cadastrados:")

for i in range(len(descricoes)):
    print(f"- {descricoes[i]}: R$ {valores[i]:.2f}")


# 3. Cálculos
total_gasto = sum(valores)
saldo_restante = total_gasto-limite_semanal

print(f"Gasto total: {total_gasto} , saldo restante: {saldo_restante}")

# SUA SOLUÇÃO: identifique gastos >= 50 usando list comprehension
gastos_significativos = [
    (desc, valor)
    for desc, valor in zip(descricoes, valores)
    if valor > 50
]

print(f"Gastos significativos: {gastos_significativos}")


#i=0
#for a in range(len(valores)):
#    if a >=50:
#        gastos_significativos


# SUA SOLUÇÃO: encontre o maior gasto (abordagem linear sem max())
if len(valores) > 0:
    indice_maior = 0
    maior_valor=0
    for i in range(1, len(valores)):
        if i > maior_valor:
            indice_maior = i
            maior_valor = i
    categoria_mais_cara = descricoes[indice_maior]
    valor_mais_caro = valores[maior_valor]

    print(f"item mais caro: {categoria_mais_cara}, valor: {valor_mais_caro}")



'''
# 4. Saída com alertas
print(f"\n📊 Total gasto: R$ {total_gasto:.2f}")
print(f"Saldo: R$ {saldo_restante:.2f}")

# SUA SOLUÇÃO: alertas condicionais
if __________:
    print(f"🚨 ALERTA: Limite ultrapassado!")
elif __________:
    print(f"⚠️  Atenção: Orçamento quase esgotado.")
else:
    print(f"✅ Tudo sob controle.")

if gastos_significativos:
    print(f"\n🔍 Gastos ≥ R$ 50:")
    for desc, val in gastos_significativos:
        print(f"   • {desc}: R$ {val:.2f}")

# BÔNUS 1: Agrupe gastos por categoria simples (ex: "Alimentação", "Transporte")
# Dica: use uma lista de categorias pré-definidas e verifique com in

# BÔNUS 2: Calcule a média de gastos por item registrado
# Dica: total_gasto / len(valores)

# BÔNUS 3: Sugira um valor máximo por gasto restante para não estourar o limite
# Fórmula: saldo_restante / (dias_restantes_da_semana * gastos_medios_por_dia)

'''