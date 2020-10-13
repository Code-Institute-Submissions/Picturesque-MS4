from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo, Category

# Create your views here.

def all_photos(request):
    """ A view to show all photos, with sorting feature included"""

    photos = Photo.objects.all()
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                photos = photos.annotate(lower_name=Lower('name'))

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        
        photos = photos.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            photos = photos.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    existent_sorting = f'{sort}_{direction}'

    context = {
        'photos': photos,
        'existent_categories': categories,
        'existent_sorting': existent_sorting,
    }

    return render(request, 'photos/photos.html', context)

    
def photo_detail(request, photo_id):
    """ A view to show individual photo characteristics """

    photo = get_object_or_404(Photo, pk=photo_id)

    context = {
        'photo': photo,
    }

    return render(request, 'photos/photo_detail.html', context)