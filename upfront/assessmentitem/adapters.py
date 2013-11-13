import grokcore.component
from plone.dexterity.utils import createContentInContainer

from upfront.assessmentitem.content.assessmentitem import IAssessmentItem
from upfront.assessmentitem.interfaces import IAssessmentItemCloner

class AssessmentItemCloner(grokcore.component.Adapter):
    grokcore.component.context(IAssessmentItem)
    grokcore.component.implements(IAssessmentItemCloner)

    def clone(self, original):
        container = original.aq_parent
        settings = {}

        names_and_descriptions = IAssessmentItem.namesAndDescriptions()
        for fname, field in names_and_descriptions:
            value = field.get(original)
            settings[fname] = value

        assessmentitem = createContentInContainer(
            container, 
            'upfront.assessmentitem.content.assessmentitem',
            checkConstraints=False,
            **settings
        )

        return assessmentitem
