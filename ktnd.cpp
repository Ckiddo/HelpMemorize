#include <stdio.h>
#include <vector>
#include <string>

/*
用于ktnd里的密码破解

*/


std::vector<std::string> store1 = {
			"about",
			"after",
			"again",
			"below",
			"could",
			"every",
			"first",
			"found",
			"great",
			"house",
			"large",
			"learn",
			"never",
			"other",
			"place",
			"plant",
			"point",
			"right",
			"small",
			"sound",
			"spell",
			"still",
			"study",
			"their",
			"there",
			"these",
			"thing",
			"think",
			"three",
			"water",
			"where",
			"which",
			"world",
			"would",
			"write"
			};
char store2[6][6];



void getin(){
	for(int i = 0;i < 6;i++	){
		scanf("%s",store2[i]);
	}
}
bool check(std::string s){
	for(int i = 0;i < 5;i++){
		bool inin = false;
		for(int j = 0;j < 6;j++){
			if(s[i] == store2[j][i]){
				inin = true;
			}
		}
		if(!inin){
			return false;
		}
	}
	printf("answer:%s\n", s.c_str());
	return true;
}
void output(){
	for(int i = 0;i < 35;i++){
		if(check(store1[i])){
			return;
		}
	}
}

void solve(){
	getin();
	output();
}

int main(){
	//check("asdf");
	solve();
}