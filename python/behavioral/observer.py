"""
The Observer pattern is a software design pattern that is
commonly used to create an efficient and flexible mechanism
for monitoring and reacting to changes in a system.
This pattern is especially useful in scenarios where an
object,known as the subject, needs to automatically notify a
list of other objects,known as observers, about any state changes.
"""
import abc


class Observer(abc.ABC):
    """
    the oberver abstraction.
    """
    def update(self, subject):
        """
        updater.
        """


class Subject:
    """
    the subject class.
    """
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        """
        attacher
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """
        detacher.
        """
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        """
        notifier.
        """
        for observer in self._observers:
            observer.update(self)

    @property
    def state(self):
        """
        state.
        """
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()


class ConcreteObserverA(Observer):
    """
    implementation of Observer.
    """
    def update(self, subject):
        if subject.state < 3:
            print("ConcreteObserverA: Reacted to event")


class ConcreteObserverB(Observer):
    """
    implementation of Observer.
    """
    def update(self, subject):
        if subject.state >= 3:
            print("ConcreteObserverB: Reacted to event")


subject = Subject()


observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()

subject.attach(observer_a)
subject.attach(observer_b)

# Change the state of the subject
subject.state = 2
subject.state = 3
