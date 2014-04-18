def cazer(s):
	charset = "abcdefghijklmnopqrstuvwxyz"
	length = len(charset)
	s = s.strip().lower()
	a = ""
	for i in range(0, len(s)):
		idx = charset.find(s[i])
		if(idx == -1):
			a += s[i]
		else:
			a += charset[(idx + 13)% length]
	return a

'''
charset = "abcdefghijklmnopqrstuvwxyz"
s = " hh123 ee llo "
print charset.find(s[0])
#print cazer(s)
#print s.strip()
'''
