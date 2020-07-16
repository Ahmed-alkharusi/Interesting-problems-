/*
The logistic map
Created on Tue Jul 14  2020

@author: Ahmed Alkharusi

*/


#include <iostream>
#include <vector>
#include <fstream>
std::vector<double> logistic_map(double current_population, const double fertility, size_t max_iteration);
std::vector<std::vector<double>> results_matrix(double current_population, std::vector<double> fertility_vec, size_t max_iteration);
std::vector<double> linspace(double start, double end, int points_no);

int main() {
    double current_population{ 0.5 };
    size_t max_iteration{ 2000 };
    std::vector<std::vector<double>> final_results;
    std::vector<double>fertility_vec;
    fertility_vec = linspace(2.4, 4, max_iteration);

    final_results = results_matrix(current_population,fertility_vec, max_iteration);

    std::ofstream output_file("results.txt");
    for (size_t i{ 0 };i < final_results.size();i++) {
        for(size_t j{ 0 };j < final_results.size();j++){
            output_file << (final_results.at(j)).at(i) << " ";
        }
        output_file << "\n";
    }
    output_file.close();
    std::ofstream output_list("linspace.txt");
    for (size_t i{ 0 };i < fertility_vec.size();i++) {
       output_list << fertility_vec.at(i) << " ";
    }
    output_list.close();
    return 0;
}

std::vector<double> logistic_map(double current_population, const double fertility, size_t max_iteration) {
    std::vector <double> result;
    result.push_back(current_population);//think about using initialziation first
    if (fertility < 3.6) {
        rsize_t temp{max_iteration};
        max_iteration = 200;
        for (rsize_t i{ 0 }; i < (max_iteration - 1);++i) {
            current_population = fertility * current_population * (1 - current_population);
            result.push_back(current_population);
        }
        for (rsize_t i{ 0 }; i < (temp-max_iteration);++i)
            result.push_back(result.at(max_iteration-1));
    }
    else {
        for (rsize_t i{ 0 }; i < (max_iteration - 1);++i) {
            current_population = fertility * current_population * (1 - current_population);
            result.push_back(current_population);
        }
    }
    return result;
}

std::vector<std::vector<double>> results_matrix(double current_population, std::vector<double> fertility_vec, size_t max_iteration) {
    std::vector<std::vector<double>> results_matrix;
    for (rsize_t i{ 0 }; i < fertility_vec.size();++i) {
        results_matrix.push_back(logistic_map(current_population,fertility_vec.at(i),max_iteration));
    }
    return results_matrix;
}
std::vector<double> linspace(double start, double end, int points_no) {
    std::vector<double> results;
    double increment{ (end - start) / points_no };
    for (double i{ start }; i < (end - increment);i += increment) {
        results.push_back(i);  
    }
    return results;
}