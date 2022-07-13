# PDI-Intmed

    
# Sumário

- [Sobre o desafio](#sobre)
- [Requisitos técnicos](#requisitos)
- [Tecnologias utilizadas](#requisitos)
- [Comandos para instalar na sua maquina](#instalação)
- [Execução do projeto](#execução)

# Sobre

Plano de desenvolvimento pessoal para empresa Intmed. O projeto é um desafio onde o desenvolvedor deve criar uma
API de autenticação simples.

# Requisitos

- primeira semana - Iniciar projeto em Django rest framework
- segunda semana - Implementar a rota de cadastro de usuário
- terceira semana - Implementar a rota de autenticação de usuário

# Técnologias 

  - [Python3](https://www.python.org/)
  - [Django Rest Framework](https://www.django-rest-framework.org/)
  - [sqlite3](https://docs.python.org/3/library/sqlite3.html)
  - [Docker](https://www.docker.com/)
  - [Docker Compose](https://docs.docker.com/compose/install/)
 
# Instalação

- São duas maneiras de instalar o projeto:
  - com o ambiente de virtual.
  - com o Docker.


Com ambiente de virtual:

1. Clone o repositório

- `git clone git@github.com:LeandroLopes1/PDI-Intmed.git`.
- Entre na pasta do repositório que você acabou de clonar:
 `cd PDI-Intmed`.

2. Crie o ambiente virtual para o projeto:

- `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências:

- `python3 -m pip install -r dev-requirements.txt`

Com o Docker:

1. Clone o repositório

- `git clone git@github.com:LeandroLopes1/PDI-Intmed.git`.
- Entre na pasta do repositório que você acabou de clonar:
 `cd PDI-Intmed`.

2. Digite no terminal:

- `docker-compose build`

3. Execute o projeto:

- `docker-compose up`


# Execução

com a venv ativa:

digite no seu terminal:

  - `python manage.py makemigrations`

  - `python manage.py migrate`

  - `python manage.py runserver`
  

Entre no endereço `http://localhost:8000/api/v1/register/` e cadastre um usuário.

para cadastrar um usuário:

```
{
    "email": "exemplo@email.com",
    "password": "teste"
}
```

se cadastar com sucesso ira aparecer status code 201 Created e o usuário será salvo no banco de dados.

o retorno do usuário será:

```
{
    "email": "exemplo@email.com"
}
```


Após, entre no endereço `http://localhost:8000/api/v1/login/` e autentique o usuário.

para autenticar o usuário:

```
{
    "email": "exemplo@email.com",
    "password": "teste"
}
```


se autenticar com sucesso ira aparecer status code 200 OK e um token para autenticação será retornado.

o retorno será:

```
{
    "refresh": "numero token",
    "access": "numero token"
    "user_id": "id do usuário"
}
```
