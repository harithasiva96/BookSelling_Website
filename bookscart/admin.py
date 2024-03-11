from django.contrib import admin
from bookscart.models import customer
admin.site.register(customer)
from bookscart.models import admin_addbooks
admin.site.register(admin_addbooks)
from bookscart.models import buynow
admin.site.register(buynow)
from bookscart.models import payment
admin.site.register(payment)
# Register your models here.
