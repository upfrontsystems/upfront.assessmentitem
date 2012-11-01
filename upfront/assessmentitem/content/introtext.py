import json

from zope.component import getUtility

from five import grok
from plone.directives import dexterity, form
from plone.dexterity.utils import addContentToContainer
from plone.dexterity.interfaces import IDexterityFTI
from plone.app.textfield import RichText
from plone.uuid.interfaces import IUUID

from Acquisition import aq_inner
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

class AddForm(dexterity.AddForm):
    """ Custom add form to specialise behaviour for ajax load
    """
    grok.name('upfront.assessmentitem.content.introtext')

    def add(self, object):
        """ override method in base class so that we can assign to
            self.new_object for use in render
        """
        fti = getUtility(IDexterityFTI, name=self.portal_type)
        container = aq_inner(self.context)
        self.new_object = addContentToContainer(container, object)

        if self.request.has_key('ajax_load'):
            self.immediate_view = "%s/%s/@@json" % (container.absolute_url(),
                                                    self.new_object.id)
        elif fti.immediate_view:
            self.immediate_view = "%s/%s/%s" % (container.absolute_url(),
                                                self.new_object.id,
                                                fti.immediate_view,)
        else:
            self.immediate_view = "%s/%s" % (container.absolute_url(),
                                             self.new_object.id)


class JSONView(grok.View):
    grok.name('json')
    grok.context(IIntroText)
    grok.require('zope2.View')

    def render(self):
        return json.dumps({'uid': IUUID(self.context)})
