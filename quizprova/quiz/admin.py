from django.contrib import admin
from .models import Banca, Orgao, Concurso, Cargo, Disciplina, Assunto, Prova, Questao, Resposta, TextoAssociado

admin.site.register(Banca)
admin.site.register(Orgao)
admin.site.register(Concurso)
admin.site.register(Cargo)
admin.site.register(Disciplina)
admin.site.register(Assunto)
admin.site.register(Prova)
admin.site.register(Questao)
admin.site.register(Resposta)
admin.site.register(TextoAssociado)