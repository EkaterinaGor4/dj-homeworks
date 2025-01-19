from django.contrib import admin

from .models import Article, Tag, ArticleTags

class ArticleTagInLine(admin.TabularInLine):
    model = ArticleTags
    fields = ["tag", "is_main"]
    formset =ArticleTagInLineFormSet

class ArticleTagInlineFormSet(BaseInlineFormSet):
    def clean(selfself):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get("is_main"):
                count += 1
            if count > 1:
                raise ValidationError('Только один тег может быть основным')
            if count == 0:
                raise ValidationError('Хотя бы один тег должен быть основным')
        return super().clean()


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    list_filter = ['title']
    inlines = [ArticleTagInLines]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
