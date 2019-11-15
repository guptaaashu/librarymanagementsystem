from django.shortcuts import render
from .models import book
from django.shortcuts import render, get_object_or_404
from student.models import 	Student
from django.utils import timezone
# Create your views here.

def detail(request):
    boo= book.objects.filter(available=True)
    return render(request, 'detail_view.html', {'books': boo})

def detail_view(request,pk):
	boo=get_object_or_404(book, pk=pk)
	return render(request, 'detailed.html', {'books': boo})

def issue(request,pk):
	boo=get_object_or_404(book, pk=pk)
	boot=book.objects.filter(pk=pk).update(available=False,issuing_date=timezone.now(),returning_date=timezone.now() + timezone.timedelta(days=5))
	user=get_object_or_404(Student, user=request.user)
	user.books_issued.add(boo)
	return render(request, 'issue.html')

def issued(request):
	user=get_object_or_404(Student, user=request.user)
	books=user.books_issued.all()
	return render(request, 'detailed1.html', {'books': books})