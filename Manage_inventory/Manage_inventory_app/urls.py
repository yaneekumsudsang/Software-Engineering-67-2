from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # แสดงรายการสินค้า
    path('add/', views.add_product, name='add_product'),  # เพิ่มสินค้าใหม่
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),  # แก้ไขสินค้า
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),  # ลบสินค้า
]
