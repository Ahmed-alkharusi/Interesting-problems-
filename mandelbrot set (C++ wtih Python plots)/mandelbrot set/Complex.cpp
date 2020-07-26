#include "Complex.h"
double Complex::re() { return real; }
double Complex::im() { return imaginary; }
Complex Complex::operator+(const Complex& rhs) {
	Complex temp{real+rhs.real, imaginary+rhs.imaginary};
	return temp;
}

Complex::Complex(double rhsReal, double rhsImaginary) 
	: real{ rhsReal } , imaginary{ rhsImaginary } {
}
Complex &Complex::operator=(const Complex& rhs){
	real =rhs.real; 
	imaginary = rhs.imaginary;
	return *this;
}
Complex Complex::operator*(const Complex& rhs) {
	Complex temp{ real * rhs.real - imaginary * rhs.imaginary, real * rhs.imaginary + imaginary * rhs.real };
	return temp;
}