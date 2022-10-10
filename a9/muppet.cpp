/*
 Class muppet for STL assignment.
 
 Author:        Daniel Birnbaum
 Last Modified:    May 18, 2020 (Daniel Birnbaum)
 */

#include <iostream>
#include <string>
#include "muppet.h"

using namespace std;

int number_of_sales = 0;
double sum_of_sales;

    muppet::muppet(string n){
        name = n;
        number_of_sales = 0;
        sum_of_sales = 0;
    }


// write the muppet member functions here

void muppet::display(){
    cout << "Salesperson name: " << name << endl;
    cout << "Number of sales: " << number_of_sales << endl;
    cout << "Total income: " << sum_of_sales << endl;
}

void muppet::addSale(double s){
    sum_of_sales = s + sum_of_sales;
    number_of_sales = number_of_sales + 1;
    
}

string muppet::getName(){
    return name;
}

int muppet::getNumSales(){
    return number_of_sales;
}

double muppet::getSumOfSales(){
    return sum_of_sales;
}
