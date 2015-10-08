from django.shortcuts import render, redirect, get_object_or_404
from .models import Institute
from .forms import InstituteForm



def institute_list(request):
	institute = Institute.objects.all()
	data = {}
	data['institute_list'] = institute
	return render(request, "administrator/institute_list.html", data)

def institute_create(request):
	form = InstituteForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('cms-admin:institute_list')
	return render(request, "administrator/institute_form.html", {'form': form})

def institute_update(request, pk):
	institute = get_object_or_404(Institute, pk=pk)
	form = InstituteForm(request.POST or None, instance=institute)
	if form.is_valid():
		form.save()
		return redirect('cms-admin:institute_list')

	return render(request, "administrator/institute_form.html", {'form': form})

def institute_delete(request, pk):
	institute = get_object_or_404(Institute, pk=pk)
	if request.method == "POST":
		institute.delete()
		return redirect('cms-admin:institute_list')

	return render(request, "administrator/institute_confirm_delete.html", {'object': institute})


