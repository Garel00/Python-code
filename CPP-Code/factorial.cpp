// Online C++ compiler to run C++ program online
#include <iostream>

int factorial(int n);

int main() {
    // Write C++ code here
    int resultado = factorial(10);
    std::cout << "Resultado: " << resultado << '\n';
    return 0;
}

int factorial(int n) {
    
    int resultado = 1;
    if(n > 1) {
        
        return n * factorial(n-1);
    } else {
        return 1;
    }
}
