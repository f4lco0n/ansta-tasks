def generate_zip_code(first_code,last_code):
	""" return list between given strings with '-' """
	first_code_to_int = int(first_code.replace("-",""))
	last_code_to_int = int(last_code.replace("-",""))
	
	zip_code_list = []
	for x in range(first_code_to_int+1,last_code_to_int,1):
		zip_code_list.append(x)

	final_list = []
	for z in zip_code_list:
		x = str(z)
		x = x[:2] + '-' + x[2:]
		final_list.append(x)

	# print(final_list)
	return final_list

def check_missing_values_in_list(given_list,n):
	""" return list with missing values in given_list compared to created_list in range 1-n"""
	created_list = []
	for x in range(1,n+1,1):
		created_list.append(x)

	mising_values_list = [x for x in created_list if not x in given_list]

	#print("given list: ", given_list)
	#print("created list: ",created_list)
	#print("missing values",mising_values_list)
	return mising_values_list


def generate_values_in_range():
	""" return list of values in range 2.0-5.5 with 0.5 step"""
	return [x * 0.5 for x in range(4,12)]



generate_zip_code("79-900","80-155")
check_missing_values_in_list([2,3,7,4,9],10)
generate_values_in_range()