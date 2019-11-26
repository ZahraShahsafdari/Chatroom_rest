from django.contrib import admin
from message.models import Conversations, Messages

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ('text' , 'sender' , 'date' , 'status')
    search_fields = ('text',)

admin.site.register(Conversations)
admin.site.register(Messages, MessageAdmin)