from django.contrib import admin
from django.urls import path
from projects import views as project_view
from employee import views as emp_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(template_name='projects/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL),name='logout'),
    path('',project_view.index,name='index'),
    path('tender/',project_view.tender,name='tender'),
    path('tender/<int:id>/',project_view.tender_details,name='tender_details'),
    path('add_tender/',project_view.add_tender,name='add_tender'),
    path('my_tender/',project_view.my_tender,name='my_tender'),
    path('add_contractor/<int:id>/',project_view.add_contractor,name='add_contractor'),
    path('edit_tender/<int:id>/',project_view.edit_tender,name='edit_tender'),
    path('supervisor/',emp_view.get_all_supervisor,name='all_supervisor'),
    path('labour/',emp_view.get_all_employee,name='all_employee'),
    path('projects/',project_view.all_projects,name='all_projects'),
    path('add_project/<int:id>',project_view.add_project,name='add_tender'),
    path('create_supervisor/',emp_view.create_super,name='create_super')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''

Add Supervisor
Add Labour

Add Labour under Super/Project - not at the time of Project Creation
Add supervisor as the same way  
Supervisor can't add Employee


Attandace

'''