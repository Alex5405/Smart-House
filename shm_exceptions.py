# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

# ----------------------------------------------------------------------------------------------------------------------

# Кастомные исключения для проекта

# ----------------------------------------------------------------------------------------------------------------------

class ExceptionErrorProtocol(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'ExceptionErrorProtocol: {0}.'.format(self.message)
        else:
            return 'ExceptionErrorProtocol: Unknown protocol!'


class ExceptionErrorCommand(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'ExceptionErrorCommand: {0}.'.format(self.message)
        else:
            return 'ExceptionErrorCommand: Unknown command!'


class ExceptionDockerFileNotFound(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'ExceptionDockerFileNotFound: {0}.'.format(self.message)
        else:
            return 'ExceptionDockerFileNotFound: Docker file does not exist!'


class ExceptionOnlineStatus(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'ExceptionOnlineStatus: {0}.'.format(self.message)
        else:
            return 'ExceptionOnlineStatus: This status does not exist!'


class ExceptionTypeSensor(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'ExceptionTypeSensor: {0}.'.format(self.message)
        else:
            return 'ExceptionTypeSensor: There is no such type of sensor!'
