#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <queue>

using namespace std;

#define MAX 4
struct node
{
	struct node * child[MAX];
	bool endWord;
};
int flag_preffix = 0;

struct node *newNode()
{
	struct node *Node = new struct node;
	Node->endWord = false;
	int i;
	for ( i = 0; i < MAX; i++)
	{
		Node->child[i] = NULL;
	}
	return Node;
}

void addWord(struct node *root, string s)
{
	int ch;
	struct node *temp = root;
	map <char , int> mp;
	mp['A'] = 0;
	
	for (int i = 0; i < s.size(); i++)
	{
		ch = s[i] - '0';
		if (temp->child[ch] == NULL)
		{
			temp->child[ch] = newNode();
		}
		
		
		temp = temp->child[ch];
		if (temp->endWord==true )
		{
			flag_preffix = 1;
		}
	}
	temp->endWord=true;
	
}


int main()
{
	int testcase, intestcase;
	cin>>testcase;
	intestcase = 1;
	int n;
	while (intestcase <= testcase)
	{
		cin>>n;
		
		int i,j;
		struct node * trie;
		trie = newNode();
		flag_preffix = 0;
		string s;
		for (i=0;i<n;i++)
		{
			cin>>s;
			addWord(trie,s);
		}
		cout<<"Case "<<intestcase<<": ";
		if (flag_preffix == 1)
		{
			cout<<"NO"<<endl;
		}
		else
		{
			cout<<"YES"<<endl;
		}
		intestcase++;
		
		delete trie;
	}
	
	return 0;
}
