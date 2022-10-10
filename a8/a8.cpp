#include <iostream> //to use cin and cout
#include <fstream>  //to get input from a file
#include <string>   //uses strings
using namespace std;
ifstream in_file;
int main() {
    in_file.open("p8input.txt", ios::in);
    if(in_file.fail()) {
        cout << "Could not open input file.  Program terminating.\n\n";
        return 9;
    }
    
    //Your code goes here
    //remember that you can read from the file by treating
    //  in_file like cin. For example,
    string name;
    double salesval;
    int last;
    double highestinc = 0;
    double income = 0;
    double nos;
    string namems;
    string namehighestinc;
    double ms = 0;
    do {
       
        in_file >> name;
        in_file >> nos;
        
        cout << "Salesperson name: " << name << endl;
        
        cout << "Number of sales: " << nos << endl;
        
        
        
        if (nos > ms){
            ms = nos;
            namems = name;
        }
        //cout << "Most sales so far: " << ms << endl;
        
        for (int i = 0; i < nos; i++){
            in_file >> salesval;
            income += salesval;
            //cout << "Counter: " << i << " Value: " << salesval << endl;
        }
        
        if (income > highestinc) {
            namehighestinc = name;
            highestinc = income;
        }
        
        cout << "Total income: " << income << endl;
        income = 0;
        
        
        
        in_file >> last;
        //cout << "namehighestinc: " <<namehighestinc << endl;
        //cout << "Last: " << last << endl;
        cout << endl;
    } while (last == -1);
    cout << "Most sales: " << namems << endl;
    cout << "Highest income: " << namehighestinc;
}
