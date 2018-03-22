<!-- Template de Documento de Arquitetura de Software versão em Markdown-->
# **Tropical Hazards**

Documento de Arquitetura
===================

----------
## Histórico  de Revisões

| Data | Versão | Descrição | Autores |
|:----:|:------:|:---------:|:-------:|
| **/03/2018 | 1.0 | Abertura do documento | - |
| **/03/2018 | 1.1 | - | - |
| **/03/2018 | 1.2 | - | - |
| **/03/2018 | 1.3 | - | - |
-----------

Sumário
----------------

* 1. [Introdução](#1-introdução)
    * 1.1 [Finalidade](#11-finalidade)
    * 1.2 [Escopo](#12-escopo)
    * 1.3 [Definições, Acrônimos e Abreviações](#13-definições-acrônimos-e-abreviações)
    * 1.4 [Referências](#14-referências)
    * 1.5 [Visão Geral](#15-visão-geral)
* 2. [Representação da Arquitetura](#2-representação-da-arquitetura)
* 3. [Metas e Restrições de Arquitetura](#3-metas-e-restrições-de-arquitetura)
* 4. [Visão de Casos de Uso](#4-visão-de-casos-de-uso)
    * 4.1 [Realizações de Casos de Uso](#41-realizações-de-casos-de-uso)
* 5. [Visão Lógica](#5-visão-lógica)
    * 5.1 [Visão Geral](#51-visão-geral)
    * 5.2 [Pacotes de Design Significativos do Ponto de Vista da Arquitetura](#52-pacotes-de-design-significativos-do-ponto-de-vista-da-arquitetura)
* 6. [Visão de Processos](#6-visão-de-processos)
* 7. [Visão de Implantação](#7-visão-de-implantação)
* 8. [Visão de Implementação](#8-visão-de-implementação)
    * 8.1 [Visão Geral](#81-visão-geral)
    * 8.2 [Camadas](#82-camadas)
* 9. [Visão de Dados (opcional)](#9-visão-de-dados-opcional)
* 10. [Tamanho e Desempenho](#10-tamanho-e-desempenho)
* 11. [Qualidade](#11-qualidade)
-----------

## 1. Introdução

*[A introdução do Documento de Arquitetura de Software deve apresentar uma visão geral de todo o Documento de Arquitetura de Software. Ela deve incluir a finalidade, o escopo, as definições, os acrônimos, as abreviações, as referências e uma visão geral do Documento de Arquitetura de Software.]*

### 1.1 Finalidade

Este documento apresenta uma visão geral abrangente da arquitetura do sistema e utiliza uma série de visões arquiteturais diferentes para ilustrar os diversos aspectos do sistema. Sua intenção é capturar e transmitir as decisões significativas do ponto de vista da arquitetura que foram tomadas em relação ao sistema.

*[Esta seção define a finalidade do Documento de Arquitetura de Software, na documentação geral do projeto, e contém uma breve descrição da estrutura do documento. Os públicos específicos do documento devem ser identificados, com uma indicação de como devem usá-lo.]*

### 1.2 Escopo

*[Faça uma breve descrição da aplicação do Documento de Arquitetura de Software; o que é afetado ou influenciado por este documento.]*

### 1.3 Definições, Acrônimos e Abreviações

*[Esta subseção deve apresentar as definições de todos os termos, acrônimos e abreviações necessários para a correta interpretação do Documento de Arquitetura de Software. Essas informações podem ser fornecidas mediante referência ao Glossário do projeto.]*

### 1.4 Referências

*[Esta subseção deve apresentar uma lista completa de todos os documentos mencionados no Documento de Arquitetura de Software. Cada documento deve ser identificado por título, número de relatório (se aplicável), data e organização responsável pela publicação. Especifique as fontes das quais é possível obter referências. Essas informações podem ser fornecidas por um anexo ou outro documento.]*

### 1.5 Visão Geral

*[Esta subseção deve descrever o conteúdo restante do Documento de Arquitetura de Software e explicar como o Documento de Arquitetura de Software está organizado.]*

## 2. Representação da Arquitetura

O projeto Tropical Hazards utiliza a  arquitetura MVC, que organiza o sistema em três partes distintas: Model, Controller e View. Para isso, iremos usar das ferramentas de trabalho (frameworks) Django Rest, VueJS e JSon.

No padrão MVC, os componentes estruturais podem ser definidos como:
  Model: Responsável pela estruturação, definição das consultas e validação dos dados. Também é neste nível que são definidos a lógica de aplicação e as regras de negócio referente ao banco de dados do sistema.

  View: É responsável pela definição de como serão feitas todas as interações com o usuário, fazendo contato direto com a camada de controle de onde recebe quais informações serão mostradas. Ou seja, a principal função da View é mostrar a interface gráfica para os usuários e fazer a comunicação com a camada de controle.

  Controller: É responsável pela integração da camada View com a Model, é nela que todas as requisições do usuário são recebidas e as ações dentro do sistema são definidas. Nesta camada também são definidas as regras de negócio referentes à manipulação do sistema.

  ![Figure 2-1](http://abap101.com/wp-content/uploads/2011/08/mvc.png "Figura 2.1 - Padrão MVC (Fonte: http://abap101.com/wp-content/uploads/2011/08/mvc.png)")

  <p>Figura 2.1 - Padrão MVC (Fonte : http://abap101.com/wp-content/uploads/2011/08/mvc.png)</p>

O Django segue o padrão arquitetural próprio dele mesmo, mais conhecido como MVT. De acordo com o Django Book, o Django segue o padrão MVC suficientemente para ser considerado um framework MVC.

#### Como funciona o MTV?

O MTV separa de forma estrutural o projeto em Django em três partes: <b>Model</b>,  <b>View</b>, <b>Template</b>. Fazendo um paralelo com o modelo MVC clássico, as View agora irão fazer o mesmo papel da Controller, e a camada Template o papel das Views. Assim podemos as seguintes definições:

Model: As models do MTV e MVC podem ser consideradas equivalentes em questão de responsabilidade. O framework Django facilita na interface com o banco de dados. Esta camada contém qualquer coisa e tudo sobre os dado: acesso de dados, validação e quais comportamentos se relacionam entre os dados.

View: As views são responsáveis pelas regras que serão apresentadas no nosso sistema. A camada view é onde ela irá se comunicar com a Model e a Template, cadastrando e tratando as informações recebidas. Retornando uma resposta para o usuário.

Template:  Templates é a camada que retorna a visão para o usuário do programa. Essa camada é composta por, HTML,CSS, javascript e etc. Geralmente linguagens focadas na apresentação do site para o usuário.

![Figure 2-2](https://arquivo.devmedia.com.br/artigos/guias/arquitetura_MTV.png "Figura 2.2 - Padrão MTV")
<p>Figura 2.2 - Padrão MTV (Fonte : https://arquivo.devmedia.com.br/artigos/guias/arquitetura_MTV.png)</p>

Apesar do Django fornecer um apoio para a criação de templates e formas de definir interações com os usuários, há ferramentas mais atuais que oferecem mais recursos principalmente quanto a parte de front-end do sistema. Devido a este fato, utilizaremos a ferramenta VueJS para a criação de interfaces.

O VueJS  é um framework de JavaScript, progressivo para a construção de interfaces de usuário, onde é possível construir sistemas com interfaces reativas, modularizadas e de sintaxe clara. Entretanto, esta ferramenta e não consegue fazer contato direto com a camada View do Django. Assim, é necessário que haja uma integração entre as duas ferramentas. Para isso utilizaremos a formatação JSON.

O JSON é uma formatação leve de troca de dados, fácil de ser gerada e interpretada por máquinas. Sua utilização é necessária devido o fato de que as trocas de dados entre interfaces e servidores devem existir somente em formato de texto. Através do JSON é possível converter qualquer objeto JavaScript em texto e qualquer JSON recebido do servidor em objetos JavaScript. Podendo assim trabalhar com os objetos JavaScript como dados comuns.


## 3. Metas e Restrições de Arquitetura

*[Esta seção descreve os requisitos de software e os objetivos que têm um impacto significativo na arquitetura, como proteção, segurança, privacidade, uso de um produto desenvolvido internamente e adquirido pronto para ser usado, portabilidade, distribuição e reutilização. Ela também captura as restrições especiais que podem ser aplicáveis: estratégia de design e implementação, ferramentas de desenvolvimento, estrutura das equipes, cronograma, código-fonte legado e assim por diante.]*

## 4. Visão de Casos de Uso

*[Esta seção lista os casos de uso ou cenários do modelo de casos de uso se eles representam uma funcionalidade central e significativa do sistema final ou se têm uma ampla cobertura de arquitetura, ou seja, se experimentam muitos elementos arquiteturais ou se enfatizam ou ilustram um determinado ponto frágil da arquitetura.]*

### 4.1 Realizações de Casos de Uso

*[Esta seção ilustra o funcionamento do software, apresentando algumas realizações (ou cenários) de casos de uso selecionadas e explica como os diversos elementos do modelo de design contribuem para a respectiva funcionalidade.]*

## 5. Visão Lógica

*[Esta seção descreve as partes significativas do ponto de vista da arquitetura do modelo de design, como sua divisão em subsistemas e pacotes. Além disso, para cada pacote significativo, ela mostra sua divisão em classes e utilitários de classe. Apresente as classes significativas do ponto de vista da arquitetura e descreva suas responsabilidades, bem como alguns relacionamentos, operações e atributos de grande importância.]*

### 5.1 Visão Geral

[Esta subseção descreve toda a decomposição do modelo de design em termos de camadas e de hierarquia de pacotes.]

### 5.2 Pacotes de Design Significativos do Ponto de Vista da Arquitetura

*[Para cada pacote significativo, inclua uma subseção com o respectivo nome, uma breve descrição e um diagrama com todos os pacotes e classes significativos nele contidos.
Para cada classe significativa no pacote, inclua o respectivo nome, uma breve descrição e, opcionalmente, uma descrição de algumas de suas responsabilidades, operações e atributos mais importantes.]*

## 6. Visão de Processos

*[Esta seção descreve a decomposição do sistema em processos leves (threads simples de controle) e processos pesados (agrupamentos de processos leves). Organize a seção em grupos de processos que se comunicam ou interagem. Descreva os modos principais de comunicação entre processos, como transmissão de mensagens e interrupções.]*

## 7. Visão de Implantação

*[Esta seção descreve uma ou mais configurações da rede física (hardware) na qual o software é implantado e executado. Ela é uma visão do Modelo de Implantação. Para cada configuração, ela deve indicar no mínimo os nós físicos (computadores, CPUs) que executam o software e as respectivas interconexões (barramento, LAN, ponto a ponto e assim por diante.) Inclua também um mapeamento dos processos da Visão de Processos nos nós físicos.]*

## 8. Visão de Implementação

*[Esta seção descreve a estrutura geral do modelo de implementação, a divisão do software em camadas e subsistemas no modelo de implementação e todos os componentes significativos do ponto de vista da arquitetura.]*

### 8.1 Visão Geral

*[Esta subseção nomeia e define as diversas camadas e o seu conteúdo, as regras que determinam a inclusão em uma camada específica e as fronteiras entre as camadas. Inclua um diagrama de componentes que mostre os relacionamentos entre as camadas.]*

### 8.2 Camadas

*[Para cada camada, inclua uma subseção com o respectivo nome, uma lista dos subsistemas localizados na camada e um diagrama de componentes.]*

## 9. Visão de Dados (opcional)

*[Uma descrição da perspectiva de armazenamento de dados persistentes do sistema. Esta seção será opcional se os dados persistentes forem poucos ou inexistentes ou se a conversão entre o Modelo de Design e o Modelo de Dados for trivial.]*

## 10. Tamanho e Desempenho

*[Uma descrição das principais características de dimensionamento do software que têm um impacto na arquitetura, bem como as restrições do desempenho desejado.]*

## 11. Qualidade

*[Uma descrição de como a arquitetura do software contribui para todos os recursos (exceto a funcionalidade) do sistema: extensibilidade, confiabilidade, portabilidade e assim por diante. Se essas características tiverem significado especial, como, por exemplo, implicações de proteção, segurança ou privacidade, elas devem ser claramente delineadas.]*
