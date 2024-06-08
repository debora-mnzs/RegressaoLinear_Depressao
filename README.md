# Regressão Linear para Análise de Depressão

O código realiza as seguintes etapas:

1. Carrega um conjunto de dados sobre depressão e seus sintomas.
    - O Dataset contém respostas de indivíduos que avaliaram sintomas de depressão entre 0 e 6 baseado na frequência que ocorrem.
    - O Dataset foi escolhido entre os disponíveis na plataforma Kaggle e pode ser visitado através do link: 'https://www.kaggle.com/datasets/hamjashaikh/mental-health-detection-dataset'.

2. Realiza a limpeza dos dados.
    - Remove linhas com valores ausentes e colunas irrelevantes.

3. Calcula a matriz de correlação entre as variáveis do conjunto de dados.
    - Imprime a matriz no formato de um heatmap.

4. Divide os dados em conjuntos de treinamento e teste
    - Separa 20% do dataset para teste e 80% para treino.
    - O random_state define uma seed para geração de números aleatórios, garantindo que com a mesma seed o número sempre será o mesmo.

5. Treina o modelo de regressão linear usando os dados de treinamento.

6. Faz previsões usando o modelo treinado e avalia o desempenho do modelo.
    - Calcula o erro médio quadrático (MSE) e coeficiente de determinação (R²).

7. Imprime a equação da linha de regressão resultante.