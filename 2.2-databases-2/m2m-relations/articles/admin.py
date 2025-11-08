from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()

        main_count = 0
        has_forms = False

        for form in self.forms:
            if not form.cleaned_data or form.cleaned_data.get("DELETE"):
                continue
            has_forms = True
            if form.cleaned_data.get("is_main"):
                main_count += 1

        if not has_forms:
            raise ValidationError("У статьи должен быть хотя бы один раздел.")
        if main_count == 0:
            raise ValidationError("Должен быть ровно один основной раздел.")
        if main_count > 1:
            raise ValidationError("Основным может быть только один раздел.")


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormSet
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "published_at"]
    inlines = [ScopeInline]