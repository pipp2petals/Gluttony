

def add_total(data):
	total = {
		"calories": 0,
		"price": 0
	}
	for item in data:
		for category in total:
			total[category] += data[item][category] * data[item]["count"]

	return total