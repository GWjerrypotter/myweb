from django.shortcuts import render
import json
import datetime as dt
import os
import uuid
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

from officialweb.filter import UsersFilter, DocsFilter
from officialweb.models import Docs
from officialweb.serializers import UserSerializer, DocSerializer
from users.models import Users


class DocsPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_query_param = 'p'


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    pagination_class = DocsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = UsersFilter
    search_fields = ('username', 'user_name')
    ordering_fields = ('dept__id',)


class DocViewSet(viewsets.ModelViewSet):
    queryset = Docs.objects.all()
    serializer_class = DocSerializer
    pagination_class = DocsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = DocsFilter
    # search_fields = ('username', 'user_name')
    # ordering_fields = ('dept__id',)


@csrf_exempt
def upload_image(request, dir_name):
    result = {"error": 1, "message": "上传出错"}
    files = request.FILES.get("imgFile", None)
    if files:
        result = image_upload(files, dir_name)
    return HttpResponse(json.dumps(result), content_type="application/json")


# 目录创建
def upload_generation_dir(dir_name):
    today = dt.datetime.today()
    dir_name = dir_name + '/%d/%d/' % (today.year, today.month)
    if not os.path.exists(settings.MEDIA_ROOT + dir_name):
        os.makedirs(settings.MEDIA_ROOT + dir_name)
    return dir_name


# 文件上传
def image_upload(files, dir_name):
    # 允许上传文件类型
    allow_suffix = ['jpg', 'png', 'jpeg', 'gif',
                    'bmp', 'zip', "swf", "flv",
                    "mp3", "wav", "wma", "wmv",
                    "mid", "avi", "mpg", "asf",
                    "rm", "rmvb", "doc", "docx",
                    "xls", "xlsx", "ppt", "htm",
                    "html", "txt", "zip", "rar",
                    "gz", "bz2"]
    file_suffix = files.name.split(".")[-1]
    if file_suffix not in allow_suffix:
        return {"error": 1, "message": "图片格式不正确"}
    relative_path_file = upload_generation_dir(dir_name)
    path = os.path.join(settings.MEDIA_ROOT, relative_path_file)
    if not os.path.exists(path):  # 如果目录不存在创建目录
        os.makedirs(path)
    file_name = str(uuid.uuid1()) + "." + file_suffix
    path_file = os.path.join(path, file_name)
    file_url = settings.MEDIA_URL + relative_path_file + file_name
    open(path_file, 'wb').write(files.file.read())
    return {"error": 0, "url": file_url}
