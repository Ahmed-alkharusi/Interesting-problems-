/*
 =============================================================================
 Simulating the double pendulum using Runge–Kutta method(RK4)
 =============================================================================

Updated on Mon Jul 20 2020
@author: Ahmed Alkharusi*/





#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <string>
#include "Array.h"


const double m1{ 1.0 }; //mass of the 1st pendulum 
const double m2{ 1.0 }; //mass of the 2nd pendulum 
const double g{ 10.0 }; //gravity
const double r1{ 1.0 }; //length of the 1st pendulum   
const double r2{ 1.0 }; //length of the 2nd pendulum   
const double pi{ 3.14159265359 };



Array deriv_a1(Array a1_arr, Array a2_arr, Array t);
Array deriv_a2(Array a2_arr, Array a1_arr, Array t);
void rk4(Array(*deriv)(Array, Array, Array), Array &func_i, Array &func_i2, double &x_i, const double h);
void output_matrix(std::vector<std::vector<double>> matrix, std::string&& file_name);


int main() {
	
	const double step_size{ 0.001 };//step size for the RK4 method
	const long unsigned int steps_no { 6000000 };//number of steps of the RK4 method
	//initial conditions
	double t{ 0 };
	Array a1_arr{ pi/2 , -3 };
	Array a2_arr{ pi/2 , 3 };

	std::vector<double> time_arr{ t };
	std::vector<std::vector<double>> Pendulum1_results;
	std::vector<std::vector<double>> Pendulum2_results;
	
	std::vector<double> temp_Pendulum2_results{t, a2_arr.angle};
	std::vector<double> temp_Pendulum1_results{t, a1_arr.angle};

	Pendulum2_results.push_back(temp_Pendulum2_results);
	Pendulum1_results.push_back(temp_Pendulum1_results);
	
	
	for (size_t i{ 0 }; i < steps_no;i++) {
		Array temp = a1_arr;
		rk4(&deriv_a1, a1_arr, a2_arr, t, step_size);
		t -= step_size;
		rk4(&deriv_a2, a2_arr, temp, t, step_size);
		temp_Pendulum2_results[0]= temp_Pendulum1_results[0]= t;
		temp_Pendulum2_results[1] = a2_arr.angle; // can output the angular speed by changing this from .angle -> .angular_speed
		temp_Pendulum1_results[1] = a1_arr.angle; // can output the angular speed by changing this from .angle -> .angular_speed
		Pendulum2_results.push_back(temp_Pendulum2_results);
		Pendulum1_results.push_back(temp_Pendulum1_results);
	}
	output_matrix(Pendulum1_results,"Pendulum1_results.txt"); //outputs to cols. 1st is the time, 2nd is the angle 
	output_matrix(Pendulum2_results, "Pendulum2_results.txt");
	return 0;
}

Array deriv_a1(Array a1_arr, Array a2_arr, Array t) {
	double num = -g * (2 * m1 + m2) * std::sin(a1_arr.angle) - m2 * g * std::sin(a1_arr.angle - 2 * a2_arr.angle) - 2 * m2 * std::sin(a1_arr.angle - a2_arr.angle) * (r2 * std::pow(a2_arr.angular_speed, 2) + r1 * std::pow(a1_arr.angular_speed, 2) * std::cos(a1_arr.angle - a2_arr.angle));
	double den = r1 * (2 * m1 + m2 - m2 * std::cos(2 * a1_arr.angle - 2 * a2_arr.angle));
	// (num / den) is the angular speed
	Array temp{ a1_arr.angular_speed,num/den };
	return  temp;
}
Array deriv_a2(Array a2_arr, Array a1_arr, Array t) { 
	double temp = (2 * std::sin(a1_arr.angle - a2_arr.angle));
	double num = temp * (r1 * std::pow(a1_arr.angular_speed, 2) * (m1 + m2) + g * (m1 + m2) * std::cos(a1_arr.angle) + r2 * std::pow(a2_arr.angular_speed, 2) * m2 * std::cos(a1_arr.angle - a2_arr.angle));
	double den = r2 * (2 * m1 + m2 - m2 * std::cos(2 * a1_arr.angle - 2 * a2_arr.angle));
	// (num / den) is the angular speed
	Array res{ a2_arr.angular_speed, num / den };
	return  res;
}

void rk4(Array(*deriv)(Array, Array, Array), Array& func_i, Array& func_i2, double& x_i, const double h) {
	Array k1 = deriv(func_i, func_i2, (k1*0)+x_i);
	Array k2 = deriv(func_i + h / 2, func_i2,  k1 * (h/ 2) );
	Array k3 = deriv(func_i + h / 2, func_i2, k2 * (h / 2));
	Array k4 = deriv(func_i + h, func_i2, k3 * h);
	func_i = func_i + ((k1 + (k2 * 2) + (k3 * 2) + k4)) * (h / 6);
	x_i += h;
}
void output_matrix(std::vector<std::vector<double>> matrix, std::string &&file_name) {
	std::ofstream output_file(file_name);
	for (size_t i{ 0 };i < matrix.size();i++) {
		for (size_t j{ 0 };j < (matrix.at(i)).size();j++) {
			output_file << (matrix.at(i)).at(j) << " ";
		}
		output_file << "\n";
	}
}
/*
 =============================================================================
 Please check the answers!!!
 =============================================================================
References:

#Implementing the RK4 method in Python 
https://youtu.be/mqoqAovXxWA
by Prof. Niels Walet  

#The formulas for the angular acceleration 
https://www.myphysicslab.com/pendulum/double-pendulum-en.html
    
#Animating the double pendulum (N.B. the implementation used here is different)
https://matplotlib.org/3.2.1/gallery/animation/double_pendulum_sgskip.html

*/



