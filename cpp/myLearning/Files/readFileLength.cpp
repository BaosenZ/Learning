#include <iostream>
#include <fstream>
#include <sstream> //buffer to read the files

int main()
{
    std::string filename = "testCase2.txt";
    std::ifstream file;
    file.open(filename);
    std::string file_contents;
    std::cout << "reading the file..." << '\n';
    if (file.is_open())
    {
        std::stringstream buffer;
        buffer << file.rdbuf();
        file_contents = buffer.str();
        file.close();
    }
    else
    {
        std::cout << "No this file found, file open fail!" << '\n';
        return 0;
    }
    std::cout << "read file successfully!" << '\n';
    std::cout << "file contents length(=bytes): " << file_contents.size() << "\n";
    std::cout << "file contents length(=bits): " << file_contents.size() * 8 << "\n";
}
