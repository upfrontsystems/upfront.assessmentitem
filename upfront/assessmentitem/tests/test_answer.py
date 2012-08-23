from zope.component import createObject
from zope.component import queryUtility

from plone.uuid.interfaces import IUUID
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from plone.dexterity.interfaces import IDexterityFTI

from base import UpfrontAssessmentItemTestBase
from base import PROJECTNAME
from base import INTEGRATION_TESTING

from upfront.assessmentitem.content.answer import IAnswer

class TestAnswer(UpfrontAssessmentItemTestBase):
    """ Basic methods to test answers """
    
    def test_answer_fti(self):
        fti = queryUtility(IDexterityFTI,
                           name='upfront.assessmentitem.content.answer')
        self.assertNotEquals(None, fti)

    def test_answer_schema(self):
        fti = queryUtility(IDexterityFTI,
                           name='upfront.assessmentitem.content.answer')
        schema = fti.lookupSchema()
        self.assertEquals(IAnswer, schema, 'Answer schema incorrect.')

    def test_answer_factory(self):
        fti = queryUtility(IDexterityFTI, 
                           name='upfront.assessmentitem.content.answer')
        factory = fti.factory
        new_object = createObject(factory)
        self.failUnless(IAnswer.providedBy(new_object))
