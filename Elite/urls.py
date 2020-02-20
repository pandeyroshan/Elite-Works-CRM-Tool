from django.contrib import admin
from django.urls import path
from projects import views as project_view
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(template_name='projects/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL),name='logout'),
    path('',project_view.index,name='index'),
    path('tender/',project_view.tender,name='tender'),
    path('tender/<int:id>/',project_view.tender_details,name='tender_details'),
    path('add_tender/',project_view.add_tender,name='add_tender')
]
