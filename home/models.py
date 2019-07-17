from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from wagtail.core.models import Page


class HomePage(Page):
    header_text1 = models.TextField(default="故 이용규 목사")
    header_text2 = models.TextField(default="설교 모음집")

    paragraph1 = models.TextField(default="총 42권")
    paragraph2 = RichTextField(default="故 이용규 목사 유작 ( 遺作 ) 성경강해 설교집 총 42권")

    button_text = models.TextField(default="설교집 바로가기")

    content_panels = Page.content_panels + [
        FieldPanel('header_text1'),
        FieldPanel('header_text2'),

        FieldPanel('paragraph1'),
        FieldPanel('paragraph2'),

        FieldPanel('button_text'),
    ]

class ProfilePage(Page):
    pass

class SermonsByNumberPage(Page):
    pass

class SermonsByScripturePage(Page):
    pass

class SermonsOnScripture(Page):
    pass

class TheologySeries(Page):
    pass