from django.db import models
import datetime
# Create your models here.
class clientcls(models.Model):
    name=models.CharField(max_length=50,verbose_name="نام ") 
    lname=models.CharField(max_length=50,verbose_name="فامیل ")
    username=models.CharField(max_length=50,verbose_name="نام کاربری")
    email=models.EmailField(max_length=150,verbose_name=" ایمیل")
    password=models.CharField(max_length=50,verbose_name=" پسورد")
    rpassword=models.CharField(max_length=50,verbose_name="تکرار پسورد ")
    class Meta:
        verbose_name="مشتری"
        verbose_name_plural="مشتریان"

    def __str__(self) -> str:
        return self.name


class Categorycls(models.Model):
    name = models.CharField(max_length=100,verbose_name="نام کتگوری")
    class Meta:
        verbose_name="کتگوری"
        verbose_name_plural="کتگوری ها"

    def __str__(self) -> str:
        return self.name
    

class productcls(models.Model):
    name=models.CharField(max_length=50,verbose_name="نام محصول")
    price=models.DecimalField(decimal_places=0,max_digits=10,verbose_name="قیمت")
    img=models.ImageField(upload_to="imgs",verbose_name="عکس ها")
    category=models.ManyToManyField(Categorycls,verbose_name="کتگری")
    des=models.CharField(max_length=2000,verbose_name="توضیحات")
    dateadd=models.DateTimeField(null=True,verbose_name="تاریخ وساعت")
    code=models.CharField(max_length=150,default=1,verbose_name="کد محصول")
    is_special=models.BooleanField(verbose_name="محصول ویژه",null=True)
    special_price=models.DecimalField(decimal_places=0,max_digits=10,verbose_name="قیمت ویژه",null=True)
    class Meta:
        verbose_name="محصول"
        verbose_name_plural=" محصولات"
    
    def __str__(self) -> str:
        return self.code
    

class cartcls(models.Model):
    client=models.ForeignKey(clientcls,on_delete=models.CASCADE,verbose_name="مشتری ")
    product=models.ForeignKey(productcls,on_delete=models.CASCADE,verbose_name="محصول ")
    qnt=models.IntegerField()
    
    class Meta:
        verbose_name="سبد"
        verbose_name_plural="سبدها"
    def __str__(self) -> str:
        return self.client


class salecls(models.Model):
    client=models.ForeignKey(clientcls,on_delete=models.CASCADE,verbose_name="مشتری ")
    defa=models.DateTimeField(default=datetime.datetime.now,verbose_name="تاریخ")
    totalprice=models.DecimalField(decimal_places=0,max_digits=10,verbose_name="قیمت نهایی")
    class Meta:
        verbose_name="فاکتور"
        verbose_name_plural="فاکتورها"
    def __str__(self) -> str:
        return self.client
    

class sale_detailscls(models.Model):
    sale=models.ForeignKey(salecls,on_delete=models.CASCADE,verbose_name="مشتری ")  
    product=models.ForeignKey(productcls,on_delete=models.CASCADE,verbose_name="مشتری ")
    qnt=models.IntegerField()
    class Meta:
        verbose_name="جزییات فاکتور"
        verbose_name_plural="جزییات فاکتورها"
    def __str__(self) -> str:
        return self.sale


  
class contactcls(models.Model):
    name=models.CharField(max_length=50,verbose_name="نام و نام خانوادگی") 
    subject=models.CharField(max_length=50,verbose_name="موضوع")
    email=models.EmailField(max_length=50,verbose_name="ایمیل")
    message= models.CharField(max_length=3000,verbose_name="پیام")
    class Meta:
        verbose_name="ارتباط"
        verbose_name_plural="ارتباطات"  

    def __str__(self):
        return self.name 
    
class sendcls(models.Model):
    send=models.IntegerField(null=True,verbose_name="هزینه ارسال ")
    class Meta:
        verbose_name="هزینه ارسال"
        verbose_name_plural="هزینه ارسال"

    
                         