import pdb

from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.user.models import User
from apps.user.serializers import UserSerializer


@api_view(["POST"])
def AuthLogin(request):
    userJSON = request.data
    user, created = User.objects.get_or_create(
        uid=userJSON['uid'],
        photoURL=userJSON['photoURL'],
        providerID=userJSON['providerId'],
        displayName=userJSON['displayName'],
        email=userJSON['email'],
        phoneNumber=userJSON['phoneNumber']
    )

    user.set_password('Informatica')
    user.save()
    authenticate(username=user.displayName, password='Informatica')

    responseJSON = UserSerializer(user)
    return Response({'uid': userJSON['uid']}, status='200')

