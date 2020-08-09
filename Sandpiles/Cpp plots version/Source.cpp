#define OLC_PGE_APPLICATION
#include "olcPixelGameEngine.h"
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <chrono>
/*
====================
 === Snadpiles ===
====================
Created on Aug 8 2020
@author : Ahmed Al-kharusi

The "olcPixelGameEngine.h" is a single header file that enables us to draw graphics.
This is created by javidx9 (OneLoneCoder). I used this and the example template provided
in his repo to draw the sandpile matrix.
please download it from his repo
https://github.com/OneLoneCoder/olcPixelGameEngine

*/

void sandpile_matrix(std::vector<std::vector<int>>& matrix, size_t& max_iteration);
void output_matrix(std::vector<std::vector<int>>& matrix, std::string&& file_name);

class Sandpile : public olc::PixelGameEngine
{
public:
	Sandpile()
	{
		sAppName = "Sandpile";
	}

	std::vector<std::vector<int>> matrix;

public:
	bool OnUserCreate() override
	{
		return true;
	}

	bool OnUserUpdate(float fElapsedTime) override
	{
		for (int x = 0; x < ScreenWidth(); x++)
			for (int y = 0; y < ScreenHeight(); y++)

				if (matrix[x][y] == 1) {
					Draw(x, y, olc::Pixel(255,255,0));
				}else if (matrix[x][y] == 2) {
					Draw(x, y, olc::Pixel(0,0,204));
				}else if (matrix[x][y] == 3) {
					Draw(x, y, olc::DARK_RED);
				}
				else {
					Draw(x, y, olc::BLACK);
				}
				
		return true;
	}
};


int main()
{
	auto start = std::chrono::high_resolution_clock::now();
	Sandpile demo;

	int resolution{ 1080 };
	size_t max_iteration = 2000000;
	std::vector<std::vector<int>> matrix1(resolution, std::vector<int>(resolution, 0));
	demo.matrix = matrix1;
	sandpile_matrix(demo.matrix, max_iteration);
	
	auto end = std::chrono::high_resolution_clock::now();
	auto time_taken = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
	std::cout << time_taken.count() / 1000.0 << " seconds " << std::endl;

	if (demo.Construct(resolution, resolution, 1, 1))
		demo.Start();


	

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
			min = 0;
			max = 2*mid_point ;
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

