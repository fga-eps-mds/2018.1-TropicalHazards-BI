# Rodando GitHub Pages localmente
Para rodar o GitHub pages localmente siga os passos:

1. Crie a imagem do Docker com:
```bash
docker build -t ghpages .
```

2. Inicie o container:
```bash
docker run --name ghpages-cont -p 4000:4000 ghpages
```

3. Acesse a página no endereço [0.0.0.0:4000](0.0.0.0:4000)
