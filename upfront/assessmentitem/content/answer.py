from five import grok

from zope import schema

from plone.directives import dexterity, form
from plone.app.textfield import RichText

from upfront.assessmentitem import MessageFactory as _

class IAnswer(form.Schema):
    """
    Answer content type
    """

    answer = RichText(
            title=_(u"Answer")
        )

    iscorrect = schema.Bool(
            title=_(u"is correct?"),
            default=False,
        )        

class Answer(dexterity.Item):
    grok.implements(IAnswer)
