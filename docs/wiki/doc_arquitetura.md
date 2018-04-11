# **Tropical Hazards**

Documento de Arquitetura
===================



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
* 4 . [Visão Lógica](#5-visão-lógica)
    * 4.1 [Visão Geral](#51-visão-geral)
    * 4.2 [Pacotes de Design Significativos do Ponto de Vista da Arquitetura](#52-pacotes-de-design-significativos-do-ponto-de-vista-da-arquitetura)
* 5 . [Visão de Processos](#6-visão-de-processos)
* 6 . [Visão de Implantação](#7-visão-de-implantação)
* 7 . [Visão de Implementação](#8-visão-de-implementação)
    * 7.1 [Visão Geral](#81-visão-geral)
    * 7.2 [Camadas](#82-camadas)
* 8 . [Visão de Dados (opcional)](#9-visão-de-dados-opcional)
* 9 . [Tamanho e Desempenho](#10-tamanho-e-desempenho)
* 10 . [Qualidade](#11-qualidade)
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

A arquitetura utilizada contém dois ambientes diferentes para a nossa aplicação, o ambiente de controle de dados que é conhecido como API e o um ambiente web para os usuarios, contemplando um portal onde a população interessada possa ter acesso as informações e um sistema de dash boards para usuários gerenciadores de conteúdo, podem assim inserir, compartilhar e salvar dados através da aplicação.

Com relação a API o  projeto **Tropical Hazards** será desenvolvido utilizando o framework Django Rest, que conta com um padrão arquitetural próprio conhecido como MVT, o qual será adotado, com algumas alterações, na execução desse projeto.

Django, segundo o próprio Django Book, segue o padrão MVC suficientemente para que este seja considerado um framework MVC, entretanto deve-se salientar a diferença entre os padrões arquiteturais.

No padrão MVC clássico a aplicação é dividida em três principais componentes interconectados, sendo estes:
<ul>
  <li> <b>Model</b> : é incumbido de tratar a parte lógica relacionada aos dados, sendo encarregado por definir sua estrutura, consultas e validação destes, atentando, obviamente, às regras de negócio relacionadas ao banco de dados.</li>
  <li> <b>View</b> : é responsável pela visualização gráfica da interface de usuário, definindo, portanto, como ocorrerão as interações com o usuário. Deve-se salientar que a View está em contato direto com a Controller, sendo esta última responsável por provêr os dados que serão renderizadas pela View.</li>
  <li> <b>Controller</b> : efetua a comunicação entre a Model e View. As requisições de usuário são processadas pela Controller que efetua as interações necessárias com a Model, enviando as demandas e recebendo dados que são posteriormente enviados para a View. É nesta camada são definidas as regras de negócio referentes à manipulação do sistema.</li>

![Figure 2-1](http://abap101.com/wp-content/uploads/2011/08/mvc.png "Figura 2.1 - Padrão MVC (Fonte: http://abap101.com/wp-content/uploads/2011/08/mvc.png)")

<p>Figura 2.1 - Padrão MVC (Fonte : http://abap101.com/wp-content/uploads/2011/08/mvc.png)</p>

No padrão MVT utilizado pelo Django ocorre a separação em três partes: **Model**, **View**, **Template**. Fazendo um paralelo com o modelo MVC clássico, a View e o Template do MVT assemelham-se, respectivamente, com a Controller e a View do MVC. Essas partes podem ser melhor definidas como:
<ul>
  <li> <b>Model</b> : a Model do MVT pode ser considerada equivalende a do MVC em termos de responsabilidade, entretanto deve-se notar que o Framework Django facilita na interface com o banco de dados.</li>
  <li> <b>View</b> : na View está contida a lógica de negócio, possuindo a lógica que define o acesso a Model e sendo responsável por enviar e definir quais dados serão exibidos na camada de Template, assemelhando-se, conforme dito anteriormente, a camada Controller do MVC clássico.</li>
  <li> <b>Template</b> : nesta camada são definidos como os dados recebidos através da View serão exibidos ao usuário, sendo, esta camada, responsável por renderizar a interface gráfica do usuário, tal qual a camada View no MVC clássico.</li>
</ul>
<br>

Juntamente com o Django utilizaremos utilizaremos uma de suas extenções o Framework Django Rest. Esta ferramenta auxiliara na construção da API do sistema, oferencendo também uma serie de outras ferramentas. Uma dessas ferramentas são os Serializers que possibilitam a conversão de tipos de dados complexos em Python, XML, JSON, entre outras. O Framework Rest também oferecem ferramentas para autenticação, e controle de requerimentos.

No frontend será utilizado o framework em javascript **Vue JS**, uma ferramenta para o desenvolvimento de Single-Page Applications. O **VueJS** desempenhará o papel de unir o template à model sendo necessário que haja uma integração entre as duas ferramentas.
<br>
<br>
![Figure 2-3](https://i.imgur.com/CnyxnP4.png)
<br>
<br>
<p align="justify">
Este framework de JavaScript possibilita o desenvolvimento de interfaces para o usuários com componentes reativos, ou seja pedaços de código reaproveitáveis formados por marcação, estilo e comportamento.  Entretanto, esta ferramenta e não consegue fazer contato direto com a camada View do Django, para isso utilizaremos a formatação JSON.  

O **JSON** (Java Script Object Notation) é uma formatação leve de troca de dados, fácil de ser gerada e interpretada por máquinas. Sua utilização é necessária devido o fato de que as trocas de dados entre interfaces e servidores devem existir somente em formato de texto. Através do JSON é possível converter qualquer objeto JavaScript em texto e qualquer JSON recebido do servidor em objetos JavaScript. Podendo assim trabalhar com os objetos JavaScript como dados comuns.
</p>


## 3. Metas e Restrições de Arquitetura
O projeto Tropical Hazards possui as seguintes metas:
<ul>
  <li>Compatibilidade com os principais browsers da atualidade: Mozilla Firefox, Google Chrome e Internet Explorer</li>
  <li>Modularidade: o código deve ter baixo acoplamento e alta modularidade, para facilitar a manutenabilidade</li>
</ul>
<br>
Há, também, as seguintes restrições:
<ul>
  <li>Framework Django 2.0.3 com Python 3.5.2</li>
  <li>Django REST: um framework utilizada para construção de WEB APIs</li>
  <li>Banco de dados relacional PostgreSQL, pois o sistema deverá ser executado em produção</li>
  <li>Padrão MVT adapatado com Vue.js cumprindo o papel da camada Template, utilizado pelo framework Django</li>
  <li>Vue.js: uma framework javascript para construção de interfaces de usuário, no sistema irá substituir a camada Template do padrão MVT</li>
</ul>

## 4. Visão Lógica

*[Esta seção descreve as partes significativas do ponto de vista da arquitetura do modelo de design, como sua divisão em subsistemas e pacotes. Além disso, para cada pacote significativo, ela mostra sua divisão em classes e utilitários de classe. Apresente as classes significativas do ponto de vista da arquitetura e descreva suas responsabilidades, bem como alguns relacionamentos, operações e atributos de grande importância.]*

### 4.1 Visão Geral

### 4.1.2 Diagrama de pacotes

O diagrama abaixo representa a arquitetura de pacotes presente no sistema. É possivel notar como que as principais classes do sistema são representadas através destes pacotes, e suas funcionalidades implementadas por meio destes.

<img src="images/Diagrams/diagrama_de_pacotes.png" alt="diagrama de arquitetura" class="responsive-img">

### 4.2 Pacotes de Design Significativos do Ponto de Vista da Arquitetura

#### 4.2.1. View
A View será responsável por gerenciar os dados e os comportamentos da aplicação. Ela fará a ligação da model com o Vue JS .

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
<p align="justify">Os micro serviços presentes no diagrama estão detalhados abaixo, descrevendo suas comunicações, conexões e justificativas para a escolha dos mesmos.</p>


#### 5.2.1 TropicalHazards_BI (Back-end)

<p align="justify">Arquitetura que utiliza o padrão MVT adaptado previamente detalhado e o framework Django Rest. Esta fronteira é responsável pelo tratamento das requisições do usuário para API e por estabelecer as conexões e comunicações com os demais serviços e API's externas. Nesta camada está presente o sistema de autenticação de usuário, gerenciamento de funcionalidades de projetos e dashboards, assim como os meios necessários para garantir a importação e persistência dos dados no banco.</p>

#### 5.2.2 TropicalHazards_BI (Front-end)

<p align="justify">Esta fronteira realiza a comunicação com a API do Back-end, lidando ao mesmo tempo com a interação com o usuário e a disponibilidade de informações. Os dados e indicadores gerados nos outros subsistemas são apresentados através desta camada.</p>

#### 5.2.3 MongoDB

<p align="justify">O banco de dados não relacional escolhido para o sistema permite uma alta performance e disponibilidade dos dados, além de se adequar para a necessidade dos dados de pesquisas recebidos serem relativamente desestruturados e permitir uma <b>escalabilidade automática</b>. Com os dados estruturados de maneira semelhante a documentos (ou objetos JSON) é possível estabelecer a comunicação com o serviço do metabase para o processamento dos dados importados e geração de gráficos e indicadores. A alta disponibilidade devido as facilidades de replicação, redundância de dados, performance com esquemas de indexação e escalabilidade horizontal com sistema de shards foram os principais motivos para a escolha deste banco NoSQL.</p>

#### 5.2.4 Metabase
<p align="justify">O serviço principal para o levantamento de indicadores a partir dos dados de pesquisas é o Metabase. Esse serviço faz a comunicação e recebe os dados do banco não relacional, permitindo filtrar, estabelecer conexões entre os dados e apresentar gráficos. O Metabase foi priorizado para integração com a API em relação a outros serviços semelhantes, pois foi testado de acordo com os recursos computacionais disponíveis para o desenvolvimento do projeto, garantindo uma eficiência para o gerenciamento dos dashboards e coleções de dados.</p>


#### 5.2.5 PostgreSQL
<p align="justify">O sistema utiliza o banco de dados PostgreSQL além do banco não relacional, para realizar uma conexão com o metabase e também salvar diversos dados referentes ao funcionamento da aplicação e sua estrutura básica, como os dados de usuários e projetos.</p>


#### 5.2.6 Nginx
<p align="justify">Servidor de HTTP e proxy reverso. Foi escolhido para integração no sistema por ser gratuito, open source e ter alta performance.</p>

## 6. Visão de Dados

*[Uma descrição da perspectiva de armazenamento de dados persistentes do sistema. Esta seção será opcional se os dados persistentes forem poucos ou inexistentes ou se a conversão entre o Modelo de Design e o Modelo de Dados for trivial.]*
