from collections import defaultdict

def get_input():
    """
    Gets the two lists of a and b from the user

    Returns:
        (list) A - list containing n words
        (list) B - list containing m words
    """
    # n, m are the number of words in list A and list B, respectinely.
    n, m = (map(int, input().split()))
    ls_a, ls_b = [], []

    # Storing the input from the user in the lists
    for i in range(n):
        ls_a.append(input())
    
    for i in range(m):
        ls_b.append(input())

    return ls_a, ls_b

def fill_dict(A):
    dict_A = defaultdict(lambda: -1)
    # Here I'm filling the dict I just made with the indecis of its elements
    for element in A:
        dict_A[element] = " ".join([str(i+1) for i, x in enumerate(A) if x == element])
    
    return dict_A

def print_indecies(B, dict_A):
    for element in B:
        print(dict_A[element])

if __name__ == '__main__':
    # I will call a function for getting the input from the user
    A, B = get_input()
    # Here I call the function to fill the dictionary with the list and its indecies
    dict_A = fill_dict(A)
    # This will print the indicies of each element of B as its occurence in A
    print_indecies(B, dict_A)