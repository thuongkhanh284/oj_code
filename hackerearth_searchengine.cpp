#include <iostream>
#include <string>

using namespace std;

#define MAX 26
struct node
{
	struct node * child[MAX];
	int maxLeaf;
};

struct node *newNode()
{
	struct node *Node = new struct node;
	Node->maxLeaf = 0;
	int i;
	for ( i = 0; i < MAX; i++)
	{
		Node->child[i] = NULL;
	}
	return Node;
}

void addWord(struct node *root, string s, int p)
{
	int ch;
	struct node *temp = root;
	for (int i = 0; i < s.size(); i++)
	{
		ch = s[i] - 'a';
		if (temp->child[ch] == NULL)
		{
			temp->child[ch] = newNode();
		}
		
		if (temp->maxLeaf < p)
		{
			temp->maxLeaf = p;
		}
		temp = temp->child[ch];
	}
	
}

int findWord(struct node *root, string s)
{
	int ch;
	struct node *temp = root;
	int i;
	for ( i = 0; i < s.size(); i++)
	{
		ch = s[i] - 'a';
		if (temp->child[ch] == NULL)
		{
			return -1;
		}	
		temp = temp->child[ch];
	}
	return temp->maxLeaf ;
}

int main()
{
	int n,q;
	cin>>n>>q;
	string s;
	int p;
	int i,j;
	node * trie;
	trie = newNode();
	for (i=0;i<n;i++)
	{
		cin>>s>>p;
		addWord(trie,s,p);
	}
	for (i=0;i<q;i++)
	{
		cin>>s;
		int ret = findWord(trie,s);
		cout<<ret<<endl;
	}
	
	return 0;
}
