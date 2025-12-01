from django.contrib import admin

from .models import Project, Transaction, UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'theme', 'created_at')
    list_filter = ('theme',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')
    list_filter = ('owner',)
    search_fields = ('name', 'description')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'amount', 'category', 'customer_name', 'project', 'date')
    list_filter = ('date', 'category', 'project')
    search_fields = ('item_name', 'customer_name')
