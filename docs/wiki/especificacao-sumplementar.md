<!-- Template de Documento de Arquitetura de Software versão em Markdown-->
# **Tropical Hazards**

Documento de Especicação Suplementar
===================

----------
## Histórico  de Revisões

| Data | Versão | Descrição | Autores |
|:----:|:------:|:---------:|:-------:|
| **/04/2018 | 1.0 | Abertura do documento | - |
| **/03/2018 | 1.1 | - | - |
| **/03/2018 | 1.2 | - | - |
| **/03/2018 | 1.3 | - | - |
-----------

Sumário
----------------

* 1 .  [Introdução](#1-introdução)
    * 1.1. [Finalidade](#11-finalidade)
    * 1.2. [Escopo](#12-escopo)
    * 1.3 [Definições, Acrônimos e Abreviações](#13-definições-acrônimos-e-abreviações)
    * 1.4 [Referências](#14-referências)
* 2 . [Usabilidade](#2-usabilidade)
* 3 . [Confiabilidade](#3-confiabilidade)
* 4 . [Suportabilidade](#4-suportabilidade)
* 5 . [Interfaces de Usuário](#5-interfaces-de-usuário)
* 6 . [Avisos Legais, de Copyright e Outros](#6-avisos-legais)


-----------

## 1. Introdução

### 1.1 Finalidade

Este documento captura os requisitos de qualidade relacionados ao sistema Observ que não foram contemplados nos documentos de Visão e de Arquitetura. A finalidade é definir os requisitos não funcionais e sspecicações suplementares relacionados ao aplicativo Observ.

### 1.2 Escopo

Este artefato documenta as especificações e requisitos não funcionais relacionados ao sistema “Observ". Serão descritas, aqui, a usabilidade, a confiabilidade e a suportabilidade do sistema, assim como as restrições de design, requisitos de interface e, ainda, informações de legalidade, direitos autorais e outros.

### 1.3 Definições, Acrônimos e Abreviações
<ul>
  <li>NMT: <em>Núcleo de Medicina Tropical</em></li>
  <li>UNB: <em>Universidade de Brasília</em></li>
  <li>MVC: <em>Model-View-Controller</em></li>
  <li>MVT: <em>Model-View-Template</em></li/>
</ul>

### 1.4 Referências

SOUSA, André; WILLER, Guilherme; BATISTA, Matheus; BELCHIOR, Emanoel. Especificação Suplementar. Disponível em: https://github.com/fga-gpp-mds/2017.1-Escola-X/wiki/Especifica%C3%A7%C3%A3o-Suplementar. Acesso em 12 de Abril de 2018.

## 2. Usabilidade

O sistema contemplar uma interação simplificada e minimalista, sendo fácil aprender e ultilizar. A aplicação proverá funcionalidades relevantes e utilizáveis para os usuários, assim como a prevenção de erros e, em casos inevitáveis dos mesmo a exibição de mensagens informativas sobre tais. Ademais, o software possuirá linguagem intuitiva e inteligível para os usuários.

## 3. Confiabilidade

O sistema deverá garantir:

 * O armazenamento e manipulação de dados, de forma que somente usuários autorizados possam fazer tais ações.

 * Deverá permitir a interação e utilização dos dados, de forma que esta não impacte na persistencia dos mesmo.

 * Um sistema de login e autenticação de usuário, de forma que os dados pessoais dos usuários sejam protejidos.

## 4. Suportabilidade

O sistema será suportado nos navegadores Google Chrome 60, Mozilla Firefox 55, Internet Explorer 8, ou superiores, em máquinas com acesso à Internet.

## 5. Interfaces

As telas de interface para o usuário estão listada a seguir, para maiores detalhes de design e interações com menus consulte este [link](ENDERECO DO PROTOTIPO).

  * Página Inicial
  * Login de Usuários
  * Cadastro de Usuários
  * Visualização de Projetos
  * Criação de Projetos
  * Edição de Projetos
  * Visualização e Criação de observatórios

## 6. Avisos Legais, de Copyright e Outros

Este programa é um software livre; você pode redistribuí-lo e/ou modificá-lo sob os termos da Licença Pública Geral GNU como publicada pela Fundação do Software Livre (FSF); na versão 3 da Licença, ou (a seu critério) qualquer versão posterior.

Este programa é distribuído na esperança de que possa ser útil, mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a Licença Pública Geral GNU para mais detalhes.

Você deve ter recebido uma cópia da Licença Pública Geral GNU junto com este programa. Se não, veja http://www.gnu.org/licenses.
