#include <iostream>
#include <limits>
#include <random>

#include <pcg_random.hpp>

int main()
{
	std::uniform_int_distribution<int> distribution_int(std::numeric_limits<int>::min(), std::numeric_limits<int>::max());
	pcg32 pcg;
	std::cout << distribution_int(pcg) << std::endl;
}
