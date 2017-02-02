from django.db import models
from django.utils import timezone

tipi = (
    (1,"Bir üzlü"),
    (2,"Iki üzlü")
)

def filedirectory(instance,filename):
    return "words/%s_%s" % (str(timezone.now()).replace(" ","_")[:19].replace(":","_"),filename)

# Create your models here.
class Orders(models.Model):
    full_name = models.CharField(max_length=255,verbose_name="Ad və Soyadı")
    universitet = models.CharField(max_length=255,verbose_name="Universitet")
    kurs = models.CharField(max_length=255,verbose_name="Kurs")
    group = models.CharField(max_length=255,verbose_name="Qrup")
    email = models.EmailField(verbose_name="E-mail")
    number = models.CharField(max_length=255,verbose_name="Nomre")
    text = models.TextField(verbose_name="Əlavə məlumat")
    key = models.CharField(max_length=255,null=True,blank=True)
    types = models.IntegerField(choices=tipi,default=1)
    date = models.DateTimeField(null=True,blank=True,default=timezone.now)

    class Meta:
        ordering = ('-id',)
        verbose_name = "Sifarişçi"
        verbose_name_plural = "Sifarişçilər"

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        super(Orders, self).save(*args, **kwargs)
        try:
            items = Uploads.objects.filter(key=self.key)
            for x in items:
                x.relation_id = self.id
                x.save()
        except:
            pass
        super(Orders, self).save(*args, **kwargs)


class Uploads(models.Model):
    relation = models.ForeignKey(Orders, null=True, blank=True)
    key = models.CharField(max_length=255,null=True,blank=True)
    file = models.FileField(upload_to=filedirectory)

    def __str__(self):
        return self.file.name

    def upload_file(self):
        return "<a href='%s' target=_blank>Faylı yüklə</a>" % self.file.name

    upload_file.short_description = "File upload"
    upload_file.allow_tags = True