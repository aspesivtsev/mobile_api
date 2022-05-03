from django.db import models
from django.urls import reverse

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
    title = models.CharField(max_length=300, verbose_name="Заголовок", help_text="название аттракциона")
    image_url = models.ImageField(upload_to='attraction', blank=True, verbose_name="Изображение JPG, PNG", help_text="690х388 *.jpg или *.png")
    short_description = models.CharField(max_length=600)
    description = models.TextField(blank=True, verbose_name="Описание", help_text="текст")
    additional_link = models.CharField(max_length=500, blank=True, verbose_name="Дополнительная ссылка")
    attr_types = models.ManyToManyField(AttractionType, blank=True)
    work_time = models.CharField(max_length=100, verbose_name="Время работы")
    age = models.IntegerField(default=6, verbose_name="Возраст")
    height = models.IntegerField(default=100, verbose_name="Рост")
    location = models.ForeignKey(ParkLocation, blank=True, null=True, on_delete=models.CASCADE)
    with_adults = models.CharField(max_length=200, blank=True, verbose_name="посещение со взрослыми")
    is_purchased_separately = models.BooleanField(default=False, verbose_name="покупается отдельно")
    specs = models.CharField(max_length=400, blank=True, verbose_name="Специальная информация")
    is_active = models.BooleanField(default=False, verbose_name="опубликован")
    is_working = models.BooleanField(default=False, verbose_name="работает")
    sorting = models.IntegerField(default=100, verbose_name="Сортировка")
    wait_time = models.IntegerField(default=10, verbose_name="Время ожидания минут")
    is_favorite = models.BooleanField(default=False, verbose_name="избранный")
    created = models.DateTimeField(auto_now_add=True, verbose_name="создан")
    modified = models.DateTimeField(auto_now=True, verbose_name="редактировался")
    def get_full_img_path(self):
        return reverse('api:attractions', args=[self.image_url].url)

    class Meta:
        ordering = ('sorting', 'title')
        verbose_name = 'Аттракцион'
        verbose_name_plural = 'Аттракционы'

    def __str__(self):
        return f'{self.title}'
