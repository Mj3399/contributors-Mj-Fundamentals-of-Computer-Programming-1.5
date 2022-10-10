/*
 This file contains functions used at the system and main level.
 
 Author:        Daniel Birnbaum
 Last Modified:    May 18, 2020 (Daniel Birnbaum)
 */
#include "utilities.h"
#include <string>
#include <vector>
using namespace std;



string FindMostSales(vector<muppet> most_sales_vector){
    double most_sales = 0;
    string most_sales_name;
    int number_of_sales;
    for (int i = 0; i < most_sales_vector.size(); i++){
        if (most_sales_vector[i].getNumSales() > most_sales){
            most_sales = most_sales_vector[i].getNumSales();
            most_sales_name = most_sales_vector[i].getName();
            
        }
    }
    return most_sales_name;
    
}
string FindMostSumOfSales(vector<muppet> sum_of_sales_vector){
    int sum_of_sales;
    double most_sum_sales = 0;
    string most_sum_sales_name;
    for (int i=0; i< sum_of_sales_vector.size(); i++){
        if (sum_of_sales_vector[i].getSumOfSales() > most_sum_sales){
            most_sum_sales = sum_of_sales_vector[i].getSumOfSales();
            most_sum_sales_name = sum_of_sales_vector[i].getName();
            
        }
    }
    return most_sum_sales_name;
}

// write your functions here
