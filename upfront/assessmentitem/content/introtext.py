from five import grok
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.uuid.interfaces import IUUID

from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName

from upfront.assessmentitem import MessageFactory as _

grok.templatedir('templates')

class IIntroText(form.Schema):
    """ Introduction to a set of related questions
    """

    introduction = RichText(
        title=_(u"Introduction")
    )

class IntroText(dexterity.Item):
    grok.implements(IIntroText)

    def Title(self):
        """ return the first 30 characters of the intro as title
        """
        if getattr(self, 'introduction', None):
            intro = self.introduction.output
            transforms = getToolByName(self, 'portal_transforms')
            intro = transforms.convertTo('text/plain', intro).getData().strip()
            return intro[:30] + ' ...'
        else:
            return ''

class View(dexterity.DisplayForm):
    """ Custom view of intro text that hides metadata in the page
    """
    grok.context(IIntroText)
    grok.require('zope2.View')
    grok.template('introtext-view')

    def uid(self):
        return IUUID(self.context)

    def path(self):
        return '/'.join(self.context.getPhysicalPath()) 
