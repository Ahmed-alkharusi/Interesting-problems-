/*
====================
 === Snadpiles ===
====================
Created on Aug 8 2020
@author : Ahmed Al-kharusi
*/

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <chrono>
void sandpile_matrix(std::vector<std::vector<int>>& matrix, size_t& max_iteration);
void output_matrix(std::vector<std::vector<int>>& matrix, std::string&& file_name);

int main() {
	auto start = std::chrono::high_resolution_clock::now();

	int resolution{ 401 };
	size_t max_iteration = 10000;
	std::vector<std::vector<int>> matrix(resolution, std::vector<int>(resolution, 0));
	
	sandpile_matrix(matrix, max_iteration);
	std::cout << "Writing file ...\n";

	output_matrix(matrix, "result.txt");

	auto end = std::chrono::high_resolution_clock::now();
	auto time_taken = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
	std::cout << time_taken.count() / 1000.0 << " seconds " << std::endl;

	return 0;
}
void output_matrix(std::vector<std::vector<int>>& matrix, std::string&& file_name) {
	std::ofstream output_file(file_name);
	for (size_t i{ 0 };i < matrix.size();i++) {
		for (size_t j{ 0 };j < (matrix.at(i)).size();j++) {
			output_file << (matrix.at(i)).at(j) << " ";
		}
		output_file << "\n";
	}
}
void sandpile_matrix(std::vector<std::vector<int>>& matrix, size_t& max_iteration) {
	size_t mid_point = static_cast<size_t>((matrix.size() - 1) / 2);

	matrix[mid_point][mid_point] = static_cast<int>(1.2 * max_iteration);
	size_t min = 0;
	size_t max = 0;
	for (size_t k{ 0 };k < (max_iteration);k++) {
		if ((k + 1) < mid_point) {
			min = (mid_point - (k + 1));
			max = (mid_point + (k + 1));
		}
		else {
			min = mid_point - 200;//200 is arbitrary (added to make the code faster)
			max = mid_point + 200;
		}

		for (size_t i{ min };i < max;i++) {

			for (size_t j{ min };j < max;j++) {
				if (matrix[i][j] > 3) {
					matrix[i][j] -= 4;
					matrix[i][j + 1] += 1;
					matrix[i][j - 1] += 1;
					matrix[i + 1][j] += 1;
					matrix[i - 1][j] += 1;
				}
			}
		}
	}
}


