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

   <tr>
	   	<td>17/03/2018</td>
                <td>1.0.1</td>
	   	<td>Corrigindo erros da primeira versão</td>
	   	<td>Andre Bargas</td>

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

<p align = "justify">O documento de visão tem como objetivo demonstrar uma visão completa sobre o <em>webapp</em> Tropical Hazards BI deixando claro sua proposta, características e utilidade;</p>

## 1.2	Escopo

<ul>
<li>Receber dados referentes a doenças tropicais</li>
<li>Fazer análise estatística dos dados recebidos</li>
<li>Profissionais da saúde devem possuir perfis para gerencias (dashboards)</li>
<li>Mostar metadados, onde os profissionais poderam submeter dados para serem analisados</li>
<li>Plataforma para visualização dos indicadores e dados para o público interessados</li>
<li>Gerar relatórios exportáveis</li>
</ul>

## 1.3	Definições, acrônimos e abreviações

<ul>
<li>FGA - Faculdade do Gama (UnB)</li>
<li>UnB - Universidade de Brasília</li>
<li>MDS - Métodos de Desenvolvimento de Software</li>
<li>EPS - Engenharia de Produto de software</li>
<li>MVT - Model View Template</li>
</ul>

## 1.4 Referências

IBM Knowledge Center - Documento de Visão: A estrutura de tópicos do documento de visão. Disponível em: <https://www.ibm.com/support/knowledgecenter/pt-br/SSWMEQ_3.0.1/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.htm>. Acesso em: 22 ago. 2017;

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

# 2. Posicionamento

## 2.1 Oportunidade de Negócio

<p align = "justify"> Pesquisadores da Universidade de Brasília(Unb) precisam resolver um problema de automatizar a análise estatística de dados referentes as doenças tropicais, sendo que esses dados não possuem um padrão definido.

Nosso projeto irá oferecer uma análise dos fatores determinantes de proteção, os mecanismos envolvidos na imunopatologia e possíveis mecanismos envolvendo drogas imunomoduladoras que poderiam auxiliar na diminuição da morbidade e mortalidade de doenças tropicais.

Para o profissional de saúde e pesquisadores o <em>webapp</em> terá uma série de ferramentas para utilizar e gerar gráficos com indicadores.

Para os usuários serão disponibilizados uma interface web onde podera ser encontrar informações sobre as principais doenças tropicais e seus indicativos.</p>


## 2.2 Descrição do problema

<table>

   <tr>
	   	<td><strong>O problema de</strong> </td>
	   	<td><strong>Falta de informações sobre doenças tropicais</strong></td>
   </tr>


   <tr>
	   	<td><strong>afeta</strong> </td>
	   	<td>População geral</td>
   </tr>


   <tr>
	   	<td><strong>cujo impacto é</strong> </td>
	   	<td> Mais casos de surtos de doenças tropicais, devido a falta de informações</td>
   </tr>

   <tr>
	   	<td><strong>uma solução seria</strong> </td>
	   	<td>Um sistema para o estudo e geração de indicativos a respeito de doenças tropicais</td>
   </tr>

</table>

<table>

   <tr>
	   	<td><strong>O problema de</strong> </td>
	   	<td><strong>Disperção de dados e dificuldade de processamento de dados a respeito
      de doenças tropicais</strong></td>
   </tr>


   <tr>
	   	<td><strong>afeta</strong> </td>
	   	<td>Profissionais da saúde</td>
   </tr>


   <tr>
	   	<td><strong>cujo impacto é</strong> </td>
	   	<td> Inacessibilidade a dados de pesquisas a respeito de doenças tropicais </td>
   </tr>

   <tr>
	   	<td><strong>uma solução seria</strong> </td>
	   	<td>Um sistema onde profissionais da saúde pudessem amazenar e processar seus dados</td>
   </tr>

</table>

## 2.3 Instrução de Posição do Produto

<table>

   <tr>
	   	<td><strong>Para</strong> </td>
	   	<td><strong>Profissonais da saúde e População Geral</strong></td>
   </tr>

   <tr>
	   	<td><strong>que</strong> </td>
	   	<td>Desejam um plataforma para consulta e analise de dados a respeito de doenças tropicais</td>
   </tr>


   <tr>
	   	<td><strong><em>O Webapp</em></strong> </td>
	   	<td>Descrição</td>
   </tr>

   <tr>
	   	<td><strong>que</strong> </td>
	   	<td>Descrição</td>
   </tr>

   <tr>
	   	<td><strong>Diferente de</strong> </td>
	   	<td>Descrição</td>
   </tr>


   <tr>
	   	<td><strong>Nosso produto</strong> </td>
	   	<td>Descrição</td>
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
	   	<td> Profissionais da saúde </td>
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
	   	<td> Publico geral que desejam saber sobre doenças tropicais </td>
   </tr>


   <tr>
	   	<td><strong>Profissionais de Saúde</strong></td>
	   	<td> Profissionais que utilizam a plataforma para fins de consulta e analise de dados. </td>
   </tr>

</table>

## 3.2 Ambiente do Usuário
O sistema será utilizado nos browsers Google Chrome, Safari, Internet Explorer, Firefox, Opera e Edge.


## 3.3 Perfis dos Envolvidos


## 3.3.1 Equipe de Desenvolvimento
<table>

   <tr>
	   	<td><strong>Representante</strong></td>
	   	<td>**André Bargas, Eduardo Yoshida, João Pedro, Max Henrique, Pedro Daniel**</td>
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
	   	<td>**André Filho, Arthur Assis, Iago Carvalho, Mateus Batista, Renata Souza**</td>
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
	   	<td>**Dra. Carla Rocha, Coaches de EPS, Coaches de MDS**</td>
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
	   	<td>-</td>
   </tr>
</table>

## 3.3.4 Cliente

<table>


   <tr>
	   	<td><strong>Representante</strong></td>
	   	<td>Lorem impsom</td>
   </tr>


   <tr>
	   	<td> <strong>Descrição</strong></td>
	   	<td>Lorem impsom</td>
   </tr>


   <tr>
	   	<td><strong>Tipo</strong></td>
	   	<td>Lorem impsom</td>
   </tr>


   <tr>
	   	<td><strong>Responsabilidade</strong></td>
	 	<td>Lorem impsom</td>
   </tr>


   <tr>
	   	<td><strong>Critérios de Sucesso</strong></td>
	   	<td>Lorem impsom</td>
   </tr>


   <tr>
	   	<td><strong>Envolvimento</strong></td>
	   	<td>Lorem impsom</td>
   </tr>

   <tr>
	   	<td><strong>Problemas</strong></td>
	   	<td>Lorem impsom</td>
   </tr>
</table>

## 3.4 Perfis dos Usuários

## 3.4.1 Pesquisadores

<table>

   <tr>
	   	<td><strong>Representante</strong></td>
	   	<td>Lorem impsom</td>
   </tr>


   <tr>
	   	<td> <strong>Descrição</strong></td>
	   	<td>Lorem impsom</td>
   </tr>


   <tr>
	   	<td><strong>Tipo</strong></td>
	   	<td>Lorem impsom</td>
   </tr>


   <tr>
	   	<td><strong>Responsabilidade</strong></td>
	   	<td>Lorem impsom</td>
   </tr>


   <tr>
	   	<td><strong>Critérios de Sucesso</strong></td>
	   	<td>Lorem impsom</td>
   </tr>


   <tr>
	   	<td><strong>Envolvimento</strong></td>
	   	<td>Lorem impsom</td>
   </tr>

   <tr>
	   	<td><strong>Problemas</strong></td>
	   	<td>Lorem impsom</td>
   </tr>
</table>

## 3.4.2 Profissionais de saúde

<table>

   <tr>
	   	<td><strong>Representante</strong></td>
	   	<td>Lorem impsom</td>
   </tr>


   <tr>
	   	<td> <strong>Descrição</strong></td>
	   	<td>Lorem impsom</td>
   </tr>


   <tr>
	   	<td><strong>Tipo</strong></td>
	   	<td>Lorem impsom</td>
   </tr>


   <tr>
	   	<td><strong>Responsabilidade</strong></td>
	   	<td>Lorem impsom</td>
   </tr>


   <tr>
	   	<td><strong>Critérios de Sucesso</strong></td>
	   	<td>Lorem impsom</td>
   </tr>


   <tr>
	   	<td><strong>Envolvimento</strong></td>
	   	<td>Lorem impsom</td>
   </tr>

   <tr>
	   	<td><strong>Problemas</strong></td>
	   	<td>Lorem impsom</td>
   </tr>
</table>

## 3.5 Principais Necessidades dos Usuários ou dos Envolvidos

<p align="justify"> Organização de dados, mostrar gráficos, apontar localidades com maior risco de doenças tropicais.</p>

## 3.6 Alternativas e Concorrência

##### 3.6.1 Aplicativo Mobile: <em>Sem Dengue</em>
<p align ="justify">
O aplicativo <em>Sem Dengue</em> permite que usuários insiram e visualizem locais com focos do mosquito Aedes Aegypti. Oferecem também a possibilidade 
</p>

# 4. Visão Geral do Produto

<p align="justify">O sistema contará com uma plataforma capaz de comunhar diferentes dados a respeito de doenças tropicais, fornecendo uma interface para pesquisadores e profissionais da saude submeterem dados para analise. Alem disso esta plataforma contemplara com uma interface/ dashboard para usuarios da web ter acesso a dados e inidicadores de doenças tropicais.
</p>

# 5. Recursos do Produto

# 6. Restrições


## 6.1 Restrições de Design

Interface/ dashboard para publico geral e para profissionais/ pesquisadores da area da saúde.

## 6.2 Restrições de Implementação
<p align="justify">Criação de um modelo padronizado de observatório/dashboard através de uma plataforma web e disponibilizar dados através de ponto de acesso remoto (API).</p>

## 6.3 Restrições de Segurança

A definir


## 6.4 Restrições de Uso

A definir
