from django.shortcuts import render, redirect
from .models import Category, Photo

def gallery(request):
    #selecting what photos to show based on category
    category=request.GET.get('category')
    if category==None:
        photos = Photo.objects.all()
    else :
        photos = Photo.objects.filter(category__name=category)    

    categories = Category.objects.all()

    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id = pk)
    return render(request, 'photos/photo.html', {'photo': photo})

def addPhoto(request):
    categories = Category.objects.all()

    if request.method == "POST":
        data=request.POST
        image = request.FILES.get('image')
     #setting the category value  
        #if selected a category
        if data['category'] !='none' :
            category= Category.objects.get(id=data['category'])
        #if selected category new, then creating a new category and giving it the name     
        elif data['category_new'] !='': 
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else : #when theres no specific cat
            category= None    

        # creating photo
        photo = Photo.objects.create(
            category= category,
            description= data['description'] ,
            image=image,
        )

        return redirect('gallery')  #redirecting to gallery page after uploading photo  

    context = {'categories': categories}
    return render(request, 'photos/add.html',context)

def aboutUs(request):
    return render(request, 'photos/aboutUs.html')

def feedback(request):
    return render(request, 'photos/feedback.html')