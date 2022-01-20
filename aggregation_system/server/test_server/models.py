from enum import Enum
from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.
# class StageStatuses(models.TextChoices):
#     check_secret_case = '0', 'Secret'
#     check_open_case = '1', 'Open'


class ProgramLanguages(models.TextChoices):
    PYTHON = 1, _('Python')


# class SolutionStatus(models.TextChoices):
#     best_solution = '0', 'Best'
#     good_solution = '1', 'Good'
#     bad_true_solution = '2', 'Bad_True'
#     bad_unwork_solution = '3', 'Bad_Unwork'
#     bad_operating_case_solution = '4', 'Bad_Operating'


class OperatingTime(models.Model):
    """ Operatin time of code work. All in seconds

    Arguments:
        max_time: max good time to passed test
        min_time: record time of solution in this test case
        average_time: the average work time is not the best solution of the problems is at most 30% worse than min and 40% less than maximum
    """
    max_time = models.FloatField(default=0.0)
    min_time = models.FloatField(default=0.0)
    average_time = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.average_time


class ResourceLoad(models.Model):
    """Information about system load


    """
    cpu = models.FloatField(default=0.0)
    ram = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.cpu


class SystemLoadInformation(models.Model):
    """ Information about system load from test case
    Arguments:
        max_params: max load of system
        min_params: min load of system
    """
    max_params: ResourceLoad
    min_params: ResourceLoad

    def __str__(self) -> str:
        return self.max_params.cpu


class CaseParam(models.Model):
    """Params of test case to test they

    Arguments:
        test_case: input value to solution
        operating_time: operatin time of code work
        resource_loading: information about system load when code run
    """
    test_case = models.JSONField(default=dict)
    operating_time: OperatingTime
    resource_load: SystemLoadInformation

    def __str__(self) -> str:
        return self.test_case


class TaskParams(models.Model):

    """Params that they come to testing system from testing client

    Arguments:
        user_id - personal user id like in database
        task_id - personal task id like in database
        program_language - name of program language to test code
        case_params - dataclass of case params for test solution
        solution - code in program language to test in test data
    """
    user_id = models.UUIDField()
    task_id = models.UUIDField()
    program_language = models.PositiveSmallIntegerField(
        choices=ProgramLanguages.choices,
        default=1,
    )
    case_params: CaseParam
    solution = models.JSONField(default=str)

    def __str__(self) -> str:
        return self.user_id


class ReportSystemLoad(models.Model):
    """Information about report of system load

    Arguments:
        resource_load: information about system load when code run
        time_spent: time spent when system run
    """
    resource_load: ResourceLoad
    time_spent = models.PositiveBigIntegerField(default=0.0)

    def __str__(self) -> str:
        return self.time_spent


class ProcessingResult(models.Model):
    """ Return dataclass about test information
    from test system to test client

    Arguments:
        user_id - personal user id like in database
        task_id - personal task id like in database
        program_language - name of program language to test code
        case_params - dataclass of case params for test solution
        solution - code in program language to test in test data
    """
    user_id = models.UUIDField()
    task_id = models.UUIDField()
    program_language = models.PositiveSmallIntegerField(
        choices=ProgramLanguages.choices,
        default=1,
    )
    solution = models.JSONField(default=str)
    result_params: ReportSystemLoad

    def __str__(self) -> str:
        return self.user_id
