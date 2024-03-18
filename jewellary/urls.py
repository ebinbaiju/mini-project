from django.urls import path
from . import views

urlpatterns = [
    path('customer/',views.insert,name="customer"),
    path('view/',views.view,name="view"),
    path('detailedview/<str:pk>',views.detailedview,name="detailedview"),
    path('delete/<str:pk>',views.delete,name="deleted"),
    path('update/<str:pk>',views.update,name="update"),
    path('customerlogin/',views.customerlogin,name="customerlogin"),
    path('userlog/',views.userlog,name="userlog"),
    path('logoutuser/',views.logoutuser,name="logoutuser"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('alog/',views.alog,name="alog"),
    path('staff/',views.input,name="staff"),
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('product/',views.product,name="product"),
    path('cart/',views.cart,name="cart"),
    path('view1/',views.view1,name="view"),
    path('detailedview1/<str:pk>',views.detailedview1,name="detailedview1"),
    path('delete1/<str:pk>',views.delete1,name="deleted1"),
    path('update1/<str:pk>',views.update1,name="update1"),
    path('stafflogin/',views.stafflogin,name="stafflogin"),
    path('staffwelcome/',views.staffwelcome,name="staffwelcome"),
    path('stafflog/',views.stafflog,name="stafflog"),
    path('logoutuser1/',views.logoutuser1,name="logoutuser1"),
    path('customerwelcome/',views.customerwelcome,name="customerwelcome"),
    path('add_product/',views.add_product,name="add_product"),
    path('staffproduct_update/<str:pk>', views.staffproduct_update, name='staffproduct_update'),
    # path('product/<int:product_id>/', views.product_update, name='product_update1'),
    # path('product/<int:product_id>/update/', views.product_update, name='product_update')
]
