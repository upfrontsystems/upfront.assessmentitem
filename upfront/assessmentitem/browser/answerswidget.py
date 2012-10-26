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

    def updateActions(self):
        """ Add remove button for each answer """
        MultiWidget.updateActions(self)
        for widget in self.widgets:
            but = button.Button('%s.remove' % widget.name,
                                title=u'Remove Answer')
            self.buttons += button.Buttons(but)

            handler = button.Handler(but, self.__class__.handleRemove)
            self.handlers.addHandler(but, handler)
        self.actions.update()

    @button.buttonAndHandler(_('Add Answer'), name='add',
                             condition=attrgetter('allowAdding'))
    def handleAdd(self, action):
        self.appendAddingWidget()

    def handleRemove(self, action):
        wlist = []
        for widget in self.widgets:
            key = '%s.buttons.%s.remove' % (self.name, widget.name)
            if key in self.request:
                field_name = action.field.getName()
                del self.actions[field_name]
                del self.buttons[field_name]
            else:
                wlist.append(widget)
        self.widgets = wlist
        self.value = [widget.value for widget in self.widgets]

@zope.interface.implementer(interfaces.IFieldWidget)
def answersFieldWidgetFactory(field, request):
    """IFieldWidget factory for AnswersWidget."""
    return widget.FieldWidget(field, AnswersWidget(request))


@zope.interface.implementer(interfaces.IFieldWidget)
def AnswersFieldWidget(field, request):
    """IFieldWidget factory for AnswersWidget."""
    return answersFieldWidgetFactory(field, request)

