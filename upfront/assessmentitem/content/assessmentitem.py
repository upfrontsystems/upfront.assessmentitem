from zope import schema
from zope.interface import Interface
from zope.interface import alsoProvides 
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from five import grok
from plone.directives import dexterity, form
from plone.dexterity.utils import createContentInContainer
from plone.app.textfield import RichText
from plone.formwidget.contenttree import ObjPathSourceBinder
from z3c.form.browser.radio import RadioFieldWidget
from z3c.form import button
from z3c.relationfield import RelationChoice

from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage

from upfront.assessmentitem import MessageFactory as _
from upfront.assessmentitem.content.answer import IAnswer
from upfront.assessmentitem.content.introtext import IIntroText
from upfront.assessmentitem.browser.introwidget import IntroFieldWidget
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

    form.widget(introduction=IntroFieldWidget)
    introduction = RelationChoice(
            title=_(u"Introduction"),
            description=_(u"A common introduction to a serious of "
                           "related questions, for example a poem "
                           "or image that are referred to by more than "
                           "one question"),
            source=ObjPathSourceBinder(
                object_provides=IIntroText.__identifier__),
            required=False,
        )

    question = RichText(
            title=_(u"Question")
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

class AssessmentItemEditForm(dexterity.EditForm):
    grok.name('edit')
    grok.context(IAssessmentItem)
    grok.template('assessmentitem-edit')
