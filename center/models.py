from django.db import models


tipi = (
    (1,"Bir üzlü"),
    (2,"Iki üzlü")
)

# Create your models here.
class Orders(models.Model):
    full_name = models.CharField(max_length=255,verbose_name="Ad və Soyadı")
    universitet = models.CharField(max_length=255,verbose_name="Universitet")
    kurs = models.CharField(max_length=255,verbose_name="Kurs")
    group = models.CharField(max_length=255,verbose_name="Qrup")
    email = models.EmailField(verbose_name="E-mail")
    number = models.CharField(max_length=255,verbose_name="Nomre")
    text = models.TextField(verbose_name="Əlavə məlumat")
    types = models.IntegerField(choices=tipi,default=1)

    class Meta:
        ordering = ('-id',)
        verbose_name = "Sifarişçi"
        verbose_name_plural = "Sifarişçilər"

    def __str__(self):
        return self.full_name
