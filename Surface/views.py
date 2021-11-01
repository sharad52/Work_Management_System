from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import reverse
from Surface.models import WorkDetail
from django.contrib import messages
from Surface.forms import WorkDetailForm

# Create your views here.
def Index(request,*args,**kwargs):
	work = WorkDetail.objects.all()
	total_work = WorkDetail.objects.count()
	context = {
	'work_count':total_work,
	'work':work,
	}
	return render(request,'index.html',context)

def addWork(request,*args,**kwargs):
	form = WorkDetailForm()
	if request.method == 'POST':
		# print(request.method=='POST')
		# print(request.POST)
		form = WorkDetailForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request,'Saved Successfully')
			return HttpResponseRedirect(reverse('SurfaceApp:index'))
	else:
		form = WorkDetailForm()
	context= {
		'action':'Add',
		'form':form,
	}
	return render(request,'pages/add-form.html',context)

def UpdateWork(request,slug):
	work = get_object_or_404(WorkDetail,slug=slug)
	form = WorkDetailForm(instance=work)
	if request.method == 'POST':
		form = WorkDetailForm(request.POST,instance=work)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			return HttpResponseRedirect(reverse('SurfaceApp:index'))
	context= {
		'action':'Update',
		'form':form,

	}
	return render(request,'pages/add-form.html',context)

def DeleteWork(request,slug):
	work = get_object_or_404(WorkDetail,slug=slug)
	if request.method == 'POST':
		work.delete()
		messages.success(request,'Deleted Successfully')
		return HttpResponseRedirect(reverse('SurfaceApp:index'))
	context= {
		'work':work,

	}
	return render(request,'pages/delete-form.html',context)


def TestFunction(request,*args,**kwargs):
	return HttpResponse("Test function")