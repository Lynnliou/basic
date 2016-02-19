#coding=utf-8
from django.db import models

class event(models.Model):
    event_context=models.TextField(verbose_name='事件')
    event_time=models.DateTimeField(verbose_name='时间')
    update_time=models.DateTimeField(verbose_name='更新时间',null=True)
    event_state=models.BooleanField(verbose_name='状态',default=False)

    class Meta:
        verbose_name='事件'
        verbose_name_plural=verbose_name
        db_table='event'
    def __unicode__(self):
        return self.event_name