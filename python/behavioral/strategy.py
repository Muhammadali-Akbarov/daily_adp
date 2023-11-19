"""
The Strategy design pattern is a behavioral software design pattern that
enables selecting an algorithm's behavior at runtime. This pattern is particularly
useful in scenarios where you want to define a family of algorithms,
encapsulate each one, and make them interchangeable. The Strategy pattern
lets the algorithm vary independently from clients that use it.

components of the strategy pattern:
    1) Context: The class that uses a Strategy implementation to perform a task.
    2) Strategy Interface: A common interface for all concrete strategies.
        It declares a method the Context uses to execute a strategy.
    3) Concrete Strategies: Implementations of the Strategy interface,
        each representing a different algorithm.
"""
import abc


class Strategy:
    """
    abstract class.
    """
    @abc.abstractmethod
    def execute(self, data):
        """
        execute abstract method.
        """


class ConcreteStrategyA(Strategy):
    """
    Conrete strategy A
    """
    def execute(self, data):
        print(f"executing strategy A data: {data}")


class ConcreteStrategyB(Strategy):
    """
    Conrete strategy B
    """
    def execute(self, data):
        print(f"executing strategy B data: {data}")


class Context:
    """
    the context of strategy
    """
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        """
        set strategy.
        """
        self._strategy = strategy

    def execute_strategy(self, data):
        """
        execute strategy.
        """
        return self._strategy.execute(data)


if __name__ == "__main__":
    data = {
        "name": "Muhammadali",
        "telegram": "@muhammadalive",
        "website": "https://muhammadalive.com"
    }

    context = Context(ConcreteStrategyA())
    result = context.execute_strategy(data)

    context.set_strategy(ConcreteStrategyB())
    result = context.execute_strategy(data)
