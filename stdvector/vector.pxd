from libcpp.vector cimport vector
cdef extern from "stdvector.h":
    cdef extern vector[float] get_a_vec()
