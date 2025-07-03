from django.contrib import admin
from .models import Pedido, PedidoProduto

class PedidoProdutoInline(admin.TabularInline):
    model = PedidoProduto
    extra = 1  # linhas vazias para adicionar novos produtos no pedido
    autocomplete_fields = ['produto']  # ajuda na busca se muitos produtos

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'feito', 'entregue', 'pago', 'data', 'total']
    inlines = [PedidoProdutoInline]
    search_fields = ['cliente']
    list_filter = ['data']

    def total(self, obj):
        return obj.total

    total.short_description = 'Total'
    total.admin_order_field = None
