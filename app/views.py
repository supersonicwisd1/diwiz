from django.shortcuts import render, redirect
from diwiz.settings import EMAIL_HOST_USER
from .models import Gallery, Home, History, Blog, Teacher, Comment
from django.views.generic import ListView,DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import CommentForm, ContactForm
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(ListView):
    template_name = 'index.html'
    model = Home
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['intros'] = Home.objects.all()
        context['histories'] = History.objects.all()
        return context
    
class AboutPageView(ListView):
    template_name = 'abouts.html'
    model = Home
    
class BlogPageView(ListView):
    template_name = 'blogs.html'
    model = Blog
    context_object_name = 'blogs'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['comment'] = Blog.objects.all()
        return context

    
class TeacherPageView(ListView):
    template_name = 'teachers.html'
    model = Teacher
    context_object_name = 'teachers'
    
class GalleryPageView(ListView):
    template_name = 'galleries.html'
    model = Gallery
    context_object_name = 'photos'
    

class SingleBlogView(DetailView):
    template_name = 'blogSingles.html'
    model = Blog
    context_object_name = 'blog'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        comments_connected = Comment.objects.filter(
            post=self.get_object()).order_by('-date_added')
        context['comments'] = comments_connected
        context['comment_form'] = CommentForm(instance=self.request.user)

        return context
    def post(self, request, *args, **kwargs):
        new_comment = Comment(name=request.POST.get('name'),
                              email=request.POST.get('email'),
                              body=request.POST.get('body'),
                                  post=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
    
    
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = Blog.objects.filter(
            Q(title__icontains=search_term) |
            Q(category__icontains=search_term) |
            Q(info__icontains=search_term) 
        )
        context = {
            'search_term': search_term,
            'blogs': search_results
        }
        return render(request, 'search.html', context)
    else:
        return redirect('blogs')
    
def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            phone = form.cleaned_data.get('phone')
            sender = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            subject = "Message from {} {}, with email: {} and phone: {}".format(first_name, last_name, sender, phone)
        
        send_mail(
            subject,
            message,
            sender,
            [EMAIL_HOST_USER],
            fail_silently=False,
        )
        messages.success(request, "Success")
        return redirect('contacts')
    return render(request, 'contacts.html',{'form': form})

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blogcreate.html'
    fields = ['title', 'category', 'info', 'summary', 'image']
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, "You have added a New Blog")
        return redirect('blogs')
    
class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blogupdate.html'
    fields = ['title', 'category', 'info', 'summary', 'image']
    
    def form_valid(self,form):
        instance = form.save()
        return redirect('blogSingle', instance.pk)
    
class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'deleteblog.html'
    success_url = '/'
    
class HistoryAddView(LoginRequiredMixin, CreateView):
    model = History
    template_name = 'addhistory.html'
    fields = ['year','info']
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, "You have added a New History")
        return redirect('home')
    
class GalleryAddView(LoginRequiredMixin, CreateView):
    model = Gallery
    template_name = 'galleryadd.html'
    fields = ['info','image']
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, "You have added a New Blog")
        return redirect('galleries')

    
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect("home")
    else:
        form = UserCreationForm()
            
    return render(request, "registration/signup.html", {'form':form,})

#To Edit Admin From Views
class AdminEditPageView(LoginRequiredMixin, ListView):
    template_name = 'adminedit.html'
    model = Home