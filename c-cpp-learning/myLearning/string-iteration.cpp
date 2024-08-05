// Iterate over characters of a string.
// Ref: https://www.geeksforgeeks.org/iterate-over-characters-of-a-string-in-c/

#include <iostream>

// Driver Code
int main()
{
    std::string str = "GeeksforGeeks";

    std::cout << "str iteration using string index: ";
    // Traverse the string
    int N = str.length();
    for (int i = 0; i < N; i++)
    {
        // Print current character
        std::cout << str[i] << " ";
    }
    std::cout << "\n";

    std::cout << "str iteration using iterator: ";
    // Stores address of a character of str
    // Traverse the string
    std::string::iterator it;
    for (it = str.begin(); it != str.end(); it++)
    {
        // Print current character
        std::cout << *it << " ";
    }
}
