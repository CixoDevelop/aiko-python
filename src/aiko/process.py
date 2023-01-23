from enum import Enum
from .message_box import message_box_t


class process_types_t(Enum):
    REACTIVE = 0
    CONTINUOUS = 1
    SIGNAL = 2


class process_t:
    def __init__(self, process_pid, process_type, worker, parameter):
        self.__process_pid = process_pid
        self.process_type = process_type
        self.worker = worker
        self.parameter = parameter
        self.message_box = message_box_t()


    def get_pid(self):
        return self.__process_pid


    def get_type(self):
        return self.process_type
