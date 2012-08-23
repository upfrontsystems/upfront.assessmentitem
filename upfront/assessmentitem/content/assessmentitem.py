from five import grok
from zope import schema
from plone.directives import dexterity, form
from plone.app.textfield import RichText

from upfront.assessmentitem import MessageFactory as _

class IAssessmentItem(form.Schema):
    """
    Assessment Item content type
    """

    introduction = RichText(
            title=_(u"Introduction"),
            required=False,
        )

class AssessmentItem(dexterity.Container):
    grok.implements(IAssessmentItem)

