from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Company
from django.http import JsonResponse
import json

@api_view(['POST'])
def create_company(request):
    try:
        data = json.loads(request.body)
        id = data['id']
        name = data['name']

        # Проверка на наличие компании с таким УНП
        if Company.objects.filter(id=id).exists():
            return JsonResponse({"error": "Компания с таким УНП уже существует"}, status=400)

        # Создание компании
        company = Company.objects.create(id=id, name=name)
        return JsonResponse({"message": "Компания успешно создана", "company_id": company.id}, status=201)
    except KeyError:
        return JsonResponse({"error": "Некорректные данные"}, status=400)

