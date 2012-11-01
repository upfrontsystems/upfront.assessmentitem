from five import grok
from plone.directives import dexterity, form
from plone.app.textfield import RichText

from Products.CMFCore.utils import getToolByName

from upfront.assessmentitem import MessageFactory as _

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
