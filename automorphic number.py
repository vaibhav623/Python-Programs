#shared on facebook through-https://www.facebook.com/profile.php?id=100050860832683&__tn__=%2CdC-R-R&eid=ARDuk8Rr3EEw3FqqWx3lziLGNrWrt_ypSR226g5tGR9kkuEqqdLxEcommfcRRcs7qi-oBsSsIkv2Mt0e&hc_ref=ARQXz5WZb-6cSKEOJgWmgQcaiLW3ATG7gGdv0-IZHYPR6kyp4HUyo-x1S_A8o1S2H_8&fref=nf

# Python program to check if a number is Authomorphic 

# Function to check Automorphic number 
def isAutomorphic(N) : 

	# Store the square 
	sq = N * N 
	
	# Start Comparing digits 
	while (N > 0) : 

		# Return false, if any digit of N doesn't 
		# match with its square's digits from last 
		if (N % 10 != sq % 10) : 
			return False
	
		# Reduce N and square 
		N /= 10
		sq /= 10
	
	return True
	
# Driver code 
N = 5
if isAutomorphic(N) : 
	print "Automorphic"
else : 
	print "Not Automorphic"
	

