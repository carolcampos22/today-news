from django.contrib import admin
from base.models import Register

# Register your models here.
@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'created_at', 'category']
    search_fields = ['title', 'category', 'created_at']
    list_filter = ['created_at']


