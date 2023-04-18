#include <iostream>
#include <fstream> // ifstream
#include <sstream> // stringstream
#include <cmath>

// Driver code
int main()
{
    std::ifstream inputfile("testCase0.pgm");
    std::string inputLine = "";
    // Get 1st line: version
    getline(inputfile, inputLine);
    if (inputLine.compare("P2") != 0)
        std::cout << "Not P2"
                  << "\n";
    else
        std::cout << "pgm file version: " << inputLine << "\n";
    // Second line: comment
    getline(inputfile, inputLine);
    std::cout << "Comment: " << inputLine << "\n";

    // Continue with a stringstream
    std::stringstream ss;
    int numcols = 0, numrows = 0, colorscale = 0;
    ss << inputfile.rdbuf();
    // 3rd and 4th line: picture size and color scale
    ss >> numcols >> numrows >> colorscale;
    std::cout << "number of columns:" << numcols << "\n";
    std::cout << "number of rows:" << numrows << "\n";
    std::cout << "color scale:" << colorscale << "\n";

    // Loop the pixel data to 2D array
    int col = 0, row = 0;
    int array[numrows][numcols];
    for (row = 0; row < numrows; ++row)
        for (col = 0; col < numcols; ++col)
            ss >> array[row][col];
    inputfile.close();

    // print the array to see the result
    for (row = 0; row < numrows; ++row)
    {
        for (col = 0; col < numcols; ++col)
        {
            std::cout << array[row][col] << " ";
        }
        std::cout << "\n";
    }

    int seam[8][2] = {
        {0, 0},
        {1, 1},
        {2, 1},
        {3, 2},
        {4, 2},
        {5, 2},
        {6, 0},
        {7, 2},
    };

    // shift col
    int i, seamcol;
    for (row = 0; row < numrows; ++row)
    {
        seamcol = seam[row][1];
        for (i = seamcol; i < numcols - 1; ++i)
        {
            array[row][i] = array[row][i + 1];
        }
    }

    for (row = 0; row < numrows; ++row)
    {
        for (col = 0; col < numcols; ++col)
        {
            std::cout << array[row][col] << " ";
        }
        std::cout << "\n";
    }

    int pixels_remove_seam_array[numrows][numcols -1] = {0};
    for (row = 0; row < numrows; ++row)
    {
        for (col = 0; col < numcols-1; ++col)
        {
            pixels_remove_seam_array[row][col] = array[row][col];
        }
    
    }
    for (row = 0; row < numrows; ++row)
    {
        for (col = 0; col < numcols-1; ++col)
        {
            std::cout << pixels_remove_seam_array[row][col] << " ";
        }
        std::cout << "\n";
    }
}