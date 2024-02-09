from expression import Expression
from overrides import override


class OneExpression(Expression):
    @override
    def one(self) -> str:
        return 'I'

    @override
    def four(self) -> str:
        return 'IV'

    @override
    def five(self) -> str:
        return 'V'

    @override
    def nine(self) -> str:
        return 'IX'

    @override
    def multiplier(self) -> int:
        return 1
