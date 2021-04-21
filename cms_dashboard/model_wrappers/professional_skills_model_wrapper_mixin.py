from django.apps import apps as django_apps
from .professional_skills_model_wrapper import (
    StrategicOrientationModelWrapper, ResultsFocusModelWrapper,
    LeadershipAndMotivationModelWrapper, InnovationAndCreativityModelWrapper,
    PlanningSkillsModelWrapper, InterpersonalSkillsModelWrapper,
    CommunicationSkillsModelWrapper, KnowledgeAndProductivityModelWrapper,
    QualityOfWorkModelWrapper)
from .model_wrapper_mixin import ProfessionalSkillsWrapperMixin


class StrategicOrientationModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    strategic_model_cls = 'contract.strategicorientation'
    strategic_wrapper_cls = StrategicOrientationModelWrapper


class ResultsFocusModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    results_focus_model_cls = 'contract.resultsfocus'
    results_focus_wrapper_cls = ResultsFocusModelWrapper


class LeadershipAndMotivationModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    leadership_model_cls = 'contract.leadershipandmotivation'
    leadership_wrapper_cls = LeadershipAndMotivationModelWrapper


class InnovationAndCreativityModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    innovation_model_cls = 'contract.innovationandcreativity'
    innovation_wrapper_cls = InnovationAndCreativityModelWrapper


class PlanningSkillsModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    planning_skills_model_cls = 'contract.planningskills'
    planning_skills_wrapper_cls = PlanningSkillsModelWrapper


class InterpersonalSkillsModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    interpersonal_skills_model_cls = 'contract.interpersonalskills'
    interpersonal_skills_wrapper_cls = InterpersonalSkillsModelWrapper


class CommunicationSkillsModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    communication_skills_model_cls = 'contract.communicationskills'
    communication_skills_wrapper_cls = CommunicationSkillsModelWrapper


class KnowledgeAndProductivityModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    knowledge_model_cls = 'contract.knowledgeandproductivity'
    knowledge_wrapper_cls = KnowledgeAndProductivityModelWrapper


class QualityOfWorkModelWrapperMixin(ProfessionalSkillsWrapperMixin):

    quality_of_work_model_cls = 'contract.qualityofwork'
    quality_of_work_wrapper_cls = QualityOfWorkModelWrapper
