from django.db import models


class Material(models.Model):
    nome = models.CharField(max_length=100)
    quantidade_em_estoque = models.DecimalField(max_digits=10, decimal_places=2)
    unidade = models.CharField(max_length=20)  # ex: gramas, ml, unidades

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    materiais = models.ManyToManyField(Material, through='ProdutoMaterial')

    def __str__(self):
        return self.nome


class ProdutoMaterial(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantidade_utilizada = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('produto', 'material')

    def __str__(self):
        return f"{self.quantidade_utilizada} {self.material.unidade} de {self.material.nome} em {self.produto.nome}"
