"""
The Decorator pattern is a structural design pattern that allows
you to add new behaviors or responsibilities to objects without
altering their existing code. It is achieved by creating a set
of decorator classes that are used to wrap concrete components.
"""
import abc


class NotificationService(abc.ABC):
    """
    the abstract.
    """
    @abc.abstractmethod
    def send(self, message):
        """
        abstract method to send.
        """


class EmailNotificationService(NotificationService):
    """
    email notification service.
    """
    def send(self, message):
        print(f"Sending email: {message}")


class NotificationDecorator(NotificationService):
    """
    notification decorator.
    """
    def __init__(self, notification_service):
        self._notification_service = notification_service

    @abc.abstractmethod
    def send(self, message):
        pass


class EncryptionDecorator(NotificationDecorator):
    """
    encryption decorator.
    """
    def send(self, message):
        encrypted_message = f"Encrypting message: {message}"
        self._notification_service.send(encrypted_message)


class LoggingDecorator(NotificationDecorator):
    """
    logging decorator.
    """
    def send(self, message):
        print(f"Logging message: {message}")
        self._notification_service.send(message)


if __name__ == "__main__":
    email_service = EmailNotificationService()

    encrypted_email_service = EncryptionDecorator(email_service)
    logged_encrypted_email_service = LoggingDecorator(encrypted_email_service)

    logged_encrypted_email_service.send("Hello, Decorator Pattern!")
