from zope.component import createObject
from zope.component import queryUtility

from plone.uuid.interfaces import IUUID
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from plone.dexterity.interfaces import IDexterityFTI

from base import UpfrontAssessmentItemTestBase
from base import PROJECTNAME
from base import INTEGRATION_TESTING

from upfront.assessmentitem.content.assessmentitem import IAssessmentItem

class TestAssessmentItem(UpfrontAssessmentItemTestBase):
    """ Basic methods to test assessment item """
    
    def test_assessmentitem_fti(self):
        fti = queryUtility(
            IDexterityFTI, name='upfront.assessmentitem.content.assessmentitem')
        self.assertNotEquals(fti, None, 'No assessmentitem fti')

    def test_assessmentitem_schema(self):
        fti = queryUtility(
            IDexterityFTI, name='upfront.assessmentitem.content.assessmentitem')
        schema = fti.lookupSchema()
        self.assertEquals(
            IAssessmentItem, schema, 'assessmentitem schema incorrect.')

    def test_assessmentitem_factory(self):
        fti = queryUtility(
            IDexterityFTI, name='upfront.assessmentitem.content.assessmentitem')
        factory = fti.factory
        new_object = createObject(factory)
        self.failUnless(
            IAssessmentItem.providedBy(new_object),
            'assessmentitem provides wrong interface.')

    def test_assessment_item(self):
        self._createAssessmentItem()
        view = self.assessmentitem.restrictedTraverse('@@view')
        assessment_item = view.assessment_item()
        self.assertEquals(self.assessmentitem,assessment_item)

    def test_questions(self):
        self._createAssessmentItem()
        view = self.assessmentitem.restrictedTraverse('@@view')
        questions = view.questions()
        self.assertEquals(self.question,questions[0].getObject())

    def test_marks_string(self):
        self._createAssessmentItem()
        view = self.assessmentitem.restrictedTraverse('@@view')
        marks_string = view.marks_string(1)
        self.assertEquals(marks_string,'mark')
        marks_string = view.marks_string(2)
        self.assertEquals(marks_string,'marks')
