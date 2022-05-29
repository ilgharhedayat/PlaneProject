from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class SiteSetting(SingletonModel):
    title = models.CharField(max_length=125, verbose_name="عنوان سایت")
    logo = models.ImageField(upload_to='', verbose_name="لوگو")
    address = models.CharField(max_length=500, verbose_name="آدرس")
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    instagram = models.URLField(verbose_name="اینستاگرام", blank=True)
    linkedin = models.URLField(verbose_name="لینکدین", blank=True)
    twitter = models.URLField(verbose_name="واتساپ", blank=True)
    facebook = models.URLField(verbose_name='فیس بوک', blank=True)
    copyrights = models.CharField(max_length=500, verbose_name="کپی رایت")
    lang = models.FloatField(blank=True, verbose_name='طول جغرافیایی')
    lat = models.FloatField(blank=True, verbose_name='عرض جغرافیایی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'


class AboutUs(SingletonModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'


class BaseCore(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    title = models.CharField(max_length=15)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ContactUs(BaseCore):
    TITLE = (
        ('تستی', 'تستی'),
    )
    title = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'تماس باما'
        verbose_name_plural = 'تماس با ما'


class WorkWith(BaseCore):
    TITLE = (
        ('تستی', 'تستی'),
    )
    title = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'همکاری با ما'
        verbose_name_plural = 'همکاری با ما'


class Service(models.Model):
    title = models.CharField(max_length=125)
    image = models.ImageField(upload_to='')
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'حدمت'
        verbose_name_plural = 'خدمات'


class Rules(SingletonModel):
    title = models.CharField(max_length=125)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'قوانین'
        verbose_name_plural = 'قوانین'
