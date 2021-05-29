#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin>>n;
    int boy[n];
    for(int i=0;i<n;i++){
        cin>>boy[i];
    }
    int m;
    cin>>m;
    int girl[m];
    for(int i=0;i<n;i++){
        cin>>girl[i];
    }
    sort(boy,boy+n);
    sort(girl,girl+m);
    int ans=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(abs(girl[j]-boy[i])<=1){
                ans++;
                girl[j]=-5;
                break;
            }
        }
    }
    cout<<ans;
    return 0;
}