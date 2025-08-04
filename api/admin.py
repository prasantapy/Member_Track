from django.contrib import admin

from api.models import Member
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display=['id','name','email','phone','join_date','membership_type']
