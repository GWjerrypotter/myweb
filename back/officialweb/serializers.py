from rest_framework import serializers

from officialweb.models import Docs
from users.models import Users, DeptMent


# class DeptSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DeptMent
#         fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    # dept = DeptSerializer()

    class Meta:
        model = Users
        fields = ('url', 'username', 'password', 'user_name', 'user_phone', 'dept', 'user_remark')

    # def create(self, validated_data):
    #     dept_data = validated_data.pop('dept')
    #     user = Users.objects.create(**validated_data)
    #     DeptMent.objects.create(dept_name=dept_data.dept_name, dept_phone=dept_data.dept_phone, dept_remark=dept_data.dept_remark)
    #     return user


class DocSerializer(serializers.ModelSerializer):
    publish_time = serializers.DateTimeField(format="%Y-%m-%d", required=False, read_only=True)

    class Meta:
        model = Docs
        fields = ('url', 'doc_type', 'doc_title', 'author', 'doc_content',
                  'doc_file', 'publish_time', 'clicks', 'doc_remark')
