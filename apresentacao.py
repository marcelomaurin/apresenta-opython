# -*- coding: utf-8 -*-
"""Olá, este é o Colaboratory

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb

# Apresentação teórica

# 1. Introdução Teórica
O que é Programação?

Programação é como ensinar o computador a fazer o que queremos. Quando programamos, escrevemos instruções que o computador segue para realizar tarefas. Essas instruções são escritas em uma linguagem que o computador entende, como o Python.

Por que Aprender Programação?

Aprender a programar é como aprender uma nova língua que permite você criar jogos, aplicativos, e até controlar robôs! Além disso, ajuda a desenvolver o raciocínio lógico e a resolver problemas de forma criativa.

# 2. Apresentação da Linguagem Python
O que é Python?

Python é uma linguagem de programação que é fácil de aprender e usar, especialmente para iniciantes. Ela é muito popular porque é simples, mas ao mesmo tempo poderosa. Python é usada em todo tipo de aplicação, desde desenvolvimento de sites até inteligência artificial.

Por que Python?

Simplicidade: Python tem uma sintaxe clara e direta, o que facilita a leitura e a escrita de código.
Comunidade: Muitos programadores usam Python, então você sempre encontrará ajuda e exemplos online.
Versatilidade: Você pode usar Python para praticamente qualquer coisa: jogos, ciência de dados, automação, e muito mais.

# Codificação

# 3. Explicação Básica do Código
Agora, vamos ver um exemplo de código em Python que mostra como podemos usar programação para transformar dados em gráficos.

## Objetivo do Código:

Vamos criar um gráfico que mostra as notas de uma turma em três disciplinas (Matemática, História e Ciências) ao longo de quatro anos. A menor nota será 6.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Nomes dos alunos
alunos = [f'Aluno {i+1}' for i in range(10)]

# Disciplinas
disciplinas = ['Matemática', 'História', 'Ciências']

# Anos
anos = [2021, 2022, 2023, 2024]

# Gerando notas aleatórias (entre 5 e 10) para cada aluno, disciplina e ano
np.random.seed(0)  # Para reprodutibilidade
notas = np.random.randint(5, 11, size=(len(alunos), len(disciplinas), len(anos)))

# Criando um DataFrame para visualização
df = pd.DataFrame(data=notas.reshape(len(alunos)*len(disciplinas), len(anos)),
                  index=pd.MultiIndex.from_product([alunos, disciplinas], names=['Aluno', 'Disciplina']),
                  columns=anos)

# Exibindo o DataFrame
print("Notas dos alunos ao longo dos anos:")
print(df)

# Gráfico 1: Notas de uma disciplina específica ao longo dos anos
disciplina_escolhida = 'Matemática'
df_disciplina = df.xs(disciplina_escolhida, level='Disciplina')

plt.figure(figsize=(10, 6))
for aluno in alunos:
    plt.plot(anos, df_disciplina.loc[aluno], marker='o', label=aluno)

plt.title(f'Notas dos Alunos em {disciplina_escolhida} ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Nota')
plt.xticks(anos)
plt.ylim(5, 10)  # Definindo o limite do eixo Y entre 5 e 10
plt.legend(title='Alunos', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show()

# Gráfico 2: Média das notas da classe em cada disciplina ao longo dos anos
df_media_classe = df.groupby(level='Disciplina').mean()

plt.figure(figsize=(10, 6))
for disciplina in disciplinas:
    plt.plot(anos, df_media_classe.loc[disciplina], marker='o', label=disciplina)

plt.title('Média das Notas da Classe em Cada Disciplina ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Nota Média')
plt.xticks(anos)
plt.ylim(5, 10)  # Definindo o limite do eixo Y entre 5 e 10
plt.legend(title='Disciplinas', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show()

"""## Explicação do Código:

Importação de Bibliotecas:

matplotlib.pyplot: Usada para criar gráficos.
numpy: Usada para gerar as notas de forma aleatória.
pandas: Usada para organizar e manipular os dados.
Geração de Notas:

As notas são geradas aleatoriamente entre 6 e 10 para cada aluno em cada disciplina ao longo dos quatro anos.
Gráficos:

Gráfico 1: Mostra as notas dos alunos em Matemática ao longo dos anos.
Gráfico 2: Mostra a média das notas de toda a classe em cada disciplina ao longo dos anos.
Conclusão:

Com esse código, vimos como podemos usar Python para transformar dados (como notas de alunos) em gráficos que ajudam a entender melhor o desempenho da turma. Programar pode ser divertido e muito útil!

# 4. Tipos de Gráficos em Python: Como Cada um Proporciona uma Visão Diferente
## 4.1. Gráfico de Linhas
O que é?

Um gráfico de linhas conecta pontos de dados com uma linha, mostrando como algo muda ao longo do tempo.
Quando Usar?

Ideal para mostrar tendências ou mudanças ao longo de períodos de tempo.
Exemplo:

Usado para visualizar a evolução das notas dos alunos em Matemática ao longo dos anos.
"""

plt.plot(anos, df_disciplina.loc[aluno], marker='o', label=aluno)

"""##  4.2. Gráfico de Barras
O que é?

Um gráfico de barras usa barras para representar dados. A altura de cada barra indica o valor dos dados.
Quando Usar?

Perfeito para comparar quantidades diferentes entre várias categorias.
Exemplo:

Usado para comparar a média das notas de diferentes disciplinas em um ano específico.
"""

plt.bar(disciplinas, df_media_classe[2024])

"""## 4.3. Gráfico de Pizza
O que é?

Um gráfico de pizza divide um círculo em fatias que representam proporções de um todo.
Quando Usar?

Ideal para mostrar a participação de cada parte em relação ao todo.
Exemplo:

Pode ser usado para mostrar a proporção das notas em uma disciplina específica em um determinado ano.
"""

plt.pie(df_media_classe[2024], labels=disciplinas, autopct='%1.1f%%')

"""## 4.4. Gráfico de Dispersão
O que é?

Um gráfico de dispersão usa pontos para representar a relação entre duas variáveis diferentes.
Quando Usar?

Útil para observar correlações ou padrões entre dois conjuntos de dados.
Exemplo:

Pode ser usado para mostrar a correlação entre as notas de Matemática e Ciências.
"""

plt.scatter(df_disciplina.loc['Aluno 1'], df.xs('Ciências', level='Disciplina').loc['Aluno 1'])

"""## 4.5. Histograma
O que é?

Um histograma mostra a distribuição de um conjunto de dados, agrupando valores em intervalos.
Quando Usar?

Usado para entender a distribuição de dados, como a frequência de diferentes faixas de notas.
Exemplo:

Pode ser usado para mostrar a distribuição das notas de todos os alunos em uma disciplina.
python
Copia
"""

plt.hist(df_disciplina.values.flatten(), bins=5)

"""## 4.5 Conclusão
Cada tipo de gráfico oferece uma maneira única de visualizar os dados:

Gráfico de Linhas: Melhor para ver mudanças ao longo do tempo.
Gráfico de Barras: Ideal para comparações diretas entre categorias.
Gráfico de Pizza: Mostra proporções dentro de um conjunto.
Gráfico de Dispersão: Revela correlações entre variáveis.
Histograma: Visualiza a distribuição de dados.
Escolher o tipo certo de gráfico depende do que você quer destacar nos dados. Com a prática, você aprenderá a escolher o gráfico que melhor comunica a informação desejada.
"""