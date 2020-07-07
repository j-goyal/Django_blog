from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    #return HttpResponse("this is home")
    return render(request,'home/home.html')

def about(request):
    #messages.success(request, 'This is about Page')
    return render(request,'home/about.html')


def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')  # can also use request.POST['name']
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        content = request.POST.get('content')
        #print(name,phone,email,content)

        if len(name)<2 or len(email)<6 or len(phone)<10 or len(content)<4:
            messages.error(request, "Warning! Please fill the form correctly")
        else:
            contact = Contact(name=name, phone=phone, email=email, content=content) # create obj of Contact class
            contact.save()
            messages.success(request,"Hurraah! Your message has been successfully sent")

    return render(request,'home/contact.html')


def search(request):
    query = request.GET['query']

    if len(query)==0:
        messages.error(request, "Please enter something to search")
        return redirect('home')
    
    if len(query)>70:
        allposts = Post.objects.none()    # blank query syntax
    else:
        allpostsTitle = Post.objects.filter(title__icontains=query)
        allpostsContent = Post.objects.filter(content__icontains=query)
        allpostsAuthor = Post.objects.filter(author__icontains=query)
        allposts = allpostsTitle.union(allpostsContent, allpostsAuthor)

    
    if allposts.count()==0:
        messages.warning(request,"No search result found. Please refine your query")
    
    context = {'allposts':allposts, 'query':query}
    return render(request, 'home/search.html', context)


def handleSignup(request):
    if request.method=='POST':
        # get all the params
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # check for errorenous user
        
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username should only contains letters and numbers")
            return redirect('home')

        if not fname.isalpha() or not lname.isalpha():
            messages.error(request, "Your Name should not contain numbers")
            return redirect('home')


        # create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your jCoder account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("Error - 404 not found")  


def handleLogin(request):
    if request.method=='POST':
        # get all the params
        loginusername = request.POST.get('loginusername')
        loginpass= request.POST.get('loginpass')

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged in")
            return redirect('home')

        else:
            messages.error(request, "Invalid Credentails, Please try again")
            return redirect('home')


    else:
        return HttpResponse("Error - 404 not found")



def handleLogout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')



