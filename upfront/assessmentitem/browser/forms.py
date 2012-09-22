from five import grok

from zope.interface import Interface
from zope.component.hooks import getSite

from plone.directives import dexterity
from plone.dexterity.utils import createContentInContainer
from z3c.form import form, button

from Acquisition import aq_inner
from Products.statusmessages.interfaces import IStatusMessage

from upfront.assessmentitem import MessageFactory as _
from upfront.assessmentitem.content.assessmentitem import IAssessmentItem

from upfront.assessmentitem.interfaces import IUpfrontAssessmentItemLayer

grok.templatedir('templates')
grok.layer(IUpfrontAssessmentItemLayer)

class AssessmentItemAddForm(dexterity.AddForm):
    grok.name('upfront.assessmentitem.content.assessmentitem')
    grok.template('add-assessmentitem')
    grok.layer(IUpfrontAssessmentItemLayer)

    # clear the label
    label = ''

    formname = 'add-assessmentitem-form'
    kssformname = "kssattr-formname-++add++\
                   upfront.assessmentitem.content.assessmentitem"

    @button.buttonAndHandler(_('Save'), name='save')
    def handleAdd(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        obj = self.createAndAdd(data)
        if obj is not None:
            # mark only as finished if we get the new object
            self._finishedAdd = True
            IStatusMessage(self.request).addStatusMessage(
                _(u"Item created"), "info")

        # acquisition wrap object
        obj = self.context._getOb(obj.id)

        # group answer data on request by key
        data = {}

        for key in self.request.keys():
            if not key.startswith('form.widgets.answer'):
                continue
            answerid, fieldname = key.split('-')
            data.setdefault(answerid, {})
            fieldset = data.get(answerid)
            fieldset[fieldname] = self.request.get(key)

        # sort the keys to preserve order
        keys = data.keys()
        keys.sort()

        # create answers
        for key in keys:
            values = data[key]
            createContentInContainer(
                obj,
                "upfront.assessmentitem.content.answer",
                **values
                )


class QuestionEditForm(dexterity.EditForm):
    grok.name('edit')
    grok.context(IAssessmentItem)
    grok.template('edit-assessmentitem')

    formname = 'edit-assessmentitem-form'
    kssformname = "kssattr-formname-@@edit"


class AnswerForm(grok.View):
    grok.name('upfront.assessmentitem.answerform')
    grok.context(Interface)
    grok.template('answerform')

    def update(self):
        self.answerid = self.request.get('answerid')
        self.answerfieldname = 'form.widgets.%s-answer' % self.answerid
        self.iscorrectfieldname = 'form.widgets.%s-iscorrect' % self.answerid
        self.content = self.request.get('content', '')
        self.rows = self.request.get('rows', 5)
        self.cols = self.request.get('cols', 60)
