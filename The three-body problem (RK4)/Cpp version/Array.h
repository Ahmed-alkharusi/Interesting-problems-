#pragma once
class Array


{
public:
	double position{ 0 };
	double speed{ 0 };
	Array(double x_i, double y_i);
	Array operator+(double rhs);
	Array operator+(Array rhs);
	Array operator*(double rhs);
	Array(const Array& rhs);
	Array& operator=(Array rhs);
};

