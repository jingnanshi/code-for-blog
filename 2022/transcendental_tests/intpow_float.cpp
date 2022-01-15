#include <cmath>
#include <cstdio>
#include <cstring>

#define ITERATIONS 10000000

float bench_std_pow(int exp) {
    float result = 0;

    for(size_t i = 0; i < ITERATIONS; ++i){
        result += std::pow(static_cast<float>(i), exp);
    }

    return result;
}

float bench_pow_2() {
    float result = 0;

    for(size_t i = 0; i < ITERATIONS; ++i){
        float base = static_cast<float>(i);
        result += base * base;
    }

    return result;
}

float bench_pow_4() {
    float result = 0;

    for(size_t i = 0; i < ITERATIONS; ++i){
        float base = static_cast<float>(i);
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

