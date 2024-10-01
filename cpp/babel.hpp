#ifndef BABEL_HPP
#define BABEL_HPP

#include <string>
#include <gmp.h>

class Babel
{
    unsigned long k;
    mpz_t mask;
    mpz_t a, b, c;

    unsigned long q, s;
    mpz_t w, z;

    mpz_t one;

public:
    Babel();
    void swap(mpz_t x, mpz_t y);
    void lcg(mpz_t x, mpz_t y);
    void rlcg(mpz_t x, mpz_t y);
    void encode(mpz_t x, mpz_t y);
    void decode(mpz_t x, mpz_t y);
    char* to_string(const char* string, bool enc = true);
};

#endif // BABEL_HPP
