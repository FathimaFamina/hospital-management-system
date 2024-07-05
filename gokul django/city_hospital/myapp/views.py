from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import BookingForm

from.models import Departments,Doctors
from.models import Appointment

def base(request):
   return render(request,'base.html')

def home(request):
   return render(request,'home.html')

def about(request):
   return render(request,'about.html')

def booking(request):
   return render(request,'booking.html')

def doctor(request):
   return render(request,'doctors.html')

def appoinment(request):
   
   form=BookingForm()
   dict_form={
      'form':form
   }
   return render(request,'appoinment.html',dict_form)

def department(request):
   dic_dept={
      "dept":Departments.objects.all()
   }

   return render(request,'department.html',dic_dept)

def contact(request):
   return render(request,'contact.html')

def doctors(request):
   dic_doc={
      "doctors":Doctors.objects.all()
   }
   return render(request,'doctors.html',dic_doc)



# from .models import Appointment

def appoinment(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the form data to the model
            appoinment = Appointment(
                p_name=form.cleaned_data['p_name'],
                p_phone=form.cleaned_data['p_phone'],
                p_email=form.cleaned_data['p_email'],
                doc_name=form.cleaned_data['doc_name'],
                booking_date=form.cleaned_data['booking_date'],
            )
            appoinment.save()
            return redirect('appoinment')  # Redirect to a success page
    else:
        form = BookingForm()

    return render(request, 'appoinment.html', {'form': form})

      
# def appoinment(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             # Save the form data to the model
#             Appointment = form.save()
#             return redirect('appoinment')  # Redirect to a success page
#     else:
#         form = BookingForm()

#     return render(request, 'appoinment.html', {'form': form})




       