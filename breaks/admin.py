from django.contrib import admin
from django.contrib.admin import TabularInline
from breaks.models import organisations, groups, replacements, dicts, breaks
from django.urls import reverse
from django.utils.html import format_html


# region ----------------------------------- INLINES -------------------------------------------------
class ReplacementEmployeeInline(TabularInline):
    model = replacements.ReplacementEmployee
    fields = ('employee', 'status',)


# endregion ---------------------------------------------------------------------------------------


# region ----------------------------------- MODELS -------------------------------------------------

@admin.register(organisations.Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director',)


@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', 'min_active',)


@admin.register(replacements.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'data', 'break_start',
                    'break_end', 'break_max_duration')
    inlines = (ReplacementEmployeeInline,)


@admin.register(breaks.Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'replacement_link', 'break_start', 'break_end', 'status',
    )
    list_filter = ('status',)
    empty_value_display = 'Unknown'
    radio_fields = {'status': admin.VERTICAL}

    def replacement_link(self, obj):
        link = reverse(
            'admin:breaks_replacement_change', args=[obj.replacement.id]
        )
        return format_html('<a href="{}">{}</a>', link, obj.replacement)


@admin.register(dicts.ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active',)


@admin.register(dicts.BreakStatus)
class BreakStatusAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'name', 'sort', 'is_active',
    )

# endregion ---------------------------------------------------------------------------------------
