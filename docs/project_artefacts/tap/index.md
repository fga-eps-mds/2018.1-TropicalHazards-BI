# Termo de Abertura do Projeto

[1. Introdução](#1-introdução)

[2. Termos e definições](#2-termos-e-definições)

[3. Descrição do Projeto](#3-descrição-do-projeto)

[4. Propósito e justificativa do projeto](#4-propósito-e-justificativa-do-projeto)  

[5. Objetivos do projeto](#5-objetivos-do-projetosmart)  

[6. Requisitos de alto nível](#6-requisitos-de-alto-nível)

[7. Riscos](#7-riscos)

[8. Resumo do cronograma de marcos](#8-resumo-do-cronograma-de-marcos)

[9. Resumo do orçamento](#9-custo-estimado-do-projeto)  

[10. Partes interessadas](#10-lista-das-partes-interessadas)

[11. Requisitos para aprovação do projeto](#11-requisitos-para-a-aprovação-do-projeto)

[12. Gerência do projeto](#12-gerência-do-projeto)

[13. Referências](#13-referências)


## 1. Introdução
O presente documento tem como objetivo formalizar o início do projeto Tropical Hazards BI, descrevendo o planejamento inicial de custos, riscos, tempo, restrições e cronograma de marcos. Assim como expor os objetivos e contexto de aplicação da solução e as partes interessadas envolvidas no projeto.

## 2. Termos e definições
Esta seção representa um dicionário dos diversos  termos utilizados na descrição do projeto, procurando apresentar suas respectivas definições de acordo com os contextos do problema e organização.

<table class="responsive-table highlight bordered">
    <thead>
      <tr>
        <th>Termo</th>
        <th>Descrição</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Dados de pesquisas</td>
        <td>Coleção de dados e informações relacionadas a doenças tropicais que foram previamente tratadas e devem ser disponibilizadas.</td>
      </tr>  
      <tr>
        <td>Indicadores</td>
        <td>São levantados a partir da seleção de certos dados de pesquisas e consistem em métricas objetivas, de claro entendimento e compreensão, que transmitem informações relevantes para um determinado contexto ou estudo.</td>
      </tr>
      <tr>
        <td>Observatório ou Dashboard</td>
        <td>Funcionalidade do sistema responsável pela apresentação dos indicadores para os profissionais do NMT ou interessados.</td>
      </tr>   
      <tr>
        <td>Projeto</td>
        <td>No contexto de um usuário do NMT utilizando o sistema, um projeto possui funcionamento semelhante a um repositório de dados, ou seja, existe uma organização principal onde cada profissional pode criar um projeto pessoal que disponibiliza dados de pesquisas para diferentes observatórios.</td>
      </tr>
</table>

## 3. Descrição do Projeto
O Tropical Hazards BI é um sistema de Observatório de Dados direcionado para pesquisadores e profissionais de saúde do Núcleo de Medicina Tropical (NMT) da Universidade de Brasília (UNB) que visa atender à necessidade de visualização de dados e geração de indicadores dos seus diferentes projetos em uma mesma plataforma.


## 4. Propósito e Justificativa do Projeto
O Núcleo de Medicina Tropical possui um núcleo responsável por desenvolver pesquisas relacionadas a doenças tropicais. Os vários projetos de pesquisa não possuem tecnologias em comum nem um observatório/dashboard padronizado. Além disso, os pesquisadores apresentam os dados obtidos entre si por meio de arquivos ou no próprio computador pessoal, sem acesso remoto ou padronização de visualização.


Dessa forma, o software Tropical Hazards BI propõe uma exibição de dados coletados pelos pesquisadores de forma centralizada, assim como a geração de indicadores relevantes para as pesquisas e sua análise estatística, a fim de melhorar a visualização de informações relevantes para os pesquisadores de diferentes frentes de pesquisas do NMT.


## 5. Objetivos do Projeto (SMART)
O objetivo do projeto é criar um observatório de dados e indicadores baseado em dashboards pessoais compartilháveis para os profissionais do Núcleo de Medicina Tropical da UnB até a data de entrega da Release 2.


O projeto tem como critério de sucesso trabalhar com os diferentes contextos de dados relacionados a doenças tropicais, além de aceitar os seguintes padrões de armazenamento de dados utilizados pelo NMT: JSON, CSV, EXCEL e Banco de Dados.

## 6. Requisitos de Alto Nível
 O Tropical Hazards BI será uma plataforma web que concentra a visualização de dados dos diferentes projetos de pesquisas do NMT por pesquisadores e interessados. Entre os requisitos de alto nível tem-se:
     <ul>
        <li>O sistema dever ser de fácil manuseio;</li>
        <li>Os indicadores levantadas devem ser apresentados por meio de um dashboard;</li>
        <li>O design deve ser simples e minimalista;</li>
        <li>Um projeto criado por um profissional do NMT deve disponibilizar acesso aos seus dados para os diversos observatórios;</li>
    </ul>


## 7. Riscos
Os principais riscos do desenvolvimento do Tropical Hazards BI e suas ações preventivas são:
<table class="responsive-table highlight bordered">
    <thead>
      <tr>
        <th>Riscos</th>
        <th>Ações Preventivas</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Membro trancar ou abandonar a disciplina.</td>
        <td>Distribuir as tarefas de maneira proporcional, sem sobrecarregar os membros da equipe.</td>
      </tr>  
      <tr>
        <td>Time de desenvolvimento pouco integrado.</td>
        <td>Promover encontros constantes para sanar dificuldades, incentivar a colaboração entre os membros da equipe.</td>
      </tr>  
      <tr>
        <td>Equipe de desenvolvimento sem capacidade técnica.</td>
        <td>Realização de treinamentos para melhorar o conhecimento da equipe e criação de canal de comunicação exclusivo para sanar dúvidas.</td>
      </tr>
      <tr>
        <td>Comunicação falha entre o time.</td>
        <td>Proporcionar uma boa integração entre os membros da equipe com a exposição das atividades executadas entre eles, utilizar um meio de comunicação comum a todos os membros, manter encontros agendados e constantes para sanar dúvidas e dificuldades no projeto, acompanhar as atividades dos membros.</td>
        </tr>
      <tr>
        <td>Membro do time que faz estágio.</td>
        <td>Conscientizar o membro do time quanto ao comprometimento necessário para a execução do projeto e monitorar a organização de horários desse membro. </td>
      </tr>
    </tbody>  
</table>


## 8. Resumo do cronograma de marcos
As disciplinas de Métodos de Desenvolvimento de Software (MDS) e Engenharia de Produto de Software (EPS) definem eventos importantes para o projeto desenvolvido por seus alunos. São eles:
<ul>
  <li>Início do projeto (06/03/2018): Início das disciplinas e preparação para o projeto.</li>
  <li>Release 1 (19/04/2018): Apresentação das funcionalidades implementadas, bem como documentação referente a esse período.</li>
  <li>Release 2 (data a definir):  Apresentação das funcionalidades restantes previstas para o escopo.</li>
</ul>


## 9. Custo Estimado do Projeto
### 9.1. Recursos Humanos
O valor médio de um aluno de Engenharia de Software da UnB, de acordo com o Relatório de Gestão 2016³, é R$ 26.040,00. Levando em consideração o tempo de curso de 5 anos (10 semestres) e a necessidade da obtenção de 240 créditos para a graduação, estima-se que cada aluno pegue 24 créditos por semestre, totalizando 48 créditos por ano. Como cada crédito é estimado em 15 horas por aula tem-se o seguinte custo por hora de cada aluno:
<b>26.040 / (15*48) = 36,17</b>

A equipe é composta por 10 membros e 3 Coachs, sendo todos estudantes de Engenharia de Software da UnB. Considerando que cada membro trabalhará 10 horas por semana e cada Coach auxiliará a equipe durante 2 horas por semana durante as 18 semanas de desenvolvimento do projeto, temos o seguinte custo:
<table style="text-align: center" class="responsive-table highlight bordered">
    <thead>
        <tr>
            <th></th>
            <th>Quantidade</th>
            <th>Horas/semana</th>
            <th>Semanas</th>
            <th>Preço por membro</th>
            <th>Custo Final</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>Membros</b></td>
            <td>10</td>
            <td>10</td>
            <td>18</td>
            <td>36,17</td>
            <td>65.106,00</td>
        </tr>
        <tr>
            <td><b>Coachs</b></td>
            <td>3</td>
            <td>2</td>
            <td>18</td>
            <td>36,17</td>
            <td>3.906,36</td>
        </tr>
        <tr>
            <td><b>Total</b></td>
            <td>13</td>
            <td>12</td>
            <td>18</td>
            <td>36,17</td>
            <td><b>69.012,36</b></td>
        </tr>
    </tbody>
</table>

### 9.2. Equipamentos de Trabalho

  Para a efetiva realização das atividades relacionadas ao projeto, cada integrante da equipe de trabalho necessitará
  de um notebook, para a codificação do projeto e para a elaboração de documentos e internet banda larga.<br>
  Os requisitos mínimos para cada um desses aparelhos e serviços são:


<table style="text-align: center" class="responsive-table highlight bordered">
  <thead>
    <tr>
      <th>Equipamento</th>
      <th>Requisitos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Notebook</td>
      <td>
        <ul>
          <li>500Gb de HDD.</li>
          <li>Mínimo de 4Gb de memória RAM</li>
          <li>Processador core i5-7200u ou superior.</li>
          <li>Sistema operacional Linux baseado em Debian.</li>
          <li>Carregador bivolt.</li>          
        </ul>
      </td>
    </tr>
      </tbody>
</table>


  Com base nos requisitos listados acima, e após minuciosa pesquisa no mercado nacional, foi levantada a seguinte tabela de custos de equipamento:

<table style="text-align: center" class="responsive-table highlight bordered">
  <thead>
    <tr>
      <th>Equipamento</th>
      <th>Nome</th>
      <th>Preço unit.</th>
      <th>Quantidade</th>
      <th>Custo final</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Notebook</td>
      <td>Acer aspire ES1-572-52M5</td>
      <td>R$ 1.999,99</td>
      <td>10</td>
      <td>R$ 19.999,90</td>
    </tr>
   </tbody>
</table>


  Assim, o orçamento a ser gasto com os equipamentos de trabalho é de <strong>R$ 26.694,90</strong>.


### 9.3. Licenças de serviços

  A equipe do projeto optou pelo uso de softwares livres para serem usados durante toda a vida útil do projeto, acarretando em nenhum custo com a aquisição de softwares.


### 9.4. Serviços

 Para a realização das atividades do projeto é necessário acesso a Internet Banda larga com o seguintes requisitos mínimos:

<table class="responsive-table highlight bordered">
  <thead>
    <tr>
      <th>Equipamento</th>
      <th>Requisitos</th>
  <tbody>
    <tr>
      <td>Internet</td>
      <td>
        <ul>
          <li>Banda Larga.</li>
          <li>20MB de velocidade.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

  Com base nos requisitos listados acima, e após análise de mercado, foi levantada a seguinte tabela de custos:


<table class="responsive-table highlight bordered">
  <thead>
    <tr>
      <th>Serviço</th>
      <th>Nome</th>
      <th>Preço unit.</th>
      <th>Quantidade</th>
      <th>Tempo(meses)</th>
      <th>Custo final</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Internet</td>
      <td>NET Banda larga de 20MB</td>
      <td>R$ 59,90</td>
      <td>10</td>
      <td>5</td>
      <td>R$ 2.995,00</td>
    </tr>
  </tbody>
</table>

### 9.5. Totais

  Levando em conta os custos retratados anteriormente, e levando em conta uma margem de segurança de orçamento de 15% do valor total, se obtém a seguinte tabela contendo o resultado orçamentário final:


<table class="responsive-table highlight bordered">
  <thead>
    <tr>
      <th>Área</th>
      <th>Custo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Recursos humanos</td>
      <td>R$ 69.012,36</td>
    </tr>
    <tr>
      <td>Equipamentos</td>
      <td>R$ 19.999,90</td>
    </tr>
    <tr>
      <td>Licensas</td>
      <td>R$ 0,00</td>
    </tr>
    <tr>
      <td>Serviços</td>
      <td>R$ 2.995,00</td>
    </tr>
    <tr>
      <td><strong>Custo previsto</strong></td>
      <td>R$ 92.007,26</td>
    </tr>
    <tr>
      <td><strong>Margem de segurança (15%)</strong></td>
      <td>R$ 13.801,09</td>
    </tr>
    <tr>
      <td><strong>Custo total</strong></td>
      <td><strong>R$ 105.808,35</strong></td>
    </tr>
  </tbody>
</table>

## 10. Lista das partes interessadas
<ul>
  <li>Profissionais da área da saúde: Profissionais que desejam conhecer os dados estatísticos referentes a pesquisas de doenças tropicais.</li>
  <li>Pesquisadores do Núcleo de Medicina Tropical (NMT): Pesquisadores que desejam visualizar os dados, gerar indicadores, e analisar estatisticamente informações de doenças relevantes para suas pesquisas.</li>
  <li>Equipe de Engenharia de Produto de Software (EPS):
  Alunos do curso de Engenharia de Software da Universidade de Brasília (UNB) da disciplina de Engenharia de Produto de Software (EPS), responsáveis pelo gerenciamento do projeto.</li>
</ul>

<table class="responsive-table highlight bordered">
  <tr>
    <th>Nome</th>
    <th>Email</th>
  </tr>
  <tr>
    <td>André de Sousa Costa Filho</td>
    <td>andre.filho001@outlook.com</td>
  </tr>
  <tr>
    <td>Arthur José Benedito de Oliveira Assis</td>
    <td>arthur120496@gmail.com</td>
  </tr>
  <tr>
    <td>Iago Vasconcelos de Carvalho </td>
    <td>iagovc_2012@hotmail.com</td>
  </tr>
  <tr>
    <td>Matheus Batista Silva</td>
    <td>matheusbattista@hotmail.com</td>
  </tr>
  <tr>
    <td>Renata Francelino de Souza</td>
    <td>renata.rfsouza@gmail.com</td>
  </tr>
</table>

* Equipe de Desenvolvimento de Software:
Alunos do curso de Engenharia de Software da Universidade de Brasília (UNB) da disciplina de Métodos de Desenvolvimento de Software (MDS), responsáveis pelo desenvolvimento do software do projeto.  
<table class="responsive-table highlight bordered">
  <tr>
    <th>Nome</th>
    <th>Email</th>
  </tr>
  <tr>
    <td>Andre Hernandez Bargas </td>
    <td>andrebargas@gmail.com</td>
  </tr>
  <tr>
    <td>Eduardo Rodrigues Yoshida</td>
    <td>eduardoyosh@gmail.com</td>
  </tr>
  <tr>
    <td>João Pedro Gomes</td>
    <td>joaok8@gmail.com</td>
  </tr>
  <tr>
    <td>Max Henrique Barbosa</td>
    <td>maxhb.df@gmail.com</td>
  </tr>
  <tr>
    <td>Pedro Daniel Carvalho Matias</td>
    <td>pedrodaniel.unb@gmail.com</td>
  </tr>
</table>

* Product Owner:
É aluno da Universidade de Brasília que atua no projeto como representante do cliente.
<table class="responsive-table highlight bordered">
  <tr>
    <th>Nome</th>
    <th>Email</th>
  </tr>
  <tr>
    <td> Jonathan Henrique Maia de Moraes</td>
    <td>arkyebr@gmail.com</td>
  </tr>
  <tr>
    <td> Lucas Brilhante</td>
    <td>brilhante82@gmail.com</td>
  </tr>
  <tr>
    <td>Pedro Ivo Andrade</td>
    <td>andradepedroivo@gmail.com</td>
  </tr>
</table>


## 11. Requisitos para a aprovação do projeto
O principal critério para aprovação do projeto é sua validação pelo cliente após sua finalização. Para que o projeto possa ser validado o mesmo deve apresentar os requisitos funcionais e não funcionais solicitados pelo cliente, assim como a documentação necessária para sua utilização.


O projeto deve ainda satisfazer as exigências e necessidades de ambas as disciplinas envolvidas em seu desenvolvimento, cumprindo as datas estabelecidas para entrega dos diversos artefatos.


## 12. Gerência do Projeto
A equipe de gerência do projeto é formada por alunos de graduação de Engenharia de Software da Universidade de Brasília, campus Gama, que cursam a disciplina Engenharia de Produto de Software. Os alunos são responsáveis por planejar, executar e monitorar os processos relacionados ao projeto.


## 13. Referências

<ul>
  <li>PMI. Um guia do conhecimento em gerenciamento de projetos. Guia PMBOK® 5a. ed. - EUA: Project Management Institute, 2013</li>

  <li>Relatório de Gestão, Universidade de Brasília. Disponível em &lthttp://www.dpo.unb.br/index.php?option=com_phocadownload&view=category&download=558:relatorio-2016&id=1:relatorio-de-gestao&Itemid=675&gt</li>

  <li>MONTES, Eduardo. TERMO DE ABERTURA DO PROJETO. Disponível em &lthttps://escritoriodeprojetos.com.br/termo-de-abertura-do-projeto> Acesso em 05/04/2017</li>

  <li>BUILDER, Project. O QUE É TERMO DE ABERTURA DO PROJETO. Disponível em &lthttp://www.projectbuilder.com.br/blog-home/entry/projetos/o-que-e-o-termo-de-abertura-do-projeto&gt Acesso em 05/04/2017</li>
</ul>
