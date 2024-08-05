// It seems not easy to return dynamic array

#include <iostream>
#include <fstream> // ifstream
#include <sstream> // stringstream
#include <cmath>
#include <algorithm>

// Driver code
int main()
{
    int pixels_array
        pixels_array = readPGM("testCase0.pgm")
}

// function to read a .pgm file and return the pixel data as a 2D array
int **readPGM(std::string filename)
{
    std::ifstream fin(filename);
    std::string version, comment;
    fin >> version >> comment;
    int numcols, numrows, colorscale;
    fin >> numcols >> numrows >> colorscale;

    // Loop the pixel data to 2D array
    int pixels[numrows][numcols];
    int col = 0, row = 0;
    for (row = 0; row < numrows; ++row)
        for (col = 0; col < numcols; ++col)
            fin >> pixels[row][col];
    fin.close();
    return pixels;
}