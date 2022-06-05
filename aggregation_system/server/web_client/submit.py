import asyncio
import os
import subprocess
import mariadb


STATUS_TEMPLATE = [
    "RUN-ID",
    "FLAGS",
    "TIME",
    "SIZE",
    "PROB",
    "LANG",
    "STATUS",
    "SCORE-INFO",
]
EJUDGE_SQL_LOGIN = os.environ["EJUDGE_SQL_LOGIN"]
EJUDGE_SQL_PASSWORD = os.environ["EJUDGE_SQL_PASSWORD"]
EJUDGE_ADMIN_LOGIN = os.environ["EJUDGE_ADMIN_LOGIN"]
EJUDGE_ADMIN_PASSWORD = os.environ["EJUDGE_ADMIN_PASSWORD"]
EJUDGE_DATABASE_NAME = os.environ["EJUDGE_DATABASE_NAME"]
CONTROL_DIR = os.environ["CONTROL_DIR"]


async def submit_run(source_file, contest_id, language, shortname):
    # TO-DO ejudge user login
    if not os.path.isfile(f"{CONTROL_DIR}/{contest_id}"):
        result = subprocess.run(
            [
                f"{CONTROL_DIR}/ejudge-contests-cmd",
                contest_id,
                "master-login",
                f"{CONTROL_DIR}/{contest_id}",
                EJUDGE_ADMIN_LOGIN,
                EJUDGE_ADMIN_PASSWORD,
            ],
            stdout=subprocess.PIPE,
        )
        result = subprocess.run(
            [
                f"{CONTROL_DIR}/ejudge-contests-cmd",
                contest_id,
                "start-contest",
                f"{CONTROL_DIR}/{contest_id}",
            ],
            stdout=subprocess.PIPE,
        )

        # connection = mysql.connector.connect(
        #     host="localhost",
        #     user=EJUDGE_SQL_LOGIN,
        #     password=EJUDGE_SQL_PASSWORD,
        #     database=EJUDGE_SQL_LOGIN,
        # )

        connection = mariadb.connect(
            user=EJUDGE_SQL_LOGIN,
            password=EJUDGE_SQL_PASSWORD,
            host="127.0.0.1",
            port=3306,
            database=EJUDGE_DATABASE_NAME,
        )
        cursor = connection.cursor()
        query = f"UPDATE cookies SET expire = '2056-03-26 10:11:37' WHERE contest_id = {contest_id};"
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()

    result = subprocess.run(
        [
            f"{CONTROL_DIR}/ejudge-contests-cmd",
            contest_id,
            "submit-run",
            f"{CONTROL_DIR}/{contest_id}",
            shortname,
            language,
            source_file,
        ],
        stdout=subprocess.PIPE,
    )

    run_id = result.stdout.decode("utf-8").strip()

    await asyncio.sleep(15)

    result = subprocess.run(
        [
            f"{CONTROL_DIR}/ejudge-contests-cmd",
            contest_id,
            "run-status",
            f"{CONTROL_DIR}/{contest_id}",
            run_id,
        ],
        stdout=subprocess.PIPE,
    )
    answer = result.stdout.decode("utf-8").strip().split(";")
    # print(answer)

    # print(f"f {CONTROL_DIR}/{contest_id}")
    zipped = dict(zip(STATUS_TEMPLATE, answer))
    # print([zipped["PROB"], zipped["STATUS"], zipped["SCORE-INFO"]])
    return zipped


if __name__ == "__main__":
    asyncio.run(
        submit_run(
            "/home/judges/000002/problems/20/all_solutions/20_python3.py",
            "2",
            "python3",
            "20",
        )
    )
