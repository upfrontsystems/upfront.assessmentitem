from five import grok
from zope import schema
from Acquisition import aq_inner

from plone.directives import dexterity, form
from plone.app.textfield import RichText

from Products.CMFCore.utils import getToolByName

from upfront.assessmentitem import MessageFactory as _

class IAssessmentItemContainer(form.Schema):
    """
    Assessment Item content type
    """

    introduction = RichText(
            title=_(u"Introduction"),
            required=False,
        )

class AssessmentItemContainer(dexterity.Container):
    grok.implements(IAssessmentItemContainer)

grok.templatedir('templates')
class View(dexterity.DisplayForm):
    grok.context(IAssessmentItemContainer)
    grok.template('assessmentitem-container-view')
    grok.require('zope2.View')

    def assessmentitems(self):
        """ return all assessment items in the container
        """
        contentFilter = {
            'portal_type':'upfront.assessmentitem.content.assessmentitem'
            }
        return self.context.getFolderContents(contentFilter, full_objects=True)

    def marks_string(self, mark):
        """ return mark or marks depending if number of marks is > 1 or not
        """
        if int(mark) > 1:
            return 'marks'
        else:
            return 'mark'

class EditForm(dexterity.EditForm):
    grok.context(IAssessmentItemContainer)
    grok.template('assessmentitem-container-edit')
