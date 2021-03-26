## Modelagem e estudo do impacto de políticas públicas <br/>na disseminação de COVID-19 no Brasil

### Trabalho de Conclusão de Curso
### Ciência da Computação - Universidade Federal de Minas Gerais

**Autor:** Raydan Elias Gaspar<br/>
**Orientador:** Flavio Vinicius Diniz de Figueiredo

### Instruções para execução do projeto:

É necessário baixar o arquivo de dados do link:<br/>
https://s3-sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2020/INFLUD-08-02-2021.csv

Crie uma pasta de nome 'data' no projeto, e coloque o download dos<br/> dados dentro da pasta 'data', antes de executar o notebook do projeto.

Alternativamente, há uma forma de executar sem o download prévio dos dados,<br/> porém é necessário alterar o arquivo e descomentar o comando, e comentar<br/> o comando atual de leitura local do arquivo de dados.

Vá té o arquivo "readData.py"<br/>
Comente a linha "database = f"../data/{file_name}"", adicionando o "#"<br/>
antes da linha, dessa forma:

```# database = f"../data/{file_name}"```

Em seguida, decomente a linha "# database = 'https://s3-sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2020/INFLUD-08-02-2021.csv'"<br/>
Retirando o "#" antes da linha, dessa maneira:<br/>

```database = 'https://s3-sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2020/INFLUD-08-02-2021.csv'```

Foi realizado dessa maneira por uma limitação do computador utilizado no<br/> desenvolvimento do trabalho, onde a opção de utilizar os dados de maneira online<br/> ocasionava o travamento da máquina por ausência de recursos computacionais.
