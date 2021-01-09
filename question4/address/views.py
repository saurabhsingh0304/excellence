from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer, Address
from .forms import CreateCustomerForm, AddressForm, CustomerForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateCustomerForm()
        customer_form=CustomerForm()
        if request.method == 'POST':
            form = CreateCustomerForm(request.POST)
            customer_form=CustomerForm(request.POST)
            if form.is_valid() and customer_form.is_valid():
                user=form.save()
                customer=customer_form.save(commit=False)
                customer.user=user
                customer.save() 
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form': form, 'customer_form':customer_form}
        return render(request, 'address/registration.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        context = {}
        return render(request, 'address/login.html', context)

@login_required(login_url='login')
def home(request):
    address=Customer.address_set
    lst = address.definitions.all()
    print(lst)
    form=AddressForm()
    if request.method == 'POST':
        form=AddressForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'address':address, 'form':form}
    return render(request,'address/home.html',context)

'''
@login_required(login_url='login')
def updateaddress(request, pk):
	address = Address.objects.get(id=pk)

	form = AddressForm(instance=address)

	if request.method == 'POST':
		form = AddressForm(request.POST, instance=address)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'address/update.html', context)


@login_required(login_url='login')
def deleteaddress(request, pk):
	item = Address.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'address/delete.html', context)
'''

def logoutuser(request):
    logout(request)
    return redirect('login')


'''

'''
