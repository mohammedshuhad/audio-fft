#ifndef FFT_HPP
#define FFT_HPP

#include <iostream>
#include <complex>

#define MAX 200
#define M_PI 3.1415926535897932384

int log2(int N);
int check(int n);
int reverse(int N, int n);
void ordina(std::complex<double>* f1, int N);
void transform(std::complex<double>* f, int N);
void FFT(std::complex<double>* f, int N, double d);

#endif