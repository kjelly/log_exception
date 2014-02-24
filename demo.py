import pickle
import json
from log_exception import Tracker


def show(obj):
    del obj['frame']
    del obj['code']
    obj['locals'] = str(obj['locals'])
    obj['globals'] = str(obj['globals'])
    print json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    Tracker(show).set_trace()
    pickle.loads('sss')
