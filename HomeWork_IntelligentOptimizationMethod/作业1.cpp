#include<iostream>
int main() 
{
	const int M = 16, A = 5, C = 3, list_number = 20;
	double S[list_number] = { 1 };
	for (int i = 1; i < list_number; i++) S[i] = int(A * S[i - 1] + C) % M;
	for (int i = 0; i < list_number; i++)
	{
		S[i] /=  M;
		S[i] = -2 * sqrt(1 - S[i]) + 2;
		std::cout << S[i] << std::endl;
	}
	return 0;
}
