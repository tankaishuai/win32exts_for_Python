
#
# 抓取动态网页示例
#
url = "http://www.qq.com"

import win32exts
win32exts.load_sym("*", "*")

pText = win32exts.SysTextByBrowser(win32exts.L(url), 10, 3, None)
strText = "err"
if pText != 0:
	strText = win32exts.read_wstring(pText, 0, -1)
	win32exts.free(pText)
print (strText)
