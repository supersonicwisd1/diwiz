from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Home
from .models import History
from .models import Blog
from .models import Teacher
from .models import Gallery
from .models import Comment
# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ('title','info')
    list_editable = ('info',)
    list_per_page = 10
    search_fields = ('title','info')
    
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id','year', 'info')
    list_editable = ('info',)
    list_per_page = 5
    search_fields = ('year',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','category', 'summary','info','date_added')
    list_editable = ('info','summary')
    list_per_page = 10
    search_fields = ('title','info')
    list_filter = ('date_added',)
    
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name','info','gender')
    list_editable = ('info',)
    list_per_page = 10
    search_fields = ('name','info','gender')
    list_filter = ('gender',)
        
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('info',)
    list_per_page = 10
    search_fields = ('info',)

# @admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'date_added', 'active')
    list_filter = ('active', 'date_added')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
        
admin.site.register(Home, HomeAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.unregister(Group)
