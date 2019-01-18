# JacaEventos
Aplicativo de eventos criado para avaliação da matéria de programação corporativa.

#### Diagrama de classes
![](http://gdurl.com/clKR "Diagrama de Classes")
#### Diagrama entidade relacionamento
https://drive.google.com/file/d/0Bx9wBuIYue81a0toTU01d05GcVE/view?usp=sharing
#### Diagrama de caso de uso
![](http://gdurl.com/eiR6 "Diagrama de caso de uso")
#### Arquitetura da solução
![](http://gdurl.com/UUGM "Arquitetura de solução")

#### Tecnologias usadas
* Python/Django - linguagem e framework
* PostgreSQL - Banco de Dados
* Heroku - Deploy e Hospedagem
* Django Rest - Api
* Padrao PEP 8 para python/django

### Descrição
Esse projeto foi desenvolvido na disciplina de Programação Coorporativa com intuito de estudar como construir sistemas dentro dos padrões de projeto e em equipe.

#### Alguns prints da aplicação
![](prints/login.png "Tela de inicio")
![](prints/pagina-inicial-not-button.png "Tela de inicio")
![](prints/principal-evento.png "Tela de inicio")



#### Observações

** Para baixar e rodar o JacaEventos localmente:**

```bash
$ git clone https://github.com/leaojn/Eventos
$ git pull orgin master
$ pip install -r requirements.txt
$ python manage.py runserver
```

** Povoando o banco de dados para testes **
```bash
$ python manage.py shell
$ exec(open('povoar.py').read())
```
