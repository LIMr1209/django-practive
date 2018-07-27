from django.shortcuts import render,HttpResponse

# Create your views here.
def show_form(request):
    if request.method=="GET":
        return render(request,'form.html')
    elif request.method=="POST":
        print(request.path)
        print(request.POST)
        user=request.POST.get('user')
        password=request.POST.get('password')
        return HttpResponse(user,password)
