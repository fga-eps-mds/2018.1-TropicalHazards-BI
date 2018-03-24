# Metodologia
## Papéis
### Scrum Master
<p align = "justify">O Scrum Master é responsável por dar suporte a implementação do Scrum durante todo o processo. O Scrum master faz isso ajudando todos os membros do time a entender quais os valores, práticas e regras do Scrum.

**A principal responsabilidade desse papel é identificar os riscos e impedimentos enfrentados pelos membros do time e responder o mais rápido possível com o objetivo de mitigá-los.**

**Responsabilidades:**
- Garantir que o Time Scrum entenda os rituais e regras da metodologia.
- Garantir aplicação da metodologia.
- Garantir coleta e análise de métricas.
- Disponibilizar indicadores de forma transparente aos membros do time.
- Disponibilizar os dados necessários e condições para rituais Scrum durante a execução das Sprints.
- Identificar os riscos do projeto.
- Mover equipe para resolver impedimentos.

### Product Owner

<p align = "justify">O Product Owner tem o papel de colaborar e intermediar a comunicação entre o time de desenvolvimento e o cliente. Para isso, é necessária uma sólida compreensão do domínio do negócio e das diferentes necessidades das partes interessadas. 

<p align = "justify">Deve ser capaz de compreender as capacidades da equipe de desenvolvimento para que haja uma negociação consciente com o cliente e auxiliar o time para obter resultados que satisfaçam as expectativas e necessidades do cliente. Ou seja, deve consciliar a realidade da equipe de desenvolvimento com as expectativas dos stakeholders.

<p align = "justify">Para esse projeto, existe a atuação do Product Owner Interno e do Product Owner Externo. O Product Owner Interno é um membro da disciplina de Engenharia de Produto de Software (EPS) que se comunica mais fortemente com o Product Owner Externo, que de fato interage  diretamente com o cliente e o representa. Ao longo de todo o projeto, o Product Owner Externo será representado por um coach das disciplinas de Engenharia de Produto de Software (EPS) e Métodos de Desenvolvimento de Software (MDS).

### Product Owner Externo
<p align = "justify">O Product Owner Externo comunica-se diretamente com o cliente e apresenta suas necessidades ao time de desenvolvimento.É responsável por negociar diretamente com o cliente o escopo do projeto. Detém a propriedade dos critérios de aceitação do produto.

**Responsabilidades**
- Comunicar-se diretamente com o cliente do projeto e entender suas necessidades para o projeto.
- Garantir que as novas funcionalidades sigam a visão do projeto.
- Garantir que os requisitos definidos junto com o cliente sejam seguidos pelo time.
- Definir o escopo do projeto. 
- Validar o escopo do projeto para o time de desenvolvimento.
- Validar as entregas do produto durante a execução do projeto.

### Product Owner Interno
<p align = "justify">O Product Owner Interno deve ter uma sólida compreensão do escopo do projeto definido com o Product Owner Interno e apresentar as necessidades para o time de desenvolvimento. Está mais próximo do time de desenvolvimento e interage mais comumente com os rituais definidos pelo Scrum junto ao time. É um membro do próprio time.

**Responsabilidades**
- Comunicar-se constantemente com o Product Owner Externo para verificar a aceitação dos artefatos gerados durante o processo.
- Garantir que as novas funcionalidades sigam a visão do projeto.
- Garantir que os requisitos definidos junto com o cliente sejam seguidos pelo time.
- Garantir que todo o time tenha conhecimento dos requisitos do produto e das avaliações feitas pelo cliente.
- Motivar a equipe para propor soluções que realmente atendam as necessidades do cliente.
- Transmitir e priorizar os requisitos ou recursos do aplicação para o time de desenvolvimento.
- Definir os itens que compõem o Product Backlog.
- Ajudar a priorizar as Histórias de Usuário do Backlog da Sprint, durante o Planejamento da Sprint, esclarescendo quaisquer detalhes para a execução do trabalho. 
- Apresentar as Histórias de Usuário priorizadas ao Product Owner Externo, para que sejam validadas por ele.

**O Product Owner não deve levar novas Histórias de Usuário durante uma Sprint em execução. O planejamento da Sprint deve ser mantido até sua conclusão.**

### Arquiteto
<p align = "justify">O Arquiteto do Software é o responsável por conhecer profundamente o projeto e negócio do sistema desenvolvido, necessitando de um alto conhecimento técnico para garantir a visualização da arquitetura do sistema em alto nível para o resto da equipe, permitindo a compreensão de componentes, conectores e interfaces do software.

**A principal responsabilidade desse papel é garantir que a estrutura do software esteja organizada de modo que os componentes mais significantes do sistema sejam compostos de sistemas e interfaces sucessivamente menores.**

**Responsabilidades:**
* Garantir que a equipe possa visualizar o que é fundamental para a compreensão de um sistema em seu ambiente.
* Estar sempre atualizado em relação a evolução do código e do produto.
* Definir/Criar e especificar frameworks, padrões e técnicas para o projeto.
* Garantir que a equipe adote um design de componentização.
* Promover o desenvolvimento de um sistema com mais pontos de reutilização.
* Comunicar interações e dependências de componentes para os desenvolvedores.

### DevOps
<p align = "justify">O especialista *DevOps* é o responsável pela criação, manutenção e evolução da infraestrutura operacional do projeto, evitando que problemas relacionados a mesma afetem a equipe de desenvolvimento ou o produto.

**A principal responsabilide desse papel é viabilisar a integração e o *deploy* continuos e automatizados do software produzido pela equipe.**

**Responsabilidades:**
- Fornecer consultoria para a equipe em questões relacionadas a infraestrutura operacional.
- Identificar e propor soluções para problemas relacionados infraestrutura operacional.
- Disponibilizar ambiente de desenvolvimento estavel e homogênio pra equipe.
- Configurar ferramentas para automatizar a itegração continua do software produzido.
- Configurar ferramentas para automatizar o deploy continuo do software produzido.

### Especialista de UX/UI
<p align = "justify">O especialista de UX/UI é responsável por monitorar, validar, providenciar consultoria e auxiliar a equipe de desenvolvimento durante a elaboração das interfaces com o usuário.

**A principal responsabilide desse papel é auxiliar a equipe de desenvolvimento, com a prestação de serviços de consultoria, à implementar uma interface confortável para o usuário em suas macro e micro interações com o sistema.**

**Responsabilidades:**
- Auxiliar a equipe na produção dos documentos relacionados à UX ou UI.
- Servir consultorias quanto ao design de interfaces.
- Garantir a usabilidade da aplicação.
- Providenciar treinamentos de design à equipe, quando necessário.
- Identificar erros de front-end.
- Garantir a qualidade visual da aplicação.

## Rituais
### Sprint Planning
<p align = "justify">Tem como objetivo identificar o foco e planejar o trabalho que será realizado durante a Sprint. Esse planejamento é feito de forma colaborativa com todo o time Scrum. Ao identificar o foco e o trabalho que deve ser realizado para atingir o objetivo da Sprint o Time de Desenvolvimento decidirá como construir essas funcionalidades, dividindo cada nas tarefas necessárias para que se encaixe no conceito de **Pronto** da equipe. No planejamento da Sprint são respondidas as seguintes perguntas:

- Qual o foco dessa Sprint?
- O que pode ser entregue como resultado para atingir o foco planejado?
- Como o trabalho necessário para entregar o incremento será realizado? Ou seja, quais tarefas serão executadas?

:alarm_clock:**Time-box: 2 horas**

**Artefatos produzidos:**
- Documento de planejamento de Sprint
- Sprint Backlog

### Daily Meeting
<p align = "justify">A reunião diária tem como objetivo inspecionar o progresso em direção ao objetivo da sprint, planejar as próximas 24 horas do Time de Desenvolvimento e identificar impedimentos que podem ameaçar a entrega do incremento planejado.

Cada membro do time deve responder:
- O que eu fiz ontem que contribui para o time atingir o planejado para a Sprint?
- O que eu planejo fazer hoje?
- Quais impedimentos podem ameaçar a entrega do incremento planejado?

:alarm_clock:**Time-box: 15 minutos**

#### Local e horário de realização
<table>
    <tr>
        <td></td>
        <td><b>Local</b></td>
        <td><b>Horário</b></td>
    </tr>
    <tr>
        <td><b>Segunda</b></td>
        <td>FGA</td>
        <td>13:40</td>
    </tr>
    <tr>
        <td><b>Terça</b></td>
        <td>FGA</td>
        <td>13:40</td>
    </tr>
    <tr>
        <td><b>Quarta</b></td>
        <td>FGA</td>
        <td>13:40</td>
    </tr>
    <tr>
        <td><b>Quinta</b></td>
        <td>FGA</td>
        <td>13:40</td>
    </tr>
    <tr>
        <td><b>Sexta</b></td>
        <td>Remoto</td>
        <td>13:40</td>
    </tr>
</table>

### Sprint Review
<p align = "justify">A Revisão da Sprint é realizada no final da Sprint e tem como objetivo inspecionar o incremento produzido e adaptar o **Backlog do Produto** se necessário.É apresentado para as partes interessadas o resultado gerado na Sprint com o propósito de obter feedback e promover a colaboração.

Elementos da revisão de Sprint:

- O Product Owner esclarece quais itens do Backlog do Produto foram **Prontos** e quais não foram **Prontos**;
- O Time de Desenvolvimento identifica quais foram os gargalos que impediram que itens fossem entregues;
- O Time de Desenvolvimento demonstra o trabalho que está **Pronto** e responde questões sobre o incremento;
- O Time Scrum, orientados pela Product Owner discute os Backlog do Produto tal como está, com o objetivo de identificar possíveis alterações necessárias e os próximos alvos de entrega;
- Revisão de tempo, orçamento e métricas de qualidade.

**Artefatos produzidos:**
- Documento de revisão e retrospectiva de Sprint
- Backlog do Produto revisado

:alarm_clock:**Time-box: 1 hora**

#### Local e horário de realização
<table>
    <tr>
        <td></td>
        <td><b>Local</b></td>
        <td><b>Horário</b></td>
    </tr>
    <tr>
        <td><b>Sábado</b></td>
        <td>FGA</td>
        <td>12:30</td>
    </tr>
</table>

### Sprint Retrospective
<p align = "justify">A Retrospectiva de Sprint tem como foco o Time Scrum, é uma oportunidade para a equipe inspecionar a si próprio e identificar pontos de melhoria a serem destacados na próxima Sprint em relação as pessoas, os relacionamentos e os processos e ferramentas utilizados.

Na retrospectiva o Time Scrum deve responder:
- Quais os pontos positivos da Sprint?
- Quais os pontos negativos da Sprint?
- O que pode ser melhorado?

Ao final da retrospectiva o Time Scrum deverá identificar quais ações serão necessárias para implementar as melhorias propostas.

**Artefatos produzidos:**
- Documento de revisão e retrospectiva de Sprint

:alarm_clock:**Time-box: 45 minutos**

#### Local e horário de realização
<table>
    <tr>
        <td></td>
        <td><b>Local</b></td>
        <td><b>Horário</b></td>
    </tr>
    <tr>
        <td><b>Sábado</b></td>
        <td>FGA</td>
        <td>12:30</td>
    </tr>
</table>
