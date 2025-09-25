### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

# quantidades = [1,2,3,4,-2]

# for quantidade in quantidades:
#     if quantidade < 0:
#         print(f'Dado invalido: {quantidade}')
#     else:
#         print(f'Dados correto: {quantidade}')



### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# temp = [12,15,20,99,49,45]

# for temperatura in temp:
#     if temperatura <10:
#         print('Baixa')
#     elif temperatura <= 30:
#         print('Normal')
#     else:
#         print('ALTAAA')

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# logs = [
#     {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'},
#     {'timestamp': '2021-06-23 10:05:00', 'level': 'INFO', 'message': 'Conexão estabelecida'},
#     {'timestamp': '2021-06-23 10:10:00', 'level': 'WARNING', 'message': 'Latência alta detectada'},
#     {'timestamp': '2021-06-23 10:15:00', 'level': 'ERROR', 'message': 'Servidor não respondeu'},
#     {'timestamp': '2021-06-23 10:20:00', 'level': 'INFO', 'message': 'Processamento concluído'},
#     {'timestamp': '2021-06-23 10:25:00', 'level': 'ERROR', 'message': 'Falha ao salvar no banco de dados'}
# ]
# var = 'teeste'
# for log in logs:
#     if log['level'] == 'ERROR':
#         novo_log = {
#         'timestamp': '2021-06-23 10:30:00',
#         'level': var,
#         'message': 'Novo registro adicionado',
#         'usuario': 'sistema'
#     }
#         logs.append(novo_log)
        
#         print(logs)

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# import re

# while True:
#     try:
#         idade = int(input('Digite sua idade: '))
#         break
#     except:
#         print('Digite um numero certo MMULA!!')

# while True:
    
#     email = input('Digite seu email: ')

#     if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
#             print('Digite um email válido!')
#     else:
#         break
    
# # Validação final
# if 18 <= idade <= 65:
#     print("Dados de usuário válidos")
# else:
#     print("Erro: idade fora do intervalo permitido (18 a 65 anos)")
### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
# from datetime import datetime

# agora = datetime.now()
# hr = agora.hour
# vlr_tran = float(input('Valor da transação: '))

# if vlr_tran > 10000 or (hr < 9 or hr > 18):
#      print('ALERTA')
# else:
#      print('OK')



### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.