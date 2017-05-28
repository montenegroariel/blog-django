from .models import Menu


def menus(request):
    context = Menu.objects.all()
    return {'menus': context}