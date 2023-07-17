import os
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy

from .models import Profile
from .forms import *


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'users/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, user_id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан можете войти на сайт!')
            return redirect('login')    #blog-home
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        print(request.FILES)
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            if request.FILES.get('profile_pic', None) != None:
                try:
                    os.remove(request.user.profile_pic.url)
                except Exception as e:
                    print('Exception in removing old profile image: ', e)
                request.user.profile.profile_pic = request.FILES['profile_pic']
                request.user.profile.save()
            messages.success(request, ('Ваш профиль был успешно обновлен!'))
            return redirect('index')
        else:
            messages.error(request, ('Пожалуйста, исправьте ошибки.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/password_change.html', {
        'form': form
    })









# def edit(request):
#     return render(request, 'users/edit_profile.html')



# class EditProfilePageView(UpdateView):
#     model = Profile
#     template_name = 'users/edit_profile.html'
#     form_class = ProfileForm#  ProfileUserForm
#     success_url = reverse_lazy('index')
#
#     def get_context_data(self, *args, **kwargs):
#         users = Profile.objects.all()
#         context = super(EditProfilePageView, self).get_context_data(*args, **kwargs)
#         page_user = get_object_or_404(Profile, user_id=self.kwargs['pk'])
#         context['page_user'] = page_user
#     #    context['page_user'] = page_user
#         return context
    # second_form_class = ProfileForm

    # def get_context_data(self, **kwargs):
    #     context = super(EditProfilePageView, self).get_context_data(**kwargs)
    #     context['active_client'] = True
    #     if 'form' not in context:
    #         context['form'] = self.form_class(self.request.GET, instance=self.object)
    #         #context['form'] = self.form_class(self.request.GET)
    #     if 'form2' not in context:
    #         context['form2'] = self.second_form_class(self.request.GET, instance=self.object)
    #         #context['form2'] = self.second_form_class(self.request.GET)
    #     context['active_client'] = True
    #     return context
    #
    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = self.form_class(request.POST)
    #     form2 = self.second_form_class(request.POST)
    #
    #     if form.is_valid() and form2.is_valid():
    #         userdata = form.save(commit=False)
    #         # used to set the password, but no longer necesarry
    #         userdata.save()
    #         employeedata = form2.save(commit=False)
    #         employeedata.user = userdata
    #         employeedata.save()
    #         messages.success(self.request, 'Settings saved successfully')
    #         return redirect('index')
    #     else:
    #         return self.render_to_response(
    #             self.get_context_data(form=form, form2=form2))
    #
    # def get_success_url(self):
    #     return redirect('index')

    # class CreateProfilePageView(CreateView):
    #     model = Profile
    #
    #     template_name = 'users/create_profile.html'
    #     fields = ['profile_pic', 'date_of_birth', 'bio', 'instagram']
    #
    #     def form_valid(self, form):
    #         for i in form.instance:
    #             print(i)
    #         form.instance.user = self.request.user
    #         return super().form_valid(form)
    #
    #     success_url = reverse_lazy('index')



