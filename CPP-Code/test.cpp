
#include <iostream>
#include <algorithm>
const int n = 4;
int numeros[n] = {4, 3, 6, 1};

int algorithm1(int array[]);

int main() {
	int resultado = algorithm1(numeros);
	std::cout << "Resultado: " << resultado << '\n';
	return 0;
}

int algorithm1(int array[]) {
	int best = 0;
	for (int a = 0; a < n; a++) {
		for (int b = a; b < n; b++) {
			int sum = 0;
			for (int k = a; k <= b; k++) {
				sum += array[k];
			}
			best = std::max(best, sum);
		}
	}
	return best;
}
