from django.shortcuts import render, HttpResponse, redirect
from .models import Car, Brand
from .forms import BrandForm
# from .forms import BrandForm, CarForm

def index(request):
    # list all car brands
    brands = list(Brand.objects.all())

    return render(request, 'pages/index.html', {'brands': brands})


def detail(request, brand_id):
    # provide all attributes from brand
    brand = Brand.objects.get(pk=brand_id)
    # brand.name, brand.cars (car__set)
    cars = brand.cars.all()

    return render(request, 'pages/detail.html', {'brand': brand, 'cars': cars})

def new_brand(request):
    if request.method=='POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('brand', brand_id=brand.id)
    form = BrandForm()
    return render(request, 'pages/new_brand.html', {'form': form})

def edit_brand(request, brand_id):
    brand = Brand.objects.get(pk=brand_id)
    if request.method=='POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('brand', brand_id=brand.id)

    form = BrandForm(instance=brand)
    return render(request, 'pages/new_brand.html', {'form': form})





# # helper functions
# def get_cars(brand_id):
#     return Brand.objects.get(id=brand_id)

# def index(request):
#     # list of all the car brands + add new
#     data = {
#         'all_brands': Brand.objects.all()
#     }
#     return render(request, 'pages/index.html', data)

# def detail(request, brand_id):
#     try:
#         brand = get_cars(brand_id)
#         cars = brand.cars.all()
#         return render(request, 'pages/detail.html', {'brand': brand, 'all_cars': cars})
#     except Exception as e:
#         print(e)
#         return HttpResponse('Error')

# def new_brand(request):
#     if request.method=='POST':
#         form = BrandForm(request.POST)
#         if form.is_valid():
#             brand = form.save(commit=False)
#             brand.save()
#             return redirect('cars_app:brand', brand_id=brand.id)
#     form = BrandForm()
#     return render(request, 'pages/new_brand.html', {'form':form, 'type':'new'})

# def edit_brand(request, brand_id):
#     brand = get_cars(brand_id)
#     if request.method=='POST':
#         form = BrandForm(request.POST, instance=brand)
#         if form.is_valid():
#             brand = form.save(commit=False)
#             brand.save()
#             return redirect('cars_app:brand', brand_id=brand.id)
#     form = BrandForm(instance=brand)
#     return render(request, 'pages/new_brand.html', {'form':form, 'type':'update'})

# def delete_brand(request, brand_id):
#     if request.method=='POST':
#         brand = get_cars(brand_id)
#         brand.delete()
#         return redirect('cars_app:home')
#     return redirect('cars_app:home')

# def car_detail(request, brand_id, car_id):
#     brand = get_cars(brand_id)
#     car = Car.objects.get(id=car_id)
#     return render(request, 'pages/car_detail.html', {'brand':brand, 'car':car})

# def new_car(request, brand_id):
#     brand = get_cars(brand_id)
#     if request.method=='POST':
#         form = CarForm(request.POST)
#         if form.is_valid():
#             car = form.save(commit=False)
#             car.save()
#             return redirect('cars_app:brand', brand_id=brand_id)
#     form = CarForm({'brand':brand})
#     return render(request, 'pages/car_form.html', {'form':form, 'type':'New'})

# def edit_car(request, brand_id, car_id):
#     brand = get_cars(brand_id)
#     car = Car.objects.get(id=car_id)
#     if request.method=='POST':
#         form = CarForm(request.POST, instance=car)
#         if form.is_valid():
#             car = form.save(commit=False)
#             car.save()
#             return redirect('cars_app:car', brand_id=car.brand.id, car_id = car.id)
#     form = CarForm(instance=car)
#     return render(request, 'pages/car_form.html', {'form':form, 'type':'Update'})

# def delete_car(request, brand_id, car_id):
#     if request.method=='POST':
#         car = Car.objects.get(id=car_id)
#         car.delete()
#         return redirect('cars_app:brand', brand_id)
#     return redirect('cars_app:brand', brand_id)