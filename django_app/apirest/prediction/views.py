from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Shopping
from .serializers import ShopperSerializer
from rest_framework.decorators import api_view
from rest_framework import status

import joblib

# @csrf_exempt


@api_view(['GET', 'POST'])
def shoppers_list(request):

    if request.method == 'GET':
        shoppers = Shopping.objects.all()
        serializer = ShopperSerializer(shoppers, many=True)
        return Response(serializer.data) # JSON RESPONSE (, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShopperSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201) # JSON RESPONSE

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 400

# @csrf_exempt


@api_view(['GET', 'PUT', 'DELETE'])
def shopper_detail(request, pk):
    try:
        shopper = Shopping.objects.get(pk=pk)
    except Shopping.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ShopperSerializer(shopper)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ShopperSerializer(shopper, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        shopper.delete()
        return HttpResponse(status=204)


@csrf_exempt
def predict(request):
    """
    Renvoie une house avec la MEDV complétée
    (Attend une MEDV innexistante)
    """

    if request.method == 'GET':
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ShopperSerializer(data=data)

        if serializer.is_valid():
            data["Revenue"] = predict_revenue(data)
            serializer = ShopperSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


def predict_revenue(unscaled_data):

    colonnes = ["Administrative", "Administrative_Duration", "Informational", "Informational_Duration",
                "ProductRelated", "ProductRelated_Duration", "BounceRates", "ExitRates", "PageValues",
                "SpecialDay", "Month", "OperatingSystems", "Browser", "Region", "TrafficType", "VisitorType",
                "Weekend"]

    path_to_model = "./objects/rfc"
    path_for_encoder = "./objects/encoder"

    unscaled_data = [unscaled_data[colonne] for colonne in colonnes]

    model = joblib.load(path_to_model)
    encoder = joblib.load(path_for_encoder)

    scaled_data = encoder.transform(unscaled_data)
    revenue = model.predict(scaled_data)

    return revenue
