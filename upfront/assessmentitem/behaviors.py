from zope.interface import alsoProvides
from zope import schema

from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider

from upfront.assessmentitem import MessageFactory as _

class IMarks(form.Schema):
    """ Behavior that enables the setting of marks.
    """

    marks = schema.Int(
            title=_(u"Marks"),
            required=False,
        )

class IResponseTime(form.Schema):
    """ Behavior that enables the setting of response time.
    """

    responsetime = schema.Int(
            title=_(u"Response Time"),
            required=False,
        )

# Mark these interfaces as form field providers
alsoProvides(IMarks, IFormFieldProvider)
alsoProvides(IResponseTime, IFormFieldProvider)

