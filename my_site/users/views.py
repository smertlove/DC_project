from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileForm
from django.views.generic.detail import DetailView
from .models import Profile
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан можете войти на сайт!')
            return redirect('login')    #blog-home
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'users/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, user_id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context



class CreateProfilePageView(CreateView):
    model = Profile

    template_name = 'users/create_profile.html'
    fields = ['profile_pic','date_of_birth','email', 'bio', 'instagram']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('index')


# def edit(request):
#     return render(request, 'users/edit_profile.html')



class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'users/edit_profile.html'
    form_class = ProfileForm


    success_url = reverse_lazy('index')


# class UserEditView(UpdateView):
#     form_class = EditProfileForm
#     template_name = 'users/edit_profile.html'
#     success_url = reverse_lazy('tasks')
#
#     def get_object(self):
#         return self.request.user


# @login_required
# def profile(request):
#     return render(request, 'users/profile.html')
