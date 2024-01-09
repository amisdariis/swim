from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from theme_pixel.forms import RegistrationForm, UserLoginForm, UserPasswordResetForm, UserPasswordChangeForm, UserSetPasswordForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UpdateUserForm, UpdateProfileForm

# Create your views here.


# Pages
def index(request):
  return render(request, 'pages/index.html')

def abouts_us(request):
  return render(request, 'pages/about.html')

def contact_us(request):
  return render(request, 'pages/contact.html')

def landing_freelancer(request):
  return render(request, 'pages/landing-freelancer.html')

def blank_page(request):
  return render(request, 'pages/blank.html')

def profile_page(request):
  return render(request, 'pages/profile.html')


# Account management
class UserLoginView(LoginView):
  template_name = 'accounts/sign-in.html'
  form_class = UserLoginForm

def logout_view(request):
  logout(request)
  return redirect('/accounts/login')

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print("Account created successfully!")
      return redirect('/accounts/login')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()

  context = { 'form': form }
  return render(request, 'accounts/sign-up.html', context)

class UserPasswordResetView(PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm


def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})


# Components
def accordion(request):
  return render(request, 'components/accordions.html')

def alerts(request):
  return render(request, 'components/alerts.html')

def badges(request):
  return render(request, 'components/badges.html')

def bootstrap_carousels(request):
  return render(request, 'components/bootstrap-carousels.html')

def breadcrumbs(request):
  return render(request, 'components/breadcrumbs.html')

def buttons(request):
  return render(request, 'components/buttons.html')

def cards(request):
  return render(request, 'components/cards.html')

def dropdowns(request):
  return render(request, 'components/dropdowns.html')

def forms(request):
  return render(request, 'components/forms.html')

def modals(request):
  return render(request, 'components/modals.html')

def navs(request):
  return render(request, 'components/navs.html')

def pagination(request):
  return render(request, 'components/pagination.html')

def popovers(request):
  return render(request, 'components/popovers.html')

def progress_bars(request):
  return render(request, 'components/progress-bars.html')

def tables(request):
  return render(request, 'components/tables.html')

def tabs(request):
  return render(request, 'components/tabs.html')

def toasts(request):
  return render(request, 'components/toasts.html')

def tooltips(request):
  return render(request, 'components/tooltips.html')

def typography(request):
  return render(request, 'components/typography.html')