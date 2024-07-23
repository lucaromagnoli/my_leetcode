def find_longest(parenthesis):
    found = False
    i = -1
    counter = 0
    while i < len(parenthesis) - 1 >= 0:
        i += 1
        if parenthesis[i : i + 2] == "()":
            found = True
            counter += 2
            parenthesis = parenthesis[:i] + parenthesis[i + 2 :]
            i -= 1
        if i == len(parenthesis) - 2:
            if found:
                i = -1
    return counter


def find_max_len(s):
    stk = []  # Create an empty stack to store indices of '('
    result = 0  # Variable to store the maximum length of valid substring

    # Traverse the input string
    for i in range(len(s)):
        if s[i] == "(":  # If current character is '('
            stk.append(i)  # Push its index onto the stack
        else:
            # If stack is not empty and top of stack contains '('
            if stk and s[stk[-1]] == "(":
                stk.pop()  # Pop the index of '(' from the stack
            else:
                # Push current index onto stack as base for next valid substring
                stk.append(i)

    last = len(s)
    while stk:
        now = stk.pop()  # Pop the index of '(' from stack
        # Calculate the length of valid substring
        result = max(result, last - now - 1)
        last = now  # Update last index

    # Return the maximum length of valid substring
    return max(result, last)


r = find_max_len("(((()")
print(r)
