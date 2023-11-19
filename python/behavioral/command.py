"""
the Command design pattern is a behavioral design pattern
that encapsulates a request as an object, thereby allowing
for parameterization of clients with queues, requests, and operations.
It also provides support for undoable operations. The Command pattern
separates the sender (invoker) of a request from the object that performs
the request (receiver). It promotes loose coupling between the sender
and the receiver and allows for greater flexibility and extensibility in code.

key concepts:
    command: This is an interface or abstract class that
    declares an execute method, which is used to perform the desired action.
    Concrete command classes implement this interface and encapsulate specific actions.

    concrete command:
        These are concrete implementations of the Command interface.
        Each concrete command is responsible for invoking a specific operation on the receiver.

    receiver:
        The receiver is an object that knows how to perform the
            actual work or action associated with a command.

    invoker:
        The invoker is responsible for invoking commands.
        It holds a reference to a command object and triggers the command's execute method.

    client: The client creates and configures the command objects and sets up the invoker.

use cases:
    GUI Applications:
        Command patterns are used to implement actions like buttons,
            menu items, and keyboard shortcuts in graphical user interfaces.

    Transaction Management: Database transactions and logging systems
        often use the Command pattern to track and execute operations.

    Remote Control Systems: Remote control devices often use commands
        to control various electronic devices.

    Undo/Redo Functionality: Command patterns allow for
        undo and redo functionality in applications.
"""
import abc


class Command(abc.ABC):
    """
    Command interface.
    """
    @abc.abstractmethod
    def execute(self) -> None:
        """
        Command execute abstract method.
        """

    @abc.abstractmethod
    def undo(self) -> None:
        """
        Command undo abstract method.
        """


class Light:
    """
    Light receiver.
    """
    def turn_on(self):
        """
        Turn on command.
        """
        print("Light is on")

    def turn_off(self):
        """
        Turn off command.
        """
        print("Light is off")


class LightOnCommand(Command):
    """
    Concrete command to turn on the light.
    """
    def __init__(self, light: Light) -> None:
        self.light: Light = light

    def execute(self) -> None:
        self.light.turn_on()

    def undo(self) -> None:
        self.light.turn_off()


class RemoteControl:
    """
    The invoker class with undo/redo functionality.
    """
    def __init__(self):
        self.command = None
        self.command_history = []
        self.redo_stack = []

    def set_command(self, command):
        """
        Set command method.
        """
        self.command = command

    def press_button(self):
        """
        Execute the command and add it to the history.
        """
        if self.command:
            self.command.execute()
            self.command_history.append(self.command)
            self.redo_stack.clear()

    def press_undo(self):
        """
        Undo the last command.
        """
        if self.command_history:
            command = self.command_history.pop()
            command.undo()
            self.redo_stack.append(command)

    def press_redo(self):
        """
        Redo the last undone command.
        """
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.execute()
            self.command_history.append(command)


# Client code
if __name__ == "__main__":
    light = Light()
    light_on = LightOnCommand(light)
    remote = RemoteControl()

    remote.set_command(light_on)
    remote.press_button()
    remote.press_undo()
    remote.press_redo()
