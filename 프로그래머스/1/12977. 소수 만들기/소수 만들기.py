def solution(nums):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    for i in range(len(nums)-2):
        
        for j in range(i+1,len(nums)-1):
            for k in range(j+1, len(nums)):
                if(primenumber(nums[i]+nums[j]+nums[k])):
                    print(nums[i]+nums[j]+nums[k])
                    answer +=1
    return answer

def primenumber(x):
    for i in range(2, x):	# 2부터 x-1까지의 모든 숫자
    	if x % i == 0:		# 나눠떨어지는게 하나라도 있으면 False
        	return False
    return True