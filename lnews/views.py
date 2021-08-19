import datetime

from django.shortcuts import render
from rest_framework.request import Request as RestRequest
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny, IsAdminUser

from helpers.responses import AppResponse
from lnews.models import News, NewsCategory
from lnews.serializers import NewsSerializer, NewsCategoriesSerializer


class NewsViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny, ]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @action(methods=['POST'], detail=False)
    def all(self, request: RestRequest, pk=None):
        updated_at = request.data.get('updated_at', None)
        is_latest = request.data.get('is_latest', False)

        if updated_at is not None:
            self.queryset = self.queryset.filter(created_date__range=[updated_at, datetime.datetime.now()])

        s = self.serializer_class(self.queryset, many=True)
        return Response(AppResponse(s.data).success_body(key='news', updated_at=updated_at))

    @action(methods=['GET'], detail=True)
    def get(self, request: RestRequest, pk=None):
        item = self.queryset.filter(id=pk).first
        s = self.serializer_class(item, many=False)
        return Response(AppResponse(s.data.__str__()).success_body(key='news_item', updated_at=None))


# class NewsSecondViewSet(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated, ]
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer


class NewsCategoryViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny, ]
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategoriesSerializer

    @action(methods=['POST'], detail=False)
    def all(self, request: RestRequest, pk=None):
        updated_at = request.data.get('updated_at', None)
        if updated_at is not None:
            self.queryset = self.queryset.filter(created_date__range=[updated_at, datetime.datetime.now()])

        s = self.serializer_class(self.queryset, many=True)
        return Response(AppResponse(s.data).success_body(key='comments', updated_at=datetime.datetime.now().__str__()))
