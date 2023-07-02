from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy

from .models import Profile
from .forms import UserRegisterForm, ProfileForm



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
    fields = ['profile_pic','date_of_birth', 'bio', 'instagram']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('index')


# class CreateProfileRegister(CreateView):




def register(request):
    print("1")
    if request.method == 'POST':
        print(2)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print(3)
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(request, f'Ваш аккаунт создан можете войти на сайт!')
            return redirect('login')    #blog-home
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



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
