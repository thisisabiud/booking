# reservations/admin.py
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from reservations.models import Booking, Contact, Booth, Event

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('company', 'contact', 'email', 'phone', 'created_at', 'total_bookings')
    list_filter = ('created_at', 'company')
    search_fields = ('company', 'contact', 'email', 'phone')
    readonly_fields = ('created_at',)
    
    def total_bookings(self, obj):
        return obj.bookings.count()
    total_bookings.short_description = 'Total Bookings'

class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0
    readonly_fields = ('created_at',)
    can_delete = True
    show_change_link = True

class BoothInline(admin.TabularInline):
    model = Booth
    extra = 1
    fields = ('booth_number', 'booth_type', 'status', 'reserved_by')
    raw_id_fields = ('reserved_by',)
    show_change_link = True

@admin.register(Booth)
class BoothAdmin(admin.ModelAdmin):
    list_display = ('booth_number', 'event_link', 'booth_type', 'status', 'reserved_by', 'created_at')
    list_filter = ('status', 'booth_type', 'event')
    search_fields = ('booth_number', 'event__title', 'reserved_by__company')
    raw_id_fields = ('reserved_by',)
    readonly_fields = ('created_at', 'updated_at')
    list_select_related = ('event', 'reserved_by')
    
    def event_link(self, obj):
        url = reverse('admin:reservations_event_change', args=[obj.event.id])
        return format_html('<a href="{}">{}</a>', url, obj.event.title)
    event_link.short_description = 'Event'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('event', 'reserved_by')

from django.contrib import admin

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'booth_info', 'contact_info', 'is_confirmed', 'created_at')
    list_filter = ('created_at', 'booth__event', 'booth__status', 'is_confirmed')
    search_fields = ('booth__booth_number', 'contact__company', 'contact__email')
    raw_id_fields = ('booth', 'contact')
    readonly_fields = ('created_at', 'updated_at')

    def booth_info(self, obj):
        return f"{obj.booth.event.title} - Booth {obj.booth.booth_number}"
    booth_info.short_description = 'Booth'

    def contact_info(self, obj):
        return f"{obj.contact.company} ({obj.contact.contact})"
    contact_info.short_description = 'Contact'

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'location', 'is_active', 'total_booths', 'available_booths')
    list_filter = ('is_active', 'start_date', 'location')
    search_fields = ('title', 'description', 'location')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [BoothInline]
    date_hierarchy = 'start_date'
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Event Details', {
            'fields': ('start_date', 'end_date', 'location', 'is_active')
        }),
        ('System Fields', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    def total_booths(self, obj):
        return obj.booths.count()
    total_booths.short_description = 'Total Booths'
    
    def available_booths(self, obj):
        return obj.booths.filter(status='available').count()
    available_booths.short_description = 'Available Booths'
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('booths')

# Optional: Custom admin site configuration
class ReservationsAdminSite(admin.AdminSite):
    site_header = 'Event Reservations Administration'
    site_title = 'Event Reservations Admin'
    index_title = 'Event Reservations Management'

# Optional: Register with custom admin site
# admin_site = ReservationsAdminSite(name='reservations_admin')
# admin_site.register(Event, EventAdmin)
# admin_site.register(Booth, BoothAdmin)
# admin_site.register(Contact, ContactAdmin)
# admin_site.register(Booking, BookingAdmin)