from django.db import models
from datetime import datetime

class Esep(models.Model):
    whatsapp = models.CharField(null=True,blank=True,max_length=20,verbose_name='Ватсап')
    email = models.CharField(null=True,blank=True,max_length=20,verbose_name='Почта')
    telegram = models.CharField(null=True,blank=True,max_length=20,verbose_name='Телеграмм')

    description = models.TextField(null=True,blank=True,verbose_name='Описание')
    file = models.FileField(upload_to='files',null=True,blank=True,max_length=100,verbose_name='Файл')
    deadline = models.DateTimeField(null=True,blank=True,verbose_name='Дедлайн')

    date = models.DateTimeField(auto_now=datetime.now(),verbose_name='Дата принятия')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
    def __str__(self):
        return self.description[:20]

class Questions(models.Model):
    email = models.CharField(max_length=100,verbose_name='Почта')
    question = models.TextField(verbose_name='Вопрос')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.email