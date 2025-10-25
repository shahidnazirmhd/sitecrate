from django.contrib import admin
from django.utils.html import format_html


from .models import Author, Post, Tag, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("surname",)
    list_display = ("name", "surname",)


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at_local", "updated_at_local", "created_at", "updated_at",)
    list_filter = ("author",)
    list_display = ("title", "author", "created_at_local",)

    def created_at_local(self, obj):
        return format_html(
            '<time class="utc" datetime="{}">{}</time>',
            obj.created_at.isoformat(),
            obj.created_at.strftime('%Y-%m-%d %H:%M UTC')
        )
    created_at_local.short_description = 'Created (LocalTime)'

    def updated_at_local(self, obj):
        return format_html(
            '<time class="utc" datetime="{}">{}</time>',
            obj.updated_at.isoformat(),
            obj.updated_at.strftime('%Y-%m-%d %H:%M UTC')
        )
    updated_at_local.short_description = 'Updated (LocalTime)'

    class Media:
        js = ('js/config/app.js',)


class TagAdmin(admin.ModelAdmin):
    list_filter = ("caption",)
    list_display = ("caption",)


class CommentAdmin(admin.ModelAdmin):
    list_filter = ("post",)
    list_display = ("user_name", "post",)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)