#How do I go about this? Do I model the problem as is or do I try to solve it?

def

def calc_number_of_sheets(counts):
	sum = 0
	for i in counts:
		sum += i
	return sum

def main_job():
	job = 0
	reqd_answer = 0
	counts = [1,0,0,0,0,0]
	#Contains the number of A0,A1,A2..A5 pieces available

	while job < 17:
		number_of_sheets = calc_number_of_sheets(counts)
		available_sheets = get_sheets(counts)
		if number_of_sheets == 1:
			reqd_answer += 1
		selected_sheet =
		job +=1
