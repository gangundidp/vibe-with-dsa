def prefixToInfix(s):
    st = []
    prefix = s[::-1]
    
    for ch in prefix:
        if ch.isalnum():
            st.append(ch)
        else:
            temp = '(' + st.pop() + ch + st.pop() + ')'
            st.append(temp)
    return st[0]

exp = "*+pq-mn"
print("Prefix Expression: ", exp)
print(f"Infix Expression: {prefixToInfix(exp)}")

exp = "*-A/BC-/AKL"
print("Prefix Expression: ", exp)
print(f"Infix Expression: {prefixToInfix(exp)}")
