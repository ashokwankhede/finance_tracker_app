from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Balance(models.Model):
    user = models.ForeignKey(User, related_name='balances', on_delete=models.CASCADE)
    balance = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.balance)
    

class Transaction(models.Model):
    user = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=10)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.amount)



@receiver(post_save, sender=Transaction)
def update_related_model(sender, instance, **kwargs):
    # Get the related balance for the user who made the transaction
    related_instance = Balance.objects.filter(user=instance.user).first()
    
    if not related_instance:
        # Create a new balance if it doesn't exist
        related_instance = Balance.objects.create(user=instance.user, balance=0)
    else:
    # Update the balance based on the transaction type
        if instance.transaction_type == 'credit':
            related_instance.balance += float(instance.amount)
        else:
            related_instance.balance -= float(instance.amount)
        
    # Save the updated balance
    related_instance.save()
