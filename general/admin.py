from django.contrib import admin
from .models import Element, Category


class ElementAdmin(admin.ModelAdmin):
    fieldsets = [
        ("title", {"fields": ["title"]}),
        ("content", {"fields": ["content"]}),
        ("category", {"fields": ["category"]}),
        ("slide_num", {"fields": ["slide_num"]}),
    ]


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ("name", {"fields": ["name"]}),
    ]

admin.site.register(Element, ElementAdmin)
admin.site.register(Category, CategoryAdmin)
