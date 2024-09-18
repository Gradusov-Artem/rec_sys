from rest_framework.decorators import api_view  # type: ignore
from .models import Company, Warehouse, Product
from django.http import JsonResponse  # type: ignore
import json
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
def create_company(request):
    try:
        data: dict = json.loads(request.body)
        id: int = int(data['id'])
        name: str = data['name']

        # Проверка на наличие компании с таким УНП
        if Company.objects.filter(id=id).exists():
            return JsonResponse({"error": "Компания с таким УНП уже существует"}, status=400)

        # Создание компании
        company = Company.objects.create(id=id, name=name)
        return JsonResponse({"message": "Компания успешно создана", "company_id": company.id}, status=201)
    except KeyError:
        return JsonResponse({"error": "Некорректные данные"}, status=400)

@api_view(['POST'])
def create_warehouse(request):
    try:
        data: dict = json.loads(request.body)
        id: int = int(data['id'])
        name: str = data['name']

        # Проверка номера склада
        if Warehouse.objects.filter(id=id).exists():
            return JsonResponse({"error": "Склад с таким номером уже существует"}, status=400)

        # Создание склада
        warehouse = Warehouse.objects.create(id=id, name=name)
        return JsonResponse({"message": "Склад успешно создан", "warehouse_id": warehouse.id}, status=201)
    except KeyError:
        return JsonResponse({"error": "Некорректные данные"}, status=400)

@api_view(['POST'])
def create_product(request):
    try:
        data: dict = json.loads(request.body)
        id: int = int(data['id'])
        name: str = data['name']
        amount: int = int(data['amount'])
        measure: str = data['measure']

        # Проверка id продукта
        if Product.objects.filter(id=id).exists():
            return JsonResponse({"error": "Продукт с таким id уже существует"}, status=400)

        # Создание продукта
        product = Product.objects.create(id=id, name=name, amount=amount, measure=measure)
        return JsonResponse({"message": "Продукт успешно создан", "product_id": product.id}, status=201)
    except KeyError:
        return JsonResponse({"error": "Некорректные данные"}, status=400)

api_view(['GET'])
def list_company(request):
    companies = Company.objects.all().values('id', 'name')
    return JsonResponse({"companies": list(companies)}, status=200)

def list_warehouse(request):
    warehouses = Warehouse.objects.all().values('id', 'name')
    return JsonResponse({"warehouses": list(warehouses)}, status=200)

def list_product(request):
    products = Product.objects.all().values('id', 'name', 'amount', 'measure')
    return JsonResponse({"products": list(products)}, status=200)
