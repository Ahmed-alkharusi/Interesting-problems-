/*
====================
=The Mandelbrot set=
====================
Created on Sat Jul 25 2020

@author : Ahmed Al-kharusi*/


#include "Complex.h"
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <cmath>
int mandelbrot(Complex domain, size_t range);
void output_matrix(std::vector<std::vector<double>> matrix, std::string&& file_name);

int main() {
	
	double points_no{ 2000 };
	std::vector<std::vector<double>> result(points_no, std::vector<double>(points_no, 0));
	double x_start{ -2 };
	for (size_t i{ 0 };i < points_no;i++) {
		x_start += 3  / points_no;
		double y_start{ -1.5 };
		for (size_t j{ 0 };j < points_no;j++) {
			y_start += 3  / points_no;
			Complex temp{ x_start,y_start };
			result[j][i] = mandelbrot(temp, 100);
		}	
	}
	output_matrix(result, "results.txt");
	return 0;
}

int mandelbrot(Complex domain, size_t range) {
	Complex zo{0, 0};
	Complex result{ 0,0 };
	for (size_t i{ 0 };i < range;i++) {
		result = (zo * zo) + domain;
		zo = result;

		double ans = result.re() * result.re() + result.im() * result.im();
		if (ans >= 4)
			return i;
	}
	return 0;
}
void output_matrix(std::vector<std::vector<double>> matrix, std::string&& file_name) {
	std::ofstream output_file(file_name);
	for (size_t i{ 0 };i < matrix.size();i++) {
		for (size_t j{ 0 };j < (matrix.at(i)).size();j++) {
			output_file << (matrix.at(i)).at(j) << " ";
		}
		output_file << "\n";
	}
}