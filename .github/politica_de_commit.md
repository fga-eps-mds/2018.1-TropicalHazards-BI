# Política de *Commit*

### 1 - Faça *commits* atômicos
  Sempre divida seu trabalho em *commits* pequenos e significativos de forma que cada *commit* implemente somente uma funcionalidade.

### 2 - Sempre escreva as mensgens de seus *commits* em inglês   
  Com o intuito de tornar o projeto mais acessível para contribuidores que não falem português, foi adotado que o idioma padrão para o código e tudo que for diretamente relacionado a ele(ex: *commits*, *branches* e *comentários de codigo*) é o inglês, logo as mensagens de *commits* devem ser escritas em inglês.

### 3 - Siga a regra 50/72
  As mensagens devem ser escritas em 50 caracteres, caso seja necessário escrever uma mensagem maior, escreva um resumo em 50 caracteres, adicione um linha em branco, e descreva melhor o *commit* em quantas linhas desejar, porém todas as linhas devem ter no máximo 72 caracteres. Caso não consiga descrever o seu *commit* com essa regra, o seu commit provavelmente não é atômico.


### 4 - Use *tags* no início de seus *commits*
  Para identificar de forma fácil e rápida o inteção do *commit*, eles devem ser iniciados com uma *tags*.

  As *tags* usadas nesse projeto são:
  * [ADD] = use quando adicionar novos métodos, classes ou arquivos;
  * [DEL] = use quando remover métodos, classes ou arquivos;
  * [MERGE] = use para sinalizar *merges*;
  * [UPDATE] = use quando fizer mudanças em métodos ou classes;
  * [FIX] = use quando consertar *bugs* ou falhas no projeto;
  * [RENAME] = use quando renomear um arquivo;
  * [TEST] = use quando trabalhar com testes;
  * [DOC] = use quando for trabalhar com arquivos de documentação;


### Exemplos de boas mensgens de *commits*
  * [ADD] creates a item_search method
  <br><br>
  creates a methods that searches for items , using bubble sort, in the<br>
  class City
  <br>

  * [UPDATE] chages search algorithm item_search
  <br><br>
    chages search algorithm in item_search from bubble sort to heap sort
    <br>

  * [Test] creates tests for method item_search
