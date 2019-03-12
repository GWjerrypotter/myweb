import django_filters

from officialweb.models import Docs
from users.models import Users


class UsersFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Users
        fields = ['username', 'user_name']


class DocsFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Docs
        fields = ['doc_title', 'author', 'doc_content', 'publish_time', 'doc_remark']
