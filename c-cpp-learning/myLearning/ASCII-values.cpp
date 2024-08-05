// In this C++ program, we print the ASCII Values of all the characters.
// Ref: https://www.tutorialgateway.org/cpp-program-to-print-ascii-values-of-all-characters/
// Note: Windows cannot print all ASCII code

#include <iostream>
#include <map>

int main()
{

    std::cout << "\nUse char to print the ASCII Values of all the characters\n";
    int i;
    for (i = 0; i <= 255; i++)
    {
        std::cout << "The ASCII value of " << (char)i << " = " << i << ". ";
    }
    std::cout << "char method end!\n";
    std::cout << "\n";

    // Build the dictionary for ASCII and values.
    std::cout << "\nUse map to build dictionary and print the ASCII Values of all the characters\n";
    int dictSize = 256;
    std::map<std::string, int> dictionary;
    for (int i = 0; i < dictSize; i++)
    {
        // std::cout << "The ASCII value of " << std::string(1, i) << " = " << i << "\n ";
        dictionary[std::string(1, i)] = i;
    }
    std::cout << "dictionary end!\n";
    // Loop from dictionary
    std::cout << "\nLoop from dictionary\n";
    std::map<std::string, int>::iterator it = dictionary.begin(); // Get an iterator pointing to the first element in the map
    while (it != dictionary.end())                                // Iterate through the map and print the elements
    {
        std::cout << "ASCII: " << it->first << ", Value: " << it->second << "\n ";
        it++;
    }
    std::cout << "Loop from dictionary end!\n";

    return 0;
}