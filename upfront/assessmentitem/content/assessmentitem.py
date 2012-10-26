from zope import schema
from zope.interface import Interface
from zope.interface import alsoProvides 
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
from upfront.assessmentitem.content.answer import IAnswer
from upfront.assessmentitem.browser.answerswidget import AnswersFieldWidget

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

    form.widget(answers=AnswersFieldWidget)
    answers = schema.List(
            title = u"Answers",
            value_type = schema.Object(
                title=u'Answer',
                schema=IAnswer),
            required = False,
        )

class AssessmentItem(dexterity.Container):
    grok.implements(IAssessmentItem)

    def answers(self):
        """ return all answers
        """
        contentFilter = {
            'portal_type':'upfront.assessmentitem.content.answer'
            }
        return self.getFolderContents(contentFilter, full_objects=True)


grok.templatedir('templates')

class IAnswersField(Interface):
    """ Marker interface for add form
    """

class AssessmentItemAddForm(dexterity.AddForm):
    grok.name('upfront.assessmentitem.content.assessmentitem')

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
        self.answerfieldname = \
            'form.widgets.answers.%s.widgets.answer' % self.answerid
        self.iscorrectfieldname = \
            'form.widgets.answers.%s.widgets.iscorrect' % self.answerid
        self.content = self.request.get('content', '')
        self.rows = self.request.get('rows', 5)
        self.cols = self.request.get('cols', 60)
