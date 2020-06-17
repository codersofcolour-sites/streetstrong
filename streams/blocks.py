from wagtail.core import blocks


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
        label = "Full RichText"