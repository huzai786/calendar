from django.urls import path
from .views import home, filter_config, manage_account, add_event, DetailAccount, EditAccount, DeleteAccount, CreateAccount

urlpatterns = [
    path('', home, name='home'),
    path('filter', filter_config, name='filter'),
    path('manage_accounts', manage_account, name='manage-accounts'),
    path('add_event', add_event, name='add-event'),

    path('manage_accounts', DetailAccount.as_view(), name='account-detail'),
    path('create_account/', CreateAccount.as_view(), name='account-create'),
    path('edit_account/<str:pk>/', EditAccount.as_view(), name='account-edit'),
    path('delete_account/<str:pk>/', DeleteAccount.as_view(), name='account-delete')
]
