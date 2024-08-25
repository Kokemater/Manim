#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define N 3          // Número de puntos
#define ALPHA 0.00001 // Tasa de aprendizaje reducida
#define ITER 100000   // Número de iteraciones

double polynomial(double x, double a[6]) {
    double result = a[0];
    double x_power = x;
    for (int j = 1; j < 2; j++) {
        result += a[j] * x_power;
        x_power *= x; // Eleva x al siguiente poder sin usar pow
    }
    return result;
}

void gradientDescent(double x[], double y[], double a[2], int n) {
    double dynamic_alpha = ALPHA;

    for (int iter = 0; iter < ITER; iter++) {
        double gradients[2] = {0};

        for (int i = 0; i < n; i++) {
            double error = polynomial(x[i], a) - y[i];
            if (isnan(error) || isinf(error)) {
                printf("Error in computation: error is NaN or Inf at iteration %d\n", iter);
                return;
            }
            double x_power = 1.0;
            for (int j = 0; j < 2; j++) {
                gradients[j] += error * x_power;
                x_power *= x[i];
            }
        }

        for (int j = 0; j < 2; j++) {
            double old_a = a[j];
            a[j] -= (dynamic_alpha / n) * gradients[j];
            if (isnan(a[j]) || isinf(a[j])) {
                printf("NaN/Inf detected, reducing learning rate.\n");
                a[j] = old_a; // Revertir cambio
                dynamic_alpha *= 0.1; // Reducir la tasa de aprendizaje
                break; // Saltar a la siguiente iteración
            }
        }
    }
}

int main() {
    double x[N] = {0, 3, 4}; // Datos de entrada
    double y[N] = {3, 1 , 2}; // Valores observados

    // Normalizar los datos de entrada
    double x_min = x[0], x_max = x[0];
    for (int i = 1; i < N; i++) {
        if (x[i] < x_min) x_min = x[i];
        if (x[i] > x_max) x_max = x[i];
    }
    for (int i = 0; i < N; i++) {
        x[i] = (x[i] - x_min) / (x_max - x_min); // Escalar x a [0, 1]
    }

    double a[6]; // Coeficientes inicializados aleatoriamente
    for (int i = 0; i < 6; i++) {
        a[i] = (double)rand() / RAND_MAX * 0.01; // Inicialización pequeña
    }

    gradientDescent(x, y, a, N);

    printf("Coeficientes ajustados:\n");
    for (int i = 0; i < 6; i++) {
        printf("a%d = %f\n", i, a[i]);
    }

    return 0;
}
