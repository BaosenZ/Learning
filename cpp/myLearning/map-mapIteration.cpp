// Note that map is order based on its key

#include <iostream>
#include <string>
#include <map>

template <typename I>
std::map<std::string, int> compress(I r)
{
    // Build a dictionary using map
    std::map<std::string, int> dictionary;
    dictionary.insert({r, 100});
    dictionary["bb"] = 200;
    dictionary["dd"] = 400;
    dictionary.insert({"cc", 350});

    return dictionary;
}

// Driver Code
int main()
{
    std::map<std::string, int> out = compress("ee");

    for (auto i = out.begin(); i != out.end(); ++i)
    {
        std::cout << i->first << " ";
        std::cout << i->second << " ";
    }
}