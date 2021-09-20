# ComuTech

## Instalação

Siga os seguintes passos para instalar o projeto em sua máquina local.

1. git clone https://github.com/NicolasDestito/ComuTech.git
2. Acessar a pasta ComuTech
3. Criar um ambiente virtual (python venv)
  1. python -m venv env
  - Para Linux:
    2. source ./env/bin/activate
  - Para Windows:
    2. Caso você já não tenha feito anteriormente, abra o Power Shell como administrador e execute o comando:
    `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`
    3. .\env\Scripts\Activate.ps1
4. Então instale as bibliotecas necessárias:
  - Django
  - Pillow
  - (comando para instalar tudo ao mesmo tempo: *pip install django pillow*)
5. Faça as migrações com: python manage.py migrate
