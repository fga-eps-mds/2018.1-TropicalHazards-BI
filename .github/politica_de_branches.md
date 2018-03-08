# Política de _branches_

### 1 - Nunca dê _commit_ diretamente na _master_ ou na _development_
  Para garantir a integridade do projeto, bem como a estabilidade da _master_ ela só poderá ser alterada a partir de _Pull Requests_ da _development_, que por sua vez só sera alterada atravez de _Pull Requests_ da _branch_ que implementou aquela alteração.

### 2 - Toda _branch_ deve ser relacionada a uma _issue_
  Uma _branch_ é criada com o objetivo de alterar uma parte do projeto, e essa possivel alteração deve estar documentada em uma _issue_, de forma que seja fácil identificar qual é o tipo de modificação proposta na mesma (exceto as _branches_ _master_ e _development_).  

### 3 - Dê nomes significativos as _branches_ que criar
  Todas as _branches_ devem ser nomeadas em inglês e possuir o seguinte formato, a palavra "issue" seguido do numero da _issue_ relacionada a ela e uma breve descrição da mesma (ex: issue_78_issue_description).


### 4 - _Branches_ devem ser excluídas após o _merge_
  Com exceção da _development_, toda _branch_ deve ser excluída depois que o seu _Pull Request_ for aceito  e tenha acontecido o _merge_ da mesma com a _branch_ a qual ela foi derivada.

### 5 Crie novas _branches_ a partir de _branches_ estáveis
  Ao criar uma _branch_ garanta que sua _branch_ pai seja estável, de preferencia que ela seja filha da _development_
