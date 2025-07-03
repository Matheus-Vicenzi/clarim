from django.contrib import admin
from .models import Material, Produto, ProdutoMaterial  # importe TODOS os modelos usados

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['nome', 'quantidade_em_estoque', 'unidade']


class ProdutoMaterialInline(admin.TabularInline):
    model = ProdutoMaterial
    extra = 1  # quantas linhas vazias aparecerão para adicionar novos materiais

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco']
    search_fields = ['nome']  # <-- aqui, para habilitar o autocomplete
    inlines = [ProdutoMaterialInline]