from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=100)),
                ("text", blocks.TextBlock(required=True, max_length=300)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first"))
            ]
        )
    )

    class Meta: # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Cards"


class RichtextBlock(blocks.RichTextBlock):

    class Meta: # noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"

class SimpleRichtextBlock(blocks.RichTextBlock):

    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]

    class Meta: # noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"