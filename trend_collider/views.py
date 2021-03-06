from django.shortcuts import render
import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render, redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponseRedirect
from datetime import datetime


from .models import Weigh_In, Stock_Pick, MyUser

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


def stock_list(request):
    stocks = Stock_Pick.objects.all().values('id', 'symbol', 'description')
    stock_symbols_list = list(stocks)
    return JsonResponse(stock_symbols_list, safe=False)


def weigh_ins(request):
    weigh_ins = Weigh_In.objects.filter(
        weigh_in_user=1).values('date', 'weight', 'id').order_by('date')

    weigh_ins_list = list(weigh_ins)

    return JsonResponse(weigh_ins_list, safe=False)


@api_view(['POST'])
def add_weigh_in(request):

    if request.method == 'POST':
        now = datetime.now()
        new = Weigh_In(weigh_in_user_id=1, date=now,
                       weight=request.data['weight'])
        new.save()
        return HttpResponse("Posted")


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def weigh_in_detail(request, id):
    weigh_in = Weigh_In.objects.get(
        id=id,)
    # find weigh_in by pk (id)

    if request.method == 'DELETE':

        weigh_in.delete()
        return HttpResponse("Deleted")

    if request.method == 'POST':

        now = datetime.now()
        new = Weigh_In(weigh_in_user_id=1, date=now, weight=id)
        new.save()
        return HttpResponse("Posted")

    if request.method == 'PUT':

        weight_revised = Weigh_In(
            weigh_in_user_id=1, date=request.data['date'], weight=request.data['weight'], id=id)
        weight_revised.save()

        return HttpResponse("Updated")

    return render(request)


def index(request):

    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },

    )


def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("index")))


def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )


def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )


def public(request):
    return HttpResponse("You don't need to be authenticated to see this")


@api_view(['GET'])
def private(request):
    return HttpResponse("You should not see this message if not authenticated!")
