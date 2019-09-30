#include <iostream>
#include <vector>
#include <stdlib.h>    
#include <time.h> 

#define HILLNERBOR 500
#define SAINNERLOOP 500
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

//
int getTotalTime(const vector<int>& plan, const vector<vector<int>>& utility) {
	int res = 0;
	for (int i = 0; i < 100; i++)
		res += utility[i][plan[i]];
	return res;
}

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
int main() {
	vector<vector<int>> utility;  // 100 * 100 
	vector<int> plan,plan_SA;
	
	utility = getUtility();
	plan_SA = plan = randperm();
	int min_time = getTotalTime(plan, utility);
	double min_time_SA = min_time,res1,res2;
	
	res1 = climbHillAlgorithm(min_time, plan, utility);
	res2 = SA(min_time_SA, plan, utility);


	return 0;
}

