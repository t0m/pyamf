# Copyright (c) The PyAMF Project.
# See LICENSE.txt for details.

"""
Python compatibility values and helpers.
"""
import operator

try:
    import __builtin__ as builtins
except ImportError:
    import builtins

try:
    import urllib2
    urlopen = urllib2.urlopen
    URLError = urllib2.URLError
    Request = urllib2.Request
    request_get_data = lambda r: r.get_data()
except ImportError:
    import urllib
    from urllib.request import urlopen
    URLError = urllib.request.URLError
    Request = urllib.request.Request
    request_get_data = lambda r: r.data



import types

func_types = (
    types.BuiltinFunctionType, types.BuiltinMethodType, types.CodeType,
    types.FunctionType, types.GeneratorType, types.LambdaType, types.MethodType)
class_types = [type]
int_types = [int]
str_types = [str, bytes]

try:
    int_types.append(long)
except NameError:
    pass

try:
    str_types.append(unicode)
except NameError:
    pass

scalar_types = tuple(int_types + str_types + [float])

try:
    class_types.append(types.ClassType)
except:
    pass


int_types = tuple(int_types)
str_types = tuple(str_types)
class_types = tuple(class_types)

PosInf = 1e300000
NegInf = -1e300000
# we do this instead of float('nan') because windows throws a wobbler.
NaN = PosInf / PosInf


def isNaN(val):
    """
    @since: 0.5
    """
    return str(float(val)) == str(NaN)


def isPosInf(val):
    """
    @since: 0.5
    """
    return str(float(val)) == str(PosInf)


def isNegInf(val):
    """
    @since: 0.5
    """
    return str(float(val)) == str(NegInf)

try:
    from types import TupleType
except ImportError:
    TupleType = tuple

try:
    import new
    new_module_func = new.module
except ImportError:
    import types
    new_module_func = types.ModuleType

try:
    callable = builtins.callable
except NameError:
    def callable(obj):
        """
        Compatibility function for Python 3.x
        """
        return hasattr(obj, '__call__')

if hasattr(lambda _:_, 'func_name'):
    get_func_name = operator.methodcaller('func_name')
else:
    get_func_name = lambda f: f.__name__

try:
    unicode_type = unicode
    bytes_type = str
except NameError:
    unicode_type = str
    bytes_type = bytes

if isinstance(chr(1), unicode_type):
    if hasattr(1, 'to_bytes'):
        int_to_byte = operator.methodcaller("to_bytes", 1, "big")
    else:
        int_to_byte = lambda i: bytes((i,))
else:
    int_to_byte = chr
    
    