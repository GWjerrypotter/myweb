import json

from django.core import serializers
from django.http import JsonResponse
from django.views.generic.base import View
# from django.views.generic import ListView
from officialweb.models import Docs


class DocsListView(View):
    def get(self, request):
        docs = Docs.objects.all()
        json_data = serializers.serialize('json', docs)
        json_data = json.loads(json_data)

        return JsonResponse(json_data, safe=False)
