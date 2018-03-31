# Plano de Medição

## O Problema

A equipe composta pelos alunos da disciplina de Engenharia de Produto de Software (EPS) necessita gerenciar o projeto Tropical Hazards BI e manter o bom desempenho da equipe de desenvolvimento.
Os prazos das entregas de cada versão do produto são curtos. Assim, é necessário acompanhar, além das demandas acordadas com o cliente, o progresso do time de desenvolvimento, composto pelos alunos de Métodos de Desenvolvimento de Software (MDS) para garantir um produto final entregável com qualidade satisfatória.
Do ponto de vista de projeto, alguns riscos podem acontecer:

* Time desestimulado;
* Produto com uma qualidade ruim (alta complexidade, grande quantidade de bugs, ou mesmo incompleto);
* Dificuldades com a implementação da tecnologia no contexto do projeto;
* Produto entregue incompleto;

Dessa forma, o plano de Medição visa reduzir a ocorrência desses riscos e possibilitar a identificação de oportunidades de melhoria do processo e do produto no decorrer do projeto.

## 1. Objetivos Estratégicos
A parte de gerência do projeto possui o objetivo principal de conduzir o projeto a fim de gerar um produto de qualidade e satisfação ao cliente, de acordo com o escopo definido. Alguns objetivos de gestão que necessitam do auxílio da medição:

● Produtividade da equipe;<br>
● Qualidade do código;<br>

## 2. Planejamento de Medição

A abordagem GQM (Goal Question Metric) será adotada para identificar as métricas que atinjam os objetivos propostos para o contexto do projeto Tropical Hazards BI.

## 3. Definição dos Objetivos de Medição

## 3.1 Objetivo de Equipe
### 3.1.1 - Objetivo 1 - Equipe do projeto Tropical Hazards BI (EPS/MDS)
<table>
<tr>
  <th><b>Analisar</b></th>
  <th>Para o propósito de</th>
  <th>Com respeito à</th>
  <th>Sob o ponto de vista de</th>
  <th>No contexto de</th>
</tr>
<tr>
    <td>Time de desenvolvimento </td>
    <td>Melhorar</td>
    <td>Produtividade</td>
    <td>Gerentes de projeto</td>
    <td>Projeto Tropical Hazards BI</td>
  </tr>
</table>

## 3.2 Objetivo de Produto

### 3.2.1 - Objetivo 2 - Código fonte
<table>
  <tr>
    <th><b>Analisar</b></th>
    <th>Para o propósito de</th>
    <th>Com respeito à</th>
    <th>Sob o ponto de vista de</th>
    <th>No contexto de</th>
  </tr>
  <tr>
    <td>O código fonte</td>
    <td>Melhorar</td>
    <td>Qualidade do código</td>
    <td>Gerentes de Projeto</td>
    <td>Projeto Tropical Hazards BI</td>
  </tr>
</table>

## 4. *Abstraction Sheets*

###  Abstraction Sheet 1 do Objetivo 1
<table>
  <tr>
    <th><b>Foco na Qualidade</b></th>
    <th><b>Fatores de Variação</b></th>
  </tr>
  <tr>
    <td>
      <ul style="list-style-type:none">
        <li> <b>Q.1</b> Produtividade da equipe durante uma iteração</li>
        <li> <b>Q.2</b> Rendimento médio da equipe por iteração</li>
        <li> <b>Q.3</b> Conhecimento individual declarado das tecnologias</li>
        <li><b>Q.4</b> Tempo dedicado ao projeto</li>
      </ul>
    </td>
    <td>
    <ul>
      <li>Acontecimentos de ordem pessoal</li>
      <li> Planejamento falho</li>
      <li> Sobrecarga de atividades</li>
      <li> Experiência com a tecnologia </li>
    </ul>
    </td>
  </tr>
  <tr>
    <th><b>Hipóteses de Baseline</b></th>
    <th><b>Impacto nas hipóteses de ​Baseline</b></th>
  </tr>
  <tr>
    <td>
      <ul style="list-style-type:none">
        <li> <b>Q.1</b> Produtividade variante</li>
        <li> <b>Q.2</b> Rendimento baixo</li>
        <li><b>Q.3</b> Conhecimento mal distribuido</li>
        <li><b>Q.4</b> Poucas horas de dedicação : < 10 horas</li>
      </ul>
    </td>
    <td>
      <ul>
        <li> Excesso de trabalho em um prazo curto, aumentando a possibilidade de erros</li>
        <li> Gera atrasos na entrega do produto</li>
        <li> Sobrecarga de alguns membros e pode acarretar atrasos na entrega do produto</li>
      </ul>
    </td>
  </tr>
</table>

###  Abstraction Sheet 1 do Objetivo 2
<table>
  <tr>
    <th><b>Foco na Qualidade</b></th>
    <th><b>Fatores de Variação</b></th>
  </tr>
  <tr>
    <td>
      <ul style="list-style-type:none">
        <li> <b>Q.1</b> Complexidade Ciclomática</li>
        <li> <b>Q.2</b> Duplicação de código</li>
      </ul>
    </td>
    <td>
    <ul>
      <li> Padronização do código</li>
      <li> Complexidade do Software</li>
      <li> Experiência com a tecnologia</li>
    </ul>
    </td>
  </tr>
  <tr>
    <th><b>Hipóteses de Baseline</b></th>
    <th><b>Impacto nas hipóteses de ​Baseline</b></th>
  </tr>
  <tr>
    <td>
      <ul style="list-style-type:none">
        <li> <b>Q.1</b> Complexidade Ciclomática < 4</li>
        <li> <b>Q.2</b> Duplicação de código em nível regular</li>
      </ul>
    </td>
    <td>
      <ul>
        <li> Fator de complexidade bom, com boa manutenibilidade</li>
        <li> Necessidade de retrabalho</li>
      </ul>
    </td>
  </tr>
</table>

## 5. Questões de Medição

### 5.1 - Questões Objetivo 1 - Equipe do Projeto Tropical Hazards BI(EPS/MDS)

* Questão 1 (O01Q01) -  A equipe está sendo produtiva?
* Questão 2 (O01Q02) - A dedicação da equipe é constante?
* Questão 3 (O01Q03) - As entregas são contínuas?

### 5.2 - Questões Objetivo 2 - Código fonte

* Questão 1 (O02Q01) - Qual a complexidade ciclomática?
* Questão 2 (O02Q02) - O código fonte está manutenível?

## 6. Métricas Escolhidas

### 6.1 - Métricas do Objetivo 1 - Equipe do Projeto Tropical Hazards BI(EPS/MDS)

#### Métrica 1.1 - USs executadas por Sprint
<table>
<tr>
  <td><b>Métrica</b></td>
  <td>USs executadas na Sprint</td>  
</tr>
  <tr>
    <td><b>Objetivo de Medição</b></td>
    <td style="text-align: justify">Verificar a quantidade de USs executadas em uma Sprint em relação ao que foi planejado.</td>  
  </tr>
  <tr>
    <td><b>Fórmula de Obtenção</b></td>
    <td style="text-align: justify">O burndown é um gráfico que em sua base apresenta o
      tempo da sprint (normalmente dias) e na vertical os
      pontos planejado para a sprint. Existe uma reta
      representado a quantidade de pontos até o momento.</td>  
  </tr>
  <tr>
    <td><b>Escala de Medição</b></td>
    <td>Racional</td>  
  </tr>
  <tr>
    <td><b>Coleta</b></td>
    <td>
    Responsável: Membro de EPS
    Periodicidade: A cada iteração
    Procedimento: Uso do gráfico de <b>Burndown</b> gerado pelo <b>GitHub</b>, por meio da extensão <b>Zenhub</b>.</td>  
  </tr>
  <tr>
    <td><b>Análise</b></td>
    <td style="text-align: justify">Se as USs planejadas forem finalizadas com muita antecedêncica, isso indica que o time de desenvolvimento tem um potencial maior e foi subestimado.Caso muitas USs fiquem incompletas, houve uma superestima de execução pelo time ou houve a subestimação de algumas USs, que possam ter demandado mais esforço que o esperado.
    Se a tarefa foi iniciada e entregue muito próxima ao fim da iteração, não houve continuidade na execução da Sprint.
    Se a US não foi entregue, indica que foi planejada equivocadamente.
    É esperado que as entregas sejam constantes.</td>  
  </tr>
  <tr>
    <td><b>Meta</b></td>
    <td style="text-align: justify">Todas as USs planejadas para a Sprint sejam executadas e que sempre hajam USs entregues</td>  
  </tr>
  <tr>
    <td><b>Providência</b></td>
    <td style="text-align: justify">
    - Verificar o planejamento das USs para uma Sprint, para se adequar ao ritmo da equipe<br>
    - Monitorar a execução das atividades e a necessidade de realizar pareamentos para aumentar o nivel da equipe.
    </td>
  </tr>
</table>

#### Métrica 1.2 - Nível de conhecimento
<table>
<tr>
  <td><b>Métrica</b></td>
  <td>Nivel de conhecimento</td>  
</tr>
  <tr>
    <td><b>Objetivo de Medição</b></td>
    <td style="text-align: justify">Melhorar o rendimento de cada membro no desempenho das atividades </td>  
  </tr>
  <tr>
    <td><b>Fórmula de Obtenção</b></td>
    <td> Cada avaliação possui o seguinte peso:<br><br>
        Mito -> 1<br>
        Sei bastante -> 0,755<br>
        Me viro -> 0,55<br>
        Sei pouco -> 0,35<br>
        Socorro -> 0<br><br>
        E a fórmula para o cálculo geral de cada membro é a seguinte:<br><br>
        Pconhecimento = (((num_mito * 1) + (num_bastante * 0,755) + (num_viro * 0,55) + (num_pouco * 0,35) + (num_socorro * 0)) / num_areas) * 100<br><br>
        Onde:<br><br>
        num_mito - É a quantidade de áreas com avaliação do tipo "Mito"<br>
        num_bastante - É a quantidade de áreas com avaliação do tipo "Sei bastante"<br>
        num_viro - É a quantidade de áreas com avaliação do tipo "Me viro"<br>
        num_pouco - É a quantidade de áreas com avaliação do tipo "Sei pouco"<br>
        num_socorro - É a quantidade de áreas com avaliação do tipo "Socorro"<br>
        num_areas - É a quantidade de áreas de conhecimento avaliadas<br>
        Pconhecimento = Porcentagem geral de conhecimento de um determinado membro </td>  
  </tr>
  <tr>
    <td><b>Escala de Medição</b></td>
    <td>Ordinal</td>  
  </tr>
  <tr>
    <td><b>Coleta</b></td>
    <td style="text-align: justify">Responsável: Membro de EPS<BR>
      Periodicidade: A cada iteração
      Procedimento: Registro em tabela do nível de conhecimento em determinada ferramenta ou item. Verificar a cada iteração se houve melhora no conhecimento de uma determinada tecnologia ou
      ferramenta em relação, em relação à iteração anterior
    </td>  
  </tr>
  <tr>
    <td><b>Análise</b></td>
    <td style="text-align: justify">Pautada na verificação de dois aspectos: o nível de conhecimento, do ponto de vista pessoal, e se houve aumento do conhecimento entre as iterações. Os níveis definidos de confiança pessoal no conheimento de determinado tópico são:<br><br>
    - <b>Mito:</b> Tem muita segurança em utilizar a tecnologia, muito conhecimento e experiência.<br>
    - <b>Sei bastante:</b> Tem segurança e consegue utilizar com facilidade a tecnologia. <br>
    - <b>Me viro:</b> Se sente bem com a tecnologia, porém não tem tanto conhecimento. <br>
    - <b>Sei pouco:</b> Não possui muito conhecimento sobre a tecnologia, porém sabe algo sobre o funcionamento. <br>
    - <b>Socorro:</b> Não tem contato algum com a tecnologia e se sente confuso e totalmente inseguro.<br>
    </td>  
  </tr>
  <tr>
    <td><b>Meta</b></td>
    <td style="text-align: justify">Aumento dos níveis de conhecimento a cada iteração e disseminação do conhecimento entre os membros do time.</td>  
  </tr>
  <tr>
    <td><b>Providência</b></td>
    <td style="text-align: justify">
    Para que a meta seja atingida, algumas providências podem ser tomadas:<br><br>
    - Aplicação de pareamentos<br>
    - Realização de treinamentos<br>
    - Realização de dojôs<br>  
    </td>
  </tr>
</table>

#### Métrica 1.3 - Tempo de dedicação
<table>
<tr>
  <td><b>Métrica</b></td>
  <td>Tempo de dedicação ao Projeto</td>  
</tr>
  <tr>
    <td><b>Objetivo de Medição</b></td>
    <td style="text-align: justify">Identificar o tempo de dedicação dos membros do time com o projeto</td>  
  </tr>
  <tr>
    <td><b>Fórmula de Obtenção</b></td>
    <td>
    t = h<br><br>
    Onde:<br>
    t - tempo de dedicação em horas por semana <br>
    h - tempo de duração da dedicação (horas) Unidade de medida - horas/semana.
     </td>  
  </tr>
  <tr>
    <td><b>Escala de Medição</b></td>
    <td>Absoluta</td>  
  </tr>
  <tr>
    <td><b>Coleta</b></td>
    <td>
    Responsável: Membro de EPS.
    Periodicidade: Semanal.
    Procedimento: Registro do tempo dedicado para cada tarefa em uma tabela disponível no <b>Google Drive</b>.
    </td>  
  </tr>
  <tr>
  <td><b>Meta</b></td>
  <td>Trabalhar 10h/semana.</td>  
  </tr>
  <tr>
    <td><b>Análise</b></td>
    <td style="text-align: justify">Caso seja necessário mais que 10 horas/semana, isso pode caracterizar uma curva de aprendizagem ou sobrecarga de tarefas. Caso o tempo de decicação seja inferior a 10 horas/semana, isso pode indicar descaso com a disciplina, dependendo da quantidade de tarefas feitas, ou uma realidade do membro, devido a atividades externas. O ideal é que sejam dispendidas 10h/semana, conforme diretriz da disciplina. É necessário verificar e comparar com os outros membros da equipe, para garantir que não ocorra sobrecarga de tarefas.</td>  
  </tr>
  <tr>
    <td><b>Providência</b></td>
    <td style="text-align: justify">
    - Monitorar a execução das atividades<br>
    - Apoiar a organização pessoal do membro do time<br>
    - Em casos de excessiva dificuldade, promover treinamentos, pareamentos, dojôs, para despender menor tempo na execução da tarefa<br>
    - Motivar a equipe<br>
    </td>
  </tr>
</table>

#### Métrica 1.4 - Nível de contribuição
<table>
<tr>
  <td><b>Métrica</b></td>
  <td>Nível de contribuição</td>  
</tr>
  <tr>
    <td><b>Objetivo de Medição</b></td>
    <td>Identificar o nível de contribuição individual para o projeto e o ritmo de trabalho do membro.</td>  
  </tr>
  <tr>
    <td><b>Fórmula de Obtenção</b></td>
    <td>
    Commits por dia durante uma iteração<br><br>
     </td>  
  </tr>
  <tr>
    <td><b>Escala de Medição</b></td>
    <td>Absoluta</td>  
  </tr>
  <tr>
    <td><b>Coleta</b></td>
    <td style="text-align: justify">
    Responsável: Membro de EPS.<br>
    Periodicidade: A cada Sprint.<br>
    Procedimento: Verificar o gráfico registrado pelo <b>GitHub</b>, por meio da extensão <b>Zenhub</b>, que gera a quantidade de commits de cada membro em uma iteração.</td>  
  </tr>
  <tr>
  <td><b>Meta</b></td>
  <td>Nível contínuo e constante de commits.</td>  
  </tr>
  <tr>
    <td><b>Análise</b></td>
    <td style="text-align: justify">Caso os commits sejam concentrados ao final da iteração, isso pode indicar acúmulo de tarefas para um curto prazo e aumenta os riscos da tarefa não ser entregue, além de indicar que a execução não foi contínua, o que dificulta a curva de aprendizagem. O ideal é serem constantes, logo no início da iteração. </td>  
  </tr>
  <tr>
    <td><b>Providência</b></td>
    <td style="text-align: justify">
    - Monitorar a execução das atividades<br>
    - Apoiar a organização pessoal do membro do time<br>
    - Em casos de excessiva dificuldade, promover treinamentos, pareamentos, dojôs, para despender menor tempo na execução da tarefa<br>
    - Motivar a equipe<br>
    - Verificar a contribuição de um membro em relação ao outro para disseminar habilidades e equilibrar o time.
    </td>
  </tr>
</table>

#### Métrica 01.5 - Quantidade de Story Points por Sprint
<table>
<tr>
  <td><b>Métrica</b></td>
  <td>Quantidade de Story Points por Sprint</td>  
</tr>
  <tr>
    <td><b>Objetivo de Medição</b></td>
    <td style="text-align: justify">Identificar o nível de trabalho da equipe para que facilite a estimativa e planejamento das Sprints.</td>  
  </tr>
  <tr>
    <td><b>Fórmula de Obtenção</b></td>
    <td>
    Q = SP
    <br><br>
      Onde: <br><BR>
      Q - Quantidade de Story Points por Sprint<br>
      SP - Soma de todas os Story Points entregues dentro daquela Sprint<br>
     </td>  
  </tr>
  <tr>
    <td><b>Escala de Medição</b></td>
    <td>Racional</td>  
  </tr>
  <tr>
    <td><b>Coleta</b></td>
    <td>
    Responsável: Membro de EPS.<br>
    Periodicidade: A cada Sprint.<br>
    Procedimento: Verificar a quantidade de pontos entregues na Sprint.</td>  
  </tr>
  <tr>
  <td><b>Meta</b></td>
  <td>Nivel estável de pontos</td>  
  </tr>
  <tr>
    <td><b>Análise</b></td>
    <td style="text-align: justify">Comparar as iterações anteriores e verificar o potencial de pontos entregues. É importante considerar o nivel de maturidade da equipe relacionao a estimativas de pontos das USs. A referência de velocity é iniciada logo na primeira Sprint, quando acontece a primeira coleta e verificação de pontos entregues. O Velocity tende a aumentar após a primeira Sprint e o ideal é que se estabilize no decorrer do projeto.
  </td>  
  </tr>
  <tr>
    <td><b>Providência</b></td>
    <td style="text-align: justify"> Discrepâncias de redução de Story Points entregues indica erro nas estimativas das USs. Cabe reavaliar as estimativas e planejar de forma mais adequada a próxima Sprint.
    </td>
  </tr>
</table>


### 6.2 - Métricas do Objetivo 2 - Código fonte

#### Métrica 2.1 - Complexidade Ciclomática
<table>
  <tr>
    <td><b>Métrica</b></td>
    <td>Complexidade Ciclomática</td>
  </tr>
  <tr>
    <td><b>Objetivo de Medição</b></td>
    <td style="text-align: justify">Identificar regiões de elevada complexidade ciclomática no código a fim de corrigí-las e tratá-las, para manter a qualidade de código.</td>  
  </tr>
  <tr>
    <td><b>Fórmula de Obtenção</b></td>
    <td style="text-align: justify">
    PR = 1000000 + (A - T) * 100000<br><br>
    Onde:<br><br>
    -PR: Pontos de Remediação<br>
    - A: Valor atual, é a pontuação de um determinado método ou unidade de código<br>
    - T: é o comprimento máximo configurado ou o número de complexidade McCabe.<br>
    O resultado é exibido por letras entre "A" e "F".    
    </td>  
  </tr>
  <tr>
    <td><b>Escala de Medição</b></td>
    <td>Ordinal</td>  
  </tr>
  <tr>
    <td><b>Coleta</b></td>
    <td>
    Responsável: Membro de EPS<br>
    Periodicidade: A cada Sprint<br>
    Procedimento: Coleta realizada pela ferramenta de análise estática <b>Code Climate</b>.</td>  
  </tr>
  <tr>
    <td style="text-align: justify"><b>Análise</b></td>
    <td style="text-align: justify">A complexidade ciclomática deve ser monitorada entre as sprints para avaliar a manutenção e qualidade do código. Se a complexidade aumenta muito, isso influencia a ocorrência de erros no código e pode refletir na execução de testes.</td>  
  </tr>
  <tr>
    <td><b>Meta</b></td>
    <td>Meta é manter a classificação entre "A" e "B".</td>  
  </tr>
  <tr>
    <td><b>Providência</b></td>
    <td>Planejar a refatoração do código para melhorar o índice e qualidade do produto.</td>
  </tr>

</table>

#### Métrica 2.2 -  Duplicação de código
<table>
  <tr>
    <td><b>Métrica</b></td>
    <td>Duplicação de código</td>
  </tr>
  <tr>
    <td><b>Objetivo de Medição</b></td>
    <td style="text-align: justify">Identificar regiões de ocorrência de código duplicado a fim de corrigí-las e tratá-las, visando um código modularizado e com bom reuso.</td>  
  </tr>
  <tr>
    <td><b>Fórmula de Obtenção</b></td>
    <td style="text-align: justify">Analisada pela ferramenta de análise estática <b>Code Climate</b>, que analisa os nós das àrvores sintática abstrata (AST). Compara a semelhança entre nós e seus sub-nós.</td>  
  </tr>
  <tr>
    <td><b>Escala de Medição</b></td>
    <td>Absoluta</td>  
  </tr>
  <tr>
    <td><b>Coleta</b></td>
    <td>
    Responsável: Membro de EPS<br>
    Periodicidade: A cada Sprint<br>
    Procedimento: Coleta realizada pela
    ferramenta de análise estática <b>Code Climate</b>.</td>  
  </tr>
  <tr>
    <td><b>Análise</b></td>
    <td style="text-align: justify">A meta é que não haja duplicação de código no projeto. Caso seja identificada alguma ocorrência, isso indica que o código pode ser aprimorado e priorizado o reuso e modularidade. É necessário observar se a quantidade de código duplicado aumenta no decorrer das sprints. Se esse cenário ocorrer, a manutenção do código fica cada vez mais comprometida. O ideal é que se reduza e mantenha-se em 0.</td>  
  </tr>
  <tr>
    <td><b>Meta</b></td>
    <td>A meta é que não haja código duplicado</td>  
  </tr>
  <tr>
    <td><b>Providência</b></td>
    <td style="text-align: justify">Com a ocorrência de código duplicado, o ideal é que seja refatorado o quanto antes a fim de não comprometer o andamento do projeto e o desenvolvimento do produto.</td>
  </tr>  
</table>

#### Métrica 2.3 -  Manutenibilidade
<table>
  <tr>
    <td><b>Métrica</b></td>
    <td>Manutenibilidade</td>
  </tr>
  <tr>
    <td><b>Objetivo de Medição</b></td>
    <td style="text-align: justify">Identificar regiões de ocorrência de anomalias no código a fim de corrigí-las e tratá-las.</td>  
  </tr>
  <tr>
    <td><b>Fórmula de Obtenção</b></td>
      <td style="text-align: justify">Analisada pela ferramenta de análise estática <b>Code Climate</b>, que analisa os nós das àrvores sintática abstrata (AST). O critério aplicado pela ferramenta trata-se do <b>tempo de remediação</b>, ou seja, o tempo para reverter uma anomalia encontrada. Para arquivos, são atribuidas letras de acordo com as faixas associadas, de A a F: <br><br>
    <li> A: 0 - 2M pontos de remediação </li>
    <li> B: >2M - 4M pontos de remediação</li>
    <li> C: >4M - 8M pontos de remediação</li>
    <li> D: >8M - 16M pontos de remediação</li>
    <li> F: >16M   pontos de remediação</li><br>
    A avaliação do repositório total, é dada seguindo os critérios de tempo de remediação associado ao número total de linhas do projeto:<br><br>
    DT = TR / TI<br><br>
    Onde:<br><br>
    <li> DT: Débito técnico</li>
    <li> TR: Tempo de Remediação</li>
    <li> TI: Tempo estimado de implementação</li>
    <br>
    A ferramenta gera essa classificação por repositório com uma letra entre A e F, conforme citado acima.
    </td>  
  </tr>
  <tr>
    <td><b>Escala de Medição</b></td>
    <td>Ordinal</td>  
  </tr>
  <tr>
    <td><b>Coleta</b></td>
    <td>
    Responsável: Membro de EPS<br>
    Periodicidade: A cada Sprint<br>
    Procedimento: Coleta realizada pela
    ferramenta de análise estática <b>Code Climate</b>.</td>  
  </tr>
  <tr>
    <td><b>Análise</b></td>
    <td style="text-align: justify">A meta é que a manutenibilidade seja A. Caso outra faixa de classificação seja atribuida, conforme cresça o tempo de remediação, isso indica risco pro projeto, visto que a manutenibilidade se compromete. Caso esses valores divirjam cada vez mais da classe "A", isso indica que o produto está sendo desenvolvido sem preocupação com a manutenção, o que aumenta a ocorrência de erros. O ideal é que se mantenha em "A", tanto para os arquivos, quanto para o repositório.</td>  
  </tr>
  <tr>
    <td><b>Meta</b></td>
    <td>A meta é que a classificação de manutenibilidade seja "A".</td>  
  </tr>
  <tr>
    <td><b>Providência</b></td>
    <td style="text-align: justify">Refatoração imediata do código, a fim de não comprometer o andamento do projeto e não se propague a proporção de crescimento do tamanho do código.</td>
  </tr>  
</table>


#### Métrica 2.4 - Cobertura de Testes
<table>
  <tr>
    <td><b>Métrica</b></td>
    <td>Cobertura de Teste</td>
  </tr>
  <tr>
    <td><b>Objetivo de Medição</b></td>
    <td style="text-align: justify">Identificar o nível de cobertura de teste, para manter a qualidade do código.</td>  
  </tr>
  <tr>
    <td><b>Fórmula de Obtenção</b></td>
    <td style="text-align: justify"> A ferramenta <b>Code Climate</b> utiliza o <b>CoveragePy</b> para avaliar os trechos de código cobertos por testes em relação a quantidade de linhas de código.
    </td>  
  </tr>
  <tr>
    <td><b>Escala de Medição</b></td>
    <td>Racional</td>  
  </tr>
  <tr>
    <td><b>Coleta</b></td>
    <td>
    Responsável: Membro de EPS<br>
    Periodicidade: A cada Sprint<br>
    Procedimento: Coleta realizada pela
    ferramenta de análise estática <b>Code Climate</b>.</td>  
  </tr>
  <tr>
    <td><b>Análise</b></td>
    <td style="text-align: justify">Nas sprints iniciais, a taxa de testes tende a crescer um pouco lentamente, devido à curva de aprendizagem pelo time de desenvolvimento. Depois, o ideal é que se mantenha na meta proposta para garantir a qualidade do código. Caso essa taxa de testes decaia, é necessário avaliar a dificuldade em realizar testes, que está associado ao nível de manutenibilidade do código.</td>  
  </tr>
  <tr>
    <td><b>Meta</b></td>
    <td>A meta é 90% de cobertura de teste.</td>  
  </tr>
  <tr>
    <td><b>Providência</b></td>
    <td style="text-align: justify">Caso haja dificuldade em realizar os testes, devem ser verificados o nível de manutenibilidade, o conhecimento do time na aplicação de testes, realizar treinamentos e dojôs, planejar melhor as User Stories para a Sprint, e avaliar os critérios de aceitação, que incluem a implementação de teste.</td>
  </tr>  
</table>


## 7. Quadro-resumo
<table>
  <tr style="text-align:center">
    <th style="text-align:center">Ferramenta</th>
    <th style="text-align:center">Métrica</th>
  </tr>
  <tr>
    <td>Codeclimate</td>
    <td>
      <ul>
        <li>Complexidade Ciclomática</li>
        <li>Manutenibilidade</li>
        <li>Cobertura de Teste</li>
        <li>Duplicação de código</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>Quadro de conhecimento</td>
    <td>
      <ul>
        <li>Nível de conhecimento</li>
      </ul>
    </td>  
  </tr>

  <tr>
    <td>Tabela no Google Drive</td>
    <td>
      <ul>
        <li>Tempo de dedicação</li>
      </ul>
    </td>  
  </tr>

  <tr>
    <td>Burndown (gerado pelo GitHub)</td>
    <td>
      <ul>
        <li>User Stories entregues em uma iteração</li>
      </ul>
    </td>  
  </tr>

  <tr>
    <td>Velocity</td>
    <td>
      <ul>
        <li>Story Points entregues por iteração</li>
      </ul>
    </td>  
  </tr>

  <tr>
    <td>Commits por dia (gerado pelo GitHub)</td>
    <td>
      <ul>
        <li>Nível de contribuição</li>
      </ul>
    </td>  
  </tr>
</table>



## Referências

[Critérios do Code Climate para Manutenibilidade](https://docs.codeclimate.com/docs/maintainability)
[Critérios do Code Climate para Cobertura de Testes](https://docs.codeclimate.com/docs/cognitive-complexity)
[Duplicação de Código](https://docs.codeclimate.com/docs/duplication-concept)
[Complexidade Ciclomática](https://docs.codeclimate.com/docs/radon)
