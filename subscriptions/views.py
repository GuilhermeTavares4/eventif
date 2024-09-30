from django.shortcuts import render
from django.http import HttpResponse
from subscriptions.forms import SubscriptionForm

# Create your views here.
def subscribe(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)