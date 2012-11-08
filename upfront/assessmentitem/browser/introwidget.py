from operator import attrgetter

from z3c.form.browser.multi import MultiWidget
from plone.formwidget.contenttree.widget import ContentTreeWidget

import zope.interface
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

from z3c.form.i18n import MessageFactory as _
from z3c.form import interfaces
from z3c.form import widget
from z3c.form import button

class IIntroWidget(interfaces.IWidget):
    """ Intro Widget
    """


class IntroWidget(ContentTreeWidget):
    """ Extend content tree widget """

    zope.interface.implements(IIntroWidget)

    input_template = ViewPageTemplateFile(
        "templates/introwidget_input.pt")

    # display_template = ViewPageTemplateFile(
    #     "templates/introwidget_display.pt")

    def render(self):
        if self.mode == interfaces.INPUT_MODE:
            return self.input_template(self)
        else:
            return ContentTreeWidget.render(self)


@zope.interface.implementer(interfaces.IFieldWidget)
def introFieldWidgetFactory(field, request):
    """IFieldWidget factory for IntroWidget."""
    return widget.FieldWidget(field, IntroWidget(request))


@zope.interface.implementer(interfaces.IFieldWidget)
def IntroFieldWidget(field, request):
    """IFieldWidget factory for IntroWidget."""
    return introFieldWidgetFactory(field, request)
