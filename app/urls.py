from django.urls import path
from . import views

urlpatterns = [
    # links
    # home page
    path('', views.HomePageView.as_view(), name="home"),
    # about page
    path('about/', views.AboutPageView.as_view(), name="abouts"),
    # contact
    path('contact/', views.contact, name="contacts"),
    # blog
    path('blog/', views.BlogPageView.as_view(), name="blogs"),
    # detail blog
    path('blog-single/<int:pk>/', views.SingleBlogView.as_view(), name='blogSingle'),
    # gallery
    path('gallery/', views.GalleryPageView.as_view(), name="galleries"),
    # teachers but not functioning for now
    path('teachers/', views.TeacherPageView.as_view(), name="teachers"),
    # link to search
    path('search/', views.search, name="search"),
    # create direct update for blog
    path('blog/createblog/', views.BlogCreateView.as_view(), name="blogcreate"),
    path('blog-single/updateblog/<int:pk>/', views.BlogUpdateView.as_view(), name="blogupdate"),
    path('blog-single/deleteblog/<int:pk>/', views.BlogDeleteView.as_view(), name="deleteblog"),
    # add history   
    path('home/addhistory/', views.HistoryAddView.as_view(), name="addhistory"),
    # add photo
    path('gallery/addphoto/', views.GalleryAddView.as_view(), name="addphoto"),
    #Edit from view
    path('editadmin/', views.AdminEditPageView.as_view(), name="editadmin"),
    # sign up
    path('signup/', views.register_user, name="signup")
] 
