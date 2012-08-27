from five import grok

from zope.component.hooks import getSite

from plone.directives import dexterity
from z3c.form import form, button

from Acquisition import aq_inner

from upfront.assessmentitem import MessageFactory as _
from upfront.assessmentitem.content.question import IQuestion

from upfront.assessmentitem.interfaces import IUpfrontAssessmentItemLayer

grok.templatedir('templates')
grok.layer(IUpfrontAssessmentItemLayer)

class QuestionAddForm(dexterity.AddForm):
    grok.name('upfront.assessmentitem.content.question')
    grok.template('addquestion')
    grok.layer(IUpfrontAssessmentItemLayer)

    # clear the label
    label = ''

    formname = 'add-question-form'
    kssformname = "kssattr-formname-++add++\
                   upfront.assessmentitem.content.question"

class QuestionEditForm(dexterity.EditForm):
    grok.name('edit')
    grok.context(IQuestion)
    grok.template('editquestion')

    formname = 'edit-question-form'
    kssformname = "kssattr-formname-@@edit"


