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

