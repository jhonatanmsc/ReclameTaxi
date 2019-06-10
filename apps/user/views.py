from django.contrib.auth import authenticate
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from apps.user.models import User
from apps.user.serializers import UserSerializer


@require_http_methods(["GET", "POST"])
def AuthLogin(request):

    userJSON = request.data
    user, created = User.objects.get_or_create(
        uid=userJSON['uid'],
        photoURL=userJSON['photoURL'],
        providerID=userJSON['providerID'],
        displayName=userJSON['displayName'],
        email=userJSON['email'],
        phoneNumber=userJSON['phoneNumber']
    )

    user.set_password('Informatica')
    user.save()
    authenticate(username=user.nome, password='Informatica')

    responseJSON = UserSerializer(user)

    return HttpResponse(responseJSON, mimetype='application/json')

