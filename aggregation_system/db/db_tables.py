from sqlalchemy import DATETIME, VARCHAR, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column_property


Base = declarative_base()


class UserTypes(Base):
    __tablename__ = "user_types"

    user_type = Column(VARCHAR(30), nullable=False, unique=True, primary_key=True)


class Users(Base):
    __tablename__ = "users"

    personal_user_id = Column(Integer, nullable=False, unique=True, primary_key=True)
    user_login = Column(VARCHAR(50), nullable=False, unique=True)
    user_password = Column(VARCHAR(50), nullable=False)
    user_type = column_property(Column(VARCHAR(30), nullable=False), UserTypes.user_type)


class Marks(Base):
    __tablename__ = "marks"

    mark_value = Column(Integer, nullable=False, unique=True, primary_key=True)
    color_of_value = Column(VARCHAR(10), nullable=False)
    mark_description = Column(VARCHAR(300), nullable=False)


class Tasks(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, nullable=False, unique=True, primary_key=True)
    task_name = Column(VARCHAR(100), nullable=False, unique=True)
    task_description = Column(VARCHAR(10000), nullable=False, unique=True)
    test_data = Column(VARCHAR(500), nullable=False)
    time_to_solve = Column(Integer, nullable=False)
    resource_load = Column(VARCHAR(300), nullable=False)
    difficulty_level = column_property(Column(Integer, nullable=False), Marks.mark_value)


class CompleteTask(Base):
    __tablename__ = "complete_task"

    compete_id = Column(Integer, nullable=False, unique=True, primary_key=True)
    user = column_property(Column(Integer, nullable=False), Users.personal_user_id)
    task_id = column_property(Column(Integer, nullable=False), Tasks.task_id)
    result_mark = column_property(Column(Integer, nullable=False), Marks.mark_value)
    data_time = Column(DATETIME, nullable=False)


class StudentGroupInfo(Base):
    __tablename__ = "student_group_info"

    group_id = Column(Integer, nullable=False, unique=True, primary_key=True)
    teacher = column_property(Column(Integer, nullable=False), Users.personal_user_id)


class GroupComposition(Base):
    __tablename__ = "group_composition"

    composition_id = Column(Integer, nullable=False, unique=True, primary_key=True)
    group_id = column_property(Column(Integer, nullable=False), StudentGroupInfo.group_id)
    student_id = column_property(Column(Integer, nullable=False), Users.personal_user_id)


class MarkedTasks(Base):
    __tablename__ = "marked_tasks"

    marked_id = Column(Integer, nullable=False, unique=True, primary_key=True)
    group_id = column_property(Column(Integer, nullable=False), StudentGroupInfo.group_id)
    task_id = column_property(Column(Integer, nullable=False), Tasks.task_id)
    task_assigment_time = Column(Integer, nullable=True)
    time_solve_task = Column(Integer, nullable=True)
