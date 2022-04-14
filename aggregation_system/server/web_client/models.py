from django.db import models


class CheckSend(models.Model):
    """ Params of stage in testing
    Arguments:
        user_id - personal user id like in database
        task_id - personal task id like in database
        program_language - name of program language to test code
        testing_stage - value in tuple of testing stage
        code_file - file with the user's code
    """
    user_id = models.CharField(max_length=30)
    task_id = models.CharField(max_length=30)
    program_lang = models.CharField(max_length=30)
    testing_stage = models.IntegerField()
    code_file = models.FileField(default='default.py')

    def __str__(self) -> str:
        return self.user_id


class ResultSend(models.Model):
    """ Results of testing
        Arguments:
            solution_status - value in tuple of solution status stage
            task_id - personal task id like in database
            program_language - name of program language to test code
        """
    solution_status = models.IntegerField()
    task_id = models.CharField(max_length=30)
    program_lang = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.task_id
