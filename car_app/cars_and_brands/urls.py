from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name='home'),
    path('new/', views.new_brand, name='new_brand'),
    path('<int:brand_id>/', views.detail, name='brand'),
    path('<int:brand_id>/edit/', views.edit_brand, name='edit_brand'),
    path('<int:brand_id>/delete/', views.index, name='delete_brand'),
    # Cars
    path('<int:brand_id>/<int:car_id>', views.index, name='car'),
    path('<int:brand_id>/new', views.index, name='new_car'),
    path('<int:brand_id>/<int:car_id>/edit', views.index, name='edit_car'),
    path('<int:brand_id>/<int:car_id>/delete/', views.index, name='delete_car')
]
    




# app_name = 'cars_app'
#     # Brand
#     path('', views.index, name='home'),
#     path('new/', views.new_brand, name='new_brand'),
#     path('<int:brand_id>/', views.detail, name='brand'),
#     path('<int:brand_id>/edit/', views.edit_brand, name='edit_brand'),
#     path('<int:brand_id>/delete/', views.delete_brand, name='delete_brand'),
#     # Cars
#     path('<int:brand_id>/<int:car_id>', views.car_detail, name='car'),
#     path('<int:brand_id>/new', views.new_car, name='new_car'),
#     path('<int:brand_id>/<int:car_id>/edit', views.edit_car, name='edit_car'),
#     path('<int:brand_id>/<int:car_id>/delete/', views.delete_car, name='delete_car'),
# ]