def hcf(a, b, i):
    if a%i == 0 and b%i == 0:
        return i
    return hcf(a, b, i-1)


a= int(input("1st Number: "))
b= int(input("2nd Number: "))
	
if a < b:
    a,b = b,a

print("Answer:", str(hcf(a, b, b)))



# #include <stdio.h>

# int hcf(int a, int b, int i){
# 	if(a%i==0 && b%i==0)
# 		return i;
# 	return hcf(a,b,--i);
# }

# int main(){
# 	int a,b,c;
# 	printf("1st Number: ");
# 	scanf("%d",&a);
# 	printf("2nd Number: ");
# 	scanf("%d",&b);
# 	if(a<b){
# 		c=a;
# 		a=b;
# 		b=c;
# 	}
# 	printf("Answer: %d",hcf(a,b,b));
# 	return 0;
# }
