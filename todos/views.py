
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from turbo_response.views import (
    TurboCreateView, TurboUpdateView,
)

from todos.forms import ToDoForm, CompleteToDoForm
from todos.models import ToDo


class BaseToDoView():
    queryset = ToDo.objects.all()
    page = 'list'

    def get_success_url(self):
        url_name = self.request.POST.get('next', self.page)
        return reverse_lazy(f'todos:{url_name}')

    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url(), status=303)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return self.render_to_response(self.get_context_data(form=form), status=422)


class ListToDos(BaseToDoView, ListView):
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            page=self.page,
            todo_form=ToDoForm(),
            complete_todo_form=CompleteToDoForm(),
            has_todos=ToDo.objects.exists(),
            has_completed_todos=ToDo.objects.filter(is_completed=True).exists(),
            total_active_todos=ToDo.objects.filter(is_completed=False).count(),
        )
        return context


class ListActiveToDos(ListToDos):
    queryset = ToDo.objects.filter(is_completed=False)
    page = 'list-active'


class ListCompletedToDos(ListToDos):
    queryset = ToDo.objects.filter(is_completed=True)
    page = 'list-completed'


class CreateToDo(BaseToDoView, TurboCreateView):
    form_class = ToDoForm


class UpdateToDo(BaseToDoView, TurboUpdateView):
    form_class = ToDoForm


class CompleteToDo(BaseToDoView, TurboUpdateView):
    form_class = CompleteToDoForm


class DeleteToDo(BaseToDoView, DeleteView):
    pass


class ClearCompletedToDos(BaseToDoView, View):
    def post(self, request, *args, **kwargs):
        ToDo.objects.filter(is_completed=True).delete()
        return redirect(self.get_success_url())


class ToggleAllToDos(BaseToDoView, View):
    def post(self, request, *args, **kwargs):
        todos = ToDo.objects.all()
        completed_todos = todos.filter(is_completed=True)
        active_todos = todos.filter(is_completed=False)

        if completed_todos.count() == todos.count():
            todos.update(is_completed=False)
        else:
            active_todos.update(is_completed=True)

        return redirect(self.get_success_url())
