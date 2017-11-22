/**************************************************************************
 * 
 * ** Author:   Jon-Eric Cook
 *              Shannon Jeffers
 *              Peter Moldenhauer
 * 
 * ** Date: 12-01-17
 * 
 * ** Description: Project TSP - This program makes an attempt to solve the 
 *                              Traveling Salesman Problem.
 *
 ***************************************************************************/

#include <iostream>
#include <fstream>
#include <limits>
#include <vector>
#include <math.h>

// struct for city information
struct city {
    int id;
    int x;
    int y;
};

// calculates the distance between CityA and CityB
int calculate_distance_between_cities(std::vector<struct city>& cities, int cityA_id, int cityB_id){
    double distance_between_cities = sqrt( pow(cities[cityB_id].x - cities[cityA_id].x, 2) +
                                           pow(cities[cityB_id].y - cities[cityA_id].y, 2) );
    int rounded_distance_between_cities = round(distance_between_cities);
    return rounded_distance_between_cities;
}

// gets the distances between all the available cities
void get_distances_between_cities(std::vector<int>& distance_between_cities, std::vector<struct city>& cities) {
    int distance;
    for (int i = 0; i < cities.size(); i++){
        for (int j = 0; j < cities.size(); j++){
            distance = calculate_distance_between_cities(cities, i, j);
            distance_between_cities.push_back(distance);
        }
    }
}

bool has_been_visited(std::vector<int>& visited_cities, int city_id){
    for (int i = 0; i < visited_cities.size(); i++){
        if (visited_cities[i] == city_id)
            return true;
    }
    return false;
}

void get_city_data(std::vector<struct city>& cities, std::string file_name) {
    std::ifstream file;
    file.open(file_name);
    std::string element;
    int city_data;
    int counter = 0;
    int id;
    int x;
    int y;
    while (file >> element){
        std::size_t last_char;
        city_data = std::stoi(element, &last_char, 10);
        counter++;
        if (counter == 1) {
            id = city_data;
        } else if (counter == 2) {
            x = city_data;
        } else if (counter == 3) {
            y = city_data;
            struct city temp_city = {id,x,y};
            cities.push_back(temp_city);
            counter = 0;
        }
    }
    file.close();
}

void output_visited_cities(std::vector<int>& visited_cities, int distance_traveled, std::string file_name) {
    std::ofstream file;
    file.open(file_name+".tour");
    file << distance_traveled << "\n";
    for (int i = 0; i < visited_cities.size(); i++) {
        file << visited_cities[i] << "\n";
    }
    file.close();
}

void take_a_tour(std::vector<int>& distance_between_cities, std::vector<int>& visited_cities, int number_of_cities, int& distance_traveled) {
    int starting_city = 11;
    visited_cities.push_back(starting_city);
    int min;
    int index;

    while (visited_cities.size() < number_of_cities){
        min = std::numeric_limits<int>::max();
        index = -1;
        for (int i = 0; i < number_of_cities; i++){
            if (distance_between_cities[starting_city*number_of_cities + i] < min &&
                !has_been_visited(visited_cities, i) ){
                min = distance_between_cities[starting_city*number_of_cities + i];
                index = i;
            }
        }
        distance_traveled += min;
        visited_cities.push_back(index);
        starting_city = index;
    }
}

int main(int argc, char* argv[]) {
    clock_t clock_start = clock();

    if (argc != 2){
        std::cout << "Invalid number of arguments.\n";
        exit(1);
    }
    
    std::vector<struct city> cities;
    std::string file_name = argv[1];
    get_city_data(cities,file_name);

    std::vector<int> distance_between_cities;
    get_distances_between_cities(distance_between_cities,cities);

    std::vector<int> visited_cities;
    int distance_traveled = 0;
    take_a_tour(distance_between_cities,visited_cities,cities.size(),distance_traveled);
    distance_traveled += distance_between_cities[visited_cities[visited_cities.size()-1] * cities.size() + visited_cities[0]];
    output_visited_cities(visited_cities,distance_traveled,file_name);
    
    clock_t clock_end = clock();
    double duration = ( clock_end - clock_start ) / (double) CLOCKS_PER_SEC;
    std::cout << file_name << "  ->  " << duration << " sec\n";
    
    return 0;
}