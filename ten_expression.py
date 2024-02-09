from expression import Expression
from overrides import override


class TenExpression(Expression):
    @override
    def one(self) -> str:
        return 'X'

    @override
    def four(self) -> str:
        return 'XL'

    @override
    def five(self) -> str:
        return 'L'

    @override
    def nine(self) -> str:
        return 'XC'

    @override
    def multiplier(self) -> int:
        return 10
