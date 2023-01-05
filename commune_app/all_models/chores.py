from django.db import models
from commune_app.all_models.users import User
from .communes import Commune


class Chore(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    budget = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    assign_to = models.ForeignKey(User, on_delete=models.CASCADE)
    passed = models.BooleanField()
    completed = models.BooleanField()
    Commune = models.ForeignKey(Commune, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def description_snippet(self):
        return self.description[:50] + '...'

    @staticmethod
    def get_chore(id):
        return Chore.objects.filter(id=id).first()
