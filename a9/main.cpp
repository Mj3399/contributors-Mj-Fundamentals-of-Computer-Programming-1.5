/*
 A basic main function for testing assignment 9.
 
 Author:        Daniel Birnbaum
 Last Modified:    May 18, 2020 (Daniel Birnbaum)
 */

#include <fstream>
#include <iostream>
#include <vector>
#include "utilities.h"

using namespace std;

ifstream in_file;

int main() {
    in_file.open("p9input.txt", ios::in);
    if(in_file.fail()) {
        cout << "Could not open input file.  Program terminating.\n\n";
        return 9;
    }
    
    vector<muppet> muppets;
    
    int more_people = -1;
    
    do {
        string name = "";
        int number_of_sales = 0;
        double current_sale = 0.0;
        
        in_file >> name >> number_of_sales;
        
        
        muppet new_muppet = muppet(name);
        
        for (int i = 0; i < number_of_sales; i++) {
            in_file >> current_sale;
            new_muppet.addSale(current_sale);
        }
        
        //Print out data members
        new_muppet.display();
        cout << endl;
        
        //Save person to vector
        muppets.push_back(new_muppet);
        
        in_file >> more_people;
    } while (more_people == -1);
    
    string most_sales_name = FindMostSales(muppets);
    string max_sales_name = FindMostSumOfSales(muppets);
    
    cout << "Most sales: " << most_sales_name << endl;
    cout << "Highest income: " << max_sales_name << endl;
}
