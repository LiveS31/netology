from django.db import models


# создаем таблицу Topic с name
class Topic(models.Model):
    name = models.CharField(max_length=50,  verbose_name='Название')


    #делаем корректный вывод
    def __str__(self):
        return self.name

    # #поля пометки для таблици
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
#добовляем в таблицу строку с отношением многие ко многим
    # Уксзываем наззвание промежуточной таблици through='Scoping'
    # Такблица к которой обращается Topic
    scope = models.ManyToManyField(Topic, through='Scoping', verbose_name='Разделы')

    class Meta:
        #поля пометки для таблици
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    #Создаем таблицу Scoping
class Scoping(models.Model):
# создаем строку tag с нешним ключем и удаление если пусто,
#                       добовляем поле пометки
    tag = models.ForeignKey(Topic, on_delete=models.CASCADE,
                            verbose_name = 'Раздел')
        #BooleanField -False - может быть пустой

    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                               related_name='scopes')
    is_main = models.BooleanField(default=False, verbose_name='Основной')

#тоже поля для таблици
    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематика статьи'
    #ordering - изменение порядка модели
        ordering = ['-is_main', 'tag']
