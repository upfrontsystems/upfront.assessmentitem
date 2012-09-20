from five import grok

from zope.interface import Interface
from zope.component.hooks import getSite

from plone.directives import dexterity
from z3c.form import form, button

from Acquisition import aq_inner

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
        super(AssessmentItemAddForm, self).handleAdd(self, action)
    

class QuestionEditForm(dexterity.EditForm):
    grok.name('edit')
    grok.context(IAssessmentItem)
    grok.template('edit-assessmentitem')

    formname = 'edit-assessmentitem-form'
    kssformname = "kssattr-formname-@@edit"


class TinyMCEWidget(grok.View):
    grok.name('tinymce')
    grok.context(Interface)
    grok.template('tinymce')

    def update(self):
        self.fieldname = self.request.get('fieldname')
        self.content = self.request.get('content', '')
        self.rows = self.request.get('rows', 5)
        self.cols = self.request.get('cols', 60)
