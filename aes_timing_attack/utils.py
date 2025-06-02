import ctypes
import time
import numpy as np

libc = ctypes.CDLL("libc.so.6")

def flush(addr):
    libc.__builtin___clear_cache(ctypes.c_void_p(addr), ctypes.c_void_p(addr + 64))

def time_access(addr_ptr):
    start = time.perf_counter_ns()
    _ = addr_ptr[0]
    end = time.perf_counter_ns()
    return end - start
