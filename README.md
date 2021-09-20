# ComuTech

## Instalação

Siga os seguintes passos para instalar o projeto em sua máquina local.

1. git clone https://github.com/NicolasDestito/ComuTech.git
2. Acessar a pasta ComuTech: cd ComuTech
3. Criar um ambiente virtual (python venv): python -m venv env
4. Entre no ambiente virtual:
    - Para Linux:
      1. source ./env/bin/activate
      
    - Para Windows:
      1. Se você não tiver feito anteriormente, entre no PowerShell como administrador e execute: **Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned**
      2. execute .\env\Scripts\Activate.ps1
      
4. Então instale as bibliotecas necessárias:
    - Django
    - Pillow
    - (comando para instalar tudo ao mesmo tempo: *pip install django pillow*)
5. Faça as migrações com: python manage.py migrate
