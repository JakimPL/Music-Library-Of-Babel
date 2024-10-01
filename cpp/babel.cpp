#include "babel.hpp"
#include "constants.hpp"

Babel::Babel()
{
    mpz_init_set_str(one, "1", 2);
    mpz_init_set_str(a, const_a, 16);
    mpz_init_set_str(b, const_b, 16);
    mpz_init_set_str(c, const_c, 16);

    mpz_init_set_str(mask, const_mask, 16);

    k = 0x50bfe0;
    q = k / 8;
    s = 4 * q;

    mpz_init_set_str(w, "1", 2);
    mpz_init_set_str(z, "1", 2);

    mpz_mul_2exp(w, w, s);
    mpz_mul_2exp(z, w, s);
    mpz_sub(w, w, one);
    mpz_sub(z, z, w);
    mpz_sub(z, z, one);
}

void Babel::lcg(mpz_t x, mpz_t y)
{
    mpz_mul(y, x, a);
    mpz_add(y, y, c);
    mpz_and(y, y, mask);
}

void Babel::rlcg(mpz_t x, mpz_t y)
{
    mpz_sub(y, x, c);
    mpz_mul(y, y, b);
    mpz_and(y, y, mask);
}

void Babel::swap(mpz_t x, mpz_t y)
{
    mpz_t left, right;
    mpz_init_set(left, x);
    mpz_init_set(right, x);

    mpz_and(left, left, w);
    mpz_and(right, right, z);
    mpz_mul_2exp(left, left, s);
    mpz_div_2exp(right, right, s);

    mpz_add(y, left, right);
}

void Babel::encode(mpz_t x, mpz_t y)
{
    swap(x, y);
    lcg(y, y);
    swap(y, y);
    lcg(y, y);
}

void Babel::decode(mpz_t x, mpz_t y)
{
    rlcg(x, y);
    swap(y, y);
    rlcg(y, y);
    swap(y, y);
}

char* Babel::to_string(const char* string, bool enc)
{
    char* result = new char[k];

    mpz_t x, y;
    mpz_init_set_str(x, string, 0);
    mpz_init(y);

    if (enc) {
        encode(x, y);
    }
    else {
        decode(x, y);
    }

    mpz_get_str(result, 16, y);
    return result;
}
