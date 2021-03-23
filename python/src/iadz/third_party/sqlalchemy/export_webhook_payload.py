# -*- coding: utf-8 -*-

import argparse
import os
import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_USER = os.getenv("DB_USER") or "root"
DB_PASS = os.getenv("DB_PASS") or ""
DB_SERVER = os.getenv("DB_SERVER") or "127.0.0.1"
DB_PORT = os.getenv("DB_PORT") or 3306


def setup_parser():
    parser = argparse.ArgumentParser(description="Bash use to export webhook payload")
    parser.add_argument(
        "--subscription_id",
        help="Specify the subscription_id use for a concrete consumer",
        type=int,
        required=True,
    )
    parser.add_argument(
        "--booking_id",
        help="Specify the booking_id to determine which payload to export",
        type=int,
        required=True,
    )
    parser.add_argument(
        "--file_name",
        help="Specify the file_name to export webhook payload",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--offset",
        help="Help to extract part of webhook payload",
        type=int,
        required=False,
    )
    return parser


class Worker:
    def __init__(
        self, subscription_id: int, booking_id: int, file_name: str, offset: int = None
    ):
        self.subscription_id = subscription_id
        self.booking_id = booking_id
        self.file_name = file_name
        self.offset = offset
        self.session = None

        self.setup()

    def setup(self):
        engine = create_engine(
            f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_SERVER}:{DB_PORT}/g_integrations"
        )
        Session = sessionmaker(bind=engine)

        self.session = Session()

    def close(self):
        self.session.close()

    def dial(self):
        query = self.session.execute(
            f"""
            SELECT f.*
            FROM failed_events f
            LIMIT 1
            """
        )
        print(f"{query.fetchall()}")

    def main(self):
        query = self.session.execute(
            f"""
            SELECT f.event_name, f.record_payload‰
            FROM failed_events f
            WHERE
                f.subscription_id={self.subscription_id}
                AND (
                    f.record_id={self.booking_id}
                    OR (event_name="payment_item/created" AND record_payload->>"$.paymentItem.bookingId"={self.booking_id})
                    OR (event_name="payment_item/status_updated" AND record_payload->>"$.paymentItem.bookingId"={self.booking_id})
                    OR (event_name="transaction_record/created" AND record_payload->>"$.transactionRecord.bookingId"={self.booking_id})
                )
                AND f.id > {self.offset or 0}
            ;
            """
        )

        result = query.fetchall()
        count = 1

        with open(f"/Users/a/WebhookPayload/{self.file_name}", "a") as f:

            for resource in result:
                f.write(f"{count}.{resource[0]}")
                f.write("\n")
                payload = json.loads(resource[1])
                json.dump(payload, f, ensure_ascii=False, indent=4)
                f.write("\n\n")

                count += 1


if __name__ == "__main__":

    parser = setup_parser()

    args_ = parser.parse_args()

    worker = Worker(
        subscription_id=args_.subscription_id,
        booking_id=args_.booking_id,
        file_name=args_.file_name,
        offset=args_.offset,
    )
    worker.dial()
    # worker.main()
    worker.close()

    print("All done! ✨ 🍰 ✨")
