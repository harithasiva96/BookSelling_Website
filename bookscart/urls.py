from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='path'),
    path('form',views.form,name='form'),
    path('login',views.login,name='login'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('edit',views.edit,name='edit'),
    path('log_out',views.log_out,name='log_out'),
    path('add_books',views.addbooks,name='add_books'),
    path('books',views.viewbooks,name='books'),
    path('update/<int:id>',views.update_books,name='update'),
    path('delete/<int:id1>',views.deletion,name='delete'),
    path('books1',views.customer_viewbooks,name='books1'),
    path('buy/<int:id2>',views.buy,name='buy'),
    path('userhome',views.user_home,name='userhome'),
    path('view1',views.view_order1,name='view1'),
    path('order_approval/<int:id3>',views.order_approval,name='order_approval'),
    path('order_rejection/<int:id3>',views.order_rejection,name='order_rejection'),
    path('my_orders',views.user_vieworder,name='my_orders'),
    path('payment/<int:id4>/<int:amount>',views.paymentRegistration,name='payment')
    ]