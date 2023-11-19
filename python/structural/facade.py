"""
The Facade pattern is a structural design pattern that provides a simplified
interface to a complex system, making it easier for clients to interact with
that system. It acts as a higher-level interface that hides the underlying
complexity of a set of subsystems or classes. This pattern promotes loose
coupling between the client code and the subsystems it interacts with.
"""


# system 1
class Trip:
    """
    the trip system.
    """
    def start(self) -> None:
        """
        start the trip.
        """
        print("trip has been started")

    def stop(self) -> None:
        """
        stop the trip.
        """
        print("trip has been stopped")


# system 2
class Payment:
    """
    the payment system.
    """
    def has_debt(self) -> bool:
        """
        checks client's debt
        """
        return True


# Facade
class TripFacade:
    """
    the trip facade pattern.
    """
    def __init__(self):
        self.trip = Trip()
        self.payment = Payment()

    def start_trip(self) -> bool:
        """
        start the trip.
        """
        has_debt = self.payment.has_debt()

        if has_debt is True:
            print("client has debt!")
            self.trip.stop()
            return False

        self.trip.start()
        return True

    def finish_trip(self) -> None:
        """
        stop the trip.
        """
        print("trip finished successfully!")


# client code
if __name__ == "__main__":
    trip = TripFacade()
    STARTED = trip.start_trip()

    if STARTED:
        trip.finish_trip()
