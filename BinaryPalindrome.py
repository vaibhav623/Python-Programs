#DarkSouL

# Program to check if binary representation of a number is palindrome or not.

def binaryPallindrome(num):
	binary = bin(num)
	binary = binary[2:]
	return binary == binary[-1::-1]
if __name__ == "__main__":
    print("Enter a number : ",end="")
    n = int(input())
    f = binaryPallindrome(n)
    if(f):
        print("Yes, ", n, "is a palindrome in it's binary representation Form.")
    else:
        print("No, ", n, "is not a  palindrome in it's binary representation Form.")
