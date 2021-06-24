from django.contrib import admin

# my imports
from articles.models import Article, Comment

# my classes


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


# registering my model
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)

