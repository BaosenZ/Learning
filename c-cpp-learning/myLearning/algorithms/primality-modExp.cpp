#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

std::string fermatTest(int N, int a);
int modexp(int x, int y, int m);

int main()
{
    std::cout << fermatTest(11, 7) << '\n';
    std::cout << fermatTest(12, 8) << '\n';
    std::cout << modexp(3, 3, 5) << '\n';
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

int modexp(int x, int y, int m)
{
    if (y == 0)
    {
        return 1;
    }
    else
    {
        int z = modexp(x, y / 2, m);
        if (y % 2 == 0)
        {
            return z * z % m;
        }
        else
        {
            return x * z * z % m;
        }
    }
}