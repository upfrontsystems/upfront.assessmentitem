from zope import schema
from zope.interface import Interface
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from five import grok
from plone.directives import dexterity, form
from plone.dexterity.utils import createContentInContainer
from plone.app.textfield import RichText
from z3c.form.browser.radio import RadioFieldWidget
from z3c.form import button

from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage

from upfront.assessmentitem import MessageFactory as _

QUESTION_TYPE = SimpleVocabulary(
    [SimpleTerm(value=u'freeform',
                title=_(u'Free-form')),
     SimpleTerm(value=u'multiplechoice',
                title=_(u'Multiple Choice'))]
    )

class IAssessmentItem(form.Schema):
    """
    Assessment Item content type
    """

    question = RichText(
            title=_(u"Question")
        )

    form.widget(questiontype=RadioFieldWidget)
    questiontype = schema.Choice(
            title=_(u"Question type"),
            vocabulary=QUESTION_TYPE,
        )


class AssessmentItem(dexterity.Container):
    grok.implements(IAssessmentItem)


grok.templatedir('templates')

class AssessmentItemAddForm(dexterity.AddForm):
    grok.name('upfront.assessmentitem.content.assessmentitem')
    grok.template('assessmentitem-add')

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


class AssessmentItemEditForm(dexterity.EditForm):
    grok.name('edit')
    grok.context(IAssessmentItem)
    grok.template('assessmentitem-edit')


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
