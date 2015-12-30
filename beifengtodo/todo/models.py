#! encoding=utf8
from django.db import models

# Create your models here.

class Todo(models.Model):
    ptime = models.DateTimeField(auto_now=True,
                                 auto_created=True,
                                 verbose_name=u'记录时间')
    content = models.CharField(max_length=400,
                               verbose_name=u'待办事项')
    status = models.BooleanField(default=False)

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = u'代办事项表'
        ordering = ['-ptime']