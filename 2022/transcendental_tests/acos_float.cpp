#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <tuple>

#define VECTOR_LENGTH 500
#define ITERATIONS 100000

std::vector <std::tuple<float, float>> gen_random_vec(int length) {
  std::vector <std::tuple<float, float>> vec(length);
  for (size_t i = 0; i < vec.size(); ++i) {
    vec[i] = std::make_tuple<float, float>(rand(), rand());
  }
  return vec;
}

float bench_acos(std::vector <std::tuple<float, float>> &a, std::vector <std::tuple<float, float>> &b) {
  float result = 0;
  for (size_t i = 0; i < ITERATIONS; ++i) {
    for (size_t j = 0; j < a.size(); ++j) {
      result += std::acos(std::get<0>(a[j]) * std::get<0>(b[j]) + std::get<1>(a[j]) * std::get<1>(b[j]));
    }
  }
  return result;
}

float bench_dot(std::vector <std::tuple<float, float>> &a, std::vector <std::tuple<float, float>> &b) {
  float result = 0;
  for (size_t i = 0; i < ITERATIONS; ++i) {
    for (size_t j = 0; j < a.size(); ++j) {
      result += std::get<0>(a[j]) * std::get<0>(b[j]) + std::get<1>(a[j]) * std::get<1>(b[j]);
    }
  }
  return result;
}

int main(int argc, char **argv) {

  std::vector <std::tuple<float, float>> a = gen_random_vec(VECTOR_LENGTH);
  std::vector <std::tuple<float, float>> b = gen_random_vec(VECTOR_LENGTH);

  if (argc < 2) {
    printf("no arg provided; use dot\n");
    auto result = bench_dot(a, b);
    printf("result: %f\n", result);
    return 0;
  }

  if (strcmp("dot", argv[1]) == 0) {
    auto result = bench_dot(a, b);
    printf("result: %f\n", result);
  } else if (strcmp("acos", argv[1]) == 0) {
    auto result = bench_acos(a, b);
    printf("result: %f\n", result);
  }
}

