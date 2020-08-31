def sec_to_dhms(diff):
	diff_days = diff//(24*60*60)
	diff -= (24*60*60*diff_days)
	diff_hrs = diff//3600
	diff -= diff_hrs*3600
	diff_min = diff//60
	diff -= diff_min*60
	return [diff_days,diff_hrs,diff_min,diff]

def calculate_seconds(temp):
	val = [3600,60,1]
	sec = 0
	for i in range(len(temp)):
		sec += int(temp[i]) * val[i]
	return sec


def main():
	addresses = ['https://atcoder.jp/contests','https://codeforces.com/contests','https://www.hackerearth.com/challenges']

	import urllib.request
	import datetime
	import re
	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	urllib.request.install_opener(opener)
	date_time_obj_temp = datetime.datetime.now()
	count = 0;
	for _ in addresses:
		urllib.request.urlretrieve(_,"file0.txt")

		with open('file0.txt','r') as file:
		    webpage = file.read()


		if(count == 0):
			regex = u"<time class='fixtime fixtime-full'>(.+?)\+0900</time>"
			x = re.findall(regex,webpage)
			for date_time in x:
				date_time_obj = datetime.datetime.strptime(date_time,'%Y-%m-%d %H:%M:%S')
				difference = date_time_obj - date_time_obj_temp
				diff = difference.total_seconds()
				
				if(diff >= 0 and diff <= 48*60*60):
					diff -= (12600)
					diff = sec_to_dhms(diff)
					print("atcoder contest {} days,{} hours,{} minutes,{} seconds away".format(diff[0],diff[1],diff[2],diff[3]))

		if(count == 1):
			regex = u"Before start <span home=(.+?) noRedirection=\"true\" class=\"countdown\">(.+?)</span>"
			x = re.findall(regex,webpage)
			for bakaiti,time in x:
				if(time[0]=='<'):
					regex = u"<span title=\"(.+?)\">"
					time = re.findall(regex,time)[0]
				diff = calculate_seconds(time.split(':'))
				if(diff >= 0 and diff <= 48*60*60):
					diff = sec_to_dhms(diff)
					print("codeforces contest {} days,{} hours,{} minutes,{} seconds away".format(diff[0],diff[1],diff[2],diff[3]))

		if(count == 2):
			regex = u"<div class=\"date less-margin dark\">(.+?)</div>"
			x = re.findall(regex,webpage)
			for _ in x:
				print("hackerearth contest on",_)

		count += 1

if __name__ == '__main__':
	main()
