import mysql.connector

# Informações de conexão (substitua pelos seus valores)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  #password="sua_senha", definido a senha e o usuario
  password="admin",
  #database="db-proz-2024", definido o banco de dados
  database="db-proz-2024"
)

# Criando um cursor
##mycursor = mydb.cursor()

#Testando a conexao, mediante a uma condição a qual se faltar algo ou nem tiver o banco especifico ira retornar um error
#será criado uma cursor para acesso ao BD, para isso deve ser criado um objeto com esse nome mycursor = mydb.cursor.
if mydb.is_connected():
    print('Conectado com sucesso, bem vindo ao seu banco de dados!')
    mycursor = mydb.cursor()

# Executando uma consulta SQL, com esse objeto vamos organizar os dados nas "tabelas" que queremos ver as informaçãos e deve ser
#ser feita para cada aplicação ou seja cada uma deve ser seu select.
mycursor.execute("SELECT * FROM aluno;")

# Obtendo os resultados
myresult = mycursor.fetchall()

# Imprimindo os resultados
for x in myresult:
  print(x)

# Fechando a conexão, e toda ação deve receber uma condição de fechamaneto por meio do close() do mydb e mycursor.
mydb.close()
mycursor.close()