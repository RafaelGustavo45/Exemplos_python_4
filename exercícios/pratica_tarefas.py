
# pratica_tarefas.py
# Objetivo: Criar um mini gerenciador de tarefas usando apenas conceitos vistos até aqui

# 1. Crie uma lista vazia para armazenar tarefas
tarefas = []

# 2. Adicione 3 tarefas iniciais (strings)
# Sua solução aqui:

tarefas.append("jQuery")
tarefas.append("Banco de dados")
tarefas.append("API rest")

# 3. Imprima a tarefa prioritária (primeira da lista)
# Sua solução aqui:

priori = tarefas[0];

print("prioridade: ", priori)


# 4. Marque a primeira tarefa como concluída (substitua por "✅ " + nome da tarefa)
# Sua solução aqui:

concluido = priori+" ✅"
tarefas.pop()

tarefas.insert(0, concluido)

print("concluido: ", tarefas)

# 5. Use slicing para mostrar apenas as tarefas pendentes (exclua a primeira)
# Sua solução aqui:
print("pendentes")

for tarefa in tarefas:
    if not "✅" in tarefa:
        print(tarefa)


# 6. BÔNUS: Inverta a ordem da lista para priorizar as mais recentes
# Sua solução aqui:

tarefas.reverse()

print("Invertido: ", tarefas)