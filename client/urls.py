from django.urls import path
from client.views import SubscriberListView, SubscriberDetailView, SubscriberCreateView, SubscriberUpdateView, SubscriberDeleteView
from client.apps import ClientConfig

app_name = ClientConfig.name

urlpatterns = [
    path("new/", SubscriberCreateView.as_view(), name="create_client"),
    path("clients/", SubscriberListView.as_view(), name="clients_list"),
    path("detail_client/<int:pk>/", SubscriberDetailView.as_view(), name="detail_client"),
    path("detail_client/<int:pk>/update/", SubscriberUpdateView.as_view(), name="update_client"),
    path("delete_client/<int:pk>/", SubscriberDeleteView.as_view(), name="delete_client"),
]
