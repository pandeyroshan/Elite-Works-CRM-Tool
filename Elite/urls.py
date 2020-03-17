from django.contrib import admin
from django.urls import path
from projects import views as project_view
from employee import views as emp_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include


handler404 = 'employee.views.handler404'
handler500 = 'employee.views.handler500'

urlpatterns = [
    path('admin/',include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('rotion/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(template_name='projects/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL),name='logout'),
    path('',project_view.index,name='index'),
    path('tender/',project_view.tender,name='tender'),
    path('tender/<slug:uuid_no>/',project_view.tender_details,name='tender_details'),
    path('add_tender/',project_view.add_tender,name='add_tender'),
    path('my_tender/',project_view.my_tender,name='my_tender'),
    path('add_contractor/<int:id>/',project_view.add_contractor,name='add_contractor'),
    path('edit_tender/<int:id>/',project_view.edit_tender,name='edit_tender'),
    path('supervisor/',emp_view.get_all_supervisor,name='all_supervisor'),
    path('supervisor/<int:id>',emp_view.supervisor_detail,name='supervisor_detail'),
    path('labour/',emp_view.get_all_employee,name='all_employee'),
    path('projects/',project_view.all_projects,name='all_projects'),
    path('add_project/<int:id>',project_view.add_project,name='add_tender'),
    path('create_supervisor/',emp_view.create_super,name='create_super'),
    path('create_labour/',emp_view.create_labour,name='create_labour'),
    path('project/<int:id>/',project_view.project_details,name='project_detail'),
    path('edit_project/<int:id>',project_view.edit_project,name='edit_project'),
    path('attandance/<int:id>',emp_view.mark_attandance,name='mark_attandance'),
    path('update_supervisor/<int:id>',emp_view.update_supervisor,name='update_supervisor'),
    path('testing/',project_view.testing,name='testing')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)