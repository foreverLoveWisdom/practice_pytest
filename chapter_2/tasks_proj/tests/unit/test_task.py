"""Test the Task data type."""
from tasks import Task


def tes_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task("do something", "okken", True, 21)
    t_dict = t_task._asdict()
