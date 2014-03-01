from .core import Tracker
from color import *


def show(obj):
    file_name = obj['file_name']
    lineno = obj['lineno']
    locals_var = obj['locals']
    source_code = obj['source_code']
    header = obj['header']

    print '---------'
    print_color('%s' % (header), bg=3)
    print_color('%s: %d -> %s' % (file_name, lineno, source_code), bg=2)
    print_color('%s' % (locals_var), bg=1)
    print_color('%s' % (source_code), bg=3)
    print '---------'


Tracker(show).set_trace()
