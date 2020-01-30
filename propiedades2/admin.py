from django.contrib import admin
from propiedades2.models import Acquisition, DocumentEx, DocumentCip, DocumentCn, DocumentBlue, DocumentBuildP, \
    DocumentMR, DocumentTypeC, DocumentOther, DocumentWR, DocumentDC, DocumentPH, DocumentDB, DocumentAc, DocumentEs, \
    Location,ArchitectureRecordAcq, InternalAccountantsAcq, NotaryAcquisition, SiiRecord, Rent, Post, Staff, Region, Property, Change_property, \
    Comment, Stats, District, Notification
from reversion.admin import VersionAdmin

# Register your models here.
admin.site.register(Location)
admin.site.register(Acquisition)
admin.site.register(ArchitectureRecordAcq)
admin.site.register(InternalAccountantsAcq)
admin.site.register(NotaryAcquisition)
admin.site.register(SiiRecord)
admin.site.register(DocumentEx)
admin.site.register(DocumentCip)
admin.site.register(DocumentCn)
admin.site.register(DocumentBlue)
admin.site.register(DocumentBuildP)
admin.site.register(DocumentMR)
admin.site.register(DocumentTypeC)
admin.site.register(DocumentOther)
admin.site.register(DocumentWR)
admin.site.register(DocumentDC)
admin.site.register(DocumentPH)
admin.site.register(DocumentDB)
admin.site.register(DocumentAc)
admin.site.register(DocumentEs)
admin.site.register(Post)
admin.site.register(Rent)
admin.site.register(Staff)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Change_property)
admin.site.unregister(Change_property)
admin.site.unregister(Location)
admin.site.unregister(Acquisition)
admin.site.unregister(ArchitectureRecordAcq)
admin.site.unregister(InternalAccountantsAcq)
admin.site.unregister(NotaryAcquisition)
admin.site.unregister(SiiRecord)
admin.site.unregister(DocumentEx)
admin.site.unregister(DocumentCip)
admin.site.unregister(DocumentCn)
admin.site.unregister(DocumentBlue)
admin.site.unregister(DocumentBuildP)
admin.site.unregister(DocumentMR)
admin.site.unregister(DocumentTypeC)
admin.site.unregister(DocumentOther)
admin.site.unregister(DocumentWR)
admin.site.unregister(DocumentDC)
admin.site.unregister(DocumentPH)
admin.site.unregister(DocumentDB)
admin.site.unregister(DocumentAc)
admin.site.unregister(DocumentEs)
admin.site.unregister(Post)
admin.site.unregister(Rent)
admin.site.unregister(Staff)
admin.site.unregister(Region)
admin.site.register(Property)
admin.site.unregister(Property)
admin.site.unregister(District)
@admin.register(Property)
class PropertyAdmin(VersionAdmin):
    pass
@admin.register(Location)
class LocationAdmin(VersionAdmin):
    pass
@admin.register(Acquisition)
class AcquisitionAdmin(VersionAdmin):
    pass
@admin.register(ArchitectureRecordAcq)
class ArchitectureRecordAcqAdmin(VersionAdmin):
    pass
@admin.register(InternalAccountantsAcq)
class InternalAccountantsAcqAdmin(VersionAdmin):
    pass
@admin.register(NotaryAcquisition)
class NotaryAcquisitionAdmin(VersionAdmin):
    pass
@admin.register(SiiRecord)
class SiiRecordAdmin(VersionAdmin):
    pass
@admin.register(DocumentEx)
class DocumentExAdmin(VersionAdmin):
    pass
@admin.register(DocumentCip)
class DocumentCipAdmin(VersionAdmin):
    pass
@admin.register(DocumentCn)
class DocumentCnAdmin(VersionAdmin):
    pass
@admin.register(DocumentBlue)
class DocumentBlueAdmin(VersionAdmin):
    pass
@admin.register(DocumentBuildP)
class DocumentBuildPAdmin(VersionAdmin):
    pass
@admin.register(DocumentMR)
class DocumentMRAdmin(VersionAdmin):
    pass
@admin.register(DocumentTypeC)
class DocumentTypeCAdmin(VersionAdmin):
    pass
@admin.register(DocumentOther)
class DocumentOtherAdmin(VersionAdmin):
    pass
@admin.register(DocumentWR)
class DocumentWRAdmin(VersionAdmin):
    pass
@admin.register(DocumentDC)
class DocumentDCAdmin(VersionAdmin):
    pass
@admin.register(DocumentPH)
class DocumentPHAdmin(VersionAdmin):
    pass
@admin.register(DocumentDB)
class DocumentDBAdmin(VersionAdmin):
    pass
@admin.register(DocumentAc)
class DocumentAcAdmin(VersionAdmin):
    pass
@admin.register(DocumentEs)
class DocumentEsAdmin(VersionAdmin):
    pass
@admin.register(Post)
class PostAdmin(VersionAdmin):
    pass
@admin.register(Rent)
class RentAdmin(VersionAdmin):
    pass
@admin.register(Staff)
class StaffAdmin(VersionAdmin):
    pass
@admin.register(Region)
class RegionAdmin(VersionAdmin):
    pass
@admin.register(Change_property)
class Change_propertyAdmin(VersionAdmin):
    pass
@admin.register(Comment)
class CommentAdmin(VersionAdmin):
    pass
@admin.register(Stats)
class StatsAdmin(VersionAdmin):
    pass
@admin.register(District)
class DistrictAdmin(VersionAdmin):
    pass

@admin.register(Notification)
class NotificationAdmin(VersionAdmin):
    pass