from shop.models import Item, Purchase


items = Item.objects.all()
items
item_1 = Item(name='milk', price=70)
item_1.save()
item_2 = Item(name='bread', price=20)
item_2.save()
item_3 = Item(name='sugar', price=50)
item_3.save()
item_4 = Item(name='salt', price=40)
item_4.save()
item_5 = Item(name='egg', price=10)
item_5.save()
items = Item.objects.all()
items

purchases = Purchase.objects.all()
purchases
purchase_1 = Purchase(name='Maxim', age=20, item_id=item_1)
purchase_1.save()
purchase_2 = Purchase(name='Connor', age=24, item=item_2)
purchase_2.save()
purchase_3 = Purchase(name='Nick', age=27, item=item_3)
purchase_3.save()
purchase_4 = Purchase(name='Neil', age=19, item=item_4)
purchase_4.save()
purchase_5 = Purchase(name='Tony', age=30, item=item_5)
purchase_5.save()
purchases = Purchase.objects.all()
purchases
