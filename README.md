# Tropical Hazards BI

![](https://i.imgur.com/OhSvJLM.jpg)
[![Python 3](https://pyup.io/repos/github/fga-gpp-mds/2018.1-TropicalHazards-BI/python-3-shield.svg)](https://pyup.io/repos/github/fga-gpp-mds/2018.1-TropicalHazards-BI/)
[![Updates](https://pyup.io/repos/github/fga-gpp-mds/2018.1-TropicalHazards-BI/shield.svg)](https://pyup.io/repos/github/fga-gpp-mds/2018.1-TropicalHazards-BI/)
[![Build Status](https://travis-ci.org/fga-gpp-mds/2018.1-TropicalHazards-BI.svg?branch=master)](https://travis-ci.org/fga-gpp-mds/2018.1-TropicalHazards-BI)
[![Coverage Status](https://coveralls.io/repos/github/fga-gpp-mds/2018.1-TropicalHazards-BI/badge.svg?branch=HEAD)](https://coveralls.io/github/fga-gpp-mds/2018.1-TropicalHazards-BI?branch=HEAD)
[![Maintainability](https://api.codeclimate.com/v1/badges/7fc5f5cd8fcb47c363f8/maintainability)](https://codeclimate.com/github/fga-gpp-mds/2018.1-TropicalHazards-BI/maintainability)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Sobre

<p align="justify"> O Observ é uma plataforma online de observatórios de dados científicos com suporte à geração de mapas e gráficos. É intuitivo e colaborativo. O objetivo do sistema é auxiliar os pesquisadores e pessoas interessadas em análise de dados e estatísticas. Permite o gerenciamento e compartilhamento de dados e indicadores do seu projeto de pesquisa, seja qual for o escopo do seu trabalho. Com o Observ você pode fazer análises estatísticas, compartilhar informações gerenciadas em dashboards e disponibilizar esses dados para o público.</p>

## Deploy
[Homolog]()

## Documentação

  Se você quiser saber como utilizar o sistema ou como o mesmo foi projetado, a [documentação](https://github.com/fga-gpp-mds/2018.1-TropicalHazards-BI/tree/master/docs) do projeto pode ser encontrada no link em destaque ou pode ser acessada através do [github pages](https://fga-gpp-mds.github.io/2018.1-TropicalHazards-BI) do projeto. Para contribuir com o projeto solicitamos que acesse o nosso workflow de repositório com a [política de branches](https://fga-gpp-mds.github.io/2018.1-TropicalHazards-BI/workflow/politica_de_branches), [política de commits](https://fga-gpp-mds.github.io/2018.1-TropicalHazards-BI/workflow/politica_de_commit) e [issue workflow](https://fga-gpp-mds.github.io/2018.1-TropicalHazards-BI/workflow/issue_workflow).

## Repositórios
  Foram criados dois repositórios para o desenvolvimento do sistema, divididos em back-end e [front-end](https://github.com/fga-gpp-mds/2018.1-TropicalHazards-BI-FrontEnd). No segundo repositório estão as dependências e configurações para o ambiente de desenvolvimento com vue.js . O repositório atual é dedicado ao back-end, assim como a documentação do sistema.

## Instalação
  Nesta seção está descrito cada passo necessário para a configuração e utilização da aplicação.

  #### Pré-requisitos
  * [Git](https://git-scm.com/)
  * [Docker](https://www.docker.com/get-docker)
  * [Docker-composer](https://docs.docker.com/compose/install/#install-compose)

  #### Configuração

  Clone o repositório no diretório desejado
  ```bash
  git clone https://github.com/fga-gpp-mds/2018.1-TropicalHazards-BI.git
  ```
  
  Copie o arquivo referente as variáveis de ambiente necessárias para configuração da aplicação
  ```bash
  cp env.tmpl .env
  ```

  Utilize o seguinte comando para subir a aplicação
  ```bash
  docker-compose up
  ```

  A aplicação pode ser acessada através do localhost:
  ```
  localhost:8000
  ```

## Sobre a equipe
  [Entre em contato](https://fga-gpp-mds.github.io/2018.1-TropicalHazards-BI/project_artefacts/tap/#10-lista-das-partes-interessadas) com a nossa equipe ou descubra mais sobre as pessoas por trás do projeto e desenvolvimento do sistema.

## Licença
 [MIT](https://github.com/fga-gpp-mds/2018.1-Grupo3/blob/development/LICENSE)
