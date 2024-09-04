from django.contrib import admin
from .models import Articles, Author, Tag, Quote


admin.site.register(Articles)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Quote)

