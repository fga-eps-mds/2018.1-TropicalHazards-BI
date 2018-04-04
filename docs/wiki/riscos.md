## 1. Relação de riscos

A tabela a seguir exibe os possíveis riscos existentes no decorrer do projeto, bem como sua causa, impacto e probabilidade de ocorrência.

<table>
    <thead>
        <tr>
            <th>Risco</th>
            <th>Descrição</th>
            <th>Causa</th>
            <th>Impacto</th>
            <th>Probabilidade</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>R01</td>
            <td>Arquitetura não escalável</td>
            <td>Arquitetura mal planejada</td>
            <td>Grande</td>
            <td>Muito Alto</td>
        </tr>
        <tr>
            <td>R02</td>
            <td>Persistência de dados</td>
            <td>Negligenciar os requisitos</td>
            <td>Grande</td>
            <td>Alto</td>
        </tr>
        <tr>
            <td>R03</td>
            <td>Falta de conhecimento sobre arquitetura</td>
            <td>Inexperiência dos membros com micro-serviços</td>
            <td>Grande</td>
            <td>Moderada</td>
        </tr>
        <tr>
            <td>R04</td>
            <td>Inexperiência com a tecnologia de desenvolvimento</td>
            <td>Nova tecnologia</td>
            <td>Grande</td>
            <td>Moderada</td>
        </tr>
        <tr>
            <td>R05</td>
            <td>Projeto não atender os requisitos</td>
            <td>Levantamento de requisitos falho e falta de validação constante</td>
            <td>Grande</td>
            <td>Moderada</td>
        </tr>
        <tr>
            <td>R06</td>
            <td>Comunicação falha entre os membros</td>
            <td>Negligenciar meio de comunicação com o time</td>
            <td>Grande</td>
            <td>Moderada</td>
        </tr>
        <tr>
            <td>R07</td>
            <td>Membro desestimulado</td>
            <td>Falta de interesse com o projeto ou fatores pessoais</td>
            <td>Grande</td>
            <td>Baixa</td>
        </tr>
        <tr>
            <td>R08</td>
            <td>Membro abandonar a disciplina</td>
            <td>Falta de compromentimento com a disciplina ou fatores pessoais</td>
            <td>Grande</td>
            <td>Baixa</td>
        </tr>
        <tr>
            <td>R09</td>
            <td>Tarefas planejadas não entregues</td>
            <td>Falha no planejamento da Sprint</td>
            <td>Grande</td>
            <td>Alto</td>
        </tr>
        <tr>
            <td>R10</td>
            <td>Não ocorrer evolução de conhecimento entre membros do time</td>
            <td>Pareamento, treinamentos falhos ou falta de compromentimento do membro</td>
            <td>Grande</td>
            <td>Baixa</td>
        </tr>
        <tr>
            <td>R11</td>
            <td>Conhecimento desnivelado</td>
            <td>Falha pareamento</td>
            <td>Grande</td>
            <td>Alta</td>
        </tr>
        <tr>
            <td>R12</td>
            <td>Product Backlog incompleto</td>
            <td>Falha no elicitação de requisitos</td>
            <td>Grande</td>
            <td>Alta</td>
        </tr>
        <tr>
            <td>R13</td>
            <td>Falta de ambiente de desenvolvimento</td>
            <td>Falha no DevOps</td>
            <td>Grande</td>
            <td>Baixa</td>
        </tr>
        <tr>
            <td>R14</td>
            <td>Alteração no escopo</td>
            <td>Falta de validação constante com o cliente</td>
            <td>Médio</td>
            <td>Moderada</td>
        </tr>
        <tr>
            <td>R15</td>
            <td>Falha no acompanhamento das métricas</td>
            <td>Planejamento incorreto  e negligenciamento das métricas</td>
            <td>Médio</td>
            <td>Moderada</td>
        </tr>
        <tr>
            <td>R16</td>
            <td>Curva de aprendizado ao trabalhar com tecnologias diferentes ao mesmo tempo</td>
            <td>Padrão arquitetural definido para o projeto</td>
            <td>Médio</td>
            <td>Alta</td>
        </tr>
        <tr>
            <td>R17</td>
            <td>Inexperiência com design e usabilidade</td>
            <td>Membros não possuem conhecimento sobre desenvolvimento de produto</td>
            <td>Médio</td>
            <td>Moderada</td>
        </tr>
        <tr>
            <td>R18</td>
            <td>Falta de equipamentos</td>
            <td>Motivos pessoais</td>
            <td>Grande</td>
            <td>Muito baixa</td>
        </tr>
        <tr>
            <td>R19</td>
            <td>Comunicação falha com o cliente</td>
            <td>Falta de disponibilidade</td>
            <td>Grande</td>
            <td>Baixa</td>
        </tr>
        <tr>
            <td>R20</td>
            <td>Falta de compromentimento</td>
            <td>Membro desinteressado</td>
            <td>Grande</td>
            <td>Moderada</td>
        </tr>
        <tr>
            <td>R21</td>
            <td>Ineficiência dos treinamento</td>
            <td>Falha no planejamento,execução ou pouca participação</td>
            <td>Médio</td>
            <td>Moderada</td>
        </tr>
        <tr>
            <td>R22</td>
            <td>Ineficiência dos pareamentos</td>
            <td>Horários incompatíveis e falha no planejamento</td>
            <td>Médio</td>
            <td>Alta</td>
        </tr>
    </tbody>
</table>

<b>Observação:</b> Os riscos citados acima foram classificados para os campos de impacto e probabilidade a partir de valores indicados nas tabelas a seguir:

### 1.1 Tabela de Probabilidade
<table>
  <tr>
    <th>Probabilidade</th>
    <th>Intervalo</th>
  </tr>
  <tr>
    <td>Muito Baixa</td>
    <td>menor que 10%</td>
  </tr>
  <tr>
    <td>Baixa</td>
    <td>de 11% a 30%</td>
  </tr>
  <tr>
    <td>Média</td>
    <td>de 31% a 50%</td>
  </tr>
  <tr>
    <td>Alta</td>
    <td>de 51% a 60%</td>
  </tr>
  <tr>
    <td>Muito alta</td>
    <td>de 61% a 70%</td>
  </tr>
</table>

### 1.2 Tabela de Impacto
<table>
  <tr>
    <th>Impacto</th>
    <th>Intervalo</th>
  </tr>
  <tr>
    <td>Muito Baixa</td>
    <td>menor que 20%</td>
  </tr>
  <tr>
    <td>Baixa</td>
    <td>de 21% a 40%</td>
  </tr>
  <tr>
    <td>Média</td>
    <td>de 41% a 60%</td>
  </tr>
  <tr>
    <td>Alta</td>
    <td>de 61% a 80%</td>
  </tr>
  <tr>
    <td>Muito alta</td>
    <td>Acima de 80%</td>
  </tr>
</table>
