encoded = [
	"6092811431065039510571141117510710354110410331207041011821010109811181200034210911194121203681123113711461111107212080563037209161092112210341177118510850397106010031167106311941062037",
    "609751186125604051112101012021054038710701034107411680420117811161161104710871252105410620368112011351217041812641108111303701120103212471252036512241227106811371102050704160883113811161050117410750398122812401131102110471107109",
    "8094811431100117003471147124203681260106610910352106811501160117212020366116310671243120511871197041510861268111812471307041410901138121811080421118011461295039511461187120012131206054",
    "808350391122311661253113610801121042612410357107210580424103103541093116411701028042011741183126604081097113611341077111303741116110704180832036611581158118011081112104203611120123303721196119112041203104210571244052"
] 

# Simplified
# for s in encoded:
# 	i = 0
# 	slen = len(s)
# 	while i < slen:
# 		j = s[i:i+4]
# 		print chr(int(j[1:]) - (int(j[0]) + 2)),
# 		i += 4
# 	print ""

codes = {}
offset = 0
ascii_end = 127
while offset < 9:	
	ascii = 32
	while (ascii <= ascii_end):
		codes["{0}{1}".format(offset, str(ascii + offset + 2).zfill(3))] = chr(ascii)
		ascii += 1
	offset += 1

for string in encoded:
	left = 0
	right = 4
	e = 0
	answer = []
	while e < (len(string) / 4) + 1:
		try:
			answer.append(codes[string[left:right]])
		except:
			pass
		left += 4
		right += 4
		e += 1
	print "".join(answer)







