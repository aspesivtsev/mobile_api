from django.db import models

class AttractionType(models.Model):
    title = models.CharField(max_length=300)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Тип аттракциона'
        verbose_name_plural = 'Типы аттракционов'

    def __str__(self):
        return f'{self.title}'


class ParkLocation(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Тематическая земля'
        verbose_name_plural = 'Тематические земли'

    def __str__(self):
        return f'{self.title}'


class Attraction(models.Model):
    title = models.CharField(max_length=300)
    image_url = models.ImageField(upload_to='attraction', blank=True, verbose_name="Изображение JPG, PNG", help_text="690х388 *.jpg или *.png")
    short_description = models.CharField(max_length=600)
    description = models.TextField(blank=True, verbose_name="Описание", help_text="текст")
    attr_types = models.ManyToManyField(AttractionType, blank=True)
    work_time = models.CharField(max_length=50)
    age = models.IntegerField(default=6, verbose_name="Возраст")
    height = models.IntegerField(default=100, verbose_name="Сортировка")
    location = models.ForeignKey(ParkLocation, blank=True, null=True, on_delete=models.CASCADE)
    with_adults = models.CharField(max_length=200, verbose_name="посещение со взрослыми")
    is_purchased_separately = models.BooleanField(default=False, verbose_name="покупается отдельно")
    specs = models.CharField(max_length=400, blank=True, verbose_name="Специальная информация")
    is_active = models.BooleanField(default=False, verbose_name="активен")
    is_working = models.BooleanField(default=False, verbose_name="работает")
    sorting = models.IntegerField(default=500, verbose_name="Сортировка")
    wait_time = models.IntegerField(default=10, verbose_name="Время ожидания минут")
    is_favorite = models.BooleanField(default=False, verbose_name="избранный")
    created = models.DateTimeField(auto_now_add=True, verbose_name="создан")
    modified = models.DateTimeField(auto_now=True, verbose_name="редактировался")

    class Meta:
        ordering = ('title',)
        verbose_name = 'Аттракцион'
        verbose_name_plural = 'Аттракционы'

    def __str__(self):
        return f'{self.title}'
