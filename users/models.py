from decimal import Decimal
from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_cpf

class User(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True, validators=[validate_cpf])
    email = models.EmailField(unique=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))

    def save(self, *args, **kwargs):
        self.cpf = self.cpf.replace('.', '').replace('-', '')
        super(User, self).save(*args, **kwargs)

    def pay(self, value: Decimal):
        if not isinstance(value, Decimal):
            raise TypeError('Value deve ser um decimal')
        
        self.amount -= value
        # atomicidade, o valor so sera salvo qndo o valor for garantido

    def receive(self, value: Decimal):
        if not isinstance(value, Decimal):
            raise TypeError('Value deve ser um decimal')
        
        self.amount += value


