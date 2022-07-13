# Anotações para desenvolvimento do projeto

    Este documento tem como objetivo acrescentar normas e regras para desenvovimento 
    do projeto de acordo com as ADRs que se encontra no repositório Arquitetura-Corporativa Azure DevOps.
     
     
    adr0013 - ADR gitflow

    Seguindo o padrão gitflow, o projeto deve ter três repositórios:
    - main
    - developer
    - feature

    Para fins didáticos, usarei duas branches:
    - main
    - developer

    Para padronização dos commits, usarei o Semantic Commits.
    https://semantic-commits.com/
    O Semantic Commits é um padrão de commit que permite a identificação de tipos de commit,
    como:
    - feat: adicionar uma nova funcionalidade
    - fix: corrigir um bug
    - docs: adicionar documentação
    - style: corrigir estilo
    - refactor: refatorar código
    - test: adicionar testes
    - chore: corrigir bugs ou manter o projeto funcionando
    
    adr0014 - ADR rest

    Para o desenvolvimento do projeto, usarei API REST.

    Todo payload deve ser enviado em JSON e o cabeçalho deve conter o token de autenticação.
    O token deve ser gerado pelo usuário que deseja autenticar.
    O payload deve conter o nome do usuário e a senha.

    A rota será em inglês citada na adr0014.
    ex:
    curl -X POST -H "Content-Type: application/json" -d '{"username":"admin","password":"admin"}' http://my-application-url/v1/login

    adr0016 - ADR design

    O projeto terá um README.md contendo uma breve descrição do projeto, suas necessidades e como executá-lo.

    a Estrutura do projeto deve ser:
    - README.md
    - src
    - test
    - docs
    - .gitignore
    - requirements.txt
    






