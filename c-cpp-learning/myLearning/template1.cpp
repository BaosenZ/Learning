// C++ template
// Ref: https://www.youtube.com/watch?v=I-hZkUa9mIs&t=754s&ab_channel=TheCherno

#include <iostream>
#include <string>

template <typename T>
void Print(T value)
{
    std::cout << value << "\n";
}

// If no template, we need to write two same functions
// void Print(int i){
//     std::cout << i << "\n";
// }
// void Print(std::string s){
//     std::cout << s << "\n";
// }

int main()
{
    Print(5);
    Print<int>(5); // This is the same as above
    Print("Hello!");
    Print<std::string>("Hello!"); // This is the same as above
}