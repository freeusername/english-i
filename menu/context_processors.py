from menu.models import Item

def menu(request):
    items = Item.objects.all()
    # sub_items = Subitem.objects.all
    # bottom_items = Item.objects.filter(location=MENU_LOCATION_BOTTOM)
    ctx = {}
    ctx['items'] = items
    # ctx['sub_items'] = sub_items
    # ctx['bottom_items'] = bottom_items
    return ctx
