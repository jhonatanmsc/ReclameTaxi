from django.db import models


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

    class Meta:
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'

    def __str__(self):
        return f'{self.name}, placa: {self.placa}'


class ItemPlatform(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, null=True, blank=True, related_name='drivers')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True, related_name='apps')

    class Meta:
        verbose_name = 'aplicativo / motorista'
        verbose_name_plural = 'aplicativo / motorista'

    def __str__(self):
        return f'{self.driver.name}, app: {self.platform.name}'


class Report(models.Model):
    uid = models.CharField(max_length=255, null=True, blank=True)
    descr = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    changed = models.DateField(auto_now=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True, related_name="reports")
    aproved = models.BooleanField(default=True)
    resolved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Reclamação'
        verbose_name_plural = 'Reclamações'

    def __str__(self):
        resolvido = 'sim' if self.resolved else 'não'
        return f'uid: {self.uid}, motorista: {self.driver.name}, resolvido: {resolvido}'


class Comment(models.Model):
    uid = models.CharField(max_length=255, null=True, blank=True)
    descr = models.CharField(max_length=90, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    changed = models.DateField(auto_now=True)
    report = models.ForeignKey(Report, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return f'uid: {self.uid}, criado em: {self.created}'
