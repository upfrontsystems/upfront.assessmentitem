from zope.component import adapts
from zope.interface import alsoProvides
from zope.component import createObject
from zope.interface import implements
from zope.component import getUtility
from zope.component import queryUtility 
from zope.component import queryMultiAdapter

from zope.viewlet.interfaces import IViewletManager

from Products.Five.browser import BrowserView as View
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.Document import Document

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehaviorAssignable
from plone.behavior.interfaces import IBehavior
from plone.dexterity.interfaces import IDexterityFTI
from plone.directives.form import IFormFieldProvider
from plone.testing.z2 import Browser
from plone.uuid.interfaces import IUUID

from base import UpfrontAssessmentItemTestBase
from base import PROJECTNAME
from base import INTEGRATION_TESTING

from upfront.assessmentitem.interfaces import IUpfrontAssessmentItemLayer
from upfront.assessmentitem.behaviors import IMarks
from upfront.assessmentitem.behaviors import IResponseTime

from upfront.assessmentitem.content.question import IQuestion
from upfront.assessmentitem.content.answer import IAnswer


class TestMarks(UpfrontAssessmentItemTestBase):
    """ Test the behavior that enables marks on dexterity content.
    """
    implements(IBehaviorAssignable)
    
    def test_marks_behavior(self):

        fti = queryUtility(IDexterityFTI, 
                           name='upfront.assessmentitem.content.question')
        factory = fti.factory
        new_question = createObject(factory)
        self.failUnless(IQuestion.providedBy(new_question))

        fti = queryUtility(IDexterityFTI, 
                           name='upfront.assessmentitem.content.answer')
        factory = fti.factory
        new_answer = createObject(factory)
        self.failUnless(IAnswer.providedBy(new_answer))
 
        marks_behavior = getUtility(IBehavior, 
                        name = 'upfront.assessmentitem.behaviors.IMarks')

        # We expect this behavior to be a form field provider. Let's verify that
        self.failUnless(IFormFieldProvider.providedBy(marks_behavior.interface)) 

        # assert that you cannot add this behavior to a non-dexterity 
        # content type
        doc = Document('doc')
        marks_adapter = IMarks(doc, None)
        self.assertEquals(False,marks_adapter is not None)

        # assert that new_question object implements the behavior
        marks_adapter2 = IMarks(new_question, None)
        self.assertEquals(True,marks_adapter2 is not None)
        
        # assert that new_answer object does not implements the behavior
        marks_adapter3 = IMarks(new_answer, None)
        self.assertEquals(False,marks_adapter3 is not None)


class TestResponseTime(UpfrontAssessmentItemTestBase):
    """ Test the behavior that enables response time on dexterity content.
    """
    implements(IBehaviorAssignable)
    
    def test_responsetime_behavior(self):

        fti = queryUtility(IDexterityFTI, 
                           name='upfront.assessmentitem.content.question')
        factory = fti.factory
        new_question = createObject(factory)
        self.failUnless(IQuestion.providedBy(new_question))

        fti = queryUtility(IDexterityFTI, 
                           name='upfront.assessmentitem.content.answer')
        factory = fti.factory
        new_answer = createObject(factory)
        self.failUnless(IAnswer.providedBy(new_answer))

        rt_behavior = getUtility(IBehavior, 
                        name = 'upfront.assessmentitem.behaviors.IResponseTime')

        # We expect this behavior to be a form field provider. Let's verify that
        self.failUnless(IFormFieldProvider.providedBy(rt_behavior.interface)) 

        # assert that you cannot add this behavior to a non-dexterity 
        # content type
        doc = Document('doc')
        rt_adapter = IResponseTime(doc, None)
        self.assertEquals(False,rt_adapter is not None)

        # assert that new_question object implements the behavior
        rt_adapter2 = IResponseTime(new_question, None)
        self.assertEquals(True,rt_adapter2 is not None)
        
        # assert that new_answer object does not implements the behavior
        rt_adapter3 = IResponseTime(new_answer, None)
        self.assertEquals(False,rt_adapter3 is not None)




