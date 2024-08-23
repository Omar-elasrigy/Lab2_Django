from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from Account.models import *

def list(request):
    trainees = Trainee.objects.all()
    context = {'trainees': trainees}
    return render(request, 'trainee/list.html', context)

    

def update_trainee(request, id):
    trainee = get_object_or_404(Trainee, pk=id)
    
    if request.method == 'POST':
  
        name = request.POST.get('name')
        account_id = request.POST.get('Account_id')

      
        if name and 0 < len(name) <= 100:
            trainee.name = name
            trainee.id_obj = get_object_or_404(Account, pk=account_id)
            trainee.save()
            return redirect('list')
        else:
        
            context = {
                'trainee': trainee,
                'error': 'Invalid name'
            }
            return render(request, 'trainee/update.html', context)
    
    context = {
        'trainee': trainee,
        'accounts': Account.objects.all() 
    }
    return render(request, 'trainee/update.html', context)

    
def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, pk=id)

    if request.method == 'POST':
   
        trainee.delete()
      
        return redirect('list')  

 
    return render(request, 'trainee/delete.html', {'trainee': trainee})

    

def show_details_trainee(request, id):
    trainee = get_object_or_404(Trainee, pk=id)
    return render(request, 'trainee/showDetails.html', {'trainee': trainee})

def create(request):
    context={}
    context['accounts']=Account.objects.all()
    if(request.method=='POST'):
         context={}
         
         
         if(len(request.POST['name'])>0 and len(request.POST['name'])<=100):
                        Traineeobj=Trainee()
                        Traineeobj.name = request.POST.get('name')
                        Traineeobj.id_obj=Account.objects.get(pk=request.POST['Account_id'])
                        Traineeobj.save()
                        return redirect('list')  

         else:
                context['error']='invalid name'
    return render (request,'trainee/create.html',context)


