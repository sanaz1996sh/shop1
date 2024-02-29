from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(contactcls)
admin.site.register(productcls)
admin.site.register(Categorycls)
admin.site.register(clientcls)
admin.site.register(salecls)
admin.site.register(sendcls)


admin.site.site_header="بخش مدیریت"
admin.site.site_title="فروشگاه ساعت"
