from zope.component import createObject
from zope.component import queryUtility

from plone.uuid.interfaces import IUUID
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from plone.dexterity.interfaces import IDexterityFTI

from base import UpfrontAssessmentItemTestBase
from base import PROJECTNAME
from base import INTEGRATION_TESTING

from upfront.assessmentitem.content.question import IQuestion

class TestQuestion(UpfrontAssessmentItemTestBase):
    """ Basic methods to test questions """
    
    def test_question_fti(self):
        fti = queryUtility(IDexterityFTI,
                           name='upfront.assessmentitem.content.question')
        self.assertNotEquals(None, fti)

    def test_question_schema(self):
        fti = queryUtility(IDexterityFTI,
                           name='upfront.assessmentitem.content.question')
        schema = fti.lookupSchema()
        self.assertEquals(IQuestion, schema, 'Question schema incorrect.')

    def test_question_factory(self):
        fti = queryUtility(IDexterityFTI,
                           name='upfront.assessmentitem.content.question')
        factory = fti.factory
        new_object = createObject(factory)
        self.failUnless(IQuestion.providedBy(new_object))
