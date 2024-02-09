from abc import ABC, abstractmethod
from context import Context


class Expression(ABC):
    def interpret(self, context: Context):
        if len(context.input) == 0:
            return

        if context.input.startswith(self.nine()):
            context.output = context.output + 9 * self.multiplier()
            context.input = context.input[2:]
            return

        if context.input.startswith(self.four()):
            context.output = context.output + 4 * self.multiplier()
            context.input = context.input[2:]
            return

        if context.input.startswith(self.five()):
            context.output = context.output + 5 * self.multiplier()
            context.input = context.input[1:]

        while context.input.startswith(self.one()):
            context.output = context.output + 1 * self.multiplier()
            context.input = context.input[1:]

    @abstractmethod
    def one(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def four(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def five(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def nine(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def multiplier(self) -> int:
        raise NotImplementedError
