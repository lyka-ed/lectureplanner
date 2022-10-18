from django.shortcuts import render, redirect, get_object_or_404
from .form import LectureForm
from .models import Lecture, Lab


# Create your views here.

def details(request, id):
    lecture = get_object_or_404(Lecture, pk=id)

    return render(request, 'lectures/details.html', {"lecture": lecture })

def labs_list(request):
    return render(request, 'lectures/labs_list.html',{"labs": Lab.objects.all()})


def form(request):
    if request.method == "POST":
        form = LectureForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = LectureForm()         

    return render(request, 'lectures/form.html',{"form":form})

