from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Pages
    path('', views.index),
    #path('about-us/', views.abouts_us, name='about_us'),
    #path('contact-us/', views.contact_us, name='contact_us'),
    #path('blank/', views.blank_page, name='blank'),
    path('profile/',views.profile_page, name='profile'),
    path('equipe/',views.equipe_page, name='equipe'),


    # Authentication
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name = 'accounts/password_change_done.html'
    ), name='password_change_done'),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),


    # Components
    path('accordion/', views.accordion, name='accordion'),
    path('alerts/', views.alerts, name='alerts'),
    path('badges/', views.badges, name='badges'),
    path('bootstrap-carousels/', views.bootstrap_carousels, name='carousels'),
    path('breadcrumbs/', views.breadcrumbs, name='breadcrumbs'),
    path('buttons/', views.buttons, name='buttons'),
    path('cards/', views.cards, name='cards'),
    path('dropdowns/', views.dropdowns, name='dropdowns'),
    path('forms/', views.forms, name='forms'),
    path('modals/', views.modals, name='modals'),
    path('navs/', views.navs, name='navs'),
    path('pagination/', views.pagination, name='pagination'),
    path('popovers/', views.popovers, name='popovers'),
    path('progress-bars/', views.progress_bars, name='progress_bars'),
    path('tables/', views.tables, name='tables'),
    path('tabs/', views.tabs, name='tabs'),
    path('toasts/', views.toasts, name='toasts'),
    path('tooltips/', views.tooltips, name='tooltips'),
    path('typography/', views.typography, name='typography'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
