# Planejamento dos Testes de Usabilidade

### Objetivo
O principal objetivo do Teste de Usabilidade do sistema Observ é determinar as respostas emocionais, feedback, tempo, passos e número de erros resultantes da interação do usuário com a aplicação. Ao final dos testes a equipe visa encontrar problemas e oportunidades de melhorias.

### Perfil de usuário
* Usuários que tenham experiência no dia a dia com websites.
* Usuários com experiência em aplicações para manipulação de dados.

### Ambiente
* Notebook com a ferramenta SimpleScreenRecorder instalado;

### Regras
Duração de 10 minutos.

## Tópicos de Análise
Para os testes de usabilidade que serão usados no projeto, serão avaliados os seguintes tópicos:

<ul>
  <li>
    <b>Simplicidade da interface:</b> A facilidade de entendimento da interface por meio do usuário.
  </li>
  <li>
    <b>Desempenho do usuário:</b> tempo e passos necessários para a completude de tarefas.
  </li>
  <li>
    <b>Precisão no uso:</b> Quantidade de erros cometidos pelo usuário na realização da tarefa.
  </li>
  <li>
    <b>Resposta emocional:</b> Como a pessoa se sentiu durante a atividade.
  </li>
  <li>
    <b>Lembrança e reconhecimento:</b> Reconhecimento da aplicação após certo período de tempo.
  </li>
</ul>

## Avaliação
<table>
  <thead>
    <tr>
      <th>Tópico</th>
      <th>Medida</th>
      <th>Fórmula</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Simplicidade da Interface</th>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Desempenho do usuário</th>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Precisão de Uso</th>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Resposta emocional</th>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Lembrança e reconhecimento</th>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Número de erros cometidos</th>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

## Testes Utilizados
Aqui estão definidos os testes de usabilidade que serão aplicados pela equipe.
É importante resaltar que existem testes que cobrem vários dos tópicos de análise.
Antes de iniciar os testes, deve-se passar algumas informações ao usuário:
* Informar que quem será testado é o sistema e não o usuário.
* Pedir para o usuário falar em voz alta o que ele está pensando.
* Será utilizada a ferramenta de captura de tela "SimpleScreenRecorder" para acompanhar os passos de navegação do usuário pelo sistema Observ.


### Teste 01 - Teste de Workflow

#### Objetivo
Avaliar a implementação da interface do sistema ao ser utilizada pelo usuário.

#### Duração
* Máximo de 5 minutos.

#### Roteiro do Teste

1. O usuário estando na página principal, pesquisa pelo dashboard x.
2. Após receber o resultado da pesquisa, o usuário entra no dashboard escolhido.
3. O usuário confere os dados e baixa os dados do dashboard.
4. O usuário volta para a página principal.
5. O usuário realiza cadastro.
6. O usuário cria um projeto.
7. O usuário faz upload de um set de dados.
8. O usuário cria um dashboard.
9. O usuário entra no dashboard.
11. O usuário baixa os dados do dashboard.

---

### Teste 02 - Teste de Workflow (usuário alterado)

#### Objetivo
Avaliar a navegação da interface, considerando que os usuários estarão sob condições adversas durante o teste.

#### Justificativa
Esse teste foi idealizado baseado na ideia de Richard Littauer, o artigo do mesmo se encontra nas referências do documento.

#### Duração
* Máximo de 5 minutos.

#### Roteiro do Teste

1. O usuário estando na página principal, pesquisa pelo dashboard x.
2. Após receber o resultado da pesquisa, o usuário entra no dashboard escolhido.
3. O usuário confere os dados e baixa os dados do dashboard.
4. O usuário volta para a página principal.
5. O usuário realiza cadastro.
6. O usuário cria um projeto com tags.
7. O usuário faz upload de um set de dados com extensão .csv.
8. O usuário parametriza os dados.
9. O usuário cria um dashboard.
12. O usuário entra no dashboard.
13. O usuário baixa os dados do dashboard.

---
## Teste 03 - Teste de Workflow - Gerar indicadores  

#### Duração
* Máximo de 5 minutos.

#### Roteiro do Teste

* Meta da tarefa: Gerar indicadores.

1. O usuário realiza cadastro.
2. O usuário realiza o login.
2. O usuário seleciona um projeto.
3. O usuário seleciona um dataset.
4. O usuário seleciona os dados.
6. O usuário gera um gráfico com indicadores.


## Referências

- [The User Has Sobered Up - Littauer, Richard](https://medium.com/@richlitt/the-user-has-sobered-up-df0b411997ea)
- [Testes de Usabilidade](https://www.caelum.com.br/apostila-ux-usabilidade-mobile-web/usabilidade/#o-que--medido)
