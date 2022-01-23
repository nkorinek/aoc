## DO NOT RUN THIS WILL CRASH COMPUTER

# from aocd.models import Puzzle
# import numpy as np
# from numba import njit
# from timeit import default_timer as timer
#
# puzzle = Puzzle(year=2021, day=6)
#
# data = puzzle.input_data
#
# # This is gonna make me learn how to run a script on my gpu haha
#
# # @njit
# def check_lanternfish_amount(arr, num_days):
#     lanternfish_arr = np.copy(arr)
#     days = np.array(list(range(num_days)))
#     for day in days:
#         print("Made it to day " + str(day))
#         print("------------")
#         start = timer()
#         new_fish = lanternfish_arr==0
#         print("Get mask: ", timer()-start)
#         start = timer()
#         amount_new_fish = new_fish.sum()
#         print("Get sum: ", timer()-start)
#         start = timer()
#         fish_refresh = new_fish*np.int32(7)
#         print("Get 6's: ", timer()-start)
#         start = timer()
#         lanternfish_arr = lanternfish_arr-np.int32(1)
#         print("Subtract: ", timer()-start)
#         start = timer()
#         lanternfish_arr = np.add(lanternfish_arr, fish_refresh)
#         print("add: ", timer()-start)
#         start = timer()
#         curr_length = ~np.isnan(lanternfish_arr).sum()
#         lanternfish_arr[curr_length:curr_length+amount_new_fish] = 8
#         print("append: ", timer()-start)
#     return(lanternfish_arr.shape[0])
#
# if __name__ == "__main__":
#
#     lanternfish = np.fromiter(data.split(','), dtype=int)
#
#     yeehaw = np.empty(1000000000)
#     yeehaw[:] = np.nan
#     # yeehaw[1:lanternfish.shape[0]] = lanternfish
#
#     answer_a = check_lanternfish_amount(yeehaw, 80)
#
#     print(answer_a)
#
#     # answer_b = check_lanternfish_amount(lanternfish, 256)
#     #
#     # print(answer_b)
