from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),

    # path('pricing/<str:data_param>/', views.data_display_view, name='data_display'),

    path("pricing/<str:data_param>/", views.pricing, name="Pricing"),
    path("contact/", views.contact, name="ContactUs"),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.user_logout, name='user_logout'),
    path("user_login/", views.user_login, name="user_login"),


    # path('user_login/', views.user_login, name='user_login_simple'),

    path("register/", views.register, name="register"),
    path('register/free/', views.register, {'user_type': 'free'}, name='user_register_free'),
    path('register/pro/', views.register, {'user_type': 'pro'}, name='user_register_pro'),
    path('register/ultrapro/', views.register, {'user_type': 'ultrapro'}, name='user_register_ultrapro'),

    # Main Content Display
    path("agromore/", views.home, name="home"),
    path('agromore/dashboard/',         views.home, {'screen_content': 'dashboard'},            name='screen_content_dashboard'),
    path('agromore/analytics/',         views.home, {'screen_content': 'analytics'},            name='screen_content_analytics'),
    path('agromore/datalog/',           views.home, {'screen_content': 'datalog'},              name='screen_content_datalog'),
    path('agromore/api_key/',           views.home, {'screen_content': 'api_key'},              name='screen_content_api_key'),
    path('agromore/documantation/',     views.home, {'screen_content': 'documantation'},        name='screen_content_documantation'),
    path('agromore/account/',           views.home, {'screen_content': 'account'},              name='screen_content_account'),


    # path("datalog/", views.datalog, name="datalog"),
    # path("recommedation/", views.recommendation, name="recommedation"),
    # path("dashboard/", views.dashboard, name="dashboard"),

    # Store Data
    path("store-data/", views.store_data, name="store_data"),


    path('apikey/data/', views.getfielddata, name='getfielddata'),

    path('generate-api-key/', views.generate_api_key, name='generate_api_key'),
    path('recommend-data/', views.recommend_data, name='recommend_data'),

    path('line_chart/', views.line_chart, name='line-chart'),

    # path("products/<int:myid>", views.productView, name="ProductView"),
    # path("products/<str:myslug>", views.productView, name="ProductView"),

]