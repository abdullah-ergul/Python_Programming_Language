def findMax(A, i, max):
	if i<0:
		return max

	if A[i] > max:
		max= A[i]
	return findMax(A, i-1, max)


A= [1,3,2,7,5]
max= A[0]

print("Maximum value in list:", str(findMax(A, len(A)-1, max)))



# #include <stdio.h>


# int enb_bul(int A[], int i, int enb){
# 	if(i<0)
# 		return enb;
# 	if(A[i]>enb)
# 		enb= A[i];
# 	return enb_bul(A,--i,enb);
# }

# int main(){
# 	int A[]= {1,3,2,7,9};
# 	int enb= A[0];
# 	printf("Dizideki en buyuk eleman: %d",enb_bul(A,6,enb));
	
# 	return 0;
# }
