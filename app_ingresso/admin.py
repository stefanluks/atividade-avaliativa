from django.contrib import admin

from .models import Pessoa
from .models import PessoaFisca
from .models import Ingresso
from .models import Inscricao
from .models import Evento

@admin.register(Pessoa)
@admin.register(PessoaFisca)
@admin.register(Inscricao)
@admin.register(Ingresso)
@admin.register(Evento)

class NoticiaAdmin(admin.ModelAdmin):
    pass

