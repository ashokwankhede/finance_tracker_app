from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreationForm
from .models import User, Transaction, Balance
from django.contrib.auth import authenticate, login


# Create your views here.

def create_user(request):
    form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})




def sign_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home', username)
    return render(request, 'sign_in.html')



def home(request, username):
    user_record = User.objects.get(username=username)
    user_balance = Balance.objects.filter(user=user_record).first()
    user_transactions = Transaction.objects.filter(user=user_record).order_by('-created_at')
    return render(request, 'home.html', {'user': user_record, 'balance': user_balance, 'transactions': user_transactions})


def create_transaction(request, username):
    if request.method == "POST":
        print("username: ", username)
        amount = request.POST["amount"]
        transaction_type = request.POST["transaction_type"]
        description = request.POST["description"]
        user = User.objects.get(username=username)
        Transaction.objects.create(user=user, amount=amount, transaction_type=transaction_type, description=description)
        return redirect('home', username)