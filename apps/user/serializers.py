from rest_framework import serializers

from apps.user.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'uid', 'displayName', 'email', 'phoneNumber', 'photoURL', 'providerID']
