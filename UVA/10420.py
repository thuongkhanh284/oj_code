# Problem 10420 List of Conquests
import operator
n = int(input())
country_dict = dict()
for i in range(n):
	s = input()
	country = s.split()[0]
	
	if (country in country_dict):
		country_dict[country] = country_dict[country] + 1
	else:
		country_dict[country] = 1
sorted_dict = sorted(country_dict)
for ct in sorted_dict:
	val = country_dict[ct]
	print(ct,val)

	