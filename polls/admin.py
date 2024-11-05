from django.contrib import admin
from django import forms
from django.db import models
from myapp.models import Person
from .models import Author, Editor, Reader, Question, Choice
from myproject.admin_site import custom_admin_site
from myapp.widgets import RichTextEditorWidget
from django.utils.html import format_html

class ChoiceInline(admin.StackedInline):  # Choose Stacked or Tabular
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

@admin.register(Author, site=custom_admin_site)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "view_birth_date"]

    @admin.display(empty_value="???")
    def view_birth_date(self, obj):
        return obj.birth_date

class FlatPageAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ["url", "title", "content", "sites"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["registration_required", "template_name"],
            },
        ),
    ]

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    birthday = models.DateField()
    
    @admin.display(boolean=True)
    def born_in_fifties(self):
        return 1950 <= self.birthday.year < 1960

    @admin.display
    def colored_name(self):
        return format_html(
            '<span style="color: #{};">{} {}</span>',
            self.color_code,
            self.first_name,
            self.last_name,
        )

class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "born_in_fifties"]
class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": RichTextEditorWidget},
    }

# Registering all the admin classes
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Person, PersonAdmin)
admin.site.register(MyModel, MyModelAdmin)
admin.site.empty_value_display = "(None)"