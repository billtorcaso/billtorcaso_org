""" The HOMEPAGE model for billtorcaso.org """

from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
)
from wagtail.core.fields import StreamField
from wagtail.core.models import Page



class HomePage(Page):
    """ For billtorcaso.org """
    pass

###    body = StreamField(
###        BaseStreamBlock(),
###        verbose_name="Page body",
###        blank=True
###    )
###    content_panels = Page.content_panels + [
###        StreamFieldPanel('body'),
###    ]
###
###
