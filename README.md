# Turtle-Python-Lab
REST webservice criado para aprender o básico de Python, Flask, PyMongo e MongoDB.

Criar um banco no MongoDB, com os seguintes campos:
- Nome
- Telefone
- E-mail
- Idade

### Criação do banco
Dentro do MongoDB:
```
use turtle

db.turtle.insert({	
    "nome": "Matheus de Souza",
    "telefone": "1234567890",
    "email": "matheus.de.souza@ibm.com",
    "idade": 22
});
```

### Utilizando o projeto
Clonar esse repositório
```
git clone https://github.ibm.com/Matheus-de-Souza/Turtle-Python-Lab.git
```

Pelo terminal, dentro do diretório do projeto, executar
```
python app.py
```

### Endpoints
```
/
```
Retorna somente uma mensagem de texto, no estilo Hello World.

---

```
/consultaregistros
```
Retorna todos os registros do banco de dados, em formato JSON.

---

```
/consultaregistrosemail?email=<email>
```
Retorna todos os registros que possuem email igual ao parâmetro passado.

---
