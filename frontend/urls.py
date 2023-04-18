
from django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home),
    path('search', views.search, name='search'),
    path('index.html', views.home),
    path('blog.html', views.all_news),
    path('News/<int:id>/<str:title>/', views.detail),
    path('category.html', views.all_category),
    path('category/<int:id>/<str:title>/',views.category_news),
    path('Contact_us.html', views.contect_us),
    path('ecom_product.html', views.ecom_product),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
