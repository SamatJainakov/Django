from django.urls import path

from . import views

urlpatterns = [
    path('shop/', views.list_item, name='list_item'),
    path('shop/<int:item_id>/detail/', views.detail_item, name='detail_item'),
]
