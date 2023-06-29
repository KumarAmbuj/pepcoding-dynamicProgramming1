def targetsum(n,target,arr):
    if n==0:
        return False
    if target==0:
        return True
    if target<0:
        return False

    return targetsum(n-1,target,arr) or targetsum(n-1,target-arr[n-1],arr)

def findtargetsum(arr,target):

    n=len(arr)
    if targetsum(n,target,arr):
        print('possible')
    else:
        print('not possible')

arr=[4,2,7,1,3]
target=10
findtargetsum(arr,target)