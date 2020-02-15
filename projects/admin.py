from django.contrib import admin
from .models import other_contractors_bid, Tender
from django.contrib.auth.models import Group
from django.contrib.admin import AdminSite
# Register your models here.

admin.site.site_url = "/"

class InlineContractors(admin.TabularInline):
    model = other_contractors_bid
    extra = 1

class TenderAdmin(admin.ModelAdmin):
    inlines = [InlineContractors]
    list_display = (
        'tender_number',
        'tender_name',
        'tender_submission_date',
        'physical_submission_date',
        'tech_bid_opening_date',
        'bid_status',
        'prize_bid',
        )
    list_filter = (
        'tender_submission_date',
        'physical_submission_date',
        'tech_bid_opening_date',
        'bid_status',
        'prize_bid',
    )
    search_fields = (
        'tender_submission_date',
        'physical_submission_date',
        'tech_bid_opening_date',
        'bid_status',
        'prize_bid',
    )


admin.site.register(Tender,TenderAdmin)
admin.site.unregister(Group)
admin.site.register(other_contractors_bid)