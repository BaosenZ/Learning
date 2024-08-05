#include <iostream>
#include <fstream>

int main()
{
    std::ifstream inputfile;   // create input file stream
    inputfile.open("p_q.txt"); // open the file

    if (inputfile.is_open())
    {
        std::string p;
        std::string q;

        inputfile >> p;
        inputfile >> q;

        std::cout << p.length() << '\n';
        std::cout << q.length();
    }
}