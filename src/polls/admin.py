from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    """
    Add choices to admin
    """
    model = Choice
    extra = 2  # extra fields to ourt choices


class QuestionAdmin(admin.ModelAdmin):
    """
    Customize the admin
    """
    # divide admin form in groups
    fieldsets = [
        (None, {'fields': ['question_text']}),
        # section
        ('Fechas de publicación', {'fields': ['pub_date'],
                                   'classes': ['collapse']})  # collap. section
    ]
    # add class choices
    inlines = [ChoiceInline]

    # show individual model fields
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # side bar
    list_filter = ['pub_date']

    # searching
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
