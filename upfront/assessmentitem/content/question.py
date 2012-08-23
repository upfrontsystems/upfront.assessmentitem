from five import grok

from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from z3c.form.browser.radio import RadioFieldWidget
from plone.app.textfield import RichText

from plone.directives import dexterity, form
from plone.app.textfield import RichText

from upfront.assessmentitem import MessageFactory as _

QUESTION_TYPE = SimpleVocabulary(
    [SimpleTerm(value=u'freeform',
                title=_(u'Free-form')),
     SimpleTerm(value=u'multiplechoice',
                title=_(u'Multiple Choice'))]
    )

class IQuestion(form.Schema):
    """
    Question content type
    """

    question = RichText(
            title=_(u"Question")
        )

    form.widget(questiontype=RadioFieldWidget)
    questiontype = schema.Choice(
            title=_(u"Question type"),
            vocabulary=QUESTION_TYPE,
        )

class Question(dexterity.Container):
    grok.implements(IQuestion)
