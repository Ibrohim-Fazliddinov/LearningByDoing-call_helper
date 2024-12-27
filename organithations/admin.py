from django.contrib import admin
from django.contrib.admin import TabularInline, StackedInline
from organithations.models import groups, organisations, dicts
from breaks.models.replacements import GroupInfo

# region ----------------------------------- INLINES -----------------------


class EmployeeInline(TabularInline):
    model = organisations.Employee
    fields = ('user', 'position', 'date_joined',)


class MemberInline(TabularInline):
    model = groups.Member
    fields = ('user', 'date_joined',)


class ProfileBreakInline(StackedInline):
    model = GroupInfo
    fields = (
        'min_active',
        'break_start',
        'break_end',
        'break_max_duration')
# endregion ------------------------------------------------------------------

# region ----------------------------------- MODELS --------------------------


@admin.register(dicts.Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active',)


@admin.register(organisations.Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director',)
    inlines = (EmployeeInline,)
    readonly_fields = (
        'created_at',
        'created_by',
        'updated_at',
        'updated_by'
    )


@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    inlines = (MemberInline, ProfileBreakInline)
    readonly_fields = (
        'created_at',
        'created_by',
        'updated_at',
        'updated_by'
    )
# endregion ------------------------------------------------------------------
