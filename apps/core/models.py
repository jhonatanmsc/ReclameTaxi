from django.db import models


class Reputation(models.Model):
    descr = models.CharField(max_length=90, null=True, blank=True)
    score = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Reputação'
        verbose_name_plural = 'Reputações'


class Platform(models.Model):
    name = models.CharField(max_length=90, null=True, blank=True)

    class Meta:
        verbose_name = 'Aplicativo'
        verbose_name_plural = 'Aplicativos'


class Driver(models.Model):
    name = models.CharField(max_length=90, null=True, blank=True)
    placa = models.CharField(max_length=10, null=True, blank=True)
    reputation = models.ForeignKey(Reputation, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'


class ItemPlatform(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, null=True, blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'aplicativo / motorista'
        verbose_name_plural = 'aplicativo / motorista'


class Report(models.Model):
    descr = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    changed = models.DateField(auto_now=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)
    aproved = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Reclamação'
        verbose_name_plural = 'Reclamações'


class Comment(models.Model):
    descr = models.CharField(max_length=90, null=True, blank=True)
    report = models.ForeignKey(Report, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
