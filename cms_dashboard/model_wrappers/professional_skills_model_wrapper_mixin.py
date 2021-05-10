from .professional_skills_model_wrapper import (
    StrategicOrientationModelWrapper, ResultsFocusModelWrapper,
    LeadershipAndMotivationModelWrapper, InnovationAndCreativityModelWrapper,
    PlanningSkillsModelWrapper, InterpersonalSkillsModelWrapper,
    CommunicationSkillsModelWrapper, KnowledgeAndProductivityModelWrapper,
    QualityOfWorkModelWrapper)
from .model_wrapper_mixin import ProfessionalSkillsWrapperMixin


class StrategicOrientationModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    strategic_model_cls = 'bhp_personnel.strategicorientation'
    strategic_wrapper_cls = StrategicOrientationModelWrapper


class ResultsFocusModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    results_focus_model_cls = 'bhp_personnel.resultsfocus'
    results_focus_wrapper_cls = ResultsFocusModelWrapper


class LeadershipAndMotivationModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    leadership_model_cls = 'bhp_personnel.leadershipandmotivation'
    leadership_wrapper_cls = LeadershipAndMotivationModelWrapper


class InnovationAndCreativityModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    innovation_model_cls = 'bhp_personnel.innovationandcreativity'
    innovation_wrapper_cls = InnovationAndCreativityModelWrapper


class PlanningSkillsModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    planning_skills_model_cls = 'bhp_personnel.planningskills'
    planning_skills_wrapper_cls = PlanningSkillsModelWrapper


class InterpersonalSkillsModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    interpersonal_skills_model_cls = 'bhp_personnel.interpersonalskills'
    interpersonal_skills_wrapper_cls = InterpersonalSkillsModelWrapper


class CommunicationSkillsModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    communication_skills_model_cls = 'bhp_personnel.communicationskills'
    communication_skills_wrapper_cls = CommunicationSkillsModelWrapper


class KnowledgeAndProductivityModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    knowledge_model_cls = 'bhp_personnel.knowledgeandproductivity'
    knowledge_wrapper_cls = KnowledgeAndProductivityModelWrapper


class QualityOfWorkModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    quality_of_work_model_cls = 'bhp_personnel.qualityofwork'
    quality_of_work_wrapper_cls = QualityOfWorkModelWrapper
