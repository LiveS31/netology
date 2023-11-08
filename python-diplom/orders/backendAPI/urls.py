from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from .views import RegisterUser, LoginUser, UserDetails, ContactView, \
    ProviderUpdate, ProviderState, ProductView, CartView, OrderView, ProviderOrders, CategoryView, ShopView, \
    ConfirmAccount

app_name = 'backendAPI'

urlpatterns = [
    path('user/register', RegisterUser.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/login', LoginUser.as_view(), name='user-login'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/details', UserDetails.as_view(), name='user-details'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
    path('shops', ShopView.as_view(), name='shops'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('products', ProductView.as_view(), name='products'),
    path('partner/update', ProviderUpdate.as_view(), name='partner-update'),
    path('partner/state', ProviderState.as_view(), name='partner-state'),
    path('partner/orders', ProviderOrders.as_view(), name='partner-shopAPI'),
    path('cart', CartView.as_view(), name='cart'),
    path('order', OrderView.as_view(), name='order'),
]
