"""bookstore_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django admin
    path('anything-but-admin/', admin.site.urls),


    # User management
    # path('accounts/', include('django.contrib.auth.urls')),
    # # lo reemplazamos por:
    path('accounts/', include('allauth.urls')),  # new
    # Si te preguntas a donde estan los templates
    # de All Auth, en lugar de templates/registration
    # estan en templates/account, podriamos eliminar
    # las otras templates que no uso osea /registration

    # Local apps
    # path('accounts/', include('users.urls')),  # lo sacamos
    # porque usamos AllAuth que tiene su singup
    path('', include('pages.urls')),
    path('books/', include('books.urls')),  # new
    path('orders/', include('orders.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


""" rutas asociadas a auth.urls
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
 """


# para que las herramientas de perfomance aparezcan solamente
# en caso de que sea en debug mode

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
