"""
-> novo repositorio 
 git init

-> verificar o ststus 
git status

-> mostrar pasta oculta 
ls -a

-> limpar a tela
clear 

->  criar o autor do versionamento 
git config --global user.nome "Luan"

-> configurar o email do autor 
git config --global user.email "luan@gmail.com"

-> verificar o email e o nome do autor 
git config user.nome
 
git config user.email

-> colocando as coisas na area de preparação 
git add .

-> finalizar (

git commit -m "Criamos uma lista com 3 cursos"

-> verificar o registro que criou 
git log
commit 0e1cee28ad193e8239b3c88bd7b3080e14bf1c1c (HEAD -> master)
Author: unknown <luan@gmail.com>
Date:   Wed Apr 12 20:27:53 2023 -0300

    Criamos uma lista com 3 cursos
 

--> mostrar o commit mais pequeno
 git log --oneline

 

 --> voltar na linha do tempo 



manha@SNRFTLBINC2-26 MINGW64 ~/Documents/programação app (master)
$ git checkout 0e1cee2
Note: switching to '0e1cee2'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 0e1cee2 Criamos uma lista com 3 cursos

->  voltar pro commint atual 
$ git checkout master


-> verificar qual ramo vc está 
git branch

-> criar um novo ramo 
git branch (nome da branch) 

-> utilizar o ramo criado 
 git checkout funcionario


-> veriicar se tem algum repositorio 

git remote -v


->  adicionar git repositorio
git remote add origin (site)


-> mandar o repositorio para o git hub 
git push  (origin/ apelito do site ) ( master/ nome do git) 

-> clonar os codgos em python 
git clone (link do git hub)


-> trazer o link pra si (atualizar)
git pull origin master

-> colocar os novos codigos no git hub (depois do | git add . | git commit -m "comentário") 
 git push origin master 





"""