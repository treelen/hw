from django.db import models

CATEGORY_CHOICES  = (
    ("PR", "Происшествия"),
    ("POL", "Политика"),
    ("SP", "Спорт"),
    ("KU", "Культура")
)

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default="SP", verbose_name="Категория")
    status = models.BooleanField(default=True, verbose_name="Статус") 

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Запись поста"
        verbose_name_plural = "Записи поста"