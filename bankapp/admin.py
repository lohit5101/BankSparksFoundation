from django.contrib import admin
from .models import customer
from .models import Transact
admin.site.register(customer)
admin.site.register(Transact)
