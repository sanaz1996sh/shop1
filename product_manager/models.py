from django.db import models

# Create your models here.
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
    category=models.ManyToManyField(Categorycls,verbose_name="کتگری",default=1)
    des=models.CharField(max_length=2000,verbose_name="توضیحات",default=1)
    dateadd=models.DateTimeField(null=True,verbose_name="تاریخ وساعت")
    code=models.CharField(max_length=150,default=1,verbose_name="کد محصول")
    is_special=models.BooleanField(verbose_name="محصول ویژه",null=True)
    special_price=models.DecimalField(decimal_places=0,max_digits=10,verbose_name="قیمت ویژه",null=True)
    
    class Meta:
        verbose_name="محصول"
        verbose_name_plural=" محصولات"

    def __str__(self) -> str:
            return self.name 
        