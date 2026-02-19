def postfixToInfix(s: str):
    st = []
    
    for ch in s:
        if ch.isalnum():
            st.append(ch)
        else:
            # tmp = "(" + st.pop() + ch + st.pop() + ")"
            # tmp = f"({st.pop()}{ch}{st.pop()})"
            op2 = st.pop()
            op1 = st.pop()
            st.append(f"({op1}{ch}{op2})")
    return st[-1]

exp = "ab+c*"
print("Postfix: ", exp)
print("Infix: ", postfixToInfix(exp))