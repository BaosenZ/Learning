#include <iostream>
#include <fstream> // ifstream
#include <sstream> // stringstream

int main()
{
    std::ifstream inputfile("testCase0.pgm");

    // Read pgm file and get the pgm pixels array

    std::string inputLine;
    // Get 1st line: version
    getline(inputfile, inputLine);
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
    int col, row;

    // int **pixel_array = new int *[numrows * numcols];
    // for (int i = 0; i < numcols; i++)
    //     pixel_array[i] = new int[numcols];
    // for (row = 0; row < numrows; ++row)
    //     for (col = 0; col < numcols; ++col)
    //         pixel_array[row][col] = 8;

    int pixel_array_ori[numrows][numcols];
    for (row = 0; row < numrows; ++row)
        for (col = 0; col < numcols; ++col)
            ss >> pixel_array_ori[row][col];
    inputfile.close();

    int **pixel_array = new int *[numrows];
    for (int i = 0; i < numrows; i++)
    {
        pixel_array[i] = new int[numcols];
    }
    for (row = 0; row < numrows; ++row)
        for (col = 0; col < numcols; ++col)
            pixel_array[row][col] = pixel_array_ori[row][col];
    // print the pixels array from pgm file
    std::cout << "pixel array from file"
              << "\n";
    for (row = 0; row < numrows; ++row)
    {
        for (col = 0; col < numcols; ++col)
        {
            std::cout << pixel_array[row][col] << " ";
        }
        std::cout << "\n";
    }
}
