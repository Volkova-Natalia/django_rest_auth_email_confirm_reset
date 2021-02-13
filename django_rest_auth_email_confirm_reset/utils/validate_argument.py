"""
Checking that arguments belong to certain types.
You can specify several types,
    including undefined which means that the argument was not be passed into a function and it has default value

You can yse it like that:
@validate_type_argument
def function(*, kwarg1: str, kwarg2: types([dict, type(None), undefined])):
    pass
-----

Checking that an argument belongs to a certain subset of possible variants.

-----

Implementation using a decorator.
"""


from doctest import testmod


# --------------------------------------------------
class types(list):
    pass


class undefined(object):
    pass
# --------------------------------------------------


# --------------------------------------------------
def validate_type_argument(func):

    def wrapper(*args, **kwargs):
        # print('\nfunc.__annotations__', func.__annotations__)
        for name_argument, types_argument in func.__annotations__.items():
            if type(types_argument) is not types:
                types_argument = types([types_argument])
            if (name_argument not in kwargs) and (undefined in types_argument):
                continue
            if type(kwargs[name_argument]) not in types_argument:
                raise TypeError("'Argument '%s' for function %s%s must be type %s, not %s"
                                % (name_argument,
                                   func.__qualname__,
                                   func.__code__.co_varnames[:func.__code__.co_argcount],
                                   types_argument,
                                   type(kwargs[name_argument])))

        result = func(*args, **kwargs)
        return result

    return wrapper
# --------------------------------------------------


# --------------------------------------------------
@validate_type_argument
def validate_argument(*, name_argument: str, allowed_argument_values: list):

    def decorator(func):

        def wrapper(*args, **kwargs):
            # print('args                    ', args)
            # print('kwargs                  ', kwargs)
            # print('name_argument           ', name_argument)
            # print('allowed_argument_values ', allowed_argument_values)
            argument = kwargs[name_argument]
            if argument not in allowed_argument_values:
                raise ValueError(
                    "The argument '%s' of the function %s%s can not be '%s', it must be one of following: %s"
                    % (name_argument,
                       func.__qualname__,
                       func.__code__.co_varnames[:func.__code__.co_argcount],
                       argument, allowed_argument_values))

            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator
# --------------------------------------------------
