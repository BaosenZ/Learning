#include <iostream>
#include <fstream>
#include <sstream>

// function decleration
int modExp(int x, int y, int m);

int main(int argc, char **argv)
{
    // convert argv from char to string
    std::string argv2 = argv[2];

    // sign a given file
    if (argv2 == "s")
    {
        std::cout << "sign a given file: " << '\n';

        // open mydoc.txt and read all mydoc file contents
        std::string filename = argv[3];
        std::ifstream file;
        file.open(filename);
        std::string mydoc_file_contents;
        if (file.is_open())
        {
            std::stringstream buffer;
            buffer << file.rdbuf();
            mydoc_file_contents = buffer.str();
            std::cout << "mydoc file contents: " << mydoc_file_contents << "\n";
            file.close();
        }
        else
        {
            std::cout << "No this file found, file open fail!" << '\n';
            return 0;
        }
        std::cout << "mydoc file contents: " << mydoc_file_contents << "\n";

        // hash mydoc file contents
        // std::hash<std::string> myStdHash;
        // int myDocHash = myStdHash(mydoc_file_contents);
        // std::cout << "myDocHash: " << myDocHash << "\n";

        // hash mydoc file contents just from sting to int
        int myDocHash = std::stoi(mydoc_file_contents);
        std::cout << "myDocHash: " << myDocHash << "\n";

        // read d,n from d_n.txt
        int d, n;
        std::ifstream dnfile;   // create input file stream
        dnfile.open("d_n.txt"); // open the file
        if (dnfile.is_open())
        {
            dnfile >> d;
            dnfile >> n;
            std::cout << "d: " << d << '\n';
            std::cout << "n: " << n << '\n';
        }
        else
        {
            std::cout << "No this file found, file open fail!" << '\n';
        }

        // sign hashed file
        int mySignHash = modExp(myDocHash, d, n);
        std::ofstream mySignHashFile("mydoc.txt.signature");
        std::cout << "mysignHash: " << mySignHash << "\n";
        std::cout << "My signed hash is saved to mydoc.txt.signature file!"
                  << "\n";
        mySignHashFile << mySignHash;

        std::cout << "signed successfully!";
    }
    else if (argv2 == "v")
    {
        std::cout << "Verify the signed file: " << '\n';

        // open mydoc.txt and read all mydoc file contents
        std::string filename = argv[3];
        std::ifstream file;
        file.open(filename);
        std::string mydoc_file_contents;
        if (file.is_open())
        {
            std::stringstream buffer;
            buffer << file.rdbuf();
            mydoc_file_contents = buffer.str();
            file.close();
        }
        else
        {
            std::cout << "No this file found, file open fail!" << '\n';
        }
        std::cout << "mydoc file contents: " << mydoc_file_contents << "\n";

        // hash mydoc file contents
        // std::hash<std::string> myStdHash;
        // int mydocHash = myStdHash(mydoc_file_contents) % 100000 + 100000000;
        // std::cout << "My Doc Hash: " << mydocHash;

        // hash mydoc file contents just from sting to int
        int myDocHash = std::stoi(mydoc_file_contents);
        std::cout << "myDocHash: " << myDocHash << "\n";

        // read signed hash from mydoc.txt.signature
        std::string signature_file_name = argv[4];
        int signedHash;
        std::ifstream hash_sig_file;             // create input file stream
        hash_sig_file.open(signature_file_name); // open the file
        if (hash_sig_file.is_open())
        {
            hash_sig_file >> signedHash;
        }
        else
        {
            std::cout << "No this file found, file open fail!" << '\n';
        }
        std::cout << "my signed hash: " << signedHash << '\n';

        // read e,n from e_n.txt
        int e, n;
        std::ifstream enfile;   // create input file stream
        enfile.open("e_n.txt"); // open the file
        if (enfile.is_open())
        {
            enfile >> e;
            enfile >> n;
            std::cout << "e: " << e << '\n';
            std::cout << "n: " << n << '\n';
        }
        else
        {
            std::cout << "No this file found, file open fail!" << '\n';
        }

        // "encrpt" saved hash value using public key in e_n.txt
        int myDecode = modExp(signedHash, e, n);
        std::cout << "myDecode: " << myDecode << '\n';

        // compare hash value and encrypt saved hash value using public key in e_n.txt
        if (myDecode == myDocHash)
        {
            std::cout << "authentic";
        }
        else
        {
            std::cout << "modified";
        }
    }
    else
    {
        std::cout << "Please retype command line arguments!";
    }
}

// function to calculate x^y mod m
int modExp(int x, int y, int m)
{
    if (y == 0)
    {
        return 1;
    }
    else
    {
        int z = modExp(x, y / 2, m);
        if (y % 2 == 0)
        {
            return z * z % m;
        }
        else
        {
            return x * z * z % m;
        }
    }
}