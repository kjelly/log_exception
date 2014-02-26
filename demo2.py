import pickle
import json
import logging
from log_exception import Tracker
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


if __name__ == '__main__':
    Tracker(show).set_trace()
    a = 'sss'
    pickle.loads(a)
