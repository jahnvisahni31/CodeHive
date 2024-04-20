class Solution{
    public:
    //arr1,arr2 : the arrays
    // n, m: size of arrays
    //Function to return a list containing the union of the two arrays. 
    vector<int> findUnion(int arr1[], int arr2[], int n, int m)
    {
        //Your code here
        //return vector with correct order of elements
        
        vector<int>ans;
        int i=0,j=0;
        while(i<n and j<m){
            if(arr1[i] < arr2[j]){
                while(i<n-1 and arr1[i]==arr1[i+1]){
                    i++;
                }
                ans.push_back(arr1[i]);
                while(j<m and arr1[i]==arr2[j]){
                    j++;
                }
                i++;
            }
            else{
                while(j<m-1 and arr2[j]==arr2[j+1]){
                    j++;
                }
                ans.push_back(arr2[j]);
                while(i<n and arr2[j]==arr1[i]){
                    i++;
                }
                j++;
            }
        }
        while(i < n){
            while(i<n-1 and arr1[i]==arr1[i+1]){
                i++;
            }
            ans.push_back(arr1[i++]);
        }
        while(j < m){
            while(j<m-1 and arr2[j]==arr2[j+1]){
                j++;
            }
            ans.push_back(arr2[j++]);
        }
        return ans;
    }
};
