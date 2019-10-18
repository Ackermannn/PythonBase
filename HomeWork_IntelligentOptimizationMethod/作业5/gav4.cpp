#include<iostream>
#include<vector>
#include<cstdlib>
#include<time.h>
#include<algorithm>
#include<numeric>

#define N 9999 // 随机数设定小数位有四位

using namespace std;
clock_t start, ct_end; 
const vector<int> DF_VALUE = { 28, 16, 24, 18, 22, 6, 14, 0, 20, 12, 10, 2, 8, 4, 6, 30 };
const double R = 0.9;			// 标定系数r
const double M = 100;		    // 标定系数M
const int GENE_LEN = 25;		// 染色体长度
const int POP_SIZE = 100;	    // 种群数量 最好是偶数
const double PC = 0.9;			// 交叉概率
const double PM = 0.002;		// 变异概率

// 重载cout << 
ostream& operator<<(ostream& os, const vector<double>& vec) {
	os << '[';
	for (auto iter = vec.begin(); iter < vec.end() - 1; iter++) {
		os << *iter << ',';
	}
	os << *(vec.end() - 1) << ']' << endl;
	return os;
} 
ostream& operator<<(ostream& os, const vector<int>& vec) {
	os << '[';
	for (auto iter = vec.begin(); iter < vec.end() - 1; iter++) {
		os << *iter << ',';
	}
	os << *(vec.end() - 1) << ']' << endl;
	return os;
}
// 定义 vector +-/基本运算
vector<double> operator-(const vector<double>& vec, int a) {
	vector<double> ans;
	for (auto x : vec) {
		ans.push_back(x - a);
	}
	return ans;
}
vector<double> operator+(const vector<double>& vec, double a) {
	vector<double> ans;
	for (int x : vec) {
		ans.push_back(x + a);
	}
	return ans;
}
vector<double> operator/(const vector<double>& vec, double a) {
	vector<double> ans;
	for (auto x : vec) {
		ans.push_back(x / a);
	}
	return ans;
}
// 随机整数产生器
int rand_int(int a, int b) {
	return (rand() % (b - a + 1)) + a;	
}
// U(0,1) 产生器
double urand() {
	double u_rand = rand() % (N + 1) / (double)(N + 1);
	return u_rand;
}

class GA {
public:
	double sigma = M;
	vector<vector<int>> population;
	double max_fitness = 0, local_max = 0;
	vector<int> max_g;
	vector<double> fitness, value;
	
	GA() {
		srand(time(0)); /*根据当前时间设置“随机数种子”*/
		// 种群初始化
		for (int i = 0; i < POP_SIZE; i++) {
			vector<int> temp = {};
			for (int j = 0; j < GENE_LEN; j++) {
				temp.push_back(rand_int(0,15));
			}
			population.push_back(temp);
		}
	}
	// 定义目标函数
	int DF(const vector<int>& x) {
		int sum = 0;
		for (int i : x) {
			sum += DF_VALUE[i];
		}
		return sum;
	}
	// 计算函数值
	void cal_value() {
		value.clear();
		for (int i = 0; i < POP_SIZE; i++) {
			int temp = DF(population[i]);
			value.push_back(temp);
		}
		auto maxPosition = max_element(value.begin(), value.end()); //找最大
		local_max = *maxPosition;
		if (local_max >= max_fitness) { // 更新历史最大
			max_fitness = local_max;
			max_g = population[maxPosition - value.begin()];
		}
	}
	// 动态线性参数标定
	void calibrate() { 
		auto minPosition = min_element(value.begin(), value.end());
		fitness = value - *minPosition + sigma;
		sigma *= R;
	}
	// 选择——轮盘赌
	void roulette() {
		vector<double> choice_p, accu_p;
		double temp_sum = accumulate(fitness.begin(), fitness.end(), 0);
		choice_p = fitness / temp_sum; // 计算选择概率
		for (auto iter = choice_p.begin() ; iter < choice_p.end(); iter++) { // 计算累加概率
			auto temp = accumulate(choice_p.begin(), iter + 1, 0.0);
			accu_p.push_back(temp);

		}
		vector<vector<int>> new_population = population; // 转动轮盘进行选择
		for (int j = 0; j < POP_SIZE; j++) {
			double k = urand();
			for (int i = 0; i < POP_SIZE; i++) {
				if (k < accu_p[i] ) { 
					new_population[j] = population[i];
					break;
				}	
			}
		}
		population = new_population;
	}
	// 交叉——双切片交叉
	void cross() {
		int half = POP_SIZE / 2;
		for (int i = 0; i < half; i++) {
			if (urand() < PC) {
				int ch1, ch2;
				ch1 = rand_int(0, GENE_LEN); // 随机生成切点1
				ch2 = rand_int(0, GENE_LEN); // 随机生成切点2
				if (ch1 > ch2) swap(ch1, ch2); // 排序
				if (ch1 < ch2) {				// 交叉
					swap_ranges(population[i].begin() + ch1,
						population[i].begin() + ch2,
						population[i + half].begin() + ch1);
				}
			}
		}
	}
	// 变异
	void variate() {
		for (int i = 0; i < POP_SIZE; i++) {
			for (int j = 0; j < GENE_LEN; j++) {
				if (urand() < PM) {
					population[i][j] = rand_int(0, 15);
				}
			}
		}
	}
};

int main() {
	start = clock();
	GA g;
	for (int i = 0; i < 1000; i++) {
		g.cal_value();
		cout << "迭代："      << i + 1
			 << ", 种群适应度：" << g.local_max 
			 << ", 历史最大："   << g.max_fitness << endl;
		if (g.local_max == 750) break;
		g.calibrate();
		g.roulette();
		g.cross();
		g.variate();

	}
	ct_end = clock();
	cout << g.max_g << endl;
	cout << g.max_fitness / 750.0 << endl;
	cout <<"1111片段数目：" 
		<< count(g.max_g.begin(), g.max_g.end(), 15) <<"/25" << endl;
	double endtime = (double)(ct_end - start) / CLOCKS_PER_SEC;
	cout << "Total time:" << endtime << endl;		//s为单位
	return 0;
}
