class Solution:
    def accountsMerge(self, accounts):
        parent = {}
        rank = {}
        email_to_name = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
        
        # Step 1: Initialize the union-find structure and map emails to names
        for account in accounts:
            name = account[0]
            first_email = account[1]
            if first_email not in parent:
                parent[first_email] = first_email
                rank[first_email] = 0
            email_to_name[first_email] = name
            
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                    rank[email] = 0
                email_to_name[email] = name
                union(first_email, email)
        
        # Step 2: Group emails by their root
        root_to_emails = {}
        for email in parent.keys():
            root = find(email)
            if root not in root_to_emails:
                root_to_emails[root] = []
            root_to_emails[root].append(email)
        
        # Step 3: Prepare the final result
        merged_accounts = []
        for emails in root_to_emails.values():
            emails.sort()
            name = email_to_name[emails[0]]
            merged_accounts.append([name] + emails)
        
        return merged_accounts
