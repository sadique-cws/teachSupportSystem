from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "TechSupport Admin"
admin.site.site_title = "TechSupport Admin Portal"
admin.site.index_title = "Welcome to TechSupport Admin Portal"




admin.site.register(UserRole)
admin.site.register(SupportTicket)
admin.site.register(TicketComment)
admin.site.register(TicketAttachment)