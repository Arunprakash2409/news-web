from django.contrib import admin
from .models import category, News, comment
# Register your models here.

# to show the category on the admin page
admin.site.register(category)

# to show the news on the admin page
class AdminNews(admin.ModelAdmin):
    list_display = ('title','category','add_time')

admin.site.register(News, AdminNews)

# to show the comands on the admin page
class Admincomment(admin.ModelAdmin):
    list_display = ('name','email','command','status')

admin.site.register(comment, Admincomment)