#include "Array.h"
Array Array::operator+(double rhs) {
	Array temp(position + rhs, speed + rhs);
	return temp;
}
Array Array::operator+(Array rhs) {
	Array temp(position + rhs.position, speed + rhs.speed);
	return temp;
}
Array Array::operator*(double rhs) {
	Array temp(position * rhs, speed * rhs);

	return temp;
}
Array& Array::operator=(Array rhs) {
	position = rhs.position;
	speed = rhs.speed;
	return *this;
}

Array::Array(double x_i, double y_i)
	:position{ x_i }, speed{ y_i } {
}
Array::Array(const Array& rhs) : position{ rhs.position }, speed{ rhs.speed } {}
