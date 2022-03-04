# Caio Ueno e João Augusto Leite

def mergesort(arr):
    if len(arr) > 1:
        i_mid = len(arr)//2

        # divisao do array em duas metades 
        left_arr = arr[:i_mid]
        right_arr = arr[i_mid:]
        mergesort(left_arr)
        mergesort(right_arr)

        # merge dos dois lados no array principal
        i, j, k = 0, 0, 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] > right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        # se ainda faltam elementos em algum dos lados, transfere todos
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return arr


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        user_input_list = input().split()
        K = int(user_input_list[0])
        C = int(user_input_list[1])
        scores = [float(score) for score in user_input_list[2:]]
        scores_sorted = mergesort(scores)
        print(scores_sorted)
        print(scores_sorted[K-1])