# -*- coding: utf-8 -*

import os
from time import sleep

from mysql import connector
from sshtunnel import SSHTunnelForwarder


if __name__ == "__main__":

    with SSHTunnelForwarder(
        "54.179.137.16",
        ssh_username="debug",
        ssh_pkey="~/.ssh/id_rsa",
        remote_bind_address=(
            "stage-platform.cgytt8vtm5xx.ap-southeast-1.rds.amazonaws.com",
            3306,
        ),
        local_bind_address=("127.0.0.1", 10036),
    ) as server:

        print(f"server: {server}")
        print(server.local_bind_port)
        #     while True:
        #         # press Ctrl-C for stopping
        #         sleep(1)
        #         print("sleep")

        # print("FINISH!")

        user = os.getenv("USER")
        password = os.getenv("PASSWORD")
        db_name = os.getenv("DB_NAME")

        print(f"Starting connect.........")
        conn = connector.connect(
            host="127.0.0.1",
            port=10036,
            user=user,
            password=password,
            database=db_name,
        )

        cs = conn.cursor()

        cs.execute(
            """
                SELECT
                    *
                FROM
                    charges c
                LIMIT 10;
                """
        )
        result = cs.fetchall()

        print(f"result: {result}")

        cs.close()
        conn.close()
        print(f"Close connection.......")
