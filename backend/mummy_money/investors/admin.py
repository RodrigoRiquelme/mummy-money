from django.contrib import admin

from mummy_money.investors.models import Investor


@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name', 'funds')
    list_display = (
        'id',
        'root_privilege',
        'name',
        'parent',
        'funds',
        'innocence',
        'experience',
        'charisma',
        'status',
        'joining_at',
        'leaving_at'
    )
    fields = (
        'root_privilege',
        'name',
        'parent',
        'funds',
        'innocence',
        'experience',
        'charisma',
        'status'
    )
