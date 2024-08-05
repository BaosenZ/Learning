#include <iostream>
#include <fstream>
#include <tuple>

// function decleration
bool fermat2Times(int N);
int modExp(int x, int y, int m);
std::tuple<int, int, int> extendedEuclid(int a, int b);

// drive code
int main()
{
    int p, q;
    for (int i = 0; i < 100; i++)
    {
        p = rand() % 10 + 2;
        if (fermat2Times(p))
        {
            break;
        }
    }
    for (int i = 0; i < 100; i++)
    {
        q = rand() % 10 + 2;
        if (fermat2Times(q))
        {
            break;
        }
    }
    int n = p * q;
    int fe_n = (p - 1) * (q - 1);

    int e = 3;
    int gcd, x, d;
    for (int i = 0; i < 100; i++)
    {
        e = e + 2;
        std::tie(gcd, x, d) = extendedEuclid(fe_n, e);
        if (gcd == 1)
        {
            if (d < 0)
            {
                d = d + fe_n;
            }
            break;
        }
    }

    std::cout << "p: " << p << '\n';
    std::cout << "q: " << q << '\n';
    std::cout << "e: " << e << '\n';
    std::cout << "n: " << n << '\n';
    std::cout << "fe_n: " << fe_n << '\n';
    std::cout << "gcd: " << gcd << '\n';
    std::cout << "d: " << d << '\n';
    std::cout << "Note that the hashed message (int) should be from 0 to n-1!" << '\n';

    std::ofstream pqFile("p_q.txt");
    pqFile << p << '\n';
    pqFile << q;
    pqFile.close();

    std::ofstream enFile("e_n.txt");
    enFile << e << '\n';
    enFile << n;
    enFile.close();

    std::ofstream dnFile("d_n.txt");
    dnFile << d << '\n';
    dnFile << n;
    dnFile.close();
}

bool fermat2Times(int N)
{
    int a = 6;
    if (modExp(a, N - 1, N) == 1)
    {
        int a = 8;
        if (modExp(a, N - 1, N) == 1)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }
}

// function to calculate x^y mod m
int modExp(int x, int y, int m)
{
    if (y == 0)
    {
        return 1;
    }
    else
    {
        int z = modExp(x, y / 2, m);
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

std::tuple<int, int, int> extendedEuclid(int a, int b)
{
    int d, x, y;
    if (b == 0)
    {
        return {a, 1, 0};
    };
    int d1, x1, y1;
    std::tie(d1, x1, y1) = extendedEuclid(b, a % b);
    d = d1;
    x = y1;
    y = x1 - y1 * (a / b);
    return {d, x, y};
}