from django.utils import timezone
from rest_framework import serializers
from lnews.models import News, NewsCategory, NewsMedia, Profile, Country


class NewsCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = '__all__'


class MiniNewsCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ('id', 'title', 'description', 'category_image')


class NewsSerializer(serializers.ModelSerializer):
    main_category = MiniNewsCategoriesSerializer()
    category = serializers.ManyRelatedField(MiniNewsCategoriesSerializer())

    class Meta:
        model = News
        fields = ('id', 'title', 'body', 'banner', 'main_category', 'category', 'number_of_watches', 'created_date',
                  'updated_date')
