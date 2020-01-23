from django.shortcuts import render
from django.http import HttpResponse
from myapp.functions.functions import handle_uploaded_file
from myapp.forms import studentForm
def index(request):
    if request.method=='POST':
        student=studentForm(request.POST,request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("file upload successfuly")
    else:
        student = studentForm()
        return render(request,"index.html",{'form':student})
def setsession(request):
    request.session['sname']='irfan'
    request.session['semail']='irfan.sssit@gmail.com'
    return HttpResponse("session is set")
def getsession(request):
    studentname=request.session['sname']
    studentemail=request.session['semail']
    return HttpResponse(studentname+" "+studentemail);
def setcookie(request):
    response=HttpResponse("cookie set")
    response.set_cookie('java-tutorial','javapoint.com')
    return response
def getacookie(request):
    tutorial=request.COOKIES['java-tutorial']
    return HttpResponse("java tutorial @:"+ tutorial);