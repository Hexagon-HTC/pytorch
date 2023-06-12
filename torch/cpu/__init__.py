from typing import Any, Optional
from . import amp


def is_available() -> bool:
    r"""Returns a bool indicating if CPU is currently available.

    N.B. This function only exists to facilitate device-agnostic code

    """
    return True

def synchronize(device=None) -> None:
    r"""Waits for all kernels in all streams on the CPU device to complete.

    Args:
        device (torch.device or int, optional): ignored, there's only one CPU device.

    N.B. This function only exists to facilitate device-agnostic code
    """
    pass

class Stream:
    """
    N.B. This class only exists to facilitate device-agnostic code
    """
    pass

_default_cpu_stream = Stream()
_current_stream = _default_cpu_stream

def current_stream(device=None) -> Stream:
    r"""Returns the currently selected :class:`Stream` for a given device.

    Args:
        device (torch.device or int, optional): Ignored.

    N.B. This function only exists to facilitate device-agnostic code

    """
    return _current_stream

class StreamContext:
    r"""Context-manager that selects a given stream.

    N.B. This class only exists to facilitate device-agnostic code

    """
    cur_stream : Optional['torch.cuda.Stream']

    def __init__(self, stream):
        self.stream = stream
        self.prev_stream = _default_cpu_stream

    def __enter__(self):
        cur_stream = self.stream
        if cur_stream is None:
            return

        global _current_stream
        self.prev_stream = _current_stream
        _current_stream = cur_stream

    def __exit__(self, type: Any, value: Any, traceback: Any):
        cur_stream = self.stream
        if cur_stream is None:
            return

        global _current_stream
        _current_stream = self.prev_stream

def stream(stream) -> StreamContext:
    r"""Wrapper around the Context-manager StreamContext that
    selects a given stream.

    N.B. This function only exists to facilitate device-agnostic code
    """
    return StreamContext(stream)

def device_count() -> int:
    r"""Returns number of CPU devices (not cores). Always 1.

    N.B. This function only exists to facilitate device-agnostic code
    """
    return 1
