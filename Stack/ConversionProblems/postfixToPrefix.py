def postfixToPrefix(s: str):
    st = []
    
    for ch in s:
        if ch.isalnum():
            st.append(ch)
        else:
            op2 = st.pop()
            op1 = st.pop()
            
            st.append(f"{ch}{op1}{op2}")
    return st[-1]

exp = "abc*+d-"
print("Postfix: ", exp)
print(f"Prefix: {postfixToPrefix(exp)}")

exp = "ABC/-AK/L-*"
print("Postfix: ", exp)
print(f"Prefix: {postfixToPrefix(exp)}")