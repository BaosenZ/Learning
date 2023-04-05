#include <iostream>
#include <fstream>
#include <tuple>

std::tuple<int, int, int> extendedEuclid(int a, int b);
// int gcd(int a, int b);

int main()
{
    int gcd, x, y;
    std::tie(gcd, x, y) = extendedEuclid(44, 20);
    // d = gcd(35, 10);
    std::cout << "gcd: " << gcd << '\n';
    std::cout << x << '\n';
    std::cout << y << '\n'; // This is d (in RSA)
}

// std::ifstream inputfile;   // create input file stream
// inputfile.open("p_q.txt"); // open the file

// if (inputfile.is_open())
// {
//     int p;
//     int q;

//     inputfile >> p;
//     inputfile >> q;

//     std::cout << p << '\n';
//     std::cout << q;
// }

std::tuple<int, int, int> extendedEuclid(int a, int b)
{
    int d, x, y;
    if (b == 0)
    {
        return {a, 1, 0};
    };
    auto [d1, x1, y1] = extendedEuclid(b, a % b);

    d = d1;
    x = y1;
    y = x1 - y1 * (a / b);
    return {d, x, y};
}

int gcd(int a, int b)
{
    int x, y;
    if (b == 0)
    {
        x = 1;
        y = 0;
        return a;
    }
    int x1, y1;
    int d = gcd(b, a % b);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}