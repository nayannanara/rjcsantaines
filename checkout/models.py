from django.db import models


class CartItemManager(models.Manager):

    def add_item(self, cart_key, inscricao):
        if self.filter(cart_key=cart_key, inscricao=inscricao).exists():
            created = False
            cart_item = self.get(cart_key=cart_key, inscricao=inscricao)
            cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
        else:
            created = True
            cart_item = CartItem.objects.create(
                cart_key=cart_key, inscricao=inscricao, price=inscricao.preco
            )
        return cart_item, created


class CartItem(models.Model):

    cart_key = models.CharField(
        'Chave do Carrinho', max_length=40, db_index=True
    )
    inscricao = models.ForeignKey('produtos.Inscricao', verbose_name='Produto', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    objects = CartItemManager()

    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens dos Carrinhos'
        unique_together = (('cart_key', 'inscricao'),)

    def __str__(self):
        return '{} [{}]'.format(self.inscricao, self.quantity)

