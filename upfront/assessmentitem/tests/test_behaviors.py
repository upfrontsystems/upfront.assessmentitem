from zope.interface import alsoProvides 
from zope.component import queryMultiAdapter
from zope.viewlet.interfaces import IViewletManager

from Products.Five.browser import BrowserView as View
from Products.CMFCore.utils import getToolByName

from plone.uuid.interfaces import IUUID
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from base import UpfrontAssessmentItemTestBase
from base import PROJECTNAME
from base import INTEGRATION_TESTING

from upfront.assessmentitem.interfaces import IUpfrontAssessmentItemLayer
from upfront.assessmentitem.behaviors import IMarks
from upfront.assessmentitem.behaviors import IResponseTime


class TestMarks(UpfrontAssessmentItemTestBase):
    """ Test the behavior that enables marks on dexterity content.
    """
    
    def test_marks_disabled(self):
        
        return True
