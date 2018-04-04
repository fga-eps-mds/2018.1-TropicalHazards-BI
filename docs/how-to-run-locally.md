# Rodando GitHub Pages localmente
Para rodar o GitHub pages localmente siga os passos na pasta **docs** do projeto:

1. Crie a imagem do Docker com:
```bash
docker build -t ghpages .
```

2. Inicie o container:
Ao iniciar o container é necessário mapear o **diretório raiz do projeto**, ou seja, o diretório acima de **docs** para dentro do container(project-dir):

```bash
docker run --name ghpages-cont -v project-dir/:/ghpages -p 4000:4000 ghpages
```

3. Acesse a página no endereço [0.0.0.0:4000](0.0.0.0:4000)
