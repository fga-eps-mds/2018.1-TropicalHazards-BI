### Histórico de Versões


<table>

   <tr>
	   	<td> <strong>Data</strong> </td>
	   	<td> <strong>Versão</strong> </td>
	   	<td> <strong>Descrição</strong> </td>
	   	<td> <strong>Autor(es)</strong> </td>
   </tr>


   <tr>
	   	<td>16/03/2018</td>
                <td>1.0.0</td>
	   	<td>Adicionando template com informações iniciais</td>
	   	<td>João Pedro, Andre Bargas, Yoshida, Pedro Daniel</td>
   </tr>

</table>

<hr>

# Sumário

1.[Introdução](#)

 1.1 [Propósito](#)

 1.2 [Escopo](#)

 1.3 [Definições, acrônimos e abreviações](#)

 1.4 [Referências](#)

 1.5 [Visão Geral](#)

2.[Posicionamento](#)

 2.1 [Oportunidade de Negócio](#)

 2.2 [Descrição do Problema](#)

 2.3 [Instrução de Posição do Produto](#)

3.[Descrições da parte interessada e dos Usuários](#)

 3.1 [Resumo dos Usuários](#)

 3.2 [Ambiente do Usuário](#)

 3.3 [Perfis dos Envolvidos](#)

 3.4 [Perfis dos Usuários](#)

 3.5 [Principais Necessidades dos Usuários ou dos Envolvidos](#)

 3.6 [Alternativas e Concorrência](#)

4.[Visão Geral do Produto](#)

5.[Recursos do Produto](#)

6.[Restrições](#)

 6.1 [Restrições de Design](#)

 6.2 [Restrições de Implementação](#)

 6.3 [Restrições de Segurança](#)

 6.4 [Restrições de Uso](#)

# 1. Introdução

## 1.1	Propósito

<p align = "justify">O documento de visão tem como objetivo demonstrar uma visão completa sobre o <em>Webapp</em> Tropical Hazards BI deixando claro o seu escopo, funcionalidade e objetivo da aplicação.</p>

## 1.2	Escopo

<p align= "justify">O projeto Tropical Hazards BI tem como finalidade suprir uma necessidade dos pesquisadores e profissionais de saúde da NMT da Unb de receber dados referentes a doenças tropicais, fazer uma análise estatística dos dados recebidos, mostrar indicadores e dados para os profissionais e público interessado.</p>
<p align="justif">O software, a ser implementado, deve permitir que os profissionais de saúde e pesquisadores possuam perfis para gerenciar dados, levantar indicadores, exportar e compartilhar relatórios</p>

## 1.3	Definições, acrônimos e abreviações

<ul>
<li>FGA - Faculdade do Gama (UnB)</li>
<li>UnB - Universidade de Brasília</li>
<li>MDS - Métodos de Desenvolvimento de Software</li>
<li>EPS - Engenharia de Produto de software</li>
<li>MVT - Model View Template</li>
<li>NMT - Núcleo de medicina tropical</li>
</ul>

## 1.4 Referências

IBM Knowledge Center - Documento de Visão: A estrutura de tópicos do documento de visão. Disponível em: <https://www.ibm.com/support/knowledgecenter/pt-br/SSWMEQ_3.0.1/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.htm>. Acesso em: 22 ago. 2017;

PMI. Um guia do conhecimento em gerenciamento de projetos. Guia PMBOK® 5a. ed. - EUA: Project Management Institute, 2013

BATISTA, Matheus; ARAÚJO, Igor; WILLER, Guilherme; OLIVEIRA, Vinícius; BARCELOS, Filipe; SOUSA, André. Projeto Escola X: Documento de Visão. Disponível em: https://github.com/fga-gpp-mds/2017.1-Escola-X/wiki. Acesso em 22 ago. 2017;


## 1.5 Visão geral

<p align ="justify">Este documento é dividido em 7 tópicos descrevendo os detalhes das características do software proposto. Sendo dividido em:</p>
<ul>
<li><strong>Introdução</strong>: no qual é introduzido os detalhes gerais sobre a visão do projeto;</li>
<li><strong>Posicionamento</strong>: descrevendo o problema e a oportunidade de negócio;</li>
<li><strong>Descrições dos Envolvidos e dos Usuários</strong>: esta seção descreve o perfil das partes interessadas no projeto;</li>
<li><strong>Visão Geral do Produto</strong>: Esta seção fornece uma visualização de alto nível das capacidades do produto, interfaces para outros aplicativos e configurações dos sistemas;</li>
<li><strong>Recursos do Produto</strong>: breve descrição dos recursos do produto;</li>
<li><strong>Restrições</strong>: as restrições de design, restrições externas, como requisitos operacionais ou regulamentares;</li>
</ul>


<h1>2. Posicionamento</h1>


<h2>2.1 Oportunidade de Negócio</h2>

<p align = "justify"> Pesquisadores da Universidade de Brasília(Unb) precisam resolver um problema de automatizar a análise estatística de dados referentes as doenças tropicais, sendo que esses dados não possuem um padrão definido.</p>

<p align = "justify">Para o profissional de saúde e pesquisadores o, <em>webapp</em> terá uma série de ferramentas para utilizar e gerenciar dados com indicadores.</p>

<p align = "justify">Para os usuários serão disponibilizados uma interface web onde podera ser encontrar informações sobre as principais doenças tropicais e seus indicativos.</p>


### 2.2 Descrição do problema

<table>

   <tr>
	   	<td><strong>O problema </strong> </td>
	   	<td>Falta de informações sobre doenças tropicais.></td>
   </tr>


   <tr>
	   	<td><strong>Afeta</strong> </td>
	   	<td>População geral.</td>
   </tr>


   <tr>
	   	<td><strong>Cujo o Impacto é</strong> </td>
	   	<td> Mais casos de surtos de doenças tropicais, devido a falta de informações.</td>
   </tr>

   <tr>
	   	<td><strong>Uma solução</strong> </td>
	   	<td>Um sistema para o estudo e geração de indicativos a respeito de doenças tropicais.</td>
   </tr>

</table>

<table>

   <tr>
	   	<td><strong>O problema</strong> </td>
	   	<td>Disperção de dados e dificuldade de processamento de dados a respeito
      de doenças tropicais.</td>
   </tr>


   <tr>
	   	<td><strong>Afeta</strong> </td>
	   	<td>Profissionais da saúde.</td>
   </tr>


   <tr>
	   	<td><strong>Cujo o impacto é</strong> </td>
	   	<td> Inacessibilidade a dados de pesquisas a respeito de doenças tropicais. </td>
   </tr>

   <tr>
	   	<td><strong>Uma solução</strong> </td>
	   	<td>Um sistema onde profissionais da saúde pudessem amazenar e processar seus dados.</td>
   </tr>

</table>

## 2.3 Instrução de Posição do Produto

<table>

   <tr>
	   	<td><strong>Para</strong> </td>
	   	<td><strong>Profissonais da saúde e População Geral</strong></td>
   </tr>

   <tr>
	   	<td><strong>Necessidade</strong> </td>
	   	<td>Desejam uma plataforma para consulta e analise de dados a respeito de doenças tropicais.</td>
   </tr>


   <tr>
	   	<td><strong><em>O Tropical Hazards</em></strong> </td>
	   	<td>É um Web App.</td>
   </tr>

   <tr>
	   	<td><strong>Que</strong> </td>
	   	<td>Permite que os profissionais de saúde realizem pesquisas e levantamentos de informações a respeito de regiões de forma organizada. Gerando dessa forma indicadores, para melhor descrever ou condicionar a população de uma certa área.</td>
   </tr>

   <tr>
	   	<td><strong>Diferente de</strong> </td>
	   	<td>Prescrições e tabelas manuais, além de aplicações como Docsnote.</td>
   </tr>


   <tr>
	   	<td><strong>Nosso produto</strong> </td>
	   	<td>é uma solução que busca centralizar a análise de dados para melhorar a forma de compartilhamento entre os pesquisadores e profissionais de saúde da NMT.</td>
   </tr>

</table>

# 3. Descrições da parte interessada e dos Usuários


<table>

   <tr>
	   	<td> <strong>Nome</strong></td>
	   	<td> <strong>Descrição</strong> </td>
	   	<td><strong> Responsabilidade</strong></td>
   </tr>


   <tr>
	   	<td> <strong>Equipe de desenvolvimento</strong> </td>
	   	<td> Estudantes da disciplina Métodos de Desenvolvimento de Software da FGA </td>
	   	<td> Desenvolvimento, Testes, Documentação e Implementação do Sistema </td>
   </tr>


   <tr>
	   	<td><strong>Equipe de gestão de projeto</strong></td>
	   	<td> Estudantes da disciplina Engenharia de Produto de Software da FGA </td>
	   	<td> Gerir o desenvolvimento do produto identificando problemas e apontando caminhos e soluções </td>
   </tr>

   <tr>
	   	<td><strong>Equipe de avaliação e suporte</strong></td>
	   	<td> Professor e Coaches das disciplinas EPS e MDS </td>
	   	<td> Auxiliar as equipes durante o desenvolvimento do projeto </td>
   </tr>

   <tr>
	   	<td><strong>Cliente</strong></td>
	   	<td> Núcleo de Medicina Tropical </td>
	   	<td> Esclarecer os requisitos e validar o software. </td>
   </tr>

</table>


## 3.1 Resumo dos Usuários

<table>

   <tr>
	   	<td><strong>Nome</strong></td>
	   	<td><strong>Descrição</strong> </td>
   </tr>


   <tr>
	   	<td> <strong>Pesquisadores/Interessados</strong> </td>
	   	<td> Pesquisadores relacionados a área de doenças tropicais </td>
   </tr>


   <tr>
	   	<td><strong>Público Geral</strong></td>
	   	<td>Pessoas comuns interessadas em visualizar dados acerca de doenças tropicais </td>
   </tr>

</table>

## 3.2 Ambiente do Usuário
O sistema será utilizado nos browsers Google Chrome, Safari, Internet Explorer, Firefox, Opera e Edge.


## 3.3 Perfis dos Envolvidos

O Núcleo de Medicina Tropical é uma unidade de integração da UFPA destinada ao ensino de pós-graduação, pesquisa e extensão na área de Doenças Tropicais e demais temas de interesse amazônico.



## 3.3.1 Equipe de Desenvolvimento
<table>

   <tr>
	   	<td><strong>Representante</strong></td>
	   	<td>André Bargas, Eduardo Yoshida, João Pedro, Max Henrique, Pedro Daniel</td>
   </tr>


   <tr>
	   	<td> <strong>Descrição</strong></td>
	   	<td>Desenvolvedores</td>
   </tr>


   <tr>
	   	<td><strong>Tipo</strong></td>
	   	<td>Estudantes de Métodos de Desenvolvimento de Software na FGA</td>
   </tr>

   <tr>
	   	<td><strong>Responsabilidade</strong></td>
	   	<td>Documentação, Desenvolvimento, Testes e Implementação do Sistema</td>
   </tr>


   <tr>
	   	<td><strong>Critérios de Sucesso</strong></td>
	   	<td>Entregar o Software com os requisitos especificados pelo cliente dentro do prazo</td>
   </tr>


   <tr>
	   	<td><strong>Envolvimento</strong></td>
	   	<td>Alto</td>
   </tr>

   <tr>
	   	<td><strong>Problemas/Comentários</strong></td>
	   	<td>A equipe é inexperiente nas linguagens e frameworks utilizados para implementar o sistema</td>
   </tr>

</table>

## 3.3.2 Equipe de Gestão de Projeto

<table>

   <tr>
	   	<td><strong>Representante</strong></td>
	   	<td>André Filho, Arthur Assis, Iago Carvalho, Mateus Batista, Renata Souza</td>
   </tr>


   <tr>
	   	<td> <strong>Descrição</strong></td>
	   	<td>Gerentes de Projeto</td>
   </tr>


   <tr>
	   	<td><strong>Tipo</strong></td>
	   	<td>Estudantes de Engenharia de Produto de Software na FGA</td>
   </tr>


   <tr>
	   	<td><strong>Responsabilidade</strong></td>
	   	<td>Gerir o desenvolvimento do produto, identificando problemas, apontando caminhos e soluções, estabelecendo prazos e metas, organizando a equipe de desenvolvimento a fim de completar os objetivos propostos</td>
   </tr>

   <tr>
	   	<td><strong>Critérios de Sucesso</strong></td>
	   	<td>Manter a equipe focada no projeto, contribuir com a evolução profissional da equipe de desenvolvimento, estabelecer um processo de desenvolvimento de software bem definido e entregar o produto dentro do prazo, custo e nível de qualidade</td>
   </tr>


   <tr>
	   	<td><strong>Envolvimento</strong></td>
	   	<td>Alto</td>
   </tr>

   <tr>
	   	<td><strong>Problemas/Comentários</strong></td>
	   	<td>-</td>
   </tr>
</table>

## 3.3.3 Equipe de Avaliação e Suporte

<table>

   <tr>
	   	<td><strong>Representante</strong></td>
	   	<td>Dra. Carla Rocha, Coaches de EPS, Coaches de MDS</td>
   </tr>


   <tr>
	   	<td> <strong>Descrição</strong></td>
	   	<td>Equipe de avaliação e orientação das equipes de gestão e de desenvolvimento</td>
   </tr>


   <tr>
	   	<td><strong>Tipo</strong></td>
	   	<td>Professor e Coaches das disciplinas EPS e MDS</td>
   </tr>


   <tr>
	   	<td><strong>Responsabilidade</strong></td>
	   	<td>Avaliar e orientar os alunos durante o semestre, quanto aos assuntos relacionados as disciplinas de EPS e MDS em referidos projetos</td>
   </tr>


   <tr>
	   	<td><strong>Critérios de Sucesso</strong></td>
	   	<td>A entrega do projeto e sua referente documentação de forma completa e correta para o cliente</td>
   </tr>


   <tr>
	   	<td><strong>Envolvimento</strong></td>
	   	<td>Médio</td>
   </tr>

   <tr>
	   	<td><strong>Problemas</strong></td>
	   	<td>Nenhum</td>
   </tr>
</table>

## 3.3.4 Cliente

<table>


   <tr>
	   	<td><strong>Representante</strong></td>
	   	<td>Núcleo de Medicina Tropical</td>
   </tr>


   <tr>
	   	<td> <strong>Descrição</strong></td>
	   	<td>Cliente idealizador do projeto</td>
   </tr>


   <tr>
	   	<td><strong>Tipo</strong></td>
	   	<td>Pesquisadores/Profissionais de saúde</td>
   </tr>


   <tr>
	   	<td><strong>Responsabilidade</strong></td>
	 	<td>Estabelecer os requisitos e validar o software </td>
   </tr>


   <tr>
	   	<td><strong>Critérios de Sucesso</strong></td>
	   	<td>Descrever os requisitos de maneira clara</td>
   </tr>


   <tr>
	   	<td><strong>Envolvimento</strong></td>
	   	<td>Alto</td>
   </tr>

   <tr>
	   	<td><strong>Problemas</strong></td>
	   	<td>Falta de comunicação</td>
   </tr>
</table>

## 3.4 Perfis dos Usuários

Usúarios interessados em saber sobre as doenças tropicais.

## 3.4.1 Pesquisadores

<table>

   <tr>
	   	<td><strong>Representante</strong></td>
	   	<td>Pesquisadores do NMT</td>
   </tr>


   <tr>
	   	<td> <strong>Descrição</strong></td>
	   	<td>Usuário que terá acesso ao dashboard</td>
   </tr>


   <tr>
	   	<td><strong>Tipo</strong></td>
	   	<td>Pesquisadores</td>
   </tr>


   <tr>
	   	<td><strong>Responsabilidade</strong></td>
	   	<td>-</td>
   </tr>


   <tr>
	   	<td><strong>Critérios de Sucesso</strong></td>
	   	<td>Realizar a inserção de dados no dashboard e delimitar quais dados serão de acesso ao público</td>
   </tr>


   <tr>
	   	<td><strong>Envolvimento</strong></td>
	   	<td>Alto</td>
   </tr>

   <tr>
	   	<td><strong>Problemas</strong></td>
	   	<td>-</td>
   </tr>
</table>

## 3.4.2 Público Geral

<table>

   <tr>
	   	<td><strong>Representante</strong></td>
	   	<td>Público Geral</td>
   </tr>


   <tr>
	   	<td> <strong>Descrição</strong></td>
	   	<td>Pessoas comuns interessadas em doenças tropicais</td>
   </tr>


   <tr>
	   	<td><strong>Tipo</strong></td>
	   	<td>Usuário comum</td>
   </tr>


   <tr>
	   	<td><strong>Responsabilidade</strong></td>
	   	<td>-</td>
   </tr>


   <tr>
	   	<td><strong>Critérios de Sucesso</strong></td>
	   	<td>Visualizar os dados no  observatório de dados</td>
   </tr>


   <tr>
	   	<td><strong>Envolvimento</strong></td>
	   	<td>-</td>
   </tr>

   <tr>
	   	<td><strong>Problemas</strong></td>
	   	<td>-</td>
   </tr>
</table>

## 3.5 Principais Necessidades dos Usuários ou dos Envolvidos

<p align="justify">Os pesquisadores do NMT possuem um problema de visualização dos dados de seus diferentes projetos, pois não há comunhão de tecnologias nem um modelo padronizado de dashboard e observatório de dados onde esses possam ser compartilhados de forma eficiente.</p>
<p align="justify"> Logo a principal necessidade dos usuários é a criação de um sistema onde tais dados possam ser inseridos, analisados e compartilhadaos de forma organizada e eficiente. </p>

## 3.6 Alternativas e Concorrência

##### 3.6.1 Website: <em>World Health Organization</em>
<p align ="justify"> O <em>website</em> da World Health Organization possui um dashboard que permite a visualização de estatísticas acerca de diversas doenças, inclusive doenças tropicais.<br><br>
![World Health Organization](https://i.imgur.com/JkPqNdD.png)
</p>

# 4. Visão Geral do Produto

<p align="justify">O sistema contará com uma plataforma online capaz de disponibilizar dados a respeito de doenças tropicais, fornecendo mecanismos para pesquisadores e profissionais da saúde acessarem através de um dashboard, os indicadores gerados por meio de informações dos projetos do NMT. Além disso, esta plataforma contará com uma interface para os usuários comuns visualizarem os dados sobre doenças tropicais.
</p>

# 5. Recursos do Produto

<p>O sistema oferece as seguintes funcionalidades aos usúarios:</p>
<ul>
	<li>Gerenciar e manter usúarios: Tanto os pesquisadores e profissionais de saúde quanto os interessados poderão ser cadastrados no sistema, de forma que consegue adicionar, remover, ou alterar informações relacionadas aos seus perfis.</li>
	<li>Facilitar para os pesquisadores e profissionais de saúde o gerenciamento de dados, levantamento de indicadores e exportação de dados.</li>
	<li>Diminuir os erros causados devido a falta de organização e padronização dos dados</li>
	<li>Disponibilizar indicadores que auxiliam da prevenção de tais doenças tropicais</li>
	<li>Resolver o problema de visualização de dados dos diferentes projetos da NMT. Não há comunhão de tecnologias e não há nenhum modelo padronizado de observatório/dashboard.</li>
	<li>Muito das vezes a apresentação é offline, via arquivo ou na máquina do pesquisador.Isso gera uma bagunça enorme e uma grande dificuldade de compartilhar informação, nosso Software procura resolver esse problema de compartilhamento da informação.</li>
	<li>Centralizar a análise dos dados e dos indicadores, para poder compartilhar isso entre os próprios profissionais da saúde e a população em geral.</li>
</ul>

<h1> 6. Restrições</h1>

<h2>6.1 Restrições de Design</h2>

<p align="justify">O desing devera ser simples e elegante, visando também a facilidade do seu uso, para que os usuarios possam utilizar o sistema de forma intuitiva.</p>

## 6.2 Restrições de Implementação
<p align="justify">Criação de um modelo padronizado de observatório/dashboard através de uma plataforma web, onde profissionais da saude possam submeter dados de pesquisa para o geramento de estatísticas e centralização dos dados a sobre o tema doenças tropicais. Além disso é necessario que haja um portal para que a população geral possa ter acesso a estes indicativos, disponibilizando também os dados através de um ponto de acesso remoto (API).</p>

## 6.3 Restrições de Segurança

<p align="justify">Devido o fato de que pesquisadores poderem ser cotribuidores para a alimentação da base de dados do sistema, é necessario que haja uma certificação que os usuarios contribuintes sejam somente pessoas credenciadas. Para que assim possamos garantir a qualidade dos dados armazenados.</p>


## 6.4 Restrições de Uso

<p align="justify">Para o uso do sistema é necessário que os usuários tenham acesso a um dispositivo conectado à internet e que possua um navegador web compatível com o sistema. Caso o usuário do sistema não possua acesso à internet, o sistema deve mostrar uma página de erro.</p>
