# Importa um conjunto de dados pronto do sklearn
from sklearn import datasets

# Função para dividir os dados em treino e teste
from sklearn.model_selection import train_test_split

# Modelo de Machine Learning: SVM
from sklearn.svm import SVC

# ---------------------------------------
# 1) Carregar o dataset de câncer de mama
# ---------------------------------------
cancer = datasets.load_breast_cancer()

# "cancer.data"  -> características do tumor (tamanho, textura, etc.)
# "cancer.target" -> indica se é maligno (1) ou benigno (0)

# -------------------------------------------------------
# 2) Separar dados em treino (80%) e teste (20%)
# random_state serve para deixar o resultado reprodutível
# -------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.2, random_state=42
)

# -----------------------------------------------
# 3) Criar o modelo SVM com kernel linear
# kernel='linear' significa que vamos separar usando uma linha (ou plano)
# -----------------------------------------------
model = SVC(kernel='linear')

# -----------------------------------------------
# 4) Treinar o modelo usando os dados de treino
# -----------------------------------------------
model.fit(X_train, y_train)

# -----------------------------------------------
# 5) Avaliar a acurácia do modelo nos dados de teste
# score() retorna a porcentagem de acertos
# -----------------------------------------------
accuracy = model.score(X_test, y_test)

# -----------------------------------------------
# 6) Exibir resultado formatado
# -----------------------------------------------
print(f'Acurácia do Modelo: {accuracy:.2f}')