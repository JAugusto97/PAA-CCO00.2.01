if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        user_input_list = input().split()
        K = int(user_input_list[0])
        C = int(user_input_list[1])
        scores = [float(score) for score in user_input_list[2:C]]