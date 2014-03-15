import sys
import logging
import copy


def try_copy(data):
    # some inner structure use dict.
    if isinstance(data, dict):
        ret = {}
        for i in data:
            new_copy = try_copy(data[i])
            if new_copy:
                ret[i] = new_copy
        return ret
    else:
        try:
            # copy data
            return copy.deepcopy(data)
        except Exception as e:
            # if the data can't be copied
            pass
    # just return data.
    return data


def read_source_code_from_file(file_name, lineno):
    if not os.path.exists(file_name):
        return ''
    with open(file_name, 'r') as ftr:
        source_code = ftr.readlines()
        return source_code[lineno - 1].strip()


class Tracker(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Tracker, cls).__new__(cls, *args, **kwargs)
            cls._instance.callback_list = []
        return cls._instance

    def __init__(self, callback):
        self.callback_list.append(callback)

    def trace(self, frame, event, arg):
        if event in ['exception', 'c_exception']:
            code = frame.f_code
            name = code.co_name
            data = {}
            data['name'] = code.co_name
            if name[0] != '<':
                data['header'] = read_source_code_from_file(
                    code.co_filename, code.co_firstlineno)
            else:
                data['header'] = '<None>'
            data['file_name'] = code.co_filename
            data['lineno'] = frame.f_lineno
            data['source_code'] = read_source_code_from_file(
                code.co_filename, frame.f_lineno)
            data['locals'] = frame.f_locals
            data['globals'] = frame.f_globals
            data['code'] = code
            data['frame'] = frame
            for callback in self.callback_list:
                callback(try_copy(data))
        return self.trace

    def set_trace(self):
        frame = sys._getframe().f_back
        while frame:
            frame.f_trace = self.trace
            frame = frame.f_back
        sys.settrace(self.trace)
