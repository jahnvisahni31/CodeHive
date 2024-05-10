class Solution {
public:
    static bool comp(pair<double, pair<int, int>> &a, pair<double, pair<int, int>> &b) {
        return a.first < b.first;
    }

    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        int n = arr.size();
        vector<pair<double, pair<int, int>>> v;

        for(int i=0; i<n; i++)
            for(int j=i+1; j<n; j++)
                v.push_back(make_pair((double)arr[i]/arr[j], make_pair(arr[i], arr[j])));

        sort(v.begin(), v.end(), comp);

        return vector<int> {v[k-1].second.first, v[k-1].second.second};
    }
};
