from operator import attrgetter

from z3c.form.browser.multi import MultiWidget

import zope.interface

from z3c.form.i18n import MessageFactory as _
from z3c.form import interfaces
from z3c.form import widget
from z3c.form import button

class IAnswersWidget(interfaces.IWidget):
    """ Better multi widget for answers
    """


class AnswersWidget(MultiWidget):
    """Answers widget implementation."""

    @button.buttonAndHandler(_('Add'), name='add',
                             condition=attrgetter('allowAdding'))
    def handleAdd(self, action):
        self.appendAddingWidget()

    @button.buttonAndHandler(_('Remove selected'), name='remove',
                             condition=attrgetter('allowRemoving'))
    def handleRemove(self, action):
        self.widgets = [widget for widget in self.widgets
                        if ('%s.remove' % (widget.name)) not in self.request]
        self.value = [widget.value for widget in self.widgets]

@zope.interface.implementer(interfaces.IFieldWidget)
def answersFieldWidgetFactory(field, request):
    """IFieldWidget factory for AnswersWidget."""
    return widget.FieldWidget(field, AnswersWidget(request))


@zope.interface.implementer(interfaces.IFieldWidget)
def AnswersFieldWidget(field, request):
    """IFieldWidget factory for AnswersWidget."""
    return answersFieldWidgetFactory(field, request)

