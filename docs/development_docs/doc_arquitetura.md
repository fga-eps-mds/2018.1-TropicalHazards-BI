# Documento de Arquitetura

Sumário
----------------

* 1 .  [Introdução](#1-introdução)
    * 1.1. [Finalidade](#11-finalidade)
    * 1.2. [Escopo](#12-escopo)
    * 1.3 [Definições, Acrônimos e Abreviações](#13-definições-acrônimos-e-abreviações)
    * 1.4 [Referências](#14-referências)
    * 1.5 [Visão Geral](#15-visão-geral)
* 2 . [Representação da Arquitetura](#2-representação-da-arquitetura)
* 3 . [Metas e Restrições de Arquitetura](#3-metas-e-restrições-de-arquitetura)
* 4. [Visão Geral](#51-visão-geral)
    * 4.1 [Diagrama de pacotes](#41-diagrama-de-pacotes)
    * 4.2 [Pacotes de Design Significativos do Ponto de Vista da Arquitetura](#52-pacotes-de-design-significativos-do-ponto-de-vista-da-arquitetura)
* 5 . [Arquitetura dos Serviços e visão de Implementação](#5-arquitetura-dos-serviços-e-visão-de-implementação)
    * 5.1 [Visão Geral](#51-visão-geral)
    * 5.2 [Micro Serviços e camadas](#52-micro-serviços-e-camadas)
* 6 . [Visão de Dados](#6-visão-de-dados)
-----------

## 1. Introdução

### 1.1 Finalidade

Este documento apresenta uma visão geral abrangente da arquitetura do projeto Tropical Hazards, utilizando de uma série de visões arquiteturais diferentes para ilustrar os diversos aspectos do sistema. Este projeto fora realizado na disciplina Métodos de Densenvolvimento de Software em conjunto com a disciplina Engenharia de Produto de Software, e possui como principal cliente o Núcleo de Medicina Tropical da Faculdade de Medicina da Universidade de Brasília.

### 1.2 Escopo

Neste documento serão descritos os componentes de software, padrões arquiteturais adotados e *frameworks* escolhidos para o desenvolvimento do projeto que tem por objetivo a criação de um sistema que permita acesso e compartilhamento de dados acerca de doenças tropicais. O documento explora a fundo as características da arquitetura e como estas se relacionam com o projeto.

### 1.3 Definições, Acrônimos e Abreviações
<ul>
  <li>NMT: <em>Núcleo de Medicina Tropical</em></li>
  <li>UNB: <em>Universidade de Brasília</em></li>
  <li>MVC: <em>Model-View-Controller</em></li>
  <li>MVT: <em>Model-View-Template</em></li/>
</ul>

### 1.4 Referências

Fundação Universidade Federal do Paraná - Documento de Arquitetura: A estrutura de tópicos do documento de Arquitetura.  http://www.funpar.ufpr.br:8080/rup/webtmpl/templates/a_and_d/rup_sad.htm

### 1.5 Visão Geral
O presente documento faz o detalhamento e descrição de características da arquitetura escolhidas pela equipe de desenvolvimento para a solução no software do projeto Tropical Hazards. Nele estará presente:  Representação da Arquitetura, Metas e Restrições de Arquitetura, Visão Lógica, Visão de Lógica, Visão de Processos, Visão de Implantação, Visão de Implementação, Visão de Dados, Tamanho e Desempenho, Qualidade e Referências bibliográficas.

## 2. Representação da Arquitetura

A arquitetura utilizada contém dois ambientes diferentes para a nossa aplicação, o ambiente de controle de dados que é conhecido como API e o um ambiente web para os usuarios, contemplando um portal onde a população interessada possa ter acesso as informações e um sistema de dashboards onde usuários podem criar seus projetos, importar dados e adicionar colaboradores que podem gerar indicadores baseados nos dados dos projetos.

Com relação a API, o  projeto **Tropical Hazards** será desenvolvido utilizando o framework Django Rest, que conta com um padrão arquitetural próprio conhecido como MVT, o qual será adotado, com algumas alterações, na execução desse projeto.

O Django, segundo o próprio Django Book, segue o padrão MVC suficientemente para que este seja considerado um framework MVC, entretanto deve-se salientar a diferença entre os padrões arquiteturais.

No padrão MVC clássico a aplicação é dividida em três principais componentes interconectados, sendo estes:
<ul>
  <li> <b>Model</b> : é incumbido de tratar a parte lógica relacionada aos dados, sendo encarregado por definir sua estrutura, consultas e validação destes, atentando, obviamente, às regras de negócio relacionadas ao banco de dados.</li>
  <li> <b>View</b> : é responsável pela visualização gráfica da interface de usuário, definindo, portanto, como ocorrerão as interações com o usuário. Deve-se salientar que a View está em contato direto com a Controller, sendo esta última responsável por provêr os dados que serão renderizadas pela View.</li>
  <li> <b>Controller</b> : efetua a comunicação entre a Model e View. As requisições de usuário são processadas pela Controller que efetua as interações necessárias com a Model, enviando as demandas e recebendo dados que são posteriormente enviados para a View. É nesta camada são definidas as regras de negócio referentes à manipulação do sistema.</li>
</ul>

<img src="http://abap101.com/wp-content/uploads/2011/08/mvc.png" alt="Figure 2-1" class="responsive-img">

Figura 2.1 - Padrão MVC (Fonte : http://abap101.com/wp-content/uploads/2011/08/mvc.png)

No padrão MVT utilizado pelo Django ocorre a separação em três partes: **Model**, **View**, **Template**. Fazendo um paralelo com o modelo MVC clássico, a View e o Template do MVT assemelham-se, respectivamente, com a Controller e a View do MVC. Essas partes podem ser melhor definidas como:
<ul>
  <li> <b>Model</b> : a Model do MVT pode ser considerada equivalende a do MVC em termos de responsabilidade, entretanto deve-se notar que o Framework Django facilita na interface com o banco de dados.</li>
  <li> <b>View</b> : na View está contida a lógica de negócio, possuindo a lógica que define o acesso a Model e sendo responsável por enviar e definir quais dados serão exibidos na camada de Template, assemelhando-se, conforme dito anteriormente, a camada Controller do MVC clássico.</li>
  <li> <b>Template</b> : nesta camada são definidos como os dados recebidos através da View serão exibidos ao usuário, sendo, esta camada, responsável por renderizar a interface gráfica do usuário, tal qual a camada View no MVC clássico.</li>
</ul>


Juntamente com o Django utilizaremos utilizaremos uma de suas extenções o Framework Django Rest. Esta ferramenta auxiliara na construção da API do sistema, oferencendo também uma serie de outras ferramentas. Uma dessas ferramentas são os Serializers que possibilitam a conversão de tipos de dados complexos em Python, XML, JSON, entre outras. O Framework Rest também oferecem ferramentas para autenticação, e controle de requerimentos.

No front-end será utilizado o framework em javascript **Vue JS**, uma ferramenta para o desenvolvimento de Single-Page Applications. O **VueJS** desempenhará o papel de unir o template à model sendo necessário que haja uma integração entre as duas ferramentas.
<br>
<br>
<img src="https://i.imgur.com/CnyxnP4.png" alt="Figure 2-3"  class="responsive-img"/>
<br>
<br>

O front-end será desenvolvido utilizando a framework javascript Vue JS. Nesta framework o código é dividido em componentes single file, isto é, cada componente possui o css, javascript e html em um único arquivo.

Esta divisão da página em componentes auxilia no desenvolvimento de Single Page Application, também referidas como SPA. As SPA são aplicações ou sites que interagem com o usuário reescrevendo seu conteúdo de maneira dinâmica ao invés de carregar novas páginas a partir de um servidor. Nesta abordagem não há a interrupção da experiência de usuário com o carregamento de páginas, apresentando um comportamento semelhante a aplicações nativas de desktop.

Para a utilização dessa arquitetura Single Page será utilizada a biblioteca oficial do Vue JS, o Vue-Router. No Vue-Router os componentes tem suas rotas mapeadas e este é responsável por realizar o carregamento dinâmico de seu conteúdo. A comunicação dos componentes do front-end com o back-end ocorrem através de requisições HTTP realizadas para os end-points das APIs do back-end.

<img src="https://i.imgur.com/CbutZ7B.png">

Essa comunicação entre os servidores front-end e back-end ocorre através da notação de dados **JSON** (Java Script Object Notation), devido sua facilidade de ser gerada e interpretada.

Algumas requisições necessitam da autenticação de usuário, para a realização dessa autenticação adotou-se a utilização de Tokens no padrão Json Web Token. Estes tokens possuem todas as informações necessárias para autenticação do usuário no back-end, possuindo como vantagem em relação aos Tokens básicos do REST Framework a existência de uma data de expiração, possuindo, portanto, uma maior segurança.

As informações do usuário obtidas a partir desse token ao efetuar o login são mantidas no front-end de forma compartilhada entre os componentes utilizando a biblioteca Vuex, responsável por manter e atualizar o estado do usuário entre os diversos componentes.

<img src="https://i.imgur.com/DN8Tl90.png">

## 3. Metas e Restrições de Arquitetura
O projeto Tropical Hazards possui as seguintes metas:
<ul>
  <li>Compatibilidade com os principais browsers da atualidade: Mozilla Firefox, Google Chrome e Internet Explorer</li>
  <li>Modularidade: o código deve ter baixo acoplamento e alta modularidade, para facilitar a manutenabilidade</li>
</ul>


Há, também, as seguintes restrições:
<ul>
  <li>Framework Django 2.0.3 com Python 3.5.2</li>
  <li>Django REST: um framework utilizada para construção de WEB APIs</li>
  <li>Banco de dados relacional PostgreSQL, pois o sistema deverá ser executado em produção</li>
  <li>Padrão MVT adapatado com Vue.js cumprindo o papel da camada Template, utilizado pelo framework Django</li>
  <li>Vue.js: uma framework javascript para construção de interfaces de usuário, no sistema irá substituir a camada Template do padrão MVT</li>
</ul>


### 4. Visão Geral

### 4.1 Diagrama de pacotes

O diagrama abaixo representa a arquitetura de pacotes presente no sistema. É possivel notar como que as principais classes do sistema são representadas através destes pacotes, e suas funcionalidades implementadas por meio destes.

<img src="https://raw.githubusercontent.com/fga-gpp-mds/2018.1-TropicalHazards-BI/issue_141_arquitetura_dos_servicos/docs/images/Diagrams/diagrama_de_pacotes.png" class="responsive-img">

### 4.2 Pacotes de Design Significativos do Ponto de Vista da Arquitetura

#### 4.2.1. View
A View será responsável por gerenciar os dados e os comportamentos da aplicação. Ela fará a ligação da model com o Vue JS.

#### 4.2.2 Model
A pasta denominada model trará o conceito de abstração à situação apresentada no mundo real, identificando as entidades a serem utilizadas na aplicação. Além disso, a model deverá garantir a comunicação com o banco de dados.

#### 4.2.3 Test (Teste)
A aplicação de testes durante a implementação de uma aplicação é de extrema importância, por esse motivo, vão ser utilizados dois tipos de testes no projeto: teste de unidade e teste de integração. Haverá no projeto uma pasta teste a fim de englobar os arquivos desenvolvidos para tal atividade.

#### 4.2.4 Serializers
Serializers permitem que os dados complexos, tais como QuerySets e instâncias da model sejam convertidos para tipos de dados Python que podem ser facilmente fundidas em JSON, XML ou outros tipos de conteúdo. Os serializadores também fornecem desserialização, permitindo que os dados analisados ​​sejam convertidos novamente em tipos complexos, após a primeira validação dos dados recebidos.


## 5. Arquitetura dos Serviços e visão de Implementação
Nesta seção está descrita descrita a estrutura geral das camadas e Micro Serviços integrados ao software, detalhando e apresentando a interação entre os diversos serviços e sistemas. Os principais componentes e sub-componentes estão descritos nos tópicos a seguir.

### 5.1 Visão Geral

<img src="https://raw.githubusercontent.com/wiki/fga-gpp-mds/2018.1-TropicalHazards-BI/imagens/servicos.png" class="responsive-img">

### 5.2 Micro Serviços e camadas
Os micro serviços presentes no diagrama estão detalhados abaixo, descrevendo suas comunicações, conexões e justificativas para a escolha dos mesmos.


#### 5.2.1 TropicalHazards_BI (Back-end)

Arquitetura que utiliza o padrão MVT adaptado previamente detalhado e o framework Django Rest. Esta fronteira é responsável pelo tratamento das requisições do usuário para API e por estabelecer as conexões e comunicações com os demais serviços e API's externas. Nesta camada está presente o sistema de autenticação de usuário, gerenciamento de funcionalidades de projetos e dashboards, assim como os meios necessários para garantir a importação e persistência dos dados no banco.

#### 5.2.2 TropicalHazards_BI (Front-end)

Esta fronteira realiza a comunicação com a API do Back-end, lidando ao mesmo tempo com a interação com o usuário e a disponibilidade de informações. Os dados e indicadores gerados nos outros subsistemas são apresentados através desta camada.

#### 5.2.3 MongoDB

O banco de dados não relacional escolhido para o sistema permite uma alta performance e disponibilidade dos dados, além de se adequar para a necessidade dos dados de pesquisas recebidos serem relativamente desestruturados e permitir uma <b>escalabilidade automática</b>.
Com os dados estruturados de maneira semelhante a documentos (ou objetos JSON) é possível estabelecer a comunicação com o serviço do metabase para o processamento dos dados importados e geração de gráficos e indicadores.
A alta disponibilidade devido as facilidades de replicação, redundância de dados, performance com esquemas de indexação e escalabilidade horizontal com sistema de shards foram os principais motivos para a escolha deste banco NoSQL.

#### 5.2.4 Metabase
O serviço principal para o levantamento de indicadores a partir dos dados de pesquisas é o Metabase. Esse serviço faz a comunicação e recebe os dados do banco não relacional, permitindo filtrar, estabelecer conexões entre os dados e apresentar gráficos. O Metabase foi priorizado para integração com a API em relação a outros serviços semelhantes, pois foi testado de acordo com os recursos computacionais disponíveis para o desenvolvimento do projeto, garantindo uma eficiência para o gerenciamento dos dashboards e coleções de dados.


#### 5.2.5 PostgreSQL
O sistema utiliza o banco de dados PostgreSQL além do banco não relacional, para realizar uma conexão com o metabase e também salvar diversos dados referentes ao funcionamento da aplicação e sua estrutura básica, como os dados de usuários e projetos.


#### 5.2.6 Nginx
Servidor de HTTP e proxy reverso. Foi escolhido para integração no sistema por ser gratuito, open source e ter alta performance.

## 6. Visão de Dados
Esta seção apresenta a modelagem e perspectiva da persistência dos dados nos dois bancos integrados ao sistema. A fronteira do id do projeto representa a associação de cada projeto aos diversos dados de pesquisas importados e armazenados no banco não relacional.

<img src="https://i.imgur.com/G3aCHUx.png" class="responsive-img"/>
