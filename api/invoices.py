from typing import cast


class InvoiceStatus:
    pass  # TODO: implement


class InvoiceExceptionStatus:
    pass  # TODO: implement


DEFAULT_PENDING_STATUSES = [InvoiceStatus.PENDING, InvoiceStatus.PAID]
PAID_STATUSES = [InvoiceStatus.PAID, InvoiceStatus.CONFIRMED, InvoiceStatus.COMPLETE]
FAILED_STATUSES = [InvoiceStatus.EXPIRED, InvoiceStatus.INVALID]


# TODO: move it to daemon somehow
STATUS_MAPPING = {
}


def convert_status(status: int | str) -> str:
    pass  # TODO: implement
