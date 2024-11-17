# cadastro de clientes

from django.db import models

class User(models.Model):
    
    user_nickname = models.CharField(max_length=100, primary_key=True, default='')
    user_name = models.CharField(max_length=150, default='')
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default=0)
    
    def __str__(self):
        return f'Nickname: ({self.user_nickname}) | E-mail: ({self.user_email})'
                                
# models.model permite que eu interaja com o banco de dados usando métodos e atributos Python,
# em vez de escrever SQL manualmente.
# A classe User é um modelo do Django usado para representar a estrutura de uma tabela no banco de dados.
# models.CharField: define um campo como texto.
# max_length=100: limita o número de caracteres do campo a 100
# default='': O valor padrão será uma string vazia
