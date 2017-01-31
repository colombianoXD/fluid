"""Counting lines for Yoire by GoXo"""
import requests

URL = 'http://yoire.com/challenges/automation/basic/1_fast_count.php'
COOKIE = {'PHPSESSID': 'r9houb5qjp7s643f4d3foucbd7'}
SES = requests.Session()
GET = SES.get(URL, cookies=COOKIE)
TEXT = GET.content.split('\n')
LINES = len(TEXT) - 53
POSTED = SES.post(URL, data={'solution': LINES}, cookies=COOKIE)
print POSTED.content
