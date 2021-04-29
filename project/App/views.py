from django.shortcuts import render,redirect
from App.forms import RegForm,CraftsForm,ChpwdForm,WorkerForm
from django.contrib.auth.decorators import login_required
from App.models import HandiCrafts,Worker,Category,Product

# Create your views here.

def home(request):
	d=Category.objects.all()
	return render(request,'html/home.html',{'data':d})

def register(request):
	if request.method=="POST":
		q=RegForm(request.POST)
		if q.is_valid():
			q.save()
			return redirect('/lg')
	q=RegForm()
	return render(request,'html/register.html',{'u':q})

def contact(request):
	return render(request,'html/contact.html')
@login_required
def hc(request):
	if request.method=="POST":
		j=CraftsForm(request.POST,request.FILES)
		if j.is_valid():
			i=j.save(commit=False)
			i.uid_id=request.user.id
			i.save()
			return redirect('/hcft')
	j=CraftsForm()
	k=HandiCrafts.objects.filter(uid_id=request.user.id)
	return render(request,'html/handcrafts.html',{'u':j,'y':k})


@login_required
def profile(request):
	return render(request,'html/profile.html')

@login_required
def cgf(request):
	if request.method=="POST":
		print("yes")
		c=ChpwdForm(user=request.user,data=request.POST)
		if c.is_valid():
			c.save()
			return redirect('/lg')
	c=ChpwdForm(user=request)
	return render(request,'html/changepwd.html',{'t':c})


def showdata(request):
	t=CraftsForm()
	return render(request,'html/showdata.html',{'info':t})

def delete(request,st):
	hc=HandiCrafts.objects.get(id=st)
	hc.delete()
	return redirect('/hcft')

def update(request,up):
	t=HandiCrafts.objects.get(id=up)
	if request.method=="POST":
		y=CraftsForm(request.POST,instance=t)
		if y.is_valid():
			y.save()
		return redirect('/hcft')
	y=CraftsForm(instance=t)
	return render(request,'html/updateitem.html',{'f':y})

def role(request):
	return render(request,'html/roles.html')

def showdata(req):
	if req.method=="POST":
		b=WorkerForm(req.POST)
		if b.is_valid():
			b.save()
		return redirect('/sd')
	b=WorkerForm()
	a=Worker.objects.all()
	return render(req,'html/showdata.html',{'wd':a,'info':b})


def women(req,id):
	c=Category.objects.all()
	p=Product.objects.filter(pid_id=id)
	return render(req,'html/women.html',{'da':p})