from django.shortcuts import render,HttpResponse,redirect,Http404
#from django.contrib.auth import authenticate,login,logout
#from django.contrib.auth.models import User
from .models import *
from .forms import *
import logging
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException

# Create your views here.
def index(request):
    return render(request,"products_app/index.html")



def shop(request,category=None):
    cate=Categorycls.objects.all()
    if category:
        products = productcls.objects.filter(category__name__icontains=category)
    else:
        products = productcls.objects.all()
        
    s=request.GET.get("search","")
    if(s):
       products=productcls.objects.filter(name__icontains=s) 

    return render(request,"products_app/shop.html",context={"products":products,"cate":cate,"category": category, "search": s})



def contact(request):
    error=[]
    if request.method=="POST":
        frm=fcontact(request.POST)
        if frm.is_valid()==False:
            error.append("فرم معتبر نیست")
        else:
            n=frm.cleaned_data["name"]
            s=frm.cleaned_data["subject"]
            e=frm.cleaned_data["email"]
            m=frm.cleaned_data["message"]
            contactcls.objects.create(name=n,subject=s,email=e,message=m)
            return render(request,"products_app/message.html")
        
    else:    
        frm=fcontact()
    return render(request,"products_app/contact-us.html",{"form":frm,"error":error})



def about(request):
    return render(request,"products_app/about-us.html")



def log(request):
    if(request.session.get("login")):
        return redirect("/")
    
    if(request.method=="POST"):
        u=request.POST.get("user")
        p=request.POST.get("pass")
        user=clientcls.objects.filter(username=u,password=p)
        if(user) :
            request.session["login"]=u
            return redirect("/cart")
        else:
            return redirect("/error")

    return render(request,"products_app/login.html")


def sign(request):
    if request.method=="POST":
        status=False
        context={"errors":[]}
        n=request.POST.get("name")
        l=request.POST.get("lname")
        e=request.POST.get("email")
        u=request.POST.get("username")
        p=request.POST.get("password")
        rp=request.POST.get("rpassword")
        if len(p)<6:
            status=True
            context["errors"].append("password must be 6 characters")
        if p!=rp:
            status=True
            context["errors"].append("re_password is not match")

        if(status==False):    
            clientcls.objects.create(name=n,lname=l,email=e,username=u,password=p,rpassword=rp)
            return redirect("/success") 
        else:
            return render(request,"products_app/sign-up.html",context=context)
        
    return render(request,"products_app/sign-up.html")

    
def sc(request):
    return render(request,"products_app/success.html")

def successful(request):
    return render(request,"products_app/successful.html")

def unsuccessful(request):
    return render(request,"products_app/unsuccessful.html")
    

def addtocart(request,adad):
    if(request.session.get("login")):
        cl=clientcls.objects.get(username=request.session.get("login"))
        pr=productcls.objects.get(id=adad)
        ca=cartcls.objects.filter(client=cl,product=pr).first()
        if ca==None:
            cartcls.objects.create(client=cl,product=pr,qnt=1)
        else:
            ca.qnt=ca.qnt+1
            ca.save()
        return redirect("/cart")
    else:
        return redirect("/login")


def delcart(request,adad):
    if(request.session.get("login")):
        cl=clientcls.objects.get(username=request.session.get("login"))
        pr=productcls.objects.get(id=adad)
        ca=cartcls.objects.filter(client=cl,product=pr)
        ca.delete()
        return redirect("/cart")
    else:
        return redirect("/login")
     

def cart(request):
       if(request.session.get("login")):
           cl=clientcls.objects.get(username=request.session.get("login"))
           products=cartcls.objects.filter(client=cl)
           send=sendcls.objects.filter()
           t=0
           to=0
           for itm in products:
               t=t+itm.product.price*itm.qnt
           for itm in send:
               to=t+itm.send 
               
           return render(request,"products_app/cart.html",{"products":products,"t":t,"to":to,"snd":send})
       else:
           return redirect("/")
       

def edqnt(request,adad):
    if(request.session.get("login")):
        cl=clientcls.objects.get(username=request.session.get("login"))
        pr=productcls.objects.get(id=adad)
        qnt=request.POST.get("qnt")
        ca=cartcls.objects.filter(client=cl,product=pr).first()
        ca.qnt=qnt
        ca.save()
        
        return redirect("/cart")
    else:
        return redirect("/login")
    
    
def lout(request):
    del request.session["login"]
    return redirect("/login")


def error(request):
    return render(request,"products_app/error.html")


def pardakht(request):
    if(request.session.get("login")):
           cl=clientcls.objects.get(username=request.session.get("login"))
           products=cartcls.objects.filter(client=cl)
           send=sendcls.objects.filter()
           t=0
           to=0
           for itm in products:
               t=t+itm.product.price*itm.qnt
           for itm in send:
               to=t+itm.send 
        # خواندن مبلغ از هر جایی که مد نظر است
           amount = to
            # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
           user_mobile_number = '+989112221234'  # اختیاری

           factory = bankfactories.BankFactory()
           try:
                bank =  factory.create(bank_models.BankType.IDPAY) 
                bank.set_request(request)
                bank.set_amount(amount)
                # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
                bank.set_client_callback_url('/callback-gateway')
                bank.set_mobile_number(user_mobile_number)  # اختیاری
            
                # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
                # پرداخت برقرار کنید. 
                bank_record = bank.ready()
                
                # هدایت کاربر به درگاه بانک
                return bank.redirect_gateway()
           except AZBankGatewaysException as e:
                logging.critical(e)
                # TODO: redirect to failed page.
                raise e
           





def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        return redirect("/successful")

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return redirect("/unsuccessful")




