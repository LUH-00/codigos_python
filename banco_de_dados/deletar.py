import pymysql

conexao = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="departamento_bd"
)

codigo = int(input("Qual o código do funcionario deseja apagar? "))
comando = "delete from funcionario where cod_funcionario = %s"

consulta = conexao.cursor()
consulta.execute(comando, codigo)
conexao.commit()
print(consulta.rowcount, "linha foi ecluida com sucesso\n")
conexao.close()
