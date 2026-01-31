from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from client.models import Subscriber


class SubscriberListView(LoginRequiredMixin, ListView):
    """Отображение списка получателей"""

    model = Subscriber
    template_name = "client/subscriber_list.html"
    context_object_name = "subscribers"

    def get_queryset(self):
        queryset = cache.get("my_subscriber_list")
        if not queryset:
            if self.request.user.groups.filter(name="Менеджер").exists():
                queryset = Subscriber.objects.all()
            else:
                queryset = Subscriber.objects.filter(owner=self.request.user)
            cache.set("my_subscriber_list", queryset, 60 * 15)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = self.get_count()
        return context

    def get_count(self):
        subscribers = self.get_queryset()
        count = 0
        for subscriber in subscribers:
            count += 1
        return count

    def test_func(self):
        return True


@method_decorator(cache_page(60 * 15), name="dispatch")
class SubscriberDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """Подробная информация о получатели"""

    model = Subscriber
    template_name = "client/subscriber_detail.html"
    context_object_name = "subscriber"

    def test_func(self):
        subscriber = self.get_object()
        if not self.request.user.groups.filter(name="Менеджер").exists() and not self.request.user.is_staff:
            return self.request.user == subscriber.owner
        return True

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        subscriber = self.get_object()
        context["is_manager"] = self.request.user.is_staff or self.request.user.groups.filter(name="Менеджер").exists()
        context["is_owner"] = self.request.user == subscriber.owner
        return context


class SubscriberCreateView(LoginRequiredMixin, CreateView):
    """Создание получателя"""

    model = Subscriber
    template_name = "client/subscriber_form.html"
    fields = ["email", "full_name", "comment"]
    success_url = reverse_lazy("client:clients_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Устанавливаем владельца на текущего пользователя
        return super().form_valid(form)


class SubscriberUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Обновление получателя"""

    model = Subscriber
    fields = ["email", "full_name", "comment"]

    def get_success_url(self):
        return reverse("client:detail_client", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["is_manager"] = self.request.user.is_staff or self.request.user.groups.filter(name="Менеджер").exists()
        return context

    def test_func(self):
        subscriber = self.get_object()
        return self.request.user == subscriber.owner


class SubscriberDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Удаление получателя"""

    model = Subscriber
    template_name = "client/subscriber_confirm_delete.html"
    success_url = reverse_lazy("client:clients_list")

    def test_func(self):
        subscriber = self.get_object()
        return self.request.user == subscriber.owner
