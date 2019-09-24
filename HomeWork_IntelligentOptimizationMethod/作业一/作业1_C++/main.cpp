/*
作者: Ackermannn
	作业1 : 伪随机作业
	某随机变量概率密度函数为f(x) = -0.5 * x + 1, 用逆变法生成符合
	分布的随机数, 要求利用混合同余法生成均匀分布U(0, 1)的随机序列,
	令M = 16, A = 5, C = 3, S0 = 1.
*/
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