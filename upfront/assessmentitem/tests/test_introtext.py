from zope.component import createObject
from zope.component import queryUtility

from plone.dexterity.interfaces import IDexterityFTI
from plone.app.textfield.value import RichTextValue

from upfront.assessmentitem.content.introtext import IIntroText
from upfront.assessmentitem.tests.base import UpfrontAssessmentItemTestBase

class TestIntroText(UpfrontAssessmentItemTestBase):
    """ Basic methods to test answers """
    
    def test_fti(self):
        fti = queryUtility(IDexterityFTI,
                           name='upfront.assessmentitem.content.introtext')
        self.assertNotEquals(None, fti)

    def test_schema(self):
        fti = queryUtility(IDexterityFTI,
                           name='upfront.assessmentitem.content.introtext')
        schema = fti.lookupSchema()
        self.assertEquals(IIntroText, schema, 'IntroText schema incorrect.')

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, 
                           name='upfront.assessmentitem.content.introtext')
        factory = fti.factory
        new_object = createObject(factory)
        self.failUnless(IIntroText.providedBy(new_object))

    def test_title(self):
        fti = queryUtility(IDexterityFTI, 
                           name='upfront.assessmentitem.content.introtext')
        factory = fti.factory
        new_object = createObject(factory)
        self.assertEqual(new_object.Title(), '')
        new_object.introduction = RichTextValue(
            '<p>To be or no to be, that is the question!</p>')
        self.assertEqual(new_object.Title(),
                         'To be or no to be, that is the ...')
