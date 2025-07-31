from django.contrib import admin


from .models import Author, Post, Tag


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("surname",)
    list_display = ("name", "surname",)


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author",)
    list_display = ("title", "author", "created_at",)


class TagAdmin(admin.ModelAdmin):
    list_filter = ("caption",)
    list_display = ("caption",)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)