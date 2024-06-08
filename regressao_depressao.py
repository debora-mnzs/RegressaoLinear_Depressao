import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('RegressaoLinear_Depressao\\Depression.csv')

# LIMPEZA DE DADOS
# removendo linhas não preenchidas
df = df.dropna()

# removendo coluna não relevante e coluna categórica
df = df.drop(columns=['Number ','Depression State'])

# ANÁLISE DA CORRELAÇÃO
correlation_matrix = df.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Matriz de Correlação das Variáveis')
plt.show()

# REGRESSÃO LINEAR

# separando X e y 
X = df.drop(columns=['Suicidal Ideation'])
y = df['Suicidal Ideation']

# dividindo os dados em conjuntos de treinamento e teste com 20% dos dados para teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# treinando o modelo
model = LinearRegression()
model.fit(X_train, y_train)

# RESULTADO DO MODELO
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Erro médio quadrático:", mse)
print("R²:", r2)

m = model.coef_[0]
c = model.intercept_

print("Equação da linha de regressão: y =", m, "x +", c)