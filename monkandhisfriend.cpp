#include <bits/stdc++.h>
using namespace std;
 
int main()
{
   int t;
   cin>>t;
   while(t--)
   {
   		int n,m;
   		
   		long long k;
   		cin>>n>>m;
   		set<long long> mp;
   		for(int i=0;i<n;i++)
   		{
   			cin>>k;
   			mp.insert(k);
   		}
   		for(int i=0;i<m;i++)
   		{
   			cin>>k;
   			if(mp.find(k)!=mp.end())
   			{
   				cout<<"YES\n";
   			}
   			else
   			{
   					mp.insert(k);
   					cout<<"NO\n";
   			}
   			
   		}
   }
    return 0;
}
