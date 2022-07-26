def avrg(A, sum, i):
	if i >= 0:
		sum += A[i]
		return avrg(A, sum, i-1)
	else:
		return sum/ len(A)

A= [1,2,3,4,5,6]
print("Sum of Array:", avrg(A, 0, len(A)-1))



# #include <stdio.h>


# float ort(float a[], float top, int i){
# 	if(i>=0){
# 		top= top + a[i];
# 		return ort(a,top,i-1);	
# 	}
# 	else
# 		return top/6;
# }

# int main(){
# 	float A[]= {1,2,3,4,5,6}, top= 0;
	
# 	printf("Toplam: %.2f",ort(A,top,5));
	
# 	return 0;
# }
