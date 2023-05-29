import pymysql

# estabelecendo a cenexão 
conexao = pymysql.connect(
    host="localhost",  #servidor
    user="root", #local 
    passwd="",#senha
    database="departamento_bd" #banco de dados 
)


#Inserindo dados no banco 
codigo = int(input("Informe o codigo do funcionário: "))
nome = input("Informe o nome do funcionário: ")
salario = float(input("Informe o salário do funcionário: "))
cargo = input("Informe o cargo do funcionário: ")

#Colocamos %s no lugar dos dados reais, para evitar possíveis ataques sql injection. Isso é uma implementação da biblipteca pymysql.
comando = "insert into  funcionario values(%s, %s, %s, %s)"

campos = (codigo, nome, salario, cargo) #Criando uma tupla com os dados que serão substituídos no comando

consulta = conexao.cursor() # Cursor() é o objeto que irá interagir diretamente com o banco de dados 


consulta.execute(comando, campos)

conexao.commit() # gravar os dados no banco 

print(consulta.rowcount, " linha(s) inserida com sucesso \n")

conexao.close()