from zope.component import createObject
from zope.component import queryUtility

from plone.uuid.interfaces import IUUID
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from plone.dexterity.interfaces import IDexterityFTI

from base import UpfrontAssessmentItemTestBase
from base import PROJECTNAME
from base import INTEGRATION_TESTING

from upfront.assessmentitem.content.assessmentitemcontainer import \
    IAssessmentItemContainer

class TestAssessmentItemContainer(UpfrontAssessmentItemTestBase):
    """ Tests for assessment item container """
    
    def test_assessmentitemcontainer_fti(self):
        fti = queryUtility(
            IDexterityFTI,
            name='upfront.assessmentitem.content.assessmentitemcontainer'
            )
        self.assertNotEquals(fti, None, 'No assessmentitemcontainer fti')

    def test_assessmentitemcontainer_schema(self):
        fti = queryUtility(
            IDexterityFTI,
            name='upfront.assessmentitem.content.assessmentitemcontainer'
            )
        schema = fti.lookupSchema()
        self.assertEquals(
            IAssessmentItemContainer, schema,
            'assessmentitemcontainer schema incorrect.'
            )

    def test_assessmentitemcontainer_factory(self):
        fti = queryUtility(
            IDexterityFTI,
            name='upfront.assessmentitem.content.assessmentitemcontainer'
            )
        factory = fti.factory
        new_object = createObject(factory)
        self.failUnless(
            IAssessmentItemContainer.providedBy(new_object),
            'assessmentitemcontainer provides wrong interface.')

    def test_assessmentitems(self):
        self._createAssessmentItemContainer()
        view = self.assessmentitemcontainer.restrictedTraverse('@@view')
        items = view.assessmentitems()
        self.assertEquals([self.assessmentitem],items)

    def test_marks_string(self):
        self._createAssessmentItemContainer()
        view = self.assessmentitemcontainer.restrictedTraverse('@@view')
        marks_string = view.marks_string(1)
        self.assertEquals(marks_string,'mark')
        marks_string = view.marks_string(2)
        self.assertEquals(marks_string,'marks')
