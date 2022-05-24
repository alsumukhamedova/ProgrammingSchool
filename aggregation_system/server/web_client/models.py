from django.db import models


class UserTypes(models.Model):
    """ Params of stage in testing
        Arguments:
            user_type - user's type, a teacher or a student
    """
    user_type = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.user_type


class Users(models.Model):
    """ Params of stage in testing
        Arguments:
            user_login - user's login
            user_password - user's password
            user_type - student or teacher
            user_mail - user's mail
            user_name - user's name
    """
    user_login = models.CharField(max_length=50, unique=True)
    user_password = models.CharField(max_length=50)
    user_type = models.ForeignKey(UserTypes, on_delete=models.CASCADE)
    user_mail = models.CharField(max_length=50, unique=True, default="")
    user_name = models.CharField(max_length=50, default="")

    def __str__(self) -> str:
        return self.user_login


class Marks(models.Model):
    """ Params of stage in testing
        Arguments:
            color_of_value - values' color
            mark_description - description of the assessment
    """
    color_of_value = models.CharField(max_length=10, null=False)
    mark_description = models.CharField(max_length=300, null=False)


class Tasks(models.Model):
    """ Params of stage in testing
        Arguments:
            task_name - name of task
            task_description - task's description
            test_data - test's data
            time_to_solve - decision time
            resource_load - resources' load
            difficulty_level - level's difficulty
    """
    task_name = models.CharField(max_length=100, null=False, unique=True)
    task_description = models.TextField(null=False, unique=True)
    test_data = models.CharField(max_length=500, null=False)
    time_to_solve = models.IntegerField()
    resource_load = models.CharField(max_length=300, null=False)
    difficulty_level = models.ForeignKey(Marks, on_delete=models.CASCADE)


class CheckSend(models.Model):
    """ Params of stage in testing
    Arguments:
        user_id - personal user id like in database
        task_id - personal task id like in database
        program_language - name of program language to test code
        testing_stage - value in tuple of testing stage
        code - file with the user's code
    """
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    program_lang = models.CharField(max_length=30)
    code = models.TextField()

    class Meta:
        unique_together = ('user_id', 'task_id',)

    def __str__(self) -> str:
        return self.user_id


class CompleteTask(models.Model):
    """ Results of testing
        Arguments:
            user_id - personal user id like in database
            task_id - personal task id like in database
            program_lang - name of program language to test code
            status - tests' result
            time - time for testing
            size - load memory
        """
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    program_lang = models.CharField(max_length=30)
    status = models.CharField(max_length=50)
    time = models.CharField(max_length=20)
    size = models.CharField(max_length=7)

    def __str__(self) -> str:
        return self.task_id


class StudentGroupInfo(models.Model):
    group_name = models.CharField(max_length=50, null=False, default="0")
    teacher = models.ForeignKey(Users, on_delete=models.CASCADE, null=False)


class GroupComposition(models.Model):
    group_id = models.ForeignKey(StudentGroupInfo, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Users, on_delete=models.CASCADE)


class MarkedTasks(models.Model):
    group_id = models.ForeignKey(StudentGroupInfo, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    task_assigment_time = models.IntegerField()
    time_solve_task = models.IntegerField()
