def prefixToPostfix(s: str):
    st = []
    prefix = s[::-1]
    
    for ch in prefix:
        if ch.isalnum():
            st.append(ch)
        else:
            temp = st.pop() + st.pop() + ch
            st.append(temp)
    
    return st[-1]

exp = "*+ab-cd"
print("Prefix: ", exp)
print(f"Postfix: {prefixToPostfix(exp)}")
        
exp = "/-ab*+def"
print("Prefix: ", exp)
print(f"Postfix: {prefixToPostfix(exp)}")

        