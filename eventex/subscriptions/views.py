# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def new(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})

def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})
    obj = form.save()
    return HttpResponseRedirect('/inscricao/%d/' %(obj.pk))

def details(request, pk):
    subscription = get_object_or_404(Subscription, pk = pk)
    return render(request, 'subscriptions/subscription_details.html', {'subscription': subscription})