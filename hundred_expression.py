from expression import Expression
from overrides import override


class HundredExpression(Expression):
    @override
    def one(self) -> str:
        return 'C'

    @override
    def four(self) -> str:
        return 'CD'

    @override
    def five(self) -> str:
        return 'D'

    @override
    def nine(self) -> str:
        return 'CM'

    @override
    def multiplier(self) -> int:
        return 100
