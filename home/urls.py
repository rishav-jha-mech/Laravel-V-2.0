from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from home import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path("blogpost", views.blogpost, name="blogpost"),
    path("blogpost/blog/<int:id>", views.blog, name="blog"),
    path('writeablog', views.writeablog, name="writeablog"),
    path('tempo', views.tempo, name="tempo"),
    path('admin', views.admin, name="admin"),
    path('accounts/admin', views.accadmin, name="adminacc"),
    path('login', views.handleLogin,  name="login"),
    path('signup',views.handleSignup, name="signup"),
    path('logout',views.handleLogout, name="logout"),
]