from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import register, user_login, home, add_blog,user_logout


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("", home, name="home"),
    path("add-blog/", add_blog, name="add_blog"),
    path("logout/", user_logout, name="logout"),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)