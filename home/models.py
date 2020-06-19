from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from streams import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import(
    StreamFieldPanel,
    MultiFieldPanel
) 
from wagtail.images.models import Image
from wagtail.contrib.settings.models import BaseSetting, register_setting

class HomePage(Page):
    """Home page model."""

    template = "home/home_page.html"
    max_count = 1

    body = StreamField(
        [ 
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()), 
        ], 
        null=True,
        blank=True,
    )     

    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_subtitle = RichTextField(blank=True, features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
   )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta"),
        StreamFieldPanel('body'),
    ]

    class Meta:

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

@register_setting
class SiteSettings(BaseSetting):
    logo = models.OneToOneField(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Business Logo')
    panels = [
        ImageChooserPanel('logo')
    ]
@register_setting
class SocialMediaSettings(BaseSetting):
    """Social media settings for our custom website."""

    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    youtube = models.URLField(blank=True, null=True, help_text="YouTube Channel URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("youtube"),
        ], heading="Social Media Settings")
    ]