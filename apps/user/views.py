from django.contrib.auth import authenticate
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from apps.user.models import User


def AuthLogin(request):

    userJSON = request.data
    user, created = User.objects.get_or_create(
        uid=userJSON['uid'],
        photo=userJSON['photoURL'],
        provider=userJSON['providerID'],
        nome=userJSON['displayName'],
        email=userJSON['email'],
        telefone=userJSON['phoneNumber']
    )

    user.set_password('Informatica')
    user.save()
    authenticate(username=user.nome, password='Informatica')
    responseJSON = serializers.serialize('json', user)
    return HttpResponse(responseJSON, mimetype='application/json')

