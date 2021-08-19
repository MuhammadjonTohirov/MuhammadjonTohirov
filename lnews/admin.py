from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from lnews.models import Profile, User, NewsCategory, News, NewsMedia, Comment, SubComment


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category_image', 'created_date', 'created_by')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created_date', 'created_by', 'updated_by')


@admin.register(NewsMedia)
class NewsMediaAdmin(admin.ModelAdmin):
    list_display = ('media', 'created_date', 'created_by')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenting_news', 'comment_body', 'created_date', 'created_by', 'updated_by')


@admin.register(SubComment)
class SubCommentAdmin(admin.ModelAdmin):
    list_display = ('comment_to', 'comment_body', 'created_date', 'created_by', 'updated_by')
