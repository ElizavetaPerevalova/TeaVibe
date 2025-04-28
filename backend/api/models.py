from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    problem_type = models.CharField(max_length=50, choices=[
        ('technical', 'Техническая проблема'),
        ('billing', 'Проблема с оплатой'),
        ('general', 'Общая проблема'),
    ])
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.problem_type})"
