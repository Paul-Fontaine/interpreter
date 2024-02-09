from expression import Expression
from overrides import override


class ThousandExpression(Expression):
    @override
    def one(self) -> str:
        return 'M'

    @override
    def four(self) -> str:
        return 'ME'

    @override
    def five(self) -> str:
        return 'E'

    @override
    def nine(self) -> str:
        return 'MJ'

    @override
    def multiplier(self) -> int:
        return 1000
