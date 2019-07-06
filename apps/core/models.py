from django.db import models


class Reputation(models.Model):
    descr = models.CharField(max_length=90, null=True, blank=True)
    score = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Reputação'
        verbose_name_plural = 'Reputações'


class Platform(models.Model):
    name = models.CharField(max_length=90, null=True, blank=True)
    color = models.CharField(u'cor', max_length=20, null=True, blank=True)
    icon = models.CharField(u'ícone', max_length=254, null=True, blank=True)

    class Meta:
        verbose_name = 'Aplicativo'
        verbose_name_plural = 'Aplicativos'

    def __str__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=90, null=True, blank=True)
    placa = models.CharField(max_length=10, null=True, blank=True)
    reputation = models.ForeignKey(Reputation, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'


class ItemPlatform(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, null=True, blank=True, related_name='drivers')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True, related_name='apps')

    class Meta:
        verbose_name = 'aplicativo / motorista'
        verbose_name_plural = 'aplicativo / motorista'


class Report(models.Model):
    uid = models.CharField(max_length=255, null=True, blank=True)
    descr = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    changed = models.DateField(auto_now=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)
    aproved = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Reclamação'
        verbose_name_plural = 'Reclamações'


class Comment(models.Model):
    uid = models.CharField(max_length=255, null=True, blank=True)
    descr = models.CharField(max_length=90, null=True, blank=True)
    report = models.ForeignKey(Report, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
