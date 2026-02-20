class Solution:
    def asteroidCollisions(self, asteroids):
        n = len(asteroids)

        st = []
        
        for i in range(n):
                        
            # Push the asteroid in stack if a 
            # right moving asteroid is seen
            if asteroids[i] > 0:
                st.append(asteroids[i])

            # Else if the asteroid is moving 
            # left, perform the collisions
            else:
                
                # Until the right moving asteroids are 
                # smaller in size, keep on destroying them 
                while st and st[-1] > 0 and st[-1] < abs(asteroids[i]):
                    st.pop()    # Destroy the asteroid
                    
                    
                # If there is right moving asteroid 
                # which is of same size of left moving asteroid
                if st and st[-1] == asteroids[i]:
                    st.pop()    # Destroy the asteroid
                    
                # Otherwise, if there is no left moving asteroid, the right moving 
                # asteroid will not be destroyed
                elif not st or st[-1] < 0:
                    st.append(asteroids[i])

        return st
                    
                    
if __name__ == "__main__":
    arr = [10, 20, -10]
    
    sol = Solution()
    
    ans = sol.asteroidCollisions(arr)
    
    print("The state of asteroids after collisions is:", ans)   