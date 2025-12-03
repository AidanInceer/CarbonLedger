from django.urls import path

from . import views

urlpatterns = [
    path('', views.projects_view, name='projects'),
    path('project/<int:project_id>/', views.home, name='home'),
    path('project/<int:project_id>/reporting/', views.project_reporting, name='project_reporting'),
    path('project/<int:project_id>/reporting/api/', views.project_reporting_api, name='project_reporting_api'),
    path('project/<int:project_id>/configuration/', views.project_configuration, name='project_configuration'),
    path('project/<int:project_id>/summary/', views.project_summary, name='project_summary'),
    path('project/<int:project_id>/team/', views.project_team, name='project_team'),
    path('project/<int:project_id>/add/', views.add_transaction, name='add_transaction'),
    path('project/<int:project_id>/delete/<int:pk>/', views.delete_transaction, name='delete_transaction'),
    path('project/create/', views.create_project, name='create_project'),
    path('project/<int:project_id>/delete-project/', views.delete_project, name='delete_project'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('settings/', views.settings_view, name='settings'),
    path('account/', views.account_view, name='account'),
]
