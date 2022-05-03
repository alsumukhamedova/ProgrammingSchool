CREATE TABLE user_types (
    user_type VARCHAR(30) PRIMARY KEY
);

CREATE TABLE users (
    personal_user_id int PRIMARY KEY,
    user_login VARCHAR(50) not null,
    user_password VARCHAR(50) not null,
    user_type VARCHAR(30) not null,
    FOREIGN KEY (user_type) REFERENCES user_types(user_type)
);

CREATE TABLE marks (
    mark_value int PRIMARY KEY,
    color_of_value VARCHAR(10) not null,
    mark_description VARCHAR(300) not null
);

CREATE TABLE tasks (
    task_id int PRIMARY KEY,
    task_name VARCHAR(100) not null,
    task_description VARCHAR(10000) not null,
    test_data VARCHAR(500) not null,
    time_to_solve int not null, -- in seconds
    resource_load VARCHAR(300) not null,
    difficulty_level int not null,
    FOREIGN KEY (difficulty_level) REFERENCES marks(mark_value)
);

CREATE TABLE complete_task (
    compete_id int PRIMARY KEY,
    user int not null,
    task_id int not null,
    result_mark int not null,
    data_time DATETIME not null,
    FOREIGN KEY (user) REFERENCES users(personal_user_id),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (result_mark) REFERENCES marks(mark_value)
);

CREATE TABLE student_group_info(
    group_id int PRIMARY KEY,
    teacher int not null,-- in seconds
    FOREIGN KEY (teacher) REFERENCES users(personal_user_id)
);

CREATE TABLE group_composition(
    composition_id int PRIMARY KEY,
    group_id int not null,
    student_id int not null,
    FOREIGN KEY (group_id) REFERENCES student_group_info(group_id),
    FOREIGN KEY (student_id) REFERENCES users(personal_user_id)
);

CREATE TABLE marked_tasks(
    marked_id int PRIMARY Key,
    group_id int not null,
    task_id int not null,
    task_assigment_time int not null, -- in seconds
    time_solve_task int not null, -- in seconds
    FOREIGN KEY (group_id) REFERENCES student_group_info(group_id),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id)
);
