#include "Matrix.h"
Matrix::Matrix(Array arr1, Array arr2) 
	:arr_x{ arr1 }, arr_y{ arr2 }{}

Matrix Matrix::operator +(double rhs) {
	Matrix temp{arr_x+rhs,arr_y+rhs};
	return temp;
}
Matrix Matrix::operator +(Matrix rhs) {
	Matrix temp{ arr_x + rhs.arr_x,arr_y + rhs.arr_y };
	return temp;
}

Matrix Matrix::operator*(double rhs) {
	Matrix temp{ arr_x * rhs,arr_y * rhs };
	return temp;
}
Matrix& Matrix::operator=(Matrix rhs) {
	this->arr_x = rhs.arr_x;
	this->arr_y = rhs.arr_y;
	return *this;
}
Matrix::Matrix(const Matrix& rhs)
	:arr_x{ rhs.arr_x }, arr_y{ rhs.arr_y }{}