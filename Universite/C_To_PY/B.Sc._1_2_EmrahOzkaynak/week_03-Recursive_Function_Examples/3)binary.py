def binary(num):
	if num == 0:
		return num
	return num%2 + 10 * binary(int(num/2))

num= int(input("Enter a Number: "))
print("Decimal to Binary", str(num), "is:", binary(num))



# #include <stdio.h>


# int binary(int sayi){
# 	if (sayi==0)
# 		return sayi;
# 	else
# 		return (sayi%2 + 10*binary(sayi/2));
# }

# int main(){
# 	int sayi;
	
# 	printf("Sayiyi Giriniz: ");
# 	scanf("%d",&sayi);
	
# 	printf("Sayinin Binary Hali: %d", binary(sayi));
	
# 	return 0;
# }
