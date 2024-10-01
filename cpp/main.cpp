#include <string.h>
#include <iostream>
#include <fstream>

#include <gmp.h>
#include "babel.hpp"

#define READ_FILE

#ifdef READ_FILE
std::string read_file(const char* filename)
{
    std::ifstream file(filename);
    if (!file) {
        std::cerr << "Error: Unable to open file " << filename << std::endl;
        return "";
    }

    std::string str;
    std::getline(file, str);
    file.close();

    return str;
}
#endif

int main(int argc, char **argv)
{
    if (argc <= 2) {
        std::cout << "You must provide mode (encode/decode) and the argument." << std::endl;
        return 1;
    }
    else {
#ifdef READ_FILE
        std::string value_str = read_file(argv[2]);
        if (value_str.empty()) {
            return 1;
        }
#else
        const char* c = argv[2];
        std::string value_str(c);
#endif

        mpz_t x, y;
        mpz_init(y);
        mpz_init_set_str(x, value_str.c_str(), 0);

        Babel babel;
        if (strcmp(argv[1], "encode") == 0) {
            babel.encode(x, y);
            gmp_printf("%#Zx\n", y);
        }
        else if (strcmp(argv[1], "decode") == 0) {
            babel.decode(x, y);
            gmp_printf("%#Zx\n", y);
        }

        mpz_clear(x);
        mpz_clear(y);
    }

    return 0;
}
