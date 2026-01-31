from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from message.models import Message


@method_decorator(cache_page(60 * 15), name="dispatch")
class MessageListView(LoginRequiredMixin, ListView):
    """Отображение списка сообщений"""

    model = Message
    template_name = "message/messages_list.html"
    context_object_name = "messages"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = self.get_count()
        return context

    def get_count(self):
        messages = self.get_queryset()
        count = 0
        for message in messages:
            count += 1
        return count

    def get_queryset(self):
        queryset = cache.get("my_message_list")
        if not queryset:
            queryset = Message.objects.all()
            cache.set("my_message_list", queryset, 60 * 15)
        return queryset


@method_decorator(cache_page(60 * 15), name="dispatch")
class MessageDetailView(LoginRequiredMixin, DetailView):
    """Подробная информация о сообщении"""

    model = Message
    template_name = "message/message_detail.html"
    context_object_name = "message"

    def get_context_data(self, **kwargs):
        # Получаем контекст от родительского класса
        context = super().get_context_data(**kwargs)
        context["is_manager"] = (
            self.request.user.is_staff or self.request.user.groups.filter(name="Менеджеры").exists()
        )
        # Получаем сообщение из контекста

        return context


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Создание сообщения"""

    model = Message
    template_name = "message/message_form.html"
    fields = ["subject", "body"]
    success_url = reverse_lazy("message:messages_list")


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """Обновление сообщения"""

    model = Message
    fields = ["subject", "body"]

    def get_success_url(self):
        return reverse("message:detail_message", kwargs={"pk": self.object.pk})


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление сообщения"""

    model = Message
    template_name = "message/message_confirm_delete.html"
    success_url = reverse_lazy("message:messages_list")
