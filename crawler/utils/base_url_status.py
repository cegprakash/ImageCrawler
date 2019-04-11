from enum import IntEnum


class BaseUrlStatus(IntEnum):
    unprocessed = 0
    processed = 1
    deleted = 2