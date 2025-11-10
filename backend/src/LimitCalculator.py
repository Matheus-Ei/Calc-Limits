from sympy import symbols, limit, sympify, oo, E, sin, exp, log, Abs


class LimitCalculator:

    def __init__(self):
        pass

    def calculate(self, expression_str, variable_str, point_str, direction='both'):

        var = symbols(variable_str)

        try:
            expr = sympify(expression_str)
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")

        try:
            limit_point = sympify(point_str)
        except Exception as e:
            raise ValueError(f"Invalid limit point: {e}")

        dir_param = None
        if direction == 'right':
            dir_param = '+'
        elif direction == 'left':
            dir_param = '-'

        if dir_param:
            result = limit(expr, var, limit_point, dir=dir_param)
        else:
            result = limit(expr, var, limit_point)

        return result
