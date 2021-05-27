"""
created by Nagaj at 27/05/2021
"""
from constants import APP_ERROR, INVALID_NAME_CODE, INVALID_NAME_MSG, GENERAL_ERROR_MSG, INVALID_EXTENSION_MSG, \
    INVALID_EXTENSION_CODE


class BaseAPIError(Exception):
    """ A base exception class that represents a generic API error """

    code = APP_ERROR
    message = GENERAL_ERROR_MSG
    additional_info = None

    def to_json(self):
        return {
            "code": self.code,
            "message": self.message,
            "additional_info": self.additional_info,
        }


class InvalidCharForName(BaseAPIError):
    code = INVALID_NAME_CODE
    message = INVALID_NAME_MSG


class InvalidExtension(BaseAPIError):
    code = INVALID_EXTENSION_CODE
    message = INVALID_EXTENSION_MSG
