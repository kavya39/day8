from django.urls import path
from App import views
from django.contrib.auth import views as ay

urlpatterns = [
	path('',views.home,name='hm'),
	path('lg/',ay.LoginView.as_view(template_name="html/login.html"),name="lgo"),
	path('reg/',views.register,name="rg"),
	path('con/',views.contact,name='cn'),
	path('lgout/',ay.LogoutView.as_view(template_name='html/logout.html'),name="log"),
	path('pro/',views.profile,name='p'),
	path('hcft/',views.hc,name="hct"),
	path('ch/',views.cgf,name="cg"),
	path('sd/',views.showdata,name="shd"),
	path('del/<int:st>/',views.delete,name="del"),
	path('upd/<int:up>/',views.update,name="upit"),
    path('role/',views.role,name="ro"),
    path('sr/<int:id>/',views.women,name="sr")

]