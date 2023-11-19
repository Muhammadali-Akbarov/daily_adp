"""
The Proxy pattern is a structural design pattern that provides
a surrogate or placeholder for another object to control access to it.
It is often used to add an extra layer of control over the real object,
which can be useful for various purposes such as lazy loading, access control,
logging, monitoring, or providing a simplified interface to the client.
In Python, proxies are implemented using classes that mimic the interface
of the real object and delegate calls to the real object as needed.

advantage of proxy pattern:
    1) Lazy Loading: Proxies can be used for lazy loading of expensive resources or objects.
    The RealSubject is created only when it is actually needed, improving performance.

    2) Access Control: Proxies can enforce access control policies by adding authentication
    or authorization checks before allowing requests to reach the RealSubject.

    3) Logging and Monitoring: Proxies can log method invocations or collect statistics
    on the RealSubject's usage, helping with debugging and performance analysis.

    4) Simplified Interface: Proxies can provide a simplified or restricted interface
    to the RealSubject, hiding its complexity from clients.

use cases:
    1) Virtual Proxies: When dealing with large and expensive objects,
        a proxy can provide a lightweight placeholder until the actual object is needed.

    2) Access Control Proxies: Proxies can control access to sensitive resources
        by adding authentication and authorization checks.

    3) Logging Proxies: Proxies can log method calls for debugging or monitoring purposes.

    4) Remote Proxies: In distributed systems, proxies can represent objects located on
        remote servers and handle communication details like network requests.
"""
import abc


class Subject(abc.ABC):
    """
    Subject Interface
    """
    @abc.abstractmethod
    def request(self) -> None:
        """
        request abstractmethod
        """
        raise NotImplementedError(
            "not implement yet!"
        )


class RealSubject(Subject):
    """
    the real subject.
    """
    def request(self):
        print("RealSubject: Handling request")


class Proxy(Subject):
    """
    the proxy class.
    """
    def __init__(self):
        self._real_subject = None

    def request(self):
        if self._real_subject is None:
            self._real_subject = RealSubject()

        print("Proxy: Checking access")
        self._real_subject.request()


if __name__ == "__main__":
    proxy = Proxy()

    proxy.request()
