from operator import attrgetter

from z3c.form.browser.multi import MultiWidget

import zope.interface
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

from z3c.form.i18n import MessageFactory as _
from z3c.form import interfaces
from z3c.form import widget
from z3c.form import button

class IAnswersWidget(interfaces.IWidget):
    """ Better multi widget for answers
    """


class AnswersWidget(MultiWidget):
    """Answers widget implementation."""

    zope.interface.implements(IAnswersWidget)

    input_template = ViewPageTemplateFile(
        "templates/answerswidget_input.pt")

    display_template = ViewPageTemplateFile(
        "templates/answerswidget_display.pt")

    def render(self):
        """ widgetTemplate registrations in answerswidget.zcml is not
            working so force the widget templates that must be used here
        """
        if self.mode == interfaces.INPUT_MODE:
            # Enforce template and do not query it from the widget
            # template factory 
            self.template = self.input_template
        elif self.mode == interfaces.DISPLAY_MODE:
            self.template = self.display_template
        return MultiWidget.render(self)

    def updateActions(self):
        """ Add remove button for each answer """
        MultiWidget.updateActions(self)
        for widget in self.widgets:
            key = '%s.remove' % widget.name
            if key in self.buttons.keys():
                continue
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

