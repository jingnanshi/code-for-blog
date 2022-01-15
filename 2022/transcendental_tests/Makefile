all: intpow intpow_float

intpow: intpow.cpp
	$(CXX) -O3 -std=c++11 -o intpow intpow.cpp -Wall -I.

intpow_float: intpow_float.cpp
	$(CXX) -O3 -std=c++11 -o intpow_float intpow_float.cpp -Wall -I.

acos: acos.cpp
	$(CXX) -O3 -std=c++11 -o acos acos.cpp -Wall -I.

acos_float: acos_float.cpp
	$(CXX) -O3 -std=c++11 -o acos_float acos_float.cpp -Wall -I.

clean:
	rm -r -f intpow intpow_float acos acos_float
