from django.db import models
from estoque.models import Produto


class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    produtos = models.ManyToManyField(Produto, through='PedidoProduto')
    feito = models.BooleanField(default=False)
    entregue = models.BooleanField(default=False)
    pago = models.BooleanField(default=False)

    @property
    def total(self):
        total = 0
        for item in self.pedidoproduto_set.all():
            total += item.produto.preco * item.quantidade
        return total

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente}"


class PedidoProduto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    class Meta:
        unique_together = ('pedido', 'produto')

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} no pedido #{self.pedido.id}"
