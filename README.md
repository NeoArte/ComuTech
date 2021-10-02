# ComuTech
Projeto para o ENTRA21 criado pelo Dream Team no ano de 2021

## Sobre
Nosso objetivo é conectar pessoas em situações criticas e pessoas dispostas a ajuda-las em um ambiente focado em acolher essas pessoas.
Esse projeto é feito com Python (Django) para o back-end e HTML, CSS e Javascript para o front-end

## Instalação

Siga os seguintes passos para instalar o projeto em sua máquina local.

1. Clone o repositório com: ``git clone https://github.com/NicolasDestito/ComuTech.git``
2. Acessar a pasta ComuTech: ``cd ComuTech``
3. Criar um ambiente virtual (python venv): ``python -m venv env``
4. Entre no ambiente virtual:
    - Para Linux:
      1. ``source ./env/bin/activate``
      
    - Para Windows:
      1. Se você não tiver feito anteriormente, entre no PowerShell como administrador e execute: ``**Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned**``
      2. execute: ``.\env\Scripts\Activate.ps1``
      
4. Então instale as bibliotecas necessárias:
    - Django (``pip install django``)
    - Django Filter (``pip install django-filter`)
    - Django Endless Pagination (``pip install django-el-pagination``)
    - Django Multiupload - Fork por Grueebler (``pip install git+https://github.com/rgrueebler/django-multiupload.git@patch-1``)
    - Pillow (``pip install pillow``)
    - (comando para instalar tudo ao mesmo tempo: ``*pip install django django-filter django-el-pagination pip install git+https://github.com/rgrueebler/django-multiupload.git@patch-1 pillow*``)
5. Faça as migrações com: ``python manage.py migrate``
6. Confirme que todas as pastas para midias foram criadas corretamente (media, media/usuarios, media/socorros, ...)
