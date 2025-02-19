from django.contrib import admin
from trench.models import MFAMethod


@admin.register(MFAMethod)
class MFAMethodAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    pass
