from django.contrib import admin
from .models import RasoVarity, RasoReview, Store, RasoCertificate

# Register your models here.
class RasoReviewInline(admin.TabularInline):
    model = RasoReview
    extra = 2

class RasoVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_addes')
    inlines = [RasoReviewInline]


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('raso_varity',)

class RasoCertificateAdmin(admin.ModelAdmin):
    list_display = ('raso', 'certificate_number', 'issue_date', 'valid_untill')    


admin.site.register(RasoVarity, RasoVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(RasoCertificate, RasoCertificateAdmin)
