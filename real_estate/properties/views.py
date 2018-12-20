from django.shortcuts import render
from .models import Property
from .forms import PropertyForm

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
    images = []
    for i in properties:
        if count == 1:
            images = i.images.all()
            count = count + 1
    # print(images[0].image)
    return render(request, 'properties/listings.html', {'properties': properties,})

def postproperty(request):
    form = PropertyForm()
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)


    # #
    # #     if form.is_valid():
    # #
    # #         return redirect('/')
    # else:

    return render(request,'properties/propertyform.html', {'form':form})