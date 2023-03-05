from django.shortcuts import render, get_object_or_404, redirect

from .models import Item, Purchase


def list_item(request):
    item_list = Item.objects.all()
    context = {
        'items': item_list
    }
    return render(request, 'list_item.html', context)


def detail_item(request, item_id):
    detail_item_list = get_object_or_404(Item, id=item_id)
    context = {
        'items': detail_item_list
    }
    return render(request, 'detail_item.html', context)


