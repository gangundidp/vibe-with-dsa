class Solution:
    def trap(self, height):
        n = len(height)
        
        # Initialize two pointers at both ends of the list
        left, right = 0, n - 1
        
        max_left = 0
        max_right = 0
        
        total_water = 0
        
        # Iterate until left pointer meets right pointer
        while left <= right:
            # If left bar is smaller or equal to right bar
            if height[left] <= height[right]:
                # If current left bar is higher than max_left, update max_left
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    # Water trapped on left is difference between max_left and current height
                    total_water += max_left - height[left]
                left += 1  # Move left pointer to the right
            else:
                # If current right bar is higher than max_right, update max_right
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    # Water trapped on right is difference between max_right and current height
                    total_water += max_right - height[right]
                right -= 1  # Move right pointer to the left
        
        return total_water

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    
    sol = Solution()
    result = sol.trap(height)
    print("Trapped Rainwater:", result)
