#include <iostream>
#include <string>
#include <map>
#include <vector>

template <typename Iterator>
Iterator compress(const std::string &uncompressed, Iterator result)
{
    // Build the dictionary, start with 256.
    int dictSize = 256;
    std::map<std::string, int> dictionary;
    for (int i = 0; i < dictSize; i++)
        dictionary[std::string(1, i)] = i;

    std::string w;
    for (std::string::const_iterator it = uncompressed.begin();
         it != uncompressed.end(); ++it)
    {
        char c = *it;
        std::string wc = w + c;
        if (dictionary.count(wc))
            w = wc;
        else
        {
            *result++ = dictionary[w];
            // Add wc to the dictionary. Assuming the size is 4096!!!
            if (dictionary.size() < 4096)
                dictionary[wc] = dictSize++;
            w = std::string(1, c);
        }
    }

    // Output the code for w.
    if (!w.empty())
        *result++ = dictionary[w];
    return result;
}

int main(int argc, char *argv[])
{
    std::vector<int> compressed;
    // example
    std::string example = "AAAAAAABBBBBB";

    compress(example, std::back_inserter(compressed));
    for (auto itr = compressed.begin(); itr != compressed.end(); itr++)
        std::cout << "\n"
                  << *itr;
}