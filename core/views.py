from django.shortcuts import render
from .models import Donation
from .forms import DonationForm,NGOForm


from django.shortcuts import render, redirect  # Add redirect here
from .models import Donation, DonationStatus
from .forms import DonationForm

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save()
            DonationStatus.objects.create(donation=donation, status='listed')
            return redirect('home')
        else:
            # Add this to see form errors in console
            print(form.errors)  
    else:
        form = DonationForm()
    return render(request, 'core/donate.html', {'form': form})

def home(request):
    return render(request, 'core/home.html')



def map_view(request):
    donations = Donation.objects.filter(status__status='listed')
    return render(request, 'core/map.html', {'donations': donations})

def tracking(request):
    donations = Donation.objects.all()
    return render(request, 'core/tracking.html', {'donations': donations})

def notifications(request):
    return render(request, 'core/notifications.html')

def register_ngo(request):
    if request.method == 'POST':
        form = NGOForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = NGOForm()
    return render(request, 'core/register_ngo.html', {'form': form})

def registration_success(request):
    return render(request, 'core/home.html')