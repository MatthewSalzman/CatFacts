from django.contrib import admin
from core.models import Fact, Header, Footer, Email
# Register your models here.


admin.site.register(Fact)
admin.site.register(Header)
admin.site.register(Footer)
admin.site.register(Email)