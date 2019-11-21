class BaseValidationError(ValueError):
    pass


class NameTooShortError(BaseValidationError):
    pass


class NameTooLongError(BaseValidationError):
    pass


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)


"""
NOTES:
- defining exception types will state code's intent more clearly, easier to debug
- derive custom exceptions from Exception class or from more specific exceptions (ValueError, KeyError)
- use inheritance to define logically grouped exception hierarchies
"""