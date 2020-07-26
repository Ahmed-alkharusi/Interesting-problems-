#pragma once
class Complex
{private:

public:
	double real{ 0 };
	double imaginary{ 0 };
	double re();
	double im();
	Complex operator+(const Complex& rhs);
	Complex operator*(const Complex& rhs);
	Complex &operator=(const Complex& rhs);
	Complex(double rhsReal, double rhsImaginary);

};

