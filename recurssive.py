def fn_recursive_print(n):
    if n > 0:
        fn_recursive_print(n - 1)
        print(n)

x=5
fn_recursive_print(5)   

# n=4
# nums = [4,5,8,2]
# print(nums)
# q= len(nums)
# print(q) 
# print(nums[1])
# print(nums[q-1])

print("Hello, World!")