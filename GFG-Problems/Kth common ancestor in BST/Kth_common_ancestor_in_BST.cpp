//User function Template for C++

/*// A Tree node
struct Node
{
	int data;
	struct Node *left, *right;
};*/


class Solution
{
    public:
    
    /*You are required to complete below function */
    int kthCommonAncestor(Node *root, int k,int x, int y)
    {
        // your code goes here
        Node* temp =root;
        vector<int>v;
        int mi=min(x,y),mx=max(x,y);
        while(temp!=NULL){
            v.push_back(temp->data);
            if(temp->data < mi){
                temp=temp->right;
            }else if(temp->data>mx){
                temp=temp->left;
            }else {
                if(v.size()<k)return -1;
                return v[v.size()-k];
            }
        }
        return -1;
    }
};
