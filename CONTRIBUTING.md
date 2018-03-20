## Como contribuir para esse projeto

### **Você achou um bug?**

* **Tenha certeza que o bug já não foi reportado** procurando no GitHub em [Issues](https://github.com/fga-gpp-mds/2018.1-TropicalHazards-BI/issues).

* Se você não encontrou nenhuma Issue aberta para esse problema, [abra uma nova](https://github.com/fga-gpp-mds/2018.1-TropicalHazards-BI/issues/new?template=bug_report.md). Tenha certeza de incluir um **título e descrição claros**, use um dos **templates** - provendo ao menos a informação requerida - e uma **amostra de código** ou uma **sreenshot** mostrando o problema.

### **Você corrigiu um bug?**

* Abra um novo **Pull Request** no GitHub com a correção.

* Garanta que o **PR** descreva claramento o problema e solução, que contenha toda a informação necessária para o template e que esteja relacionado a pelo menos uma Issue.

* Tenha certeza de que segue a [política de commit](https://github.com/fga-gpp-mds/2018.1-TropicalHazards-BI/blob/master/docs/policies/politica_de_commit.md)

### **Você planeja adicionar uma nova funcionalidade ou mudar uma existente?**

* Primeiro, cheque na [lista de Issues](https://github.com/fga-gpp-mds/2018.1-TropicalHazards-BI/issues) e tenha certeza de que ninguém está implementando a funcionalidade que você planeja criar. Caso não exista, você pode prosseguir.

* [Abra uma nova Issue](https://github.com/fga-gpp-mds/2018.1-TropicalHazards-BI/issues/new) com as informações necessárias ao template, seguindo o padrão User Story, Feature ou Epic.

## **Contribuindo**

#### 1 Configure o ambiente de desenvolvimento
Siga os passos definidos no [README](https://github.com/fga-gpp-mds/2018.1-TropicalHazards-BI/blob/master/README.md) para configuração do ambiente de desenvolvimento.

#### 2 Configurando o repositório 
Para poder contribuir, você precisa fazer um [fork](https://guides.github.com/activities/forking/) do repositório [Tropical Hazards BI](https://github.com/fga-gpp-mds/2018.1-TropicalHazards-BI)

Em seguida clone o fork para sua máquina local:
```bash
git clone https://github.com/user-name/2018.1-TropicalHazards-BI.git
```
Você deve também deve adicionar o repositório oficial do Tropical Hazards BI como um dos repositórios remotos:
```bash
git remote add tropicalhazards https://github.com/fga-gpp-mds/2018.1-TropicalHazards-BI.git
```

#### 3 Trabalhando em uma funcionalidade
Quando estiver trabalhando em uma funcionalidade, crie uma nova branch seguindo a [política de branches](https://github.com/fga-gpp-mds/2018.1-TropicalHazards-BI/blob/master/docs/policies/politica_de_branches.md), e tome como base a branch master do repositório oficial(**tropicalhazards/master**): 
```bash
git checkout -b issue_59_funcionalidade_x tropicalhazards/master
```
Faça as alterações necessárias e realize os commits, seguindo a [política de commits](https://github.com/fga-gpp-mds/2018.1-TropicalHazards-BI/blob/master/docs/policies/politica_de_commit.md).

Após finalizar os commits envie as alterações para o seu repositório remoto:
```bash
git push origin issue_59_funcionalidade_x
```

#### 4 Pull Request
Acesse o seu fork do repositório oficial (ex: https://github.com/user-name/2018.1-TropicalHazards-BI) e clique em "Pull Requests" no painel. Na próxima página, pressione "New pull request" no canto superior direito.

Seleciona como base a branch **development** do repositório oficial(**fga-ggp-mds/2018.1-TropicalHazards**) e compare com a branch referente a nova funcionalidade, por exemplo **issue_59_funcionalidade_x**, em seguida clique em "Create new pull request".

Preencha o template sugerido com as informações necessárias para descrever a mudança proposta, conecte o Pull Request a **Issue** relacionada e confirme a criação do Pull Request.

O seu Pull Request será analizado e a equipe responsável pelo projeto garante prover o feedback mais claro possível para sua proposta de mudança.

Com :heart:,

O time Tropical Hazards BI.
