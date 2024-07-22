from django.shortcuts import render, redirect 
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User 
from django.contrib import messages, auth
from .models import Profile , Sport , Messages , Event , EventParticipation
from django.core.mail import send_mail
from django.core.mail.backends.smtp import EmailBackend
from django.conf import settings
import smtplib ,ssl
from django.http import HttpResponseBadRequest
from datetime import datetime
import razorpay
from django.views.decorators.csrf import csrf_exempt
client = razorpay.Client(auth=('rzp_test_C1O5vFewJ1uRXw', 'sxA7Gl5YUIyPtUURdtqTKNeY'))

def send_email(subject,body , reciever):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'nickrai057@gmail.com'
    smtp_password = 'snivmzmpwrvfmczj'

    from_email = 'nickrai057@gmail.com'
    to_email = reciever

    message = f'Subject: {subject}\n\n{body}'

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.sendmail(from_email, to_email, message)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        # type = request.POST['role']

        if User.objects.filter(username=username).exists():
            messages.error(request, "User is already exists!")
        else:
            if password == confirm_password:

                user = User.objects.create_user(username=username, password=password ,first_name = first_name , last_name = last_name ,email = email )
                user.save()
                profile = Profile.objects.create(user = user )
                profile.save()

                messages.success(request, "User signup successfully!")
                send_email("no-reply" , f"hello , {user.first_name}\n your registration is successfully done " ,user.email )
                print(str(user))

            else:
                messages.error(request, "Password doesn't matching")
            
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            user = request.user
            profile = Profile.objects.filter(user = user).first()
            request.session['user_type'] = str(profile.user_type)
            return redirect('/')

    return render(request, 'login.html')

def logout(request):
    if request.method == "GET":
        auth.logout(request)
        return redirect('/login')
    

@login_required(login_url='/login')
def home(request):
   
    user = request.user
    profile = Profile.objects.filter(user = user).first()
    events = Event.objects.all()
    if str(profile.user_type) == "player":
        
        return render (request ,'home.html',  {'events':events})

    else:
        
        return render(request, 'home.html', {'events':events} )
    
def gym(request):
    return render(request, 'gym.html')

def sports(request):
    page = request.GET.get('page')
    if page is not None:
        sport = Sport.objects.filter(name = page).first()
        print(sport)
        print(page)
        return render(request, 'sports.html' , {'sport': sport , 'page': 1})
    
    else:
        sports = Sport.objects.all()
        return render(request, 'sports.html' , {'sports': sports , 'page': 0})


def medical(request):
    return render(request, 'medical.html')

def add(request):
    return render(request , 'add.html')

def library(request):
    return render(request, 'library.html')

def feedback(request):
    return render(request , 'feedback.html')

def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    user_model = User.objects.get(username=request.user)
    if request.method == 'POST':
        print("abc")
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        if request.FILES.get('dp') == None:
            dp = user_profile.image
        else:
            dp = request.FILES.get('dp')

        user_profile.image = dp
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email

    user_model.save()
    user_profile.save() 
        
    return render(request,'profile.html',{'user_profile':user_profile,'user_model':user_model})




def event(request):
    events = Event.objects.all()
    return render (request , "upevent.html" ,{'events': events})

def playerstats(request):
    profiles = Profile.objects.filter(user_type = "player")
    print(profiles)
    return render(request , "playerstats.html", {'profiles': profiles})

def player_profile(request):
    id = request.GET.get("id")
    user_model = User.objects.get(id = id)
    print("firstname : ",user_model.first_name)
    user_profile = Profile.objects.get(user = user_model)
    if request.method == "POST":
        message = request.POST.get("message")
        message_model = Messages(sender = request.user, reciever = user_model , message = message , date = datetime.now())
        message_model.save()

    return render(request , "player_profile.html" ,{'user_model': user_model, 'user_profile':user_profile})


def instruction(request):
    messages = Messages.objects.filter(reciever = request.user)

    return render(request , "instruction.html", {'messages': messages})


def participate(request):
    event_id = int(request.GET.get("id"))
    event = Event.objects.get(id = event_id)
    user = request.user
    is_participate = EventParticipation.objects.filter(event = event , user = user).first()
    if is_participate == None:
        event_partcipate = EventParticipation(event = event , user = user , date = datetime.now())
        event_partcipate.save()
        return redirect("/previous_event")
    else:
        messages.error(request, "Already participated")
        # return render(request , "upevent.html")
        return redirect("/event")

def previous_event(request):
    events = EventParticipation.objects.filter(user = request.user)
    return render(request , "previous_event.html", {'events': events})


def remove_participation(request):
    event_id = int(request.GET.get("id"))
    event = Event.objects.get(id = event_id)
    EventParticipation.objects.filter(event = event).delete()
    return redirect("/previous_event")

def management(request):
    return render(request , "management.html")


def fee(request):
        
        if request.method == 'POST':
            email =request.POST.get('email')
            username = request.POST.get('username')
            amount = request.POST.get('amount_to_pay')
            print(email)
            print(username)
            print(amount)
            
            amount = amount * 100
            currency = 'INR'
            client = razorpay.Client(auth=("rzp_test_aWJEEFVRMQXO35","tiJ9kPSluGLZDv3eaXUhn1qm" ))
            payment = client.order.create({'amount': amount , 'currency': 'INR', 'payment_capture':'1'})
            payment_id = payment['id']
           


            return render(request , "fee.html" ,{'payment':payment , 'payment_id':payment_id} )
           
        else:
            return render(request , "fee.html")



@csrf_exempt
def payment(request):
 
    # only accept POST request.
    if request.method == "POST":
        email =request.POST.get('email')
        username = request.POST.get('username')
        amount = request.POST.get('amount_to_pay')
        print(email)
        print(username)
        print(amount)
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 100  # Rs. 200
                try:
 
                    # capture the payemt
                    client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return render(request, 'payment.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:
 
                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()

@csrf_exempt
def payment_success(request):
    return render(request, 'success.html')


  


