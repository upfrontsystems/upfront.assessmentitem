from five import grok
from zope import schema
from Acquisition import aq_inner

from plone.directives import dexterity, form
from plone.app.textfield import RichText

from Products.CMFCore.utils import getToolByName

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

grok.templatedir('templates')
class View(dexterity.DisplayForm):
    grok.context(IAssessmentItem)
    grok.template('viewassessmentitem')
    grok.require('zope2.View')

    def assessment_item(self):
        """ return contents of assessment item (introduction field)
        """
        return self.context.introduction.output

    def questions(self):
        """ return all question objects in the context of assessment item
        """
        contentFilter = {
                        'portal_type':'upfront.assessmentitem.content.question'}
        questions = self.context.getFolderContents(contentFilter)
        return questions

    def marks_string(self,mark):
        """ return mark or marks depending if number of marks is > 1 or not
        """
        if int(mark) > 1:
            return 'marks'
        else:
            return 'mark'

