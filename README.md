# Desafio Django

Este é um desafio para criação de um sistema de gerenciamento de propriedades rurais.

Configurei o ambiente como recomendado usando docker e docker-compose e também utilizei virtalenv além de usar o Pycharm.

## Como usar:

Após clonar o repositorio do projeto acesse a pasta do projeto e digite os seguintes comandos:

~~~
docker-compose up -d
docker-compose exec app bash
~~~
* Após acessar o bash do container faça a migração com comandos:
~~~
python src/manager.py migrate
~~~

* Agora crie um usuario para usar o Django-admin:
~~~
python src/manager.py createsuperuser
~~~

* Agora pode sair do bash do container docker e acessar a url localhost:8000/admin

## Etapas concluídas:

* ADMIN
* LOCALIZACAO
* GEOLOCALIZACAO
* INFRA (docker e docker-compose)

### Etapas não concluídas:

* INFRA: não configurei o projeto para trabalhar com caches,
talvez seja pela inexperiência com o uso do cache e em saber
qual função do software iria utilizar cache porque pelo que eu
estudei o cache deve ser usado em partes que não é necessario a
atualização dos dados constantemente e pela minha analise eu não
encontrei nenhum parte assim do software.

### O que foi fieto além:
* Na busca das propriedades mais proximas de um ponto fiz para que distancia menores que 1 KM
os dados sejam formatador para metros.
