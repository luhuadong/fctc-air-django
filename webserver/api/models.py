from django.db import models
from datetime import datetime

# Create your models here.

class TestUsers(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length=16)
    addtime=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name + ":" + self.phone

    class Meta:
        db_table = 'myapp_users' # 指定表名

"""
create table airdata(
    id       int          unsigned not null auto_increment PRIMARY KEY,
    dn       varchar(32)  not null,
    temp     float,
    humi     float,
    dust     int,
    tvoc     int,
    eco2     int,
    hcho     int,
    time     timestamp
);
"""

class AirData(models.Model):
    ''' airdata 数据表模型 '''

    #id = models.IntegerField()
    dn = models.CharField(max_length=32)
    temp = models.FloatField()
    humi = models.FloatField()
    dust = models.IntegerField()
    tvoc = models.IntegerField()
    eco2 = models.IntegerField()
    hcho = models.IntegerField()
    cdate = models.DateTimeField(default=datetime.now)

    def toDict(self):
        ob = {
            'id'   : self.id,
            'dn'   : self.dn,
            'temp' : self.temp,
            'humi' : self.humi,
            'dust' : self.dust,
            'tvoc' : self.tvoc,
            'eco2' : self.eco2,
            'hcho' : self.hcho,
            'cdate': self.cdate
        }
        return ob

    class Meta:
        db_table = 'airdata' # 指定表名