/*  <智能优化方法> 的第三次作业
*	作者 : 夏尚梓 学号 1970758
*	version 1.0
*	最后编辑时间: 2019.10.01 9:06am
*/
#include <iostream>
#include <vector>
#include <stdlib.h>    
#include <time.h> 

#define HILLNERBOR 500  // 爬山算法 随机遍历的邻居数
#define SAINNERLOOP 500 // SA 内循环次数
using namespace std;
// 工人的效用矩阵
vector<vector<int>> getUtility() {
	vector<vector<int>> utility; 
	srand((unsigned)time(NULL));
	const int MIN = 1;   //随机数产生的范围    
	const int MAX = 100;
	vector<int> ur;


	for (int j = 0; j < 100; j++)
	{
		for (int i = 0; i < 100; i++) {
			ur.push_back(MIN + rand() % (MAX + MIN - 1));
		}
		utility.push_back(ur);
		ur.clear();
	}
	return utility;
}
// 随机的初始解
vector<int> randperm() {
	vector<int> idx;
	const int MIN = 0;   //随机数产生的范围    
	const int MAX = 99;
	int changeIdx;
	srand((unsigned)time(NULL));
	for (int i = 0; i < 100; i++) // idx = 0:1:99
		idx.push_back(i);
	for (int& x : idx) {
		changeIdx = MIN + rand() % (MAX + MIN - 1);
		swap(idx[x],idx[changeIdx]);
	}
	return idx;
}  
// 计算总时间
int getTotalTime(const vector<int>& plan, const vector<vector<int>>& utility) {
	int res = 0;
	for (int i = 0; i < 100; i++)
		res += utility[i][plan[i]];
	return res;
}
// 爬山算法寻找邻居
int findMinNeighbour(vector<int>& plan, const vector<vector<int>>& utility, int min_time) {
	int temp;
	vector<int> min_plan = plan;
	  //  if 暴力搜索 所有邻域!! 4950 次!
	const int MIN = 0;   //随机数产生的范围    
	const int MAX = 99;
	srand((unsigned)time(NULL));
	for (int i = 0; i < HILLNERBOR; i++) {
		int changeIdx1 = MIN + rand() % (MAX + MIN - 1);
		int changeIdx2 = MIN + rand() % (MAX + MIN - 1);
		vector<int> ch_plan = plan;
		swap(ch_plan[changeIdx1], ch_plan[changeIdx2]);
		temp = getTotalTime(ch_plan, utility);
		if (temp < min_time) {
			min_time = temp;
			min_plan = ch_plan;
		}
	}
	plan = min_plan;// 修改上级函数中的 plan;
	return min_time;
}
// 爬山算法的 main 
double climbHillAlgorithm(int min_time, vector<int> plan, const vector<vector<int>>& utility) {
	//// 爬山算法
	int lastone = min_time;
	for (int i = 0; i < 100; i++) {

		min_time = findMinNeighbour(plan, utility, min_time);// 每次调用 plan会变
	//	cout << "爬山算法的第: " << i << "次:" << min_time << endl;
		if (min_time == lastone) break;
		lastone = min_time;
	}
	cout << "这是爬山算法.....总时间: " << min_time << endl;
	return (double)min_time;
}
// 模拟退火算法
double SA(int min_time_SA, vector<int> plan_SA, const vector<vector<int>>& utility) {
	// 模拟退火
	srand((unsigned)time(NULL));
	const int MIN = 0;   //随机数产生的范围    
	const int MAX = 99;
	double history_min = INT_MAX;
	// 初始化温度
	double T = 100;
	while (T > 0.1)
	{

		for (int i = 0; i < SAINNERLOOP; i++)
		{
			double temp;

			int changeIdx1 = MIN + rand() % (MAX + MIN - 1); // 随机选取邻居
			int changeIdx2 = MIN + rand() % (MAX + MIN - 1);
			swap(plan_SA[changeIdx1], plan_SA[changeIdx2]);
			temp = getTotalTime(plan_SA, utility);
			if (temp <= min_time_SA)
			{
				min_time_SA = temp;
				//cout << "无条件转移啦,总时间:" << min_time_SA << endl;
				if (temp < history_min) history_min = temp;
			}
			else
			{
				double probility = exp((temp - min_time_SA) / (-T));
				double randnum = (rand() % 1000 / (double)1000);
				if (randnum < probility)
				{
					min_time_SA = temp;
					//cout << "随机数是: "<<randnum <<" < "<< probility <<"..总时间:" << min_time_SA << endl;
				}
				else {
					swap(plan_SA[changeIdx1], plan_SA[changeIdx2]);//换回来
					//cout << "不接受,总时间:" << min_time_SA << endl;
				}
			}

		}
		T -= 1;
	}
	cout << "SA算法的历史最小: " << history_min << endl; // 历史最小: 537
	return history_min;
}
double ttext(vector<int> v1, vector<int> v2) {
	double sum1=0, sum2=0,mean1,mean2,s1=0,s2=0,t=0,n1= v1.size(),n2= v2.size();
	for (auto x : v1) sum1 += x;
	for (auto x : v2) sum2 += x;
	mean1 = sum1 / n1;
	mean2 = sum2 / n2;
	for (auto x : v1) s1 += (x - mean1) * (x - mean1);
	s1 /= (n1 - 1);
	for (auto x : v2) s2 += (x - mean2) * (x - mean2);
	s2 /= (n2 - 1);
	t = (mean1 - mean2) / sqrt((n1-1) * s1 + (n2-1) * s2 / (n1+ n2-2)) * (1/n1+1/n2);
	return t;
}
int main() {
	vector<vector<int>> utility;  // 100 * 100 
	vector<int> plan,v1,v2;
	
	utility = getUtility();
	plan = randperm();
	int min_time = getTotalTime(plan, utility);
	double min_time_SA = min_time,res1,res2;
	for (int i = 0; i < 30; i++) {   // 取30次循环实验
		res1 = climbHillAlgorithm(min_time, plan, utility);
		v1.push_back(res1);
		res2 = SA(min_time, plan, utility);
		v2.push_back(res2);
	}
	// T 检验
	double Tvalue;
	Tvalue = ttext(v1, v2);
	cout << "T值为: " << Tvalue << endl;
	cout << "p值取0.05时,样本空间为30时,查表得到T值为1.6973" << endl;
	if (Tvalue > 1.6973) cout << "在95%的置信水平上,两种方法有显著差异" << endl;
	else
		cout << "在95%的置信水平上,两种方法有显著差异" << endl;
	return 0;
}

