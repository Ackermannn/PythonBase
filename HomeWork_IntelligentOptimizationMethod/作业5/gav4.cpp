//不知知道为啥换了语言就不一样了
#include<iostream>
#include<vector>
#include<cstdlib>
#include<time.h>
#include<algorithm>
#include<numeric>

#define N 9999
using namespace std;
const vector<int> DF_VALUE = { 28, 16, 24, 18, 22, 6, 14, 0, 20, 12, 10, 2, 8, 4, 6, 30 };
const double R = 0.9;
const double M = 1000;        // 标定系数M
const int GENE_LEN = 25;   // 染色体长度
const int POP_SIZE = 100;  // 种群数量 最好是偶数
const double PC = 0.90;  // 交叉概率
const double PM = 0.001; // 变异概率
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
	for (int x : vec) {
		ans.push_back(x / a);
	}
	return ans;
}
int rand_int(int a, int b) {
	return (rand() % (b - a + 1)) + a;	
}
double urand() {
	double urand = rand() % (N + 1) / (double)(N + 1);
	return urand;
}
class GA {
public:
	double sigma = M;
	vector<vector<int>> population;
	int max_fitness = 0, local_max = 0;
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
	
	int DF(const vector<int>& x) {
		int sum = 0;
		for (int i : x) {
			sum += DF_VALUE[i];
		}
		return sum;
	}

	void cal_value() {
		value.clear();
		for (int i = 0; i < POP_SIZE; i++) {
			int temp = DF(population[i]);
			value.push_back(temp);
		}
		auto maxPosition = max_element(value.begin(), value.end());
		local_max = *maxPosition;
		if (local_max >= max_fitness) {
			max_fitness = local_max;
			max_g = population[maxPosition - value.begin()];
		}
	}

	void calibrate() {
		auto minPosition = min_element(value.begin(), value.end());
		int local_min = *minPosition;
		fitness = value - local_min + sigma;
		sigma *= R;
	}

	void roulette() {
		vector<double> choice_p, accu_p;
		double temp_sum = accumulate(fitness.begin(), fitness.end(), 0);
		choice_p = fitness / temp_sum;
		//cout << choice_probility << endl;
		for (auto iter = choice_p.begin() ; iter < choice_p.end(); iter++) {
			auto temp = accumulate(choice_p.begin(), iter + 1, 0.0);
			accu_p.push_back(temp);
			//cout << temp << endl;
		}
		vector<vector<int>> new_population;
		for (int j = 0; j < POP_SIZE; j++) {
			for (int i = POP_SIZE - 1; i >= 0; i--) {
				double k = urand();
				if (i == 0) { 
					new_population.push_back(population[0]);
			
				}
				else
					if (k < accu_p[i] && k > accu_p[i - 1]) {
					new_population.push_back(population[i]);
					break;
				
				}
				
			}
		}
		population = new_population;
		//cout << accu_p << endl;
	}

	void cross() {
		int half = POP_SIZE / 2;
		for (int i = 0; i < half; i++) {
			if (urand() < PC) {
				int ch1, ch2;
				ch1 = rand_int(1, GENE_LEN - 1);
				ch2 = rand_int(1, GENE_LEN - 1);
				if (ch1 > ch2) swap(ch1, ch2);
				if (ch1 < ch2)
					swap_ranges(population[i].begin() + ch1, 
								population[i].begin() + ch2,
								population[i + half].begin() + ch1);
			
			}
		}
	
	}
	
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
	GA g;
	for (int i = 0; i < 2000; i++) {
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
	cout << g.max_g << endl;
	cout << g.max_fitness / 750.0 << endl;
	cout <<"1111片段数目：" 
		<< count(g.max_g.begin(), g.max_g.end(), 15) <<"/25" << endl;
	//cout << g.fitness << endl;
	return 0;
}
