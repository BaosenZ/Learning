// Define static 2D array. Find min of one row in 2D array. Define dynamic 2D array and change size of the array.
// Ref: https://www.geeksforgeeks.org/how-to-declare-a-2d-array-dynamically-in-c-using-new-operator/

#include <iostream>
#include <algorithm>

int main()
{
    int numrows = 4;
    int numcols = 5;

    // define static 2D array
    int arr[4][5] = {
        {10, 11, 8, 5, 4},
        {20, 21, 1, 1, 1},
        {30, 31, 2, 2, 4},
        {40, 41, 4, 3, 2}};

    // fine min value of a row in 2D array
    int &min = *std::min_element(arr[0], arr[0] + 5);
    std::cout << "min value of row 0: " << min << "\n";

    int row, col; // for loop

    // define dynamic 2D array
    int **pixel_array = new int *[numrows];
    for (int i = 0; i < numrows; i++)
        pixel_array[i] = new int[numcols];
    // assign values to 2D array
    for (row = 0; row < numrows; ++row)
        for (col = 0; col < numcols; ++col)
            pixel_array[row][col] = arr[row][col];

    // print dynamic 2D array
    std::cout << "dynamic array: "
              << "\n";
    for (row = 0; row < 4; ++row)
    {
        for (col = 0; col < 5; ++col)
        {
            std::cout << pixel_array[row][col] << " ";
        }
        std::cout << "\n";
    }

    // define dynamic 2D array decrease col
    pixel_array = new int *[numrows];
    for (int i = 0; i < numrows; i++)
        pixel_array[i] = new int[numcols - 1]; // numcols-1
    // assign values to 2D array
    for (row = 0; row < numrows; ++row)
        for (col = 0; col < numcols - 1; ++col)
            pixel_array[row][col] = arr[row][col];

    // print dynamic 2D array decrase col
    std::cout << "dynamic array decrease col: "
              << "\n";
    for (row = 0; row < 4; ++row)
    {
        for (col = 0; col < 5 - 1; ++col)
        {
            std::cout << pixel_array[row][col] << " ";
        }
        std::cout << "\n";
    }
}
