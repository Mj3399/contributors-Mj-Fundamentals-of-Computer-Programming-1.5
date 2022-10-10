/*
 Class muppet for STL assignment.
 
 Author:        Daniel Birnbaum
 Last Modified:    May 18, 2020 (Daniel Birnbaum)
 */

#include <string>

using namespace std;

class muppet{
private:
    string name;
    int number_of_sales;
    double sum_of_sales;
public:
    muppet(string name);
    void display();
    void addSale(double s);
    string getName();
    int getNumSales();
    double getSumOfSales();
    
};
// write the muppet class definition here
