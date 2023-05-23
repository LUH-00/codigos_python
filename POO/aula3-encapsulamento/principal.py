import os
from conta import Conta
minhaConta = Conta(123, "Robervaldo Magalhães", 20000, 900)

os.system ("cls")
minhaConta.saldo = 80500
#minhaConta.relatorio()
minhaConta.exibirSaldo()


print ("Seu limite é ", minhaConta.getLimite())
minhaConta.setLimite(1400)

print ("Seu limite é ", minhaConta.getLimite())