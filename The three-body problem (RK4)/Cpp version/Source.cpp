/*
=============================================================================
 Solving the three - body problem numerically using the RK4
 =============================================================================
Created on Jul 30 2020
@author: Ahmed Alkharusi*/
#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>
#include <time.h>
#include "Array.h"
#include "Matrix.h"



void output_matrix(std::vector < std::vector<std::vector<double>>> result_obj, std::string&& file_name);
Matrix deriv(Matrix obj_active, Matrix obj_passive1, double mp1, Matrix obj_passive2, double mp2);
void rk4(Matrix(*deriv)(Matrix, Matrix,double, Matrix, double), Matrix &obj_active, Matrix &obj_passive1, double mp1, Matrix &obj_passive2, double mp2, const double h);
void implement_rk4(Matrix(*deriv)(Matrix, Matrix, double, Matrix, double),Matrix &obj_1,double &m1,Matrix &obj_2, double m2, Matrix &obj_3, double m3,double t, double step_size,double steps_no, std::vector<std::vector<std::vector<double>>> &result_obj1, std::vector<std::vector<std::vector<double>>> &result_obj2, std::vector<std::vector<std::vector<double>>> &result_obj3);

int main() {
	
	const double step_size{ 1.0/100000.0 };//step size for the RK4 method
	const long unsigned int steps_no{ 1000000 };//number of steps of the RK4 method
	//initial conditions (play around with these)
	double t{ 0 };
	double m1{ 1 };
	double m2{ 1 };
	double m3{ 1 };

	Matrix obj_1{ Array{0,0},  Array{0,0} };
	Matrix obj_2{ Array{1.5*pow(2.0,0.5),0}, Array{-0.5,0} };
	Matrix obj_3{ Array{pow(2.0,0.5)/2,0}, Array{3*pow(3.0/2.0,0.5),0} };

	//double v1{ 0.213841083 };
	//double v2{ 0.054293840 };
	//Matrix obj_1 {Array{-1,v1},  Array{0,v2}};
	//Matrix obj_2 {Array{1,v1}, Array{0,v2}};
	//Matrix obj_3 {Array{0,-2*m1*v1/m3 },Array{0,  -2*m1 * v2/m3 }};

	//result matrices
	std::vector<std::vector<std::vector<double>>> result_obj1;
	std::vector<std::vector<std::vector<double>>> result_obj2;
	std::vector<std::vector<std::vector<double>>> result_obj3;

	//implementation
	implement_rk4(deriv, obj_1, m1, obj_2, m2, obj_3, m3, t, step_size, steps_no, result_obj1, result_obj2, result_obj3);
	std::cout << "Writing files ...";


	output_matrix(result_obj1, "result_obj1.txt");
	output_matrix(result_obj2, "result_obj2.txt");
	output_matrix(result_obj3, "result_obj3.txt");
	return 0;
}
Matrix deriv(Matrix obj_active, Matrix obj_passive1, double mp1, Matrix obj_passive2, double mp2) {
	double v_x = (obj_active.arr_x).speed;
	double v_y = (obj_active.arr_y).speed;
	double xo = (obj_active.arr_x).position;
	double yo = (obj_active.arr_y).position;
	double xp1 = (obj_passive1.arr_x).position;
	double yp1 = (obj_passive1.arr_y).position;
	double xp2 = (obj_passive2.arr_x).position;
	double yp2 = (obj_passive2.arr_y).position;

	double acc_x = -((mp1 * (xo - xp1) / pow(pow(xo - xp1, 2.0) + pow(yo - yp1, 2.0), 3.0 / 2.0)) + (mp2 * (xo - xp2) / pow(pow(xo - xp2, 2.0) + pow(yo - yp2, 2.0), 3.0 / 2.0)));
	double acc_y = -((mp1 * (yo - yp1) / pow(pow(xo - xp1, 2.0) + pow(yo - yp1, 2.0), 3.0 / 2.0)) + (mp2 * (yo - yp2) / pow(pow(xo - xp2, 2.0) + pow(yo - yp2, 2.0), 3.0 / 2.0)));

	return Matrix{ Array{v_x,acc_x}, Array{v_y,acc_y} };
}
void rk4(Matrix(*deriv)(Matrix, Matrix, double, Matrix, double), Matrix& obj_active, Matrix& obj_passive1, double mp1, Matrix& obj_passive2, double mp2, const double h) {
	Matrix k1 = deriv( obj_active        , obj_passive1, mp1,  obj_passive2,  mp2);
	Matrix k2 = deriv( obj_active + h / 2, obj_passive1, mp1,  obj_passive2,  mp2);
	Matrix k3 = deriv( obj_active + h / 2, obj_passive1, mp1,  obj_passive2,  mp2);
	Matrix k4 = deriv( obj_active + h    , obj_passive1, mp1,  obj_passive2,  mp2);
	obj_active = obj_active + ((k1 + (k2 * 2) + (k3 * 2) + k4)) * (h / 6);
}
void implement_rk4(Matrix(*deriv)(Matrix, Matrix, double, Matrix, double), Matrix& obj_1, double& m1, Matrix& obj_2, double m2, Matrix& obj_3, double m3, double t, double step_size, double steps_no, std::vector<std::vector<std::vector<double>>>& result_obj1, std::vector<std::vector<std::vector<double>>>& result_obj2, std::vector<std::vector<std::vector<double>>>& result_obj3) {
	//std::vector<double> time_arr; implement this to calculate the time arr
	std::vector<double> obj_1_x{ {(obj_1.arr_x).position},{(obj_1.arr_x).speed} };
	std::vector<double> obj_2_x{ {(obj_2.arr_x).position},{(obj_2.arr_x).speed} };
	std::vector<double> obj_3_x{ {(obj_3.arr_x).position},{(obj_3.arr_x).speed} };

	std::vector<double> obj_1_y{ {(obj_1.arr_y).position},{(obj_1.arr_y).speed} };
	std::vector<double> obj_2_y{ {(obj_2.arr_y).position},{(obj_2.arr_y).speed} };
	std::vector<double> obj_3_y{ {(obj_3.arr_y).position},{(obj_3.arr_y).speed} };

	std::vector<std::vector<double>> obj_1_xy{ {obj_1_x},{obj_1_y} };
	std::vector<std::vector<double>> obj_2_xy{ {obj_2_x},{obj_2_y} };
	std::vector<std::vector<double>> obj_3_xy{ {obj_3_x},{obj_3_y} };

	result_obj1.push_back(obj_1_xy);
	result_obj2.push_back(obj_2_xy);
	result_obj3.push_back(obj_3_xy);
	
	for (size_t i{ 0 };i < steps_no;++i) {
		Matrix temp1 = obj_1;
		Matrix temp2 = obj_2;
		rk4(deriv, obj_1, obj_2, m2, obj_3, m3, step_size);
		rk4(deriv, obj_2, temp1, m1, obj_3, m3, step_size);
		rk4(deriv, obj_3, temp1, m1, temp2, m2, step_size);

		std::vector<double> obj_1_x{ {(obj_1.arr_x).position},{(obj_1.arr_x).speed} };
		std::vector<double> obj_2_x{ {(obj_2.arr_x).position},{(obj_2.arr_x).speed} };
		std::vector<double> obj_3_x{ {(obj_3.arr_x).position},{(obj_3.arr_x).speed} };

		std::vector<double> obj_1_y{ {(obj_1.arr_y).position},{(obj_1.arr_y).speed} };
		std::vector<double> obj_2_y{ {(obj_2.arr_y).position},{(obj_2.arr_y).speed} };
		std::vector<double> obj_3_y{ {(obj_3.arr_y).position},{(obj_3.arr_y).speed} };

		std::vector<std::vector<double>> obj_1_xy{ {obj_1_x},{obj_1_y} };
		std::vector<std::vector<double>> obj_2_xy{ {obj_2_x},{obj_2_y} };
		std::vector<std::vector<double>> obj_3_xy{ {obj_3_x},{obj_3_y} };

		result_obj1.push_back(obj_1_xy);
		result_obj2.push_back(obj_2_xy);
		result_obj3.push_back(obj_3_xy);
		//t += step_size;
	}
}
void output_matrix(std::vector < std::vector<std::vector<double>>> result_obj, std::string&& file_name) {
	std::ofstream output_file(file_name);
	for (size_t i{ 0 };i < result_obj.size();i++) {
		output_file << result_obj[i][0][0] << " " << result_obj[i][1][0] << " \n";

	}
}

/*
=============================================================================
 Please check the answers!!!
 =============================================================================
References:
#Implementing the RK4 method in Python
https ://youtu.be/mqoqAovXxWA
by Prof.Niels Walet

#for the initial conditions see
https ://doi.org/10.1093/pasj/psy057
and
https ://arxiv.org/abs/math/0011268
*/
