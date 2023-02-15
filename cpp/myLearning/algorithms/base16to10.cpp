#include <iostream>
#include <fstream>
#include <string.h>
#include <cmath>

int StrBase16ToBase10(std::string str_base16)
{
    int len = str_base16.length();
    int total = 0;
    int ans;
    for (int i = 0; i < len; i++)
    {
        std::string s;
        s.push_back(str_base16[len - i - 1]);
        ans = std::stoul(s, 0, 16);
        total = total + pow(16, i) * ans;
    }
    return total;
}

int main()
{
    std::string str_base16 = "1f";

    int len = str_base16.length();
    std::cout << len << "\n";

    int ans = std::stoul("f", 0, 16);
    std::cout << ans << "\n";

    std::cout << pow(16, 1) << "\n";
    std::cout << StrBase16ToBase10("3ef");
}