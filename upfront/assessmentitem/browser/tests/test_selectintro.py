from tarmii.theme.tests.base import TarmiiThemeTestBase

from plone.dexterity.utils import createContentInContainer
from plone.app.textfield.value import RichTextValue

class TestSelectIntro(TarmiiThemeTestBase):
    """ Test SelectIntro browser view
    """

    def test_questions(self):
        view = self.portal.restrictedTraverse('@@selectintro')
        self.assertEqual(len(view.intros()), 0)

        intro = createContentInContainer(self.portal,
            'upfront.assessmentitem.content.introtext',
            introduction=RichTextValue('<p>Introduction</p>'))

        self.assertEqual(len(view.intros()), 1)
