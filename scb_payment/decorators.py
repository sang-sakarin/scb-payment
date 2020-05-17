from functools import wraps
from .error import SCBPaymentError


def check_in_kwargs(kwarg_names):
    """
    check if the wrapped function's class have the specified kwargs
    :param kwarg_names: array of kwargs names to check
    :return:
    """
    def layer(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            for kwarg in kwarg_names:
                if kwarg not in kwargs:
                    raise SCBPaymentError('"{0}" attrs is required'.format(kwarg))
            return func(self, *args, **kwargs)
        return wrapper
    return layer
