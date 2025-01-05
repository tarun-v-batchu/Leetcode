# Get Number of Teams
# FULLTIME
# There are n candidates with the expense to hire them listed in an array. The expense to hire the i'th candidate is cost[i]. 
# The budget for hiring a pair of new members into our team is between min_cost and max_cost, both inclusive.

# Given the array cost and two integers min_cost and max_cost , find the number of pairs of people whose total expense is 
# between min_cost and max_cost, both inclusive.

# Function Description:
# Complete the function getNumTeams in the editor below.
# getNumTeams takes the following arguments:
#   - int cost[n] : the expense of hiring the candidates
#   - int min_cost: the minimum total expense
#   - int max_cost : the maximum total expense

# Returns
#    - long int: the number of pairs of candidates with the sum of costs in the given range

# Example 1 :
# Input: cost = [2, 3, 4, 5], min_cost = 5, max_cost = 7
# Output: 4
# Explanation:
# cost 1 | cost 2 | cost Sum
# 2 | 3 | 5
# 2 | 4 | 6
# 2 | 5 | 7
# 3 | 4 | 7
# Thus there are 4 possible pairs of employees.


# Example 2 :
# Input: cost = [1, 3, 5, 3, 8, 7, 2, 10], min_cost = 11, max_cost = 15
# Output: 10

# Constraints:
#   - 1≤n≤10^5
#   - 1≤cost[i]≤n
#   - 0≤min_cost≤max_cost≤10^5



def getNumTeams(cost: List[int], min_cost: int, max_cost: int)->int:
    
    table = {}
    count = 0
    
    for i in cost :
        
        for j in range(min_cost - i, max_cost - i + 1) :
            
            if j in table :
                count += table[j]
            
        if i not in table :
            table[i] = 1
        else :
            table[i] += 1
    
    return count
    
