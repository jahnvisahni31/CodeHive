class solution{
  public:
  
    int mod = 1e9+7;
    int solve(int sum, int i, int d, int totalSum, vector<int>& arr, vector<vector<int>>&dp){
        if(i>=arr.size()){
           return (2*sum-totalSum == d);
        }
        if(dp[i][sum]!=-1)return dp[i][sum];
        
        int op1 = solve(sum+arr[i],i+1,d,totalSum,arr,dp);
        int op2 = solve(sum,i+1,d,totalSum,arr,dp);
        
        return dp[i][sum] = (op1+op2)%mod;
    }
    int countPartitions(int n, int d, vector<int>& arr) {
        int totalSum = accumulate(begin(arr),end(arr),0);
        if(totalSum - d < 0 || (totalSum+d) % 2) return 0;
        vector<vector<int>>dp(n,vector<int>(totalSum+1,-1));
        return solve(0,0,d,totalSum,arr,dp);
    }
};
