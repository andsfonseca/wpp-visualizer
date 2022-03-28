from lib2to3.pgen2 import token
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

import requests
import json

import random
import string
import time

WPP_CONNECT_API_URL = "http://localhost:21465/api/"
WPP_CONNECT_SECRET = "obyocijfvnwrakjainla"

# Create your views here.
@require_http_methods(["GET"])
def index_r(request):
    getToken(request)
    return HttpResponse("Executar esta linha redireciona para o front-end. TO-DO")

@require_http_methods(["GET"])
def isConnected(request):

    session_name, token = getToken(request)

    headers = {'Authorization': f'Bearer {token}'}
    r = requests.get(f"{WPP_CONNECT_API_URL}{session_name}/status-session", headers=headers)
    result = r.json()

    if(result["status"] == "CLOSED"):
        return JsonResponse({"status": False, "message" : "Not Connected"})
    
    return JsonResponse({"status": True, "message" : "Connected"})

@require_http_methods(["GET"])
def qr(request):

    session_name, token = getToken(request)

    result = None

    while (result is None or result["status"] != "Success"):

        headers = {'Authorization': f'Bearer {token}'}
        
        r = requests.get(f"{WPP_CONNECT_API_URL}{session_name}/status-session", headers=headers)
        result = r.json()

        if(result["status"] == "CLOSED"):
            headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json', 'accept': '*/*'}
            body = {'webhook': ''}

            r = requests.post(f"{WPP_CONNECT_API_URL}{session_name}/start-session", headers=headers, data=json.dumps(body))

        time.sleep(10)
    return HttpResponse("Got your qr")

def getToken(request):
    if request.session.get("wpp-connect-token") is None:

        #Create Session Name
        session_name = generateRandomString()

        #Requisita
        r = requests.post(f"{WPP_CONNECT_API_URL}{session_name}/{WPP_CONNECT_SECRET}/generate-token")
        result = r.json()
        
        if(result["status"] != "success"):
            return "", ""

        #Salva a sessão do wpp-connect
        request.session["wpp-connect-sessioname"] = session_name
        request.session["wpp-connect-token"] = result["token"]

    return request.session.get("wpp-connect-sessioname"), request.session.get("wpp-connect-token")
    
def generateRandomString(length = 20):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
