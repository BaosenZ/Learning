#include <iostream>
#include <fstream>

int main()
{
    // Create a text string, which is used to output the text file
    std::string myText;

    // Read from the text file
    std::ifstream MyReadFile("filename.txt");

    // Use a while loop together with the getline() function to read the file line by line
    while (getline(MyReadFile, myText))
    {
        // Output the text from the file
        std::cout << myText;
    }

    // Close the file
    MyReadFile.close();
}