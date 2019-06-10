from rest_framework import serializers

from apps.user.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        exclude = ['is_admin', 'is_active', 'is_staff']
