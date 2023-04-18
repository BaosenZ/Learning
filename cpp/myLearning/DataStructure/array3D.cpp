// Define static and dynamic 3D array. Change size of 3D array.

#include <iostream>
#include <algorithm>

int main()
{
    // define static 3D array
    int Arr[4][2][3] = {
        {{2, 1, 3}, {3, 4, 5}},
        {{5, 5, 5}, {6, 6, 6}},
        {{3, 1, 3}, {5, 4, 5}},
        {{1, 1, 1}, {2, 2, 2}}};

    int row, col, e; // for loop

    // print static 3D array
    // std::cout << "Static array: "
    //           << "\n ";
    // for (row = 0; row < 4; ++row)
    // {
    //     for (col = 0; col < 2; ++col)
    //     {
    //         std::cout << "( ";
    //         for (e = 0; e < 3; ++e)
    //         {
    //             std::cout << Arr[row][col][e] << " ";
    //         }
    //         std::cout << ") ";
    //     }
    //     std::cout << "\n";
    // }

    // define dynamic 3D array
    int numrows = 4;
    int numcols = 2;
    int num_e = 3;
    int ***pixel_array = new int **[numrows];
    for (int i = 0; i < numrows; i++)
    {
        pixel_array[i] = new int *[numcols];
        for (int j = 0; j < numcols; j++)
            pixel_array[i][j] = new int[num_e];
    }
    // assign values to 3D array
    for (row = 0; row < 4; ++row)
    {
        for (col = 0; col < 2; ++col)
        {
            for (e = 0; e < 3; ++e)
            {
                pixel_array[row][col][e] = Arr[row][col][e];
            }
        }
    }
    // print dynamic 3D array
    std::cout << "Dynamic array: "
              << "\n ";
    for (row = 0; row < 4; ++row)
    {
        for (col = 0; col < 2; ++col)
        {
            std::cout << "( ";
            for (e = 0; e < 3; ++e)
            {
                std::cout << pixel_array[row][col][e] << " ";
            }
            std::cout << ") ";
        }
        std::cout << "\n";
    }

    // re-define dynamic 3D array (decrease numrows)
    pixel_array = new int **[numrows - 1]; // numrows -1
    for (int i = 0; i < numrows - 1; i++)
    {
        pixel_array[i] = new int *[numcols];
        for (int j = 0; j < numcols; j++)
            pixel_array[i][j] = new int[num_e];
    }
    // assign values to 3D array
    for (row = 0; row < numrows - 1; ++row)
    {
        for (col = 0; col < 2; ++col)
        {
            for (e = 0; e < 3; ++e)
            {
                pixel_array[row][col][e] = Arr[row][col][e];
            }
        }
    }
    // print dynamic 3D array
    std::cout << "New Dynamic array (decrease numrows): "
              << "\n ";
    for (row = 0; row < numrows - 1; ++row)
    {
        for (col = 0; col < 2; ++col)
        {
            std::cout << "( ";
            for (e = 0; e < 3; ++e)
            {
                std::cout << pixel_array[row][col][e] << " ";
            }
            std::cout << ") ";
        }
        std::cout << "\n";
    }
}