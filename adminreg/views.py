from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from django.shortcuts import  render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def admin_login(request) :
    
    if request.method == 'POST' :
        username=request.POST['username']
        password =request.POST['password']
        try:
            User.objects.get(username = username, is_superuser = True)
            user = authenticate(username = username , password = password, is_superuser = True)
            if user is not None :
                login(request, user)
                return redirect('addandshow')
            else :
                messages.error(request,'username or password not correct')
        except:
            messages.error(request,'this user is not admin')
    
 
    return render ( request , 'enroll/loginnew.html')


def add_show(request):
    
    if not request.user.is_superuser:
        return redirect('admin')
    
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
         fm.save()
         fm=StudentRegistration()
    else:
        fm=StudentRegistration()  
    stud=User.objects.all() 
    return render(request, 'enroll/addandshow.html', {'form':fm,'stu':stud })

    #This function will update/Edit
def update_data(request,id): 
     
    if request.method=='POST':
        pi=User.objects.get(pk=id) 
        fm=StudentRegistration(request.POST,instance=pi)  
        if fm.is_valid():
            fm.save() 
            
    else:
           pi=User.objects.get(pk=id) 
           fm=StudentRegistration(instance=pi)       
    return render(request,'enroll/updatestudent.html',{'form':fm})  

# for deleting the data
def delete_data(request,id):
   
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/adminreg')
                                                                                                                                                                                                                                                                                                                                                                                                                        