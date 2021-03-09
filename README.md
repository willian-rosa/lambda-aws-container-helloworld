# lambda-aws-container-helloworld
Modelo de rodar container Docker no Lambda AWS

Baseado no artigo: [Container Image Support](https://aws.amazon.com/pt/blogs/aws/new-for-aws-lambda-container-image-support/)

## Testes
- Criar build: ``docker build -t lambda/helloworld .``
- Executar Container: ```docker run --rm  lambda/helloworld```


## Manual

- Criar um reposotório no [ECR](https://console.aws.amazon.com/ecr/repositories)
- Fazer Build da Imagem, Tag e realizar o push
- Criar uma função [AWS Lambda](https://console.aws.amazon.com/lambda) do tipo Container Image
  - Function name: Nome que vai de identificação (não tem relação ao código fonte)
  - Container image URI: adicionar a imagem que acabamos de registrar.  
    