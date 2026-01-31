from django.urls import path
from message.views import MessageCreateView, MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView
from message.apps import MessageConfig

app_name = MessageConfig.name

urlpatterns = [
    path("new/", MessageCreateView.as_view(), name="create_message"),
    path("messages/", MessageListView.as_view(), name="messages_list"),
    path("detail_message/<int:pk>/", MessageDetailView.as_view(), name="detail_message"),
    path("detail_message/<int:pk>/update/", MessageUpdateView.as_view(), name="update_message"),
    path("delete_message/<int:pk>/", MessageDeleteView.as_view(), name="delete_message"),
]
