import mysql.connector

# Cria a conexão com o banco
conexao = mysql.connector.connect(
    host="localhost",       # ou IP do servidor
    user="root",
    password="sua_senha",
    database="meu_banco"
)

# Cria um cursor (objeto para executar comandos SQL)
cursor = conexao.cursor()

# Executa uma consulta
cursor.execute("SELECT nome, idade FROM pessoas")

# Recupera os resultados
resultados = cursor.fetchall()

# Exibe os dados
for nome, idade in resultados:
    print(f"{nome} tem {idade} anos.")

# Fecha a conexão
cursor.close()
conexao.close()