# pentaho-db-changer
Change dynamically Pentaho reports database connection

How to use
==========

Antes de executar o programa, é necessário configurar o arquivo de configuração(config.ini).
Para configurar o arquivo de configuração é bem simples, como mostra o exemplo abaixo.

Primeiro cria a seção conect com o elemento conect, essa seção serve para selecionar o banco que vai querer.

[conect]
conect = conect_local

Depois cria a seção default com o elemento path, esse elemento serve para selecionar o path da pasta aonde estão os arquivos do pdi.

[default]
path = /home/pdi

Depois cria as seções dos bancos que desejar. Em cada seção de 

[conect_server]
server = xxxxxx
username = xxxxxx
password = Encrypted 3b479jfbf7hwndhnn37dr345r54t

[conect_local]
server = localhost
username = root
password = Encrypted 3b479jfbf7hwndhnn37dr345r54t

Para executar é muito simples, basta executar o init.
