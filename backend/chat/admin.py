from django.contrib import admin

from chat.models import Chat, ChatHistory


class ChatHistoryInline(admin.StackedInline):
    model = ChatHistory
    extra = 0
    fields = ['message', 'created_at', 'sender']
    readonly_fields = ['created_at']


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    inlines = [ChatHistoryInline,]
    list_display = ['doctor', 'patient', '__str__']
    search_fields = ['doctor__name', 'patient__name']
