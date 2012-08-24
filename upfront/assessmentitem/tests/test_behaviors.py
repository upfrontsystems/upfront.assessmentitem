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
        types = getToolByName(self.portal, 'portal_types')
        fti = types.getTypeInfo('upfront.assessmentitem.content.question')
        fti.behaviors = \
            ('upfront.assessmentitem.behaviors.IMarks',)
        
        context = self._createQuestion()
        manager_name = 'plone.belowcontent'
        viewlet_name = 'question-add'
        layer = IUpfrontAssessmentItemLayer
        viewlet = self._find_viewlet(context, manager_name, viewlet_name, layer)
        
#        self.assertTrue(
#            viewlet[0].render() ==  "",
#            'Questions are disable; viewlet should not render.'
#        )

    def test_marks_enabled(self):
        types = getToolByName(self.portal, 'portal_types')
        fti = types.getTypeInfo('upfront.assessmentitem.content.question')
        fti.behaviors = \
            ('upfront.assessmentitem.behaviors.IMarks',)
        
        context = self._createQuestion()
        context.allowQuestions = True
        manager_name = 'plone.belowcontent'
        viewlet_name = 'question-add'
        layer = IUpfrontAssessmentItemLayer
        viewlet = self._find_viewlet(context, manager_name, viewlet_name, layer)
        
#        self.assertTrue(
#            len(viewlet[0].render()) > 0,
#            'Questions are enabled; viewlet should render.'
#        )
