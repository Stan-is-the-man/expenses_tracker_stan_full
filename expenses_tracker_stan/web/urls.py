from django.urls import path

from expenses_tracker_stan.web.views import index_page, expense_create, expense_edit, expense_delete, profile, \
    profile_edit, profile_delete, profile_create

urlpatterns = [
    path('', index_page, name='index page'),
    path('create/', expense_create, name='expense create'),
    path('edit/<int:pk>/', expense_edit, name='expense edit'),
    path('delete/<int:pk>/', expense_delete, name='expense delete'),

    path('profile/', profile, name='profile'),
    path('profile/create/', profile_create, name='profile create'),
    path('profile/edit', profile_edit, name='profile edit'),
    path('delete/', profile_delete, name='profile delete'),
]

