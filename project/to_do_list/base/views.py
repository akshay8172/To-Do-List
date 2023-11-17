from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin # Ensures that a user must be logged in to access a particular view
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from . models import Task

class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')
    
    
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        print("Form is valid:", form.is_valid())
        user = form.save()
        if user is not None:
            login(self.request, user)
        else:
            print("User is None. Form errors:", form.errors)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'       # To Change the object 
    
    def get_context_data(self, **kwargs):                                   #This is to view specific task for specific person
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(complete=False).count()
        search_input = self.request.GET.get('search-area') or ''            #To search the value filtration
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith = search_input)
        context['search_input'] = search_input
        return context
    
    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/task.html'    # To Change the template name     
   
    
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title','description']                   #To list all the   fields = '__all__'
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    
    
class TaskUpdate(LoginRequiredMixin, UpdateView):              
    model = Task
    fields = ['title','description','complete']                   #To list all the   fields = '__all__'
    success_url = reverse_lazy('tasks')
    def finish(request):
        tasks = YourModel.objects.all()
        for task in tasks:
            print(task.status)
        context = {'tasks': tasks}
        return render(request, 'your_template.html', context)
     
            
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')