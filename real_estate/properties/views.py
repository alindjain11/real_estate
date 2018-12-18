from django.shortcuts import render
from .models import Property

# Create your views here.


def listing(request, id):
    property = Property.objects.get(id=id)
    images = property.images.all()

    context={
        'property': property,
        'images':images

    }
    return render(request,'properties/listing.html',context)


def listings(request):
    properties = Property.objects.all()
    count = 1
    for i in properties:
        if count == 1:
            images = i.images.all()
            count = count + 1
    print(images[0].image)
    return render(request, 'properties/listings.html', {'properties': properties, 'images': images[0]})

