from zope.interface import Interface
from upfront.assessmentitem import MessageFactory as _

class IUpfrontAssessmentItemLayer(Interface):
    """ Marker interface for upfront.assessmentitem """

class IAssessmentItemCloner(Interface):
    """ Marks an object which can clone an assessment item """

    def clone(self):
        raise 'Not implemented' 
