import enum
from enum import Enum, auto

class EngineType(Enum):
    Presto = auto()
    Spark = auto()

    @staticmethod
    def from_str(engine_type: str):
        for e in EngineType:
            if e.name.lower() == engine_type.lower():
                return e
        raise TypeError("Invalid EngineType")

class JobStatus(enum.Enum):
    # enum.Enum 利用了meataClass 实现加每个属性时会调用__new__(); __init__(value)
    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        print('2. new value:', value, cls)
        obj._value_ = value
        return obj

    def __init__(self, label):
        print('3. init label:', label)
        self._label = label

    print('1. start')
    NEW = "NEW"
    RUNNING = "RUNNING"
    FINISHED = "FINISHED"

    @property
    def label(self):
        return self._label

    @staticmethod
    def from_str(status: str):
        for e in JobStatus:
            if e.label.lower() == status.lower():
                return e
        raise TypeError("Invalid JobStatus")

    @staticmethod
    def is_finished(status: 'JobStatus'):
        return status in (
            JobStatus.ANALYSIS_FAILED, JobStatus.COMPLETED, JobStatus.CANCELLED,
            JobStatus.FAILED)

    @staticmethod
    def is_failed(status: 'JobStatus'):
        return status in (JobStatus.ANALYSIS_FAILED, JobStatus.FAILED)

    @staticmethod
    def is_success(status: 'JobStatus'):
        return status == JobStatus.COMPLETED


#print('print label:',JobStatus.NEW.label)
