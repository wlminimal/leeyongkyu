from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from wagtail.core.models import Page


class BaseSnippetClass(models.Model):
    sermon_scripture = models.TextField(default="설교 본문")
    sermon_title = models.TextField(default="설교 제목")
    sermon_link = models.URLField(default="https://leeyongkyu.s3-us-west-1.amazonaws.com/")

    panels = [
        FieldPanel('sermon_scripture'),
        FieldPanel('sermon_title'),
        FieldPanel('sermon_link'),
    ]

    def __str__(self):
        return self.sermon_title

    class Meta:
        abstract = True


@register_snippet
class Genesis(BaseSnippetClass):
    pass

@register_snippet
class Exodus(BaseSnippetClass):
    pass



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

class SermonsByScriptureSubpage(Page):
    pass