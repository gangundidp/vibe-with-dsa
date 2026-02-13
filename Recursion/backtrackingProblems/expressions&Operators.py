class Solution:
    def dfs(self, num, target, start, current_value, last_operand, expression, result):
        # Base case: If we've reached the end of the string
        if start == len(num):
            # If the expression evaluates to the target
            if current_value == target:  
                result.append(expression)
            return
        
        for i in range(start, len(num)):
            if i > start and num[start] == '0':
                return

            current_num = num[start:i+1]  
            # Convert current number to integer
            current_num_val = int(current_num)  
            
            # If we are at the first number, just start the expression
            if start == 0:
                self.dfs(num, target, i + 1, current_num_val, current_num_val, current_num, result)
            else:
                # Add the current number with '+'
                self.dfs(num, target, i + 1, current_value + current_num_val, current_num_val, expression + "+" + current_num, result)
                
                # Add the current number with '-'
                self.dfs(num, target, i + 1, current_value - current_num_val, -current_num_val, expression + "-" + current_num, result)
                
                # Add the current number with '*'
                self.dfs(num, target, i + 1, current_value - last_operand + last_operand * current_num_val, last_operand * current_num_val, expression + "*" + current_num, result)

    # To store the valid expressions
    def addOperators(self, num, target):
        result = []  
        # Start DFS with empty expression
        self.dfs(num, target, 0, 0, 0, "", result)  
        return result

if __name__ == "__main__":
    num = "123"  
    target = 6    
    sol = Solution()
    
    result = sol.addOperators(num, target)
    
    for expr in result:
        print(expr, end=" ")