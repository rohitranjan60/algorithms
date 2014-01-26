def lois(n, random_range=100): # lois stands for longest increasing subsequence, n is the number of elements, 
	# let's create a list of n elements with random integers in the 'random range'
	iparr = [random.randint(1, random_range) for _ in range(n)]

	# let's create n sub-lists where each sub-list will hold, in future, the longest increasing subsequence up until that index
	lois = [list() for _ in range(n)]

	# Now, set the first sub-list to hold the first element of the iparr
	lois[0].append(iparr[0])

	for i in range(1, len(iparr)): # start iterating the iparr from index 1
		for j in range(i): # iterate inner loop for 0 < j < i

			# If I (meaning the number at index i in my iparr), found that there's a guy behind me (sitting at index j) who's less than me;
			# then I'll check if the length of my sub-list (meaning the sub-list at index i) 
			# is atleast 1 greater than the length of the sub-list of the guy at index j
			# If that's not true, then I really need to make sure that I acquire the sub-list of the guy sitting at index j.
			# The reason I do this is to make sure that, as the inner loop progresses, if I repeatedly keep finding guys less than me,
			# I can assure myself that I am continuously acquiring the latest and fresh longest sub-lists.
			if iparr[j] < iparr[i] and len(lois[i]) < len(lois[j]) + 1:
				# Acquire the sub-list at index j
				lois[i] = copy.deepcopy(lois[j])
		# Now that I acquired the longest possible sub-list sitting behind me, I can safely append myself to this sub-list
		lois[i].append(iparr[i])

	# Now, I have the lois stored in a sub-list for every index in the range of n numbers.
	# But, I just need the sub-list with maximum length. So, I will sort the list according to the length of sub-lists
	lois.sort(key=lambda x: len(x))

	# So, obviously the longest sub-list should now be at the end
	longest_sublist = lois[-1]

	return iparr, longest_sublist
