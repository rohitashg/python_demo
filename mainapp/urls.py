# URLconf
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from mainapp.forms import LoginForm

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html','redirect_authenticated_user': True,'authentication_form':LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^php_user_signup/$', views.php_user_signup, name='php_user_signup'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^our_blog/$', views.our_blog, name='our_blog'),
    url(r'^testimonials/$', views.testimonials, name='testimonials'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
    url(r'^python_user_signup/$', views.python_user_signup, name='python_user_signup'),
    # url(r'^forgot_password/$', views.forgot_password, name='forgot_password'),
    # url(r'^authentication/new_password/(?P<mobile_code>[\w.@+-=]+)$', views.new_password, name='new_password'),
    # url(r'^term_conditions/$', views.term_conditions, name='term_conditions'),
    # url (r'^confirm_email', views.confirm_email, name="confirm_email"),
    # url (r'^web_confirm_email', views.web_confirm_email, name="web_confirm_email"),
    # url(r'^authentication/check_email$', authentication.check_email, name='check_email'),
    # url(r'^authentication/check_admin_email$', authentication.check_admin_email, name='check_admin_email'),
    # url(r'^authentication/check_admin_mobile$', authentication.check_admin_mobile, name='check_admin_mobile'),
    # url(r'^authentication/edit_admin_mobile$', authentication.edit_admin_mobile, name='edit_admin_mobile'),
    # url(r'^authentication/remove_admin$', authentication.remove_admin, name='remove_admin'),
    # url(r'^authentication/resend_email$', authentication.resend_email, name='resend_email'),
    # url(r'^authentication/profile', authentication.profile, name='profile'),
    # url(r'^authentication/edit_profile$', authentication.edit_profile, name='edit_profile'),
    # url(r'^authentication/check_mobile', authentication.check_mobile, name='check_mobile'),
    # url(r'^authentication/edit_check_mobile', authentication.edit_check_mobile, name='edit_check_mobile'),
    # url(r'^authentication/update_mobile', authentication.update_mobile, name='update_mobile'),
    # url(r'^authentication/change_password', authentication.change_password, name='change_password'),
    # url(r'^authentication/check_code', authentication.check_mobile_code, name='check_mobile_code'),
    # url(r'^mobile_verification$', authentication.mobile_verification, name='mobile_verification'),
    # url(r'^check_mobile_verification_code', authentication.check_mobile_verification_code, name='check_mobile_verification_code'),
    # url(r'^check_old_password', authentication.check_old_password, name='check_old_password'),
    # url(r'^authentication/admin_popup', authentication.admin_popup, name='admin_popup'),
    #url(r'^property/property_add$', property.property_add, name="property_add"),
]
