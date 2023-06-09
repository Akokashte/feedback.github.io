from django.contrib import admin

from home.models import Feedback,Contact,AcademicForm, TheoryFeedback, PracticalFeedback,Practical, ParentsFeedback,AlumniFeedback

# Register your models here before executing makemigrations command.
admin.site.register(Feedback)
admin.site.register(Contact)
admin.site.register(AcademicForm)
admin.site.register(TheoryFeedback)
admin.site.register(PracticalFeedback)
admin.site.register(Practical)
admin.site.register(ParentsFeedback)
admin.site.register(AlumniFeedback)