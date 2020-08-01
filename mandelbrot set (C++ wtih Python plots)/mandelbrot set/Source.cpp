/*
============================
=Mandelbrot and Julia sets=
============================
Created on Sat Jul 25 2020
@author : Ahmed Al-kharusi*/

#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <cmath>
#include <chrono>
#include "Complex.h"
int mandelbrot(Complex &domain, const unsigned int& range);
int julia(Complex zo, const Complex &domain, const unsigned int &range);
void output_matrix(std::vector<std::vector<double>>& matrix, std::string&& file_name);

int main() {
	auto start = std::chrono::high_resolution_clock::now();
	/*some points for the Julia set
	const Complex c{-1,0.1};
	const Complex c1{ 0.61803398875,0 };
	const Complex c2{ -0.4,0.6 };
	const Complex c3{ 0.285,0.01 };
	const Complex c4{ -0.8,0.156 };
	const Complex c5{ -0.835,- 0.2321 };*/
	const Complex c6{ 0,0.8 };
	
	const unsigned int points_no{ 2000 };
	std::vector<std::vector<double>> result(points_no, std::vector<double>(points_no, 0));
	double x_start{ -2 };
	const unsigned int range{100};

	for (size_t i{ 0 };i < points_no;i++) {
		x_start += 3 / points_no;
		double y_start{ -1.5 };
		for (size_t j{ 0 };j < points_no;j++) {
			y_start += 3 / points_no;
			Complex temp{ x_start,y_start };
			//result[j][i] = mandelbrot(temp, range);//change this for the Julia set
			result[j][i] = julia(temp, c6, range);
		}
	}
	std::cout << "Writing files ... \n";
	output_matrix(result, "results.txt");

	auto end = std::chrono::high_resolution_clock::now();
	auto time_taken = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
	std::cout << time_taken.count() / 1000.0 << " seconds " << std::endl;
	return 0;
}

int mandelbrot(Complex &domain, const unsigned int& range) {
	Complex zo{ 0, 0 };
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
int julia(Complex zo, const Complex &domain, const unsigned int& range) {

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
void output_matrix(std::vector<std::vector<double>>& matrix, std::string&& file_name) {
	std::ofstream output_file(file_name);
	for (size_t i{ 0 };i < matrix.size();i++) {
		for (size_t j{ 0 };j < (matrix.at(i)).size();j++) {
			output_file << (matrix.at(i)).at(j) << " ";
		}
		output_file << "\n";
	}
}
