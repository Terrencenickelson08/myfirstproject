from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from django.views.generic import TemplateView
from django.db.models import Q
from django.conf import settings

def index(request):
    return render(request, "index.html")

def register(request):
    errorsFromModelsValidator = User.objects.registration_validator(request.POST)
    if len(errorsFromModelsValidator)>0:
        for key, value in errorsFromModelsValidator.items():
            messages.error(request, value)
        return redirect("/")
    else:
        password  = request.POST['password']
        hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        print(hash1)
        user = User.objects.create(firstname = request.POST['firstname'], lastname = request.POST['lastname'], email = request.POST['email'], password=hash1.decode())
 
        request.session['id'] =user.id
    return redirect('/landingpage')

def login (request):
    errorsFromLoginValidator = User.objects.login_validator(request.POST) 
    if len(errorsFromLoginValidator) >0:
        for key, value in errorsFromLoginValidator.items():
             messages.error(request, value)
        return redirect("/")
    # context ={
    #     "loggedinuser": User.objects.filter(email = request.POST['email'])[0]
    # }
    user = User.objects.filter(email = request.POST['email'])[0]
    request.session['id']= User.objects.filter(email = request.POST['email'])[0].id
    return redirect("/landingpage")

def landingpage(request):
    if 'id' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id = request.session['id'])
        context ={
            'loggedinuser': User.objects.get(id = request.session['id']),
            # 'allbooks': Book.objects.all(),
            # 'favbooks': Book.objects.filter(fav_books = user),
}
    return render(request, 'landingpage.html', context)

def upload(request):
    context ={}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url =fs.url(name)
    return render(request, 'upload.html', context)


def book_list(request):
    loggedinuser = User.objects.get(id = request.session['id'])
    books = Book.objects.exclude()
    favhomes = Book.objects.filter(fav_books = loggedinuser)
    context = {
        'books': books,
        'loggedinuser' : loggedinuser,
        'favhomes':favhomes
    }
    return render(request,'book_list.html', context)

def upload_book(request):
    loggedinuser = User.objects.get(id = request.session['id'])
    listing = Book(poster = loggedinuser)
    if request.method =='POST':
        form = BookForm(request.POST, request.FILES, instance= listing)
        if form.is_valid():
            form.save()
            return redirect('/books')
    else: 
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })

def showprop(request, prop_id):
    home = Book.objects.get(id = prop_id)
    user = User.objects.get(id = request.session['id'])
    context = {
        "home": home,
        "loggedinuser":user,

    }
    return render(request, "view.html", context)

def addfaves(request,prop_id):
    loggedinuser = User.objects.get(id = request.session['id'])
    this_book = Book.objects.get(id =prop_id)
    this_book.fav_books.add(loggedinuser)
    return redirect("/books")

def removejob(request, prop_id):
    this_book = Book.objects.get(id = prop_id)
    loggedinuser = User.objects.get(id = request.session['id'])
    loggedinuser.saved_books.remove(this_book)
    return redirect("/books")
        
    
def delete(request, prop_id):
    prop_to_delete = Book.objects.get(id = prop_id)
    prop_to_delete.delete()
    return redirect('/books')

def editfaves(request, prop_id):
    home = Book.objects.get(id = prop_id)
    context={
        "home":home
    }
    return render(request, "edit.html", context)

def edit(request):
    return render(request, 'edit.html')

def updateposting(request, prop_id):
    home = Book.objects.get(id = prop_id)
    loggedinuser = User.objects.get(id = request.session['id'])
    prop_to_edit = Book.objects.get (id=prop_id)
    prop_to_edit.title = request.POST["title"]
    prop_to_edit.description = request.POST["description"]
    prop_to_edit.location = request.POST["location"]
    prop_to_edit.price = request.POST["price"]
    prop_to_edit.bedrooms = request.POST["bedrooms"]
    prop_to_edit.sqft = request.POST["sqft"]
    prop_to_edit.save()
    return redirect ("/books")

