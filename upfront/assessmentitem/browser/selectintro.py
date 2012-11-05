from zope.interface import Interface
from five import grok

from Products.CMFCore.utils import getToolByName

grok.templatedir('templates')

class SelectIntro(grok.View):
    """ View for questions folder
    """
    grok.context(Interface)
    grok.name('selectintro')
    grok.template('selectintro')
    grok.require('cmf.AddPortalContent')

    def intros(self):
        """ Return all the introductions in the catalog
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        return catalog(portal_type='upfront.assessmentitem.content.introtext')


