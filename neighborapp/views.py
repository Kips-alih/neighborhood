from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from neighborapp.models import Neighborhood, Profile,Business,Location,Category,Post
from .forms import BusinessForm, ProfileForm, NeighborhoodForm,PostForm           

# Create your views here.
def index(request):
    
    posts = Post.objects.all().order_by("-id")
    return render(request, 'main/index.html', {'posts': posts})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'main/profile.html', {"form":form,'profile':profile})

@login_required(login_url="/accounts/login/")
def new_neighbor(request):
    current_user = request.user
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbor = form.save(commit=False)
            neighbor.user = current_user
            neighbor.save()
        return HttpResponseRedirect('/neighborhood')
    else:
        form = NeighborhoodForm()
    return render(request, 'main/create_neighbor.html',{'form':form})
@login_required(login_url="/accounts/login/")
def neighborhood(request):
    current_user = request.user
    neighborhood = Neighborhood.objects.all().order_by('-id')
    return render(request, 'main/neighborhoods.html', {'neighborhood': neighborhood})

@login_required(login_url='/accounts/login/')
def single_hood(request,name):
    hood = Neighborhood.objects.get(name=name)
    business = Business.objects.filter(neighborhood=hood)
    post = Post.objects.filter(neighborhood=hood)


    return render(request,'main/single_hood.html',{'hood':hood,'businesses':business,'posts':post})

def join_hood(request,id):
    neighborhood = get_object_or_404(Neighborhood, id=id)
    
    request.user.profile.neighborhood = neighborhood
    request.user.profile.save()
    return redirect('neighborhood')

def leave_hood(request, id):
    hood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('neighborhood')

@login_required(login_url="/accounts/login/")
def create_business(request):
    current_user = request.user
    if request.method == "POST":
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.save()
        return HttpResponseRedirect('/neighborhood')
    else:
        form = BusinessForm()
    return render(request, "main/add_business.html", {'form':form})

@login_required(login_url="/accounts/login/")
def business(request):
    current_user = request.user
    business = Business.objects.all().order_by('-id')
    return render(request, 'main/business.html', {'businesses': business})

@login_required(login_url='/accounts/login/')
def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        business = Business.search_by_name(search_term)
        message = f'{search_term}'

        return render(request, 'main/search.html', {'message': message, 'business':business})
    else:
        message = 'Not found'
    return render(request, 'main/search.html', {'message': message})


@login_required(login_url="/accounts/login/")
def create_post(request):
    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()

        return HttpResponseRedirect('/neighborhood')
    else:
        form = PostForm()
    return render(request, "main/create_post.html", {'form':form})

# @login_required(login_url="/accounts/login/")
# def post(request):
#     current_user = request.user
#     post = Post.objects.all().order_by('-id')
#     return render(request, 'main/posts.html', {'posts': post})