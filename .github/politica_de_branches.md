# Política de *branches*

### 1 - Nunca dê *commit* diretamente na *master* ou na *development*
  Para garantir a integridade do projeto, bem como a estabilidade da *master* ela só poderá ser alterada a partir de *Pull Requests* da *development*, que por sua vez só sera alterada atravez de *Pull Requests* da *branch* que implementou aquela alteração.

### 2 - Toda *branch* deve ser relacionada a uma *issue*
  Uma *branch* é criada com o objetivo de alterar uma parte do projeto, e essa possivel alteração deve estar documentada em uma *issue*, de forma que seja fácil identificar qual é o tipo de modificação proposta na mesma (exceto as *branches* *master* e *development*).  

### 3 - Dê nomes significativos as *branches* que criar
  Todas as *branches* devem ser nomeadas em inglês e possuir o seguinte formato, a palavra "issue" seguido do numero da *issue* relacionada a ela e uma breve descrição da mesma (ex: issue_78_issue_description).


### 4 - *Branches* devem ser excluídas após o *merge*
  Com exceção da *development*, toda *branch* deve ser excluída depois que o seu *Pull Request* for aceito  e tenha acontecido o *merge* da mesma com a *branch* a qual ela foi derivada.

### 5 Crie novas *branches* a partir de *branches* estáveis
  Ao criar uma *branch* garanta que sua *branch* pai seja estável, de preferencia que ela seja filha da *development*
