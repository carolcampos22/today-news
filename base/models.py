from django.db import models

# Create your models here.
class Register(models.Model):
    categories = (
        ('Filmes e séries', 'Filmes e séries'),
        ('Tecnologia', 'Tecnologia'),
        ('Ciências', 'Ciências'),
        ('Entretenimento', 'Entretenimento'),
        ('Saúde', 'Saúde'),
        ('Educação', 'Educação')
    )
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=500, default='Detalhes abaixo!')
    description = models.TextField(blank=True, null=False)
    image = models.URLField(max_length=500)
    category = models.CharField(max_length=50, choices=categories)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} [{self.created_at}] - {self.subtitle}'
    
    class Meta:
        verbose_name = 'Formulário de publicação de notícias'
        verbose_name_plural = 'Formulários de publicações de notícias'
        ordering = ['-created_at']