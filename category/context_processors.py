from .models import Category
# available anywhere
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)