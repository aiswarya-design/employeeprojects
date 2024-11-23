from django.shortcuts import render, redirect
from emp.models import Emp


# Create your views here.
def home(request):
    k = Emp.objects.all()
    return render(request, 'home.html', {'emp': k})


def view(request):
    k = Emp.objects.all()
    return render(request, 'view.html', {'emp': k})


def add(request):
    if request.method == "POST":
        e = request.POST['e']
        n = request.POST['n']
        a = request.POST['a']
        d = request.POST['d']
        m = request.POST['m']
        i = request.FILES.get('i')
        s = Emp.objects.create(eid=e, name=n, age=a, address=d, email=m, image=i)
        s.save()
        return redirect('emp:view')
    return render(request, 'add.html')


def details(request, p):
    k = Emp.objects.get(id=p)
    return render(request, 'details.html', {'emp': k})


def edit(request, p):
    k = Emp.objects.get(id=p)
    if request.method == "POST":
        k.eid = request.POST['e']
        k.name = request.POST['n']
        k.age = request.POST['a']
        k.address = request.POST['d']
        k.email = request.POST['m']
        if request.FILES.get('i') == "None":
            k.save()
        else:
            k.image = request.FILES.get('i')
        k.save()
        return redirect('emp:view')

    return render(request, 'edit.html', {'emp': k})


def delete(request, p):
    k = Emp.objects.get(id=p)
    k.delete()
    return redirect('emp:view')
