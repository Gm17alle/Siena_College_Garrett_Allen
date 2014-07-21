#!/usr/bin/env python

"""
Unit tests for scikits.cuda.linalg
"""

from unittest import main, makeSuite, TestCase, TestSuite

import pycuda.autoinit
import pycuda.gpuarray as gpuarray
import numpy as np

import scikits.cuda.linalg as linalg
import scikits.cuda.misc as misc

atol_float32 = 1e-6
atol_float64 = 1e-8

class test_linalg(TestCase):
    def setUp(self):
        linalg.init()

    def test_svd_ss_float32(self):
        a = np.asarray(np.random.randn(9, 6), np.float32)
        a_gpu = gpuarray.to_gpu(a)
        u_gpu, s_gpu, vh_gpu = linalg.svd(a_gpu, 's', 's')
        assert np.allclose(a, np.dot(u_gpu.get(),
                                     np.dot(np.diag(s_gpu.get()),
                                            vh_gpu.get())),
                           atol=atol_float32)  

    def test_svd_ss_float64(self):
        a = np.asarray(np.random.randn(9, 6), np.float64)
        a_gpu = gpuarray.to_gpu(a)
        u_gpu, s_gpu, vh_gpu = linalg.svd(a_gpu, 's', 's')
        assert np.allclose(a, np.dot(u_gpu.get(),
                                     np.dot(np.diag(s_gpu.get()),
                                            vh_gpu.get())),
                           atol=atol_float64)  

    def test_svd_ss_complex64(self):
        a = np.asarray(np.random.randn(9, 6) + 1j*np.random.randn(9, 6), np.complex64)
        a_gpu = gpuarray.to_gpu(a)
        u_gpu, s_gpu, vh_gpu = linalg.svd(a_gpu, 's', 's')
        assert np.allclose(a, np.dot(u_gpu.get(),
                                     np.dot(np.diag(s_gpu.get()),
                                            vh_gpu.get())),
                           atol=atol_float32)  

    def test_svd_ss_complex128(self):
        a = np.asarray(np.random.randn(9, 6) + 1j*np.random.randn(9, 6), np.complex128)
        a_gpu = gpuarray.to_gpu(a)
        u_gpu, s_gpu, vh_gpu = linalg.svd(a_gpu, 's', 's')
        assert np.allclose(a, np.dot(u_gpu.get(),
                                     np.dot(np.diag(s_gpu.get()),
                                            vh_gpu.get())),
                           atol=atol_float64)  

    def test_svd_so_float32(self):
        a = np.asarray(np.random.randn(6, 6), np.float32)
        a_gpu = gpuarray.to_gpu(a)
        u_gpu, s_gpu, vh_gpu = linalg.svd(a_gpu, 's', 'o')
        assert np.allclose(a, np.dot(u_gpu.get(),
                                     np.dot(np.diag(s_gpu.get()),
                                            vh_gpu.get())),
                           atol=atol_float32)  

    def test_svd_so_float64(self):
        a = np.asarray(np.random.randn(6, 6), np.float64)
        a_gpu = gpuarray.to_gpu(a)
        u_gpu, s_gpu, vh_gpu = linalg.svd(a_gpu, 's', 'o')
        assert np.allclose(a, np.dot(u_gpu.get(),
                                     np.dot(np.diag(s_gpu.get()),
                                            vh_gpu.get())),
                           atol=atol_float64)  

    def test_svd_so_complex64(self):
        a = np.asarray(np.random.randn(6, 6) + 1j*np.random.randn(6, 6), np.complex64)
        a_gpu = gpuarray.to_gpu(a)
        u_gpu, s_gpu, vh_gpu = linalg.svd(a_gpu, 's', 'o')
        assert np.allclose(a, np.dot(u_gpu.get(),
                                     np.dot(np.diag(s_gpu.get()),
                                            vh_gpu.get())),
                           atol=atol_float32)  

    def test_svd_so_complex128(self):
        a = np.asarray(np.random.randn(6, 6) + 1j*np.random.randn(6, 6), np.complex128)
        a_gpu = gpuarray.to_gpu(a)
        u_gpu, s_gpu, vh_gpu = linalg.svd(a_gpu, 's', 'o')
        assert np.allclose(a, np.dot(u_gpu.get(),
                                     np.dot(np.diag(s_gpu.get()),
                                            vh_gpu.get())),
                           atol=atol_float64)  

    def test_dot_matrix_float32(self):
        a = np.asarray(np.random.rand(4, 2), np.float32)
        b = np.asarray(np.random.rand(2, 2), np.float32)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c_gpu = linalg.dot(a_gpu, b_gpu)
        assert np.allclose(np.dot(a, b), c_gpu.get())

    def test_dot_matrix_float64(self):
        a = np.asarray(np.random.rand(4, 2), np.float64)
        b = np.asarray(np.random.rand(2, 2), np.float64)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c_gpu = linalg.dot(a_gpu, b_gpu)
        assert np.allclose(np.dot(a, b), c_gpu.get())

    def test_dot_matrix_complex64(self):
        a = np.asarray(np.random.rand(4, 2), np.complex64)
        b = np.asarray(np.random.rand(2, 2), np.complex64)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c_gpu = linalg.dot(a_gpu, b_gpu)
        assert np.allclose(np.dot(a, b), c_gpu.get())

    def test_dot_matrix_complex128(self):
        a = np.asarray(np.random.rand(4, 2), np.complex128)
        b = np.asarray(np.random.rand(2, 2), np.complex128)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c_gpu = linalg.dot(a_gpu, b_gpu)
        assert np.allclose(np.dot(a, b), c_gpu.get())

    def test_dot_matrix_t_float32(self):
        a = np.asarray(np.random.rand(2, 4), np.float32)
        b = np.asarray(np.random.rand(2, 2), np.float32)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c_gpu = linalg.dot(a_gpu, b_gpu, 't')
        assert np.allclose(np.dot(a.T, b), c_gpu.get())

    def test_dot_matrix_t_float64(self):
        a = np.asarray(np.random.rand(2, 4), np.float64)
        b = np.asarray(np.random.rand(2, 2), np.float64)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c_gpu = linalg.dot(a_gpu, b_gpu, 't')
        assert np.allclose(np.dot(a.T, b), c_gpu.get())

    def test_dot_matrix_t_complex64(self):
        a = np.asarray(np.random.rand(2, 4), np.complex64)
        b = np.asarray(np.random.rand(2, 2), np.complex64)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c_gpu = linalg.dot(a_gpu, b_gpu, 't')
        assert np.allclose(np.dot(a.T, b), c_gpu.get())

    def test_dot_matrix_t_complex128(self):
        a = np.asarray(np.random.rand(2, 4), np.complex128)
        b = np.asarray(np.random.rand(2, 2), np.complex128)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c_gpu = linalg.dot(a_gpu, b_gpu, 't')
        assert np.allclose(np.dot(a.T, b), c_gpu.get())

    def test_dot_matrix_h_complex64(self):
        a = np.asarray(np.random.rand(2, 4)+1j*np.random.rand(2, 4), np.complex64)
        b = np.asarray(np.random.rand(2, 2)+1j*np.random.rand(2, 2), np.complex64)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c_gpu = linalg.dot(a_gpu, b_gpu, 'c')
        assert np.allclose(np.dot(a.conj().T, b), c_gpu.get())

    def test_dot_matrix_h_complex128(self):
        a = np.asarray(np.random.rand(2, 4)+1j*np.random.rand(2, 4), np.complex128)
        b = np.asarray(np.random.rand(2, 2)+1j*np.random.rand(2, 2), np.complex128)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c_gpu = linalg.dot(a_gpu, b_gpu, 'c')
        assert np.allclose(np.dot(a.conj().T, b), c_gpu.get())

    def test_dot_vector_float32(self):
        a = np.asarray(np.random.rand(5), np.float32)
        b = np.asarray(np.random.rand(5), np.float32)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c = linalg.dot(a_gpu, b_gpu)
        assert np.allclose(np.dot(a, b), c)

    def test_dot_vector_float64(self):
        a = np.asarray(np.random.rand(5), np.float64)
        b = np.asarray(np.random.rand(5), np.float64)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c = linalg.dot(a_gpu, b_gpu)
        assert np.allclose(np.dot(a, b), c)

    def test_dot_vector_complex64(self):
        a = np.asarray(np.random.rand(5), np.complex64)
        b = np.asarray(np.random.rand(5), np.complex64)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c = linalg.dot(a_gpu, b_gpu)
        assert np.allclose(np.dot(a, b), c)

    def test_dot_vector_complex128(self):
        a = np.asarray(np.random.rand(5), np.complex128)
        b = np.asarray(np.random.rand(5), np.complex128)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c = linalg.dot(a_gpu, b_gpu)
        assert np.allclose(np.dot(a, b), c)

    def test_mdot_matrix_float32(self):
        a = np.asarray(np.random.rand(4, 2), np.float32)
        b = np.asarray(np.random.rand(2, 2), np.float32)
        c = np.asarray(np.random.rand(2, 2), np.float32)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c_gpu = gpuarray.to_gpu(c)
        d_gpu = linalg.mdot(a_gpu, b_gpu, c_gpu)
        assert np.allclose(np.dot(a, np.dot(b, c)), d_gpu.get())

    def test_mdot_matrix_float64(self):
        a = np.asarray(np.random.rand(4, 2), np.float64)
        b = np.asarray(np.random.rand(2, 2), np.float64)
        c = np.asarray(np.random.rand(2, 2), np.float64)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c_gpu = gpuarray.to_gpu(c)
        d_gpu = linalg.mdot(a_gpu, b_gpu, c_gpu)
        assert np.allclose(np.dot(a, np.dot(b, c)), d_gpu.get())

    def test_mdot_matrix_complex64(self):
        a = np.asarray(np.random.rand(4, 2), np.complex64)
        b = np.asarray(np.random.rand(2, 2), np.complex64)
        c = np.asarray(np.random.rand(2, 2), np.complex64)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c_gpu = gpuarray.to_gpu(c)
        d_gpu = linalg.mdot(a_gpu, b_gpu, c_gpu)
        assert np.allclose(np.dot(a, np.dot(b, c)), d_gpu.get())

    def test_mdot_matrix_complex128(self):
        a = np.asarray(np.random.rand(4, 2), np.complex128)
        b = np.asarray(np.random.rand(2, 2), np.complex128)
        c = np.asarray(np.random.rand(2, 2), np.complex128)
        a_gpu = gpuarray.to_gpu(a)
        b_gpu = gpuarray.to_gpu(b)
        c_gpu = gpuarray.to_gpu(c)
        d_gpu = linalg.mdot(a_gpu, b_gpu, c_gpu)
        assert np.allclose(np.dot(a, np.dot(b, c)), d_gpu.get())
 
    def test_dot_diag_float32(self):
        d = np.asarray(np.random.rand(5), np.float32)
        a = np.asarray(np.random.rand(5, 3), np.float32)
        d_gpu = gpuarray.to_gpu(d)
        a_gpu = gpuarray.to_gpu(a)
        r_gpu = linalg.dot_diag(d_gpu, a_gpu)
        assert np.allclose(np.dot(np.diag(d), a), r_gpu.get())

    def test_dot_diag_float64(self):
        d = np.asarray(np.random.rand(5), np.float64)
        a = np.asarray(np.random.rand(5, 3), np.float64)
        d_gpu = gpuarray.to_gpu(d)
        a_gpu = gpuarray.to_gpu(a)
        r_gpu = linalg.dot_diag(d_gpu, a_gpu)
        assert np.allclose(np.dot(np.diag(d), a), r_gpu.get())

    def test_dot_diag_complex64(self):
        d = np.asarray(np.random.rand(5), np.float32)
        a = np.asarray(np.random.rand(5, 3)+1j*np.random.rand(5, 3), np.complex64)
        d_gpu = gpuarray.to_gpu(d)
        a_gpu = gpuarray.to_gpu(a)
        r_gpu = linalg.dot_diag(d_gpu, a_gpu)
        assert np.allclose(np.dot(np.diag(d), a), r_gpu.get())

    def test_dot_diag_complex128(self):
        d = np.asarray(np.random.rand(5), np.float64)
        a = np.asarray(np.random.rand(5, 3)+1j*np.random.rand(5, 3), np.complex128)
        d_gpu = gpuarray.to_gpu(d)
        a_gpu = gpuarray.to_gpu(a)
        r_gpu = linalg.dot_diag(d_gpu, a_gpu)
        assert np.allclose(np.dot(np.diag(d), a), r_gpu.get())

    def test_dot_diag_t_float32(self):
        d = np.asarray(np.random.rand(5), np.float32)
        a = np.asarray(np.random.rand(3, 5), np.float32)
        d_gpu = gpuarray.to_gpu(d)
        a_gpu = gpuarray.to_gpu(a)
        r_gpu = linalg.dot_diag(d_gpu, a_gpu, 't')
        assert np.allclose(np.dot(np.diag(d), a.T).T, r_gpu.get())

    def test_dot_diag_t_float64(self):
        d = np.asarray(np.random.rand(5), np.float64)
        a = np.asarray(np.random.rand(3, 5), np.float64)
        d_gpu = gpuarray.to_gpu(d)
        a_gpu = gpuarray.to_gpu(a)
        r_gpu = linalg.dot_diag(d_gpu, a_gpu, 't')
        assert np.allclose(np.dot(np.diag(d), a.T).T, r_gpu.get())

    def test_dot_diag_t_complex64(self):
        d = np.asarray(np.random.rand(5), np.float32)
        a = np.asarray(np.random.rand(3, 5)+1j*np.random.rand(3, 5), np.complex64)
        d_gpu = gpuarray.to_gpu(d)
        a_gpu = gpuarray.to_gpu(a)
        r_gpu = linalg.dot_diag(d_gpu, a_gpu, 't')
        assert np.allclose(np.dot(np.diag(d), a.T).T, r_gpu.get())

    def test_dot_diag_t_complex128(self):
        d = np.asarray(np.random.rand(5), np.float64)
        a = np.asarray(np.random.rand(3, 5)+1j*np.random.rand(3, 5), np.complex128)
        d_gpu = gpuarray.to_gpu(d)
        a_gpu = gpuarray.to_gpu(a)
        r_gpu = linalg.dot_diag(d_gpu, a_gpu, 't')
        assert np.allclose(np.dot(np.diag(d), a.T).T, r_gpu.get())
                          
    def test_transpose_float32(self):
        a = np.array([[1, 2, 3, 4, 5, 6],
                      [7, 8, 9, 10, 11, 12]],
                     np.float32)
        a_gpu = gpuarray.to_gpu(a)
        at_gpu = linalg.transpose(a_gpu)
        assert np.all(a.T == at_gpu.get())

    def test_transpose_float64(self):
        a = np.array([[1, 2, 3, 4, 5, 6],
                      [7, 8, 9, 10, 11, 12]],
                     np.float64)
        a_gpu = gpuarray.to_gpu(a)
        at_gpu = linalg.transpose(a_gpu)
        assert np.all(a.T == at_gpu.get())

    def test_transpose_complex64(self):
        a = np.array([[1j, 2j, 3j, 4j, 5j, 6j],
                      [7j, 8j, 9j, 10j, 11j, 12j]],
                     np.complex64)
        a_gpu = gpuarray.to_gpu(a)
        at_gpu = linalg.transpose(a_gpu)
        assert np.all(a.T == at_gpu.get())

    def test_transpose_complex128(self):
        a = np.array([[1j, 2j, 3j, 4j, 5j, 6j],
                      [7j, 8j, 9j, 10j, 11j, 12j]],
                     np.complex128)
        a_gpu = gpuarray.to_gpu(a)
        at_gpu = linalg.transpose(a_gpu)
        assert np.all(a.T == at_gpu.get())

    def test_hermitian_float32(self):
        a = np.array([[1, 2, 3, 4, 5, 6],
                      [7, 8, 9, 10, 11, 12]],
                     np.float32)
        a_gpu = gpuarray.to_gpu(a)
        at_gpu = linalg.hermitian(a_gpu)
        assert np.all(a.T == at_gpu.get())

    def test_hermitian_complex64(self):
        a = np.array([[1j, 2j, 3j, 4j, 5j, 6j],
                      [7j, 8j, 9j, 10j, 11j, 12j]],
                     np.complex64)
        a_gpu = gpuarray.to_gpu(a)
        at_gpu = linalg.hermitian(a_gpu)
        assert np.all(np.conj(a.T) == at_gpu.get())

    def test_hermitian_float64(self):
        a = np.array([[1, 2, 3, 4, 5, 6],
                      [7, 8, 9, 10, 11, 12]],
                     np.float64)
        a_gpu = gpuarray.to_gpu(a)
        at_gpu = linalg.hermitian(a_gpu)
        assert np.all(a.T == at_gpu.get())

    def test_hermitian_complex128(self):
        a = np.array([[1j, 2j, 3j, 4j, 5j, 6j],
                      [7j, 8j, 9j, 10j, 11j, 12j]],
                     np.complex128)
        a_gpu = gpuarray.to_gpu(a)
        at_gpu = linalg.hermitian(a_gpu)
        assert np.all(np.conj(a.T) == at_gpu.get())

    def test_conj_complex64(self):
        a = np.array([[1+1j, 2-2j, 3+3j, 4-4j],
                      [5+5j, 6-6j, 7+7j, 8-8j]], np.complex64)
        a_gpu = gpuarray.to_gpu(a)
        linalg.conj(a_gpu)
        assert np.all(np.conj(a) == a_gpu.get())

    def test_conj_complex128(self):
        a = np.array([[1+1j, 2-2j, 3+3j, 4-4j],
                      [5+5j, 6-6j, 7+7j, 8-8j]], np.complex128)
        a_gpu = gpuarray.to_gpu(a)
        linalg.conj(a_gpu)
        assert np.all(np.conj(a) == a_gpu.get())

    def test_diag_float32(self):
        v = np.array([1, 2, 3, 4, 5, 6], np.float32)
        v_gpu = gpuarray.to_gpu(v)
        d_gpu = linalg.diag(v_gpu)
        assert np.all(np.diag(v) == d_gpu.get())

    def test_diag_float64(self):
        v = np.array([1, 2, 3, 4, 5, 6], np.float64)
        v_gpu = gpuarray.to_gpu(v)
        d_gpu = linalg.diag(v_gpu)
        assert np.all(np.diag(v) == d_gpu.get())

    def test_diag_complex64(self):
        v = np.array([1j, 2j, 3j, 4j, 5j, 6j], np.complex64)
        v_gpu = gpuarray.to_gpu(v)
        d_gpu = linalg.diag(v_gpu)
        assert np.all(np.diag(v) == d_gpu.get())

    def test_diag_complex128(self):
        v = np.array([1j, 2j, 3j, 4j, 5j, 6j], np.complex128)
        v_gpu = gpuarray.to_gpu(v)
        d_gpu = linalg.diag(v_gpu)
        assert np.all(np.diag(v) == d_gpu.get())

    def test_eye_float32(self):
        N = 10
        e_gpu = linalg.eye(N, dtype=np.float32)
        assert np.all(np.eye(N, dtype=np.float32) == e_gpu.get())

    def test_eye_float64(self):
        N = 10
        e_gpu = linalg.eye(N, dtype=np.float64)
        assert np.all(np.eye(N, dtype=np.float64) == e_gpu.get())

    def test_eye_complex64(self):
        N = 10
        e_gpu = linalg.eye(N, dtype=np.complex64)
        assert np.all(np.eye(N, dtype=np.complex64) == e_gpu.get())

    def test_eye_complex128(self):
        N = 10
        e_gpu = linalg.eye(N, dtype=np.complex128)
        assert np.all(np.eye(N, dtype=np.complex128) == e_gpu.get())

    def test_pinv_float32(self):
        a = np.asarray(np.random.rand(8, 4), np.float32)
        a_gpu = gpuarray.to_gpu(a)
        a_inv_gpu = linalg.pinv(a_gpu)
        assert np.allclose(np.linalg.pinv(a), a_inv_gpu.get(),
                           atol=atol_float32)   

    def test_pinv_float64(self):
        a = np.asarray(np.random.rand(8, 4), np.float64)
        a_gpu = gpuarray.to_gpu(a)
        a_inv_gpu = linalg.pinv(a_gpu)
        assert np.allclose(np.linalg.pinv(a), a_inv_gpu.get(),
                           atol=atol_float64)   

    def test_pinv_complex64(self):
        a = np.asarray(np.random.rand(8, 4) + \
                       1j*np.random.rand(8, 4), np.complex64)
        a_gpu = gpuarray.to_gpu(a)
        a_inv_gpu = linalg.pinv(a_gpu)
        assert np.allclose(np.linalg.pinv(a), a_inv_gpu.get(),
                           atol=atol_float32)   

    def test_pinv_complex128(self):
        a = np.asarray(np.random.rand(8, 4) + \
                       1j*np.random.rand(8, 4), np.complex128)
        a_gpu = gpuarray.to_gpu(a)
        a_inv_gpu = linalg.pinv(a_gpu)
        assert np.allclose(np.linalg.pinv(a), a_inv_gpu.get(),
                           atol=atol_float64)   

    def test_tril_float32(self):
        a = np.asarray(np.random.rand(4, 4), np.float32)
        a_gpu = gpuarray.to_gpu(a)
        l_gpu = linalg.tril(a_gpu)
        assert np.allclose(np.tril(a), l_gpu.get())   

    def test_tril_float64(self):
        a = np.asarray(np.random.rand(4, 4), np.float64)
        a_gpu = gpuarray.to_gpu(a)
        l_gpu = linalg.tril(a_gpu)
        assert np.allclose(np.tril(a), l_gpu.get())   

    def test_tril_complex64(self):
        a = np.asarray(np.random.rand(4, 4), np.complex64)
        a_gpu = gpuarray.to_gpu(a)
        l_gpu = linalg.tril(a_gpu)
        assert np.allclose(np.tril(a), l_gpu.get())   

    def test_tril_complex128(self):
        a = np.asarray(np.random.rand(4, 4), np.complex128)
        a_gpu = gpuarray.to_gpu(a)
        l_gpu = linalg.tril(a_gpu)
        assert np.allclose(np.tril(a), l_gpu.get())   

    def test_multiply_float32(self):
        x = np.asarray(np.random.rand(4, 4), np.float32)
        y = np.asarray(np.random.rand(4, 4), np.float32)
        x_gpu = gpuarray.to_gpu(x)
        y_gpu = gpuarray.to_gpu(y)
        z_gpu = linalg.multiply(x_gpu, y_gpu)
        assert np.allclose(x*y, z_gpu.get())   

    def test_multiply_float64(self):
        x = np.asarray(np.random.rand(4, 4), np.float64)
        y = np.asarray(np.random.rand(4, 4), np.float64)
        x_gpu = gpuarray.to_gpu(x)
        y_gpu = gpuarray.to_gpu(y)
        z_gpu = linalg.multiply(x_gpu, y_gpu)
        assert np.allclose(x*y, z_gpu.get())   

    def test_multiply_complex64(self):
        x = np.asarray(np.random.rand(4, 4) + 1j*np.random.rand(4, 4), np.complex64)
        y = np.asarray(np.random.rand(4, 4) + 1j*np.random.rand(4, 4), np.complex64)
        x_gpu = gpuarray.to_gpu(x)
        y_gpu = gpuarray.to_gpu(y)
        z_gpu = linalg.multiply(x_gpu, y_gpu)
        assert np.allclose(x*y, z_gpu.get())   

    def test_multiply_complex128(self):
        x = np.asarray(np.random.rand(4, 4) + 1j*np.random.rand(4, 4), np.complex128)
        y = np.asarray(np.random.rand(4, 4) + 1j*np.random.rand(4, 4), np.complex128)
        x_gpu = gpuarray.to_gpu(x)
        y_gpu = gpuarray.to_gpu(y)
        z_gpu = linalg.multiply(x_gpu, y_gpu)
        assert np.allclose(x*y, z_gpu.get())   


def suite():
    s = TestSuite()
    s.addTest(test_linalg('test_svd_ss_float32'))
    s.addTest(test_linalg('test_svd_ss_complex64'))
    s.addTest(test_linalg('test_svd_so_float32'))
    s.addTest(test_linalg('test_svd_so_complex64'))
    s.addTest(test_linalg('test_dot_matrix_float32'))
    s.addTest(test_linalg('test_dot_matrix_complex64'))
    s.addTest(test_linalg('test_dot_matrix_t_float32'))
    s.addTest(test_linalg('test_dot_matrix_t_complex64'))
    s.addTest(test_linalg('test_dot_matrix_h_complex64'))
    s.addTest(test_linalg('test_dot_vector_float32'))
    s.addTest(test_linalg('test_dot_vector_complex64'))
    s.addTest(test_linalg('test_mdot_matrix_float32'))
    s.addTest(test_linalg('test_mdot_matrix_complex64'))
    s.addTest(test_linalg('test_dot_diag_float32'))
    s.addTest(test_linalg('test_dot_diag_complex64'))
    s.addTest(test_linalg('test_dot_diag_t_float32'))
    s.addTest(test_linalg('test_dot_diag_t_complex64'))
    s.addTest(test_linalg('test_transpose_float32'))
    s.addTest(test_linalg('test_transpose_complex64'))
    s.addTest(test_linalg('test_hermitian_float32'))
    s.addTest(test_linalg('test_hermitian_complex64'))
    s.addTest(test_linalg('test_conj_complex64'))
    s.addTest(test_linalg('test_diag_float32'))
    s.addTest(test_linalg('test_diag_complex64'))
    s.addTest(test_linalg('test_eye_float32'))
    s.addTest(test_linalg('test_eye_complex64'))
    s.addTest(test_linalg('test_pinv_float32'))
    s.addTest(test_linalg('test_pinv_complex64'))
    s.addTest(test_linalg('test_tril_float32'))
    s.addTest(test_linalg('test_tril_complex64'))
    s.addTest(test_linalg('test_multiply_float32'))
    s.addTest(test_linalg('test_multiply_complex64'))
    if misc.get_compute_capability(pycuda.autoinit.device) >= 1.3:
        s.addTest(test_linalg('test_svd_ss_float64'))
        s.addTest(test_linalg('test_svd_ss_complex128'))
        s.addTest(test_linalg('test_svd_so_float64'))
        s.addTest(test_linalg('test_svd_so_complex128'))
        s.addTest(test_linalg('test_dot_matrix_float64'))
        s.addTest(test_linalg('test_dot_matrix_complex128'))
        s.addTest(test_linalg('test_dot_matrix_t_float64'))
        s.addTest(test_linalg('test_dot_matrix_t_complex128'))
        s.addTest(test_linalg('test_dot_matrix_h_complex128'))
        s.addTest(test_linalg('test_dot_vector_float64'))
        s.addTest(test_linalg('test_dot_vector_complex128'))
        s.addTest(test_linalg('test_mdot_matrix_float64'))
        s.addTest(test_linalg('test_mdot_matrix_complex128'))
        s.addTest(test_linalg('test_dot_diag_float64'))
        s.addTest(test_linalg('test_dot_diag_complex128'))
        s.addTest(test_linalg('test_dot_diag_t_float64'))
        s.addTest(test_linalg('test_dot_diag_t_complex128'))
        s.addTest(test_linalg('test_transpose_float64'))
        s.addTest(test_linalg('test_transpose_complex128'))
        s.addTest(test_linalg('test_hermitian_float64'))
        s.addTest(test_linalg('test_hermitian_complex64'))
        s.addTest(test_linalg('test_conj_complex128'))
        s.addTest(test_linalg('test_diag_float64'))
        s.addTest(test_linalg('test_diag_complex128'))
        s.addTest(test_linalg('test_eye_float64'))
        s.addTest(test_linalg('test_eye_complex128'))
        s.addTest(test_linalg('test_pinv_float64'))
        s.addTest(test_linalg('test_pinv_complex128'))        
        s.addTest(test_linalg('test_tril_float64'))
        s.addTest(test_linalg('test_tril_complex128'))
        s.addTest(test_linalg('test_multiply_float64'))
        s.addTest(test_linalg('test_multiply_complex128'))
    return s

if __name__ == '__main__':
    main(defaultTest = 'suite')
