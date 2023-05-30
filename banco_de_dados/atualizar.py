import pymysql
conexao = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="departamento_bd"
)
nome = input("Informe o novo nome dp funcionário: ")
codigo = int(input("Qual o código do funcionário? "))

comando = "update funcionario set nome = %s where  cod_funcionario = %s"

valores = (nome, codigo)

consulta = conexao.cursor()
consulta.execute(comando, valores)

conexao.commit()

print(consulta.rowcount, "linha atualizada com sucesso \n")

conexao.close()
