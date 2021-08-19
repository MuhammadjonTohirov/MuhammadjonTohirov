from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass


class BaseModel(models.Model):
    created_date = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='Updated at', auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_by', null=True,
                                   default=None, blank=False)
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='updated_by', null=True,
                                   default=None, blank=True)


class Profile(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )

    class Meta:
        verbose_name_plural = 'Profiles'


class Country(BaseModel):
    title = models.CharField(verbose_name='Country name', null=False, max_length=1024)
    flag = models.ImageField(verbose_name='Flag', null=False, help_text='A flag of the country')


class NewsCategory(BaseModel):
    title = models.CharField(verbose_name='Category name', null=False, help_text='Category title', max_length=1024)
    description = models.TextField(verbose_name='Description', null=True, max_length=2000)
    category_image = models.ImageField(verbose_name='Category image', null=True, blank=False, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News category'
        verbose_name_plural = 'News categories'


class News(BaseModel):
    title = models.CharField(verbose_name='Headline', null=False, max_length=1024)
    body = models.TextField(verbose_name='Description', null=False, max_length=1000000, default=None,
                            blank=False)
    main_category = models.ForeignKey(to=NewsCategory, on_delete=models.DO_NOTHING, blank=False, default=None,
                                      null=True, related_name='news_main_category')
    category = models.ManyToManyField(to=NewsCategory, blank=True, max_length=10, default=None,
                                      related_name='news_subcategories')
    banner = models.ImageField(verbose_name='Banner', null=True, blank=False, default=None)

    number_of_watches = models.IntegerField(verbose_name='Watch count', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News list'


class Comment(BaseModel):
    commenting_news = models.ForeignKey(to=News, verbose_name='News', null=True, default=None, blank=False,
                                        on_delete=models.CASCADE)
    comment_body = models.TextField(verbose_name='Comment', blank=False, null=True, default=None)

    def __str__(self):
        return self.comment_body


class SubComment(BaseModel):
    comment_to = models.ForeignKey(to=Comment, verbose_name='Comment', null=True, default=None, blank=False,
                                   on_delete=models.CASCADE)
    comment_body = models.TextField(verbose_name='Reply', blank=False, null=True, default=None)

    def __str__(self):
        return self.comment_body


class NewsMedia(BaseModel):
    media = models.FileField(verbose_name='Document', help_text='Photo/Document/Video/Audio', null=True, blank=False,
                             default=None)

    class Meta:
        verbose_name = 'Media list'
        verbose_name_plural = 'Media'


class FavoriteNews(BaseModel):
    fav_news = models.ForeignKey(to=News, blank=False, related_name='news_item_favorite', on_delete=models.DO_NOTHING)
    by_user = models.ForeignKey(User, blank=False, related_name='news_item_favorite_by', on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = (('fav_news', 'by_user'),)

