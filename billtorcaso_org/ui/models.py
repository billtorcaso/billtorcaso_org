from django.db import models

from django.core.exceptions import ValidationError

from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    ChoiceBlock,
    DateBlock,
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    URLBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

class HomepageBannerBlock(StructBlock):
    """
    A HomepageBannerBlock presents the content of the 'homepage hero' widget.
    """

    image = ImageChooserBlock(required=True)
    photo_credit = CharBlock(required=False)
    title = CharBlock(required=True)
    summary = TextBlock(required=True)
    url = LinkBlock()
    is_emergency = BooleanBlock(required=False)

    class Meta:
        template = "includes/blocks/homepage_banner_block.html"

class MediaGalleryImageItem(StructBlock):
    """This utility class is for use by MediaGalleryBlock."""
    image = ImageChooserBlock()
    caption = TextBlock()
    credit = TextBlock()

    class Meta:
        icon ='image'

class MediaGalleryVideoItem(StructBlock):
    """This utility class is for use by MediaGalleryBlock."""
    video = EmbedBlock()
    thumbnail = ImageChooserBlock()
    caption = TextBlock()
    credit = TextBlock()

    class Meta:
        icon ='media'


class MediaGalleryBlock(StructBlock):
    """
    """
    title = TextBlock()
    description = TextBlock()
    gallery = StreamBlock([
        ('image_item',MediaGalleryImageItem()),
        ('video_item', MediaGalleryVideoItem())
    ])

    class Meta:
        template = "includes/blocks/media_gallery.html"


class MediaChooserBlock(StructBlock):
    image = ImageChooserBlock(required=False)
    video = EmbedBlock(required=False)

    def get_context(self, value, **kwargs):
        # assert: exactly one of image and video is truthy
        context = super().get_context(value, **kwargs)

        image = value.get('image')
        video = value.get('video')

        if image:
            context['media'] = image 
            context['media_type'] = 'image'
        elif video:
            context['media'] = video 
            context['media_type'] = 'video'
        else:
            raise ValueError("MediaChooserBlock has neither 'image' nor 'video'.  Get help!")

        return context

    def clean(self, value):
        # assert: exactly one of image and video is truthy
        if all((value['image'], value['video'])) or not any((value['image'], value['video'])):
            error_messages = ["MediaChooserBlock must have exactly one of {image, video}"]
            raise ValidationError(
                "Validation error in MediaChooserBlock",
                params={block_name: error_messages for block_name in ['image', 'video']},
            )

        return super().clean(value)


    class Meta:
        template = "includes/blocks/media_chooser_block.html"

        
