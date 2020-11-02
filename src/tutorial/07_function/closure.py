# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class PaymentMethod(declarative_base()):

    __tablename__ = "payment_methods"

    id = Column(Integer, primary_key=True)
    external_id = Column(String(64), nullable=True)


    def __init__(self, default, backup):

        self.default_payment_method_id = default
        self.backup_payment_method_id = backup


def _send_bind_or_unbind_email(new, old):
    def _send(attr):
        # Send email when card added to booking
        if getattr(old, attr) is None and getattr(new, attr) is not None:
            print(f"payment_method_bind: {getattr(old, attr)} => {getattr(new, attr)}")

        # Send email when card removed from booking
        if getattr(old, attr) is not None and getattr(new, attr) is None:
            print(
                f"payment_method_unbind: {getattr(old, attr)} => {getattr(new, attr)}"
            )

    default = "default_payment_method_id"
    backup = "backup_payment_method_id"
    changed_attrs = [
        attr for attr in [default, backup] if getattr(new, attr) != getattr(old, attr)
    ]
    if default in changed_attrs:
        _send(default)

    if backup in changed_attrs:
        _send(backup)


if __name__ == "__main__":

    payment_method_1 = PaymentMethod(1, None)
    payment_method_2 = PaymentMethod(None, 1)

    _send_bind_or_unbind_email(payment_method_2, payment_method_1)

    
    print(payment_method_1.id, payment_method_1.external_id)
