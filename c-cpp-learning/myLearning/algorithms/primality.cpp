#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

std::string fermatTest(int N, int a);

int main()
{
    std::cout << fermatTest(11, 7) << '\n';
    std::cout << fermatTest(12, 8) << '\n';
}

std::string fermatTest(int N, int a)
{
    if ((int(pow(a, (N - 1))) % N) == 1)
    {
        return "Yes";
    }
    else
    {
        return "No";
    }
}