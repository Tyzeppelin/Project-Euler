from math import log10

f0 = 0
f1 = 1
fn = 1

j = 1

while log10(fn)+1 < 1000 :
	
	fn = f0 + f1
	f0 = f1
	f1 = fn
	j += 1

print("The first 1000-digits term of fibonacci sequence is the", j, "th")
