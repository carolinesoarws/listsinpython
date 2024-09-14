import copy
from PIL import Image, ImageFilter
print("##############################################")
print("##############################################")
print("")
print(" Capitulo 03 - Capítulo 03 - Deep e Shallow Copy")
print("")
print("##############################################")
print("##############################################")
print("")

# Exemplo 01 - Shallow Copy
print("Exemplo 01 - Shallow Copy")
# Lista original
lista_original = [[1, 2, 3], [4, 5, 6]]

# Fazendo uma shallow copy
lista_copia = copy.copy(lista_original)
print("Lista Original:", lista_original)
print("Lista Copiada:", lista_copia)

# Alterando um elemento na cópia
lista_copia[0][0] = 'A'
print("Lista Copiada Alterada:", lista_copia)
print("Lista Original:", lista_original)

print("#########################################")
print("")


# Exemplo 02 - Shallow Copy Exemplo 01 - Manipulação de Dados em Aplicações Financeiras
print("# Exemplo 02 - Shallow Copy Exemplo 01 - Manipulação de Dados em Aplicações Financeiras")
accounts = {'savings': [100, 200], 'checking': [50, 150]}
temporary_accounts = accounts.copy()

# Adicionando uma transação temporária
temporary_accounts['savings'].append(300)

# Ambas as listas foram modificadas
print(accounts['savings'])  # Saída: [100, 200, 300]
print(temporary_accounts['savings'])  # Saída: [100, 200, 300]

print("#########################################")
print("")

# Exemplo 03 - Shallow Copy Exemplo 02 - Gerenciamento de Estado em Aplicações de Jogos
print("Exemplo 03 - Shallow Copy Exemplo 02 - Gerenciamento de Estado em Aplicações de Jogos")
game_state = {'units': ['knight', 'archer'], 'resources': [10, 20]}
simulated_state = game_state.copy()

# Movendo uma unidade na simulação
simulated_state['units'].append('mage')

# Ambas as listas de unidades foram modificadas
print(game_state['units'])  # Saída: ['knight','archer', 'mage']
print(simulated_state['units'])  # Saída: ['knight', 'archer', 'mage']

print("#########################################")
print("")

# Exemplo 04 - Shallow Copy Desenvolvimento de Aplicações de Inventário
print("Exemplo 04 - Shallow Copy Desenvolvimento de Aplicações de Inventário")
inventory = {'warehouse1': ['item1', 'item2'], 'warehouse2': ['item3']}
temp_inventory = inventory.copy()

# Movendo um item no inventário temporário
temp_inventory['warehouse1'].remove('item1')
temp_inventory['warehouse2'].append('item1')

# O inventário original também foi alterado
print(inventory['warehouse1'])  # Saída: ['item2']
print(inventory['warehouse2'])  # Saída: ['item3', 'item1']

print("#########################################")
print("")

# Exemplo 05 - Shallow Copy Sistema de Configuração em Aplicações Web
print("Exemplo 05 - Shallow Copy Sistema de Configuração em Aplicações Web")
user_permissions = {'admin': ['read', 'write'], 'guest': ['read']}
temp_permissions = user_permissions.copy()

# Alterando permissões na cópia
temp_permissions['admin'].append('delete')

# A permissão 'delete' também foi adicionada ao original
print(user_permissions['admin'])  # Saída: ['read', 'write', 'delete']
print(temp_permissions['admin'])  # Saída: ['read', 'write', 'delete']
print("#########################################")
print("")

# Exemplo 06 - Shallow Copy Serviços de Marketing
print("Exemplo 06 - Shallow Copy Serviços de Marketing")
campaigns = {'summer': ['contact1', 'contact2'], 'winter': ['contact3']}
temp_campaigns = campaigns.copy()

# Adicionando um contato na campanha temporária
temp_campaigns['summer'].append('contact4')

# O contato também foi adicionado na lista original
print(campaigns['summer'])  # Saída: ['contact1', 'contact2', 'contact4']
print(temp_campaigns['summer'])  # Saída: ['contact1', 'contact2', 'contact4']
print("#########################################")
print("")

# Exemplo 07 - Deep Copy
print("Exemplo 07 - Deep Copy")
original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Fazendo uma deep copy da lista original
copia_profunda = copy.deepcopy(original)

# Modificando a cópia profunda
original[1][1] = 2000
copia_profunda[0][0] = 99
copia_profunda[2][2] = 999

# Mostrando os resultados
print("Original:", original)
print("Cópia Profunda:", copia_profunda)
print("#########################################")
print("")

# Exemplo 08 - Deep Copy Manipulação de Gráficos em Processamento de Imagens
print("Exemplo 08 - Deep Copy Manipulação de Gráficos em Processamento de Imagens")

imagem_original = Image.open('foto.jpg')
imagem_copia = copy.deepcopy(imagem_original)

# Aplica um filtro na cópia sem alterar a imagem original.
imagem_copia = imagem_copia.filter(ImageFilter.BLUR)
print("#########################################")
print("")

# Exemplo 09 - Deep Copy  Simulação de Cenários em Finanças
print("Exemplo 09 - Deep Copy  Simulação de Cenários em Finanças")


dados_financeiros = {
"ações": {"empresa1": 100, "empresa2": 200},
"renda_fixa": {"bonds": 300} }

cenario_1 = copy.deepcopy(dados_financeiros)
cenario_2 = copy.deepcopy(dados_financeiros)

# Testa cenários diferentes de investimento.
cenario_1["ações"]["empresa1"] += 50
cenario_2["renda_fixa"]["bonds"] -= 50
print("#########################################")
print("")

# Exemplo 10 - Deep Copy Customização de Templates em Desenvolvimento de Software
print("Exemplo 10 - Deep Copy Customização de Templates em Desenvolvimento de Software")
template_base = {
"layout": "padrão",
"cores": {"fundo": "branco", "texto": "preto"},
"componentes": ["header", "footer", "sidebar"]
}

template_cliente_a = copy.deepcopy(template_base)
template_cliente_b = copy.deepcopy(template_base)

# Customizações para cada cliente.
template_cliente_a["cores"]["fundo"] = "azul"
template_cliente_b["componentes"].append("banner")
print("#########################################")
print("")

# Exemplo 11 - Deep Copy Criação de Personagens em Jogos de RPG
print("Exemplo 11 - Deep Copy Criação de Personagens em Jogos de RPG")
base_personagem = {
"nome": "Personagem Base",
"atributos": {"força": 10, "agilidade": 8, "inteligência": 7},
"inventario": ["Espada", "Poção"]
}
guerreiro = copy.deepcopy(base_personagem)
mago = copy.deepcopy(base_personagem)

# Customizações para cada personagem.
guerreiro["atributos"]["força"] += 5
mago["atributos"]["inteligência"] += 5
mago["inventario"].append("Varinha")
print("#########################################")
print("")

# Exemplo 12 - Deep Copy Desenvolvimento de API
print("Exemplo 12 - Deep Copy Desenvolvimento de API")
resposta_base = {
"status": "sucesso",
"dados": {"usuario": "João", "id": 1234},
"mensagem": "Operação realizada com sucesso."
}
resposta_erro = copy.deepcopy(resposta_base)
resposta_parcial = copy.deepcopy(resposta_base)

# Customizações das respostas.
resposta_erro["status"] = "erro"
resposta_erro["mensagem"] = "Falha na operação."
resposta_parcial["dados"].pop("usuario")
print("#########################################")
print("")

