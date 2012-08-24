from zope.app.intid.interfaces import IIntIds
from zope.component import getUtility
from zope.interface import alsoProvides

from z3c.relationfield.relation import create_relation

from zope.component import queryMultiAdapter
from zope.viewlet.interfaces import IViewletManager

from Products.Five.browser import BrowserView as View

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
import unittest2 as unittest
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from plone.testing import z2

PROJECTNAME = "upfront.assessmentitem"

class TestCase(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import upfront.assessmentitem
        self.loadZCML(package=upfront.assessmentitem)
        z2.installProduct(app, PROJECTNAME)

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, '%s:default' % PROJECTNAME)

    def tearDownZope(self, app):
        z2.uninstallProduct(app, PROJECTNAME)

FIXTURE = TestCase()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="fixture:Integration")


class UpfrontAssessmentItemTestBase(unittest.TestCase):
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.intids = getUtility(IIntIds)

        self.portal.invokeFactory(
                              'upfront.assessmentitem.content.assessmentitem', 
                              'assessmentitem1')
        assessmentitem1 = self.portal._getOb('assessmentitem1')

    def _createQuestion(self):
        container = self.portal.assessmentitem1
        new_id = container.generateId('question')
        rel = create_relation(container.getPhysicalPath())

        container.invokeFactory('upfront.assessmentitem.content.question',
                                id=new_id,
                                relatedContent=rel,
                                text='test question 01')
        question = container._getOb(new_id)
        return question

    def _find_viewlet(self, context, manager_name, viewlet_name, layer=None):
        request = self.portal.REQUEST
        if layer:
            alsoProvides(request, layer)

        view = View(context, request)
        manager = queryMultiAdapter(
            (context, request, view),
            IViewletManager,
            manager_name,
            default=None
        )
        self.failUnless(manager)

        manager.update()
        viewlets = manager.viewlets
        viewlet = [v for v in viewlets if v.__name__ == viewlet_name]
        return viewlet

