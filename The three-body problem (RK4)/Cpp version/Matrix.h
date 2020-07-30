#pragma once
#include "Array.h"

class Matrix
{private:

public:
	Array arr_y{0,0};
	Array arr_x{ 0,0 };
	Matrix(Array arr1, Array arr2);
	Matrix operator +(double rhs);
	Matrix operator +(Matrix rhs);
	Matrix operator*(double rhs);
	Matrix& operator=(Matrix rhs);
	Matrix(const Matrix& rhs);
	
};

