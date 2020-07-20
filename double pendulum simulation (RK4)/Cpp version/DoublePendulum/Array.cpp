#include "Array.h"
Array Array::operator+(double rhs) {
	Array temp(angle + rhs,angular_speed+ rhs);
	return temp;
}
Array Array::operator+(Array rhs) {
	Array temp(angle+ rhs.angle,angular_speed+ rhs.angular_speed);
	return temp;
}
Array Array::operator*(double rhs) {
	Array temp(angle * rhs,angular_speed* rhs);

	return temp;
}
Array &Array::operator=(Array rhs) {
	angle = rhs.angle;
	angular_speed = rhs.angular_speed;
	return *this;
}

Array::Array(double x_i, double y_i) 
	:angle{ x_i }, angular_speed{ y_i } {
}
Array::Array(const Array& rhs) :angle{ rhs.angle }, angular_speed{rhs.angular_speed } {}
