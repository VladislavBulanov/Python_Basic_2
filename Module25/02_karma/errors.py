"""Module of classes of possible violations (errors) of karma."""


class Error:
    """Basic class of karma error."""
    def __str__(self):
        return 'Error description'


class KillError(Error):
    """
    Subclass of basic class 'Error'
    if you killed someone.
    """
    def __str__(self):
        return 'You killed someone'


class DrunkError(Error):
    """
    Subclass of basic class 'Error'
    if you were drunk.
    """
    def __str__(self):
        return 'You were drunk'


class CarCrashError(Error):
    """
    Subclass of basic class 'Error'
    if you were in a car accident.
    """
    def __str__(self):
        return 'You were in a car accident'


class GluttonyError(Error):
    """
    Subclass of basic class 'Error'
    if you ate too much.
    """
    def __str__(self):
        return 'You ate too much'


class DepressionError(Error):
    """
    Subclass of basic class 'Error'
    if you have become depressed.
    """
    def __str__(self):
        return 'You have become depressed'
