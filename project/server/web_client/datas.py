from dataclasses import dataclass
from enum import Enum


class StageStatuses(Enum):
    check_secret_case = 0
    check_open_case = 1


### Incoming dataclass information

class ProgramLanguages(Enum):
    Python = 0


class SolutionStatus(Enum):
    best_solution = 0
    good_solution = 1
    bad_true_solution = 2
    bad_unwork_solution = 3
    bad_operating_case_solution = 4


@dataclass
class OperatingTime:
    """ Operatin time of code work. All in seconds

    Arguments:
        max_time: max good time to passed test
        min_time: record time of solution in this test case
        average_time: the average work time is not the best solution of the problems is at most 30% worse than min and 40% less than maximum
    """
    max_time: float
    min_time: float
    average_time: float


@dataclass
class ResourceLoad:
    """Information about system load

    TODO add info about what metrics use
    """
    cpu: float
    ram: float


@dataclass
class SystemLoadInformation:
    """ Information about system load from test case
    Arguments:
        max_params: max load of system
        min_params: min load of system
    """
    max_params: ResourceLoad
    min_params: ResourceLoad


@dataclass
class CaseParam:
    """Params of test case to test they

    Arguments:
        test_case: input value to solution
        operating_time: operatin time of code work
        resource_loading: information about system load when code run
    """
    test_case: dict
    operating_time: OperatingTime
    resource_load: SystemLoadInformation


@dataclass
class TaskParams:
    """Params that they come to testing system from testing client

    Arguments:
        user_id - personal user id like in database
        task_id - personal task id like in database
        program_language - name of program language to test code
        case_params - dataclass of case params for test solution
        solution - code in program language to test in test data
    """
    user_id: str
    task_id: str
    program_language: ProgramLanguages
    case_params: CaseParam
    solution: str


### Processing result dataclass information

@dataclass
class ReportSystemLoad:
    """Information about report of system load

    Arguments:
        resource_load: information about system load when code run
        time_spent: time spent when system run
    """
    resource_load: ResourceLoad
    time_spent: float


@dataclass
class ProcessingResult:
    """ Return dataclass about test information
    from test system to test client

    Arguments:
        user_id - personal user id like in database
        task_id - personal task id like in database
        program_language - name of program language to test code
        case_params - dataclass of case params for test solution
        solution - code in program language to test in test data
    """
    user_id: str
    task_id: str
    program_language: ProgramLanguages
    solution: str
    result_params: ReportSystemLoad
