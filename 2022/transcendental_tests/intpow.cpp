#include <cmath>
#include <cstdio>
#include <cstring>

#define ITERATIONS 10000000

double bench_std_pow(int exp) {
    double result = 0;

    for(size_t i = 0; i < ITERATIONS; ++i){
        result += std::pow(static_cast<double>(i), exp);
    }

    return result;
}

double bench_pow_2() {
    double result = 0;

    for(size_t i = 0; i < ITERATIONS; ++i){
        double base = static_cast<double>(i);
        result += base * base;
    }

    return result;
}

double bench_pow_4() {
    double result = 0;

    for(size_t i = 0; i < ITERATIONS; ++i){
        double base = static_cast<double>(i);
        result += base * base * base * base;
    }

    return result;
}

int main(int argc, char **argv) {
  if (argc < 2) {
    printf("no arg provided; use std pow2\n");
    auto a = bench_std_pow(2);
    printf("result: %f\n", a);
    return 0;
  }

  if (strcmp("std2", argv[1]) == 0) {
    auto a = bench_std_pow(2);
    printf("result: %f\n", a);
  }
  else if (strcmp("std4", argv[1]) == 0) {
    auto a = bench_std_pow(4);
    printf("result: %f\n", a);
  }
  else if (strcmp("mul2", argv[1]) == 0) {
    auto a = bench_pow_2();
    printf("result: %f\n", a);
  }
  else if (strcmp("mul4", argv[1]) == 0) {
    auto a = bench_pow_4();
    printf("result: %f\n", a);
  }

}

