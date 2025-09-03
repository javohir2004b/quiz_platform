from django.contrib import admin

from questions.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in User._meta.fields]
