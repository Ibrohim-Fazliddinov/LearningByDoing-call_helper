from django.contrib import admin
from django.contrib.admin import TabularInline
from organithations.models import groups, organisations, dicts


# region ----------------------------------- INLINES -----------------------
class EmployeeInline(TabularInline):
    model = organisations.Employee
    fields = ('user', 'position', 'date_joined',)


class MemberInline(TabularInline):
    model = groups.Member
    fields = ('user', 'date_joined',)

# endregion ------------------------------------------------------------------

# region ----------------------------------- MODELS --------------------------


@admin.register(dicts.Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active',)


@admin.register(organisations.Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director',)
    inlines = (EmployeeInline,)


@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', 'min_active',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    inlines = (MemberInline,)

# endregion ------------------------------------------------------------------
