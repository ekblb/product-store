from enum import Enum


class GlobalEnumMessages(Enum):
    WRONG_STATUS_CODE = (
        "Received status code doesn't match the expected value."
    )
    WRONG_ELEMENTS_NUMBER = (
        "Number of received elements doesn't match the expected value."
    )
