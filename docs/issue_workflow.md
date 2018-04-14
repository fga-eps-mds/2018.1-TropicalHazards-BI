# Issue Workflow
Neste documento, voce encontrará informações relevantes à forma que nossa equipe
organizou em relação as _issues_ do projeto.

Uma observação importante quanto ao projeto é que estamos usando a ferramenta ZenHub integrada aos nossos repositórios.

Este documento aborda os seguintes aspectos: [_milestones_](#milestones), [_issues_ com _milestones_](#Issues_com_Milestones), [criação de _issues_](#Criação_de_Issues), 
[_labels_ em _issues_](#Labels_em_Issues) e [_pull requests_](#Pull_Requests).

## Milestones
Neste projeto, _milestones_ são usadas para a demarcação de _sprints_.

## Issues com Milestones
_Issues_ que possuem _deadlines_ demarcadas por sprints deverão ser
associadas ao _milestone_ da _sprint_.

## Criação de Issues
Uma _issue_ deve ser criada toda vez que forem identificados um dos subsequentes aspectos relacionados ao projeto:
<ul>
  <li>Identificação de bugs;</li>
  <li>Sugestão de novas funcionalidades (_user stories_, _epics_, _tasks_ entre repositório de front/back);</li>
  <li>Documentar dúvidas.</li>
</ul>

Lembrando que:
<ul>
  <li>Issues não planejadas que foram completadas durante a Sprint não devem ser pontuadas</li>
  <li>Issues referente a documentação e back-end devem ser criadas no repositório do back-end, e as issues referente ao front-end devem ser criadas no repositório do front-end</li>
  <li>
    <ul>Associar a issue a pipeline correta:
      <li>Pipeline Features: Para issues que corresponde a Features</li>
      <li>Product Backlog: Novas issues são alocadas para o backlog do produto</li>
      <li>Sprint Backlog: Issues que serão executadas na Sprint</li>
      <li>In Progress: Issues sendo executadas</li>
      <li>Pending Review: Issues que estão esperando ser revisadas, ou seja já existe um pull request associado</li>
      <li>Done: Issues completadas, ou seja já revisadas</li>
      <li>Closed: Issues fechadas após a finalização da Sprint</li>
      <li>Questions: Issues que são perguntas</li>
    </ul>
  </li>
  <li>Caso surja algum problema com uma atividade que já foi documentada em uma Issue reabra a issue, não crie uma nova</li>
</ul>

## Labels em Issues
Todas as _issues_ devem possuir _labels_ para melhor sinalização e organização do repositório.
Cada _label_ deve ser utilizada segundo seu contexto, de forma que abranja a _issue_ a ser marcada.
Algumas regras mais comuns para usar labels em issues são:
<ul>
  <li>Issues planejadas para uma milestone devem ser marcadas com a label Planned</li>
  <li>Issues não planejadas que foram completadas durante a sprint, devem ser associadas a milestone correspondente a sprint e marcadas com a label Not Planned</li>
  <li>Issues correspondentes a história de usuário devem ser sinalizadas com a label US, no caso de história técnica utilizar a label TS</li>
  <li>Issues correspondentes a algum dos papéis(Scrum Master, PO, DevOps, Arquiteto e Ux/UI) devem ser sinalizadas com com as labels disponívels para representar os papéis.</li>
  <li>Tarefas que se tornaram débitos devem ser marcadas com a label Debts</li>
</ul>


As _labels_ disponíveis podem ser encontradas [aqui](https://github.com/fga-gpp-mds/2018.1-TropicalHazards-BI/labels)


## Pull Requests
Assim como as _issues_, os _Pull Requests_ devem ser corretamente demarcados com _labels_,
sendo que algumas _labels_ são passíveis de serem usadas apenas por PR's - como a _label_ de **pending review**.

Observações sobre _Pull requests_ :
<ul>
  <li>Pull requests não devem ser pontuados</li>
  <li>Em Pull requests é necessário marcar ao menos um Reviewer</li>
</ul>
