def HCF(a, b, i):
	if a%i == 0 and b%i == 0:
		return i
	return HCF(a, b, i-1)


a= int(input("First Number: "))
b= int(input("Second Number: "))

if a < b:
	a,b = b,a

print("Answer is:", HCF(a, b, b))



# #include <stdio.h>


# int obeb(int a, int b){
# 	int c,i;
# 	if(a<b)
# 		c=a;a=b;b=c;
	
# 	for(i=b; i>0; i--){
# 		if(a%i==0 && b%i == 0)
# 			return i;
# 	}
# 	return i;
# }

# int main(){
# 	int a,b,c;
	
# 	printf("Ilk sayi: ");
# 	scanf("%d",&a);
# 	printf("Ikinci sayi: ");
# 	scanf("%d",&b);
	
# 	c= obeb(a,b);
# 	printf("Cevap= %d",c);
	
# 	return 0;
# }
