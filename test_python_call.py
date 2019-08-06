import win32exts

global g_index
global g_buf

#
# allocate a buffer
#
g_index = 0
g_buf = win32exts.malloc(2*260)

#
# load library symbols
#
iCount = win32exts.load_sym("user32", "*")

#
# sample: call EnumWindows & GetWindowTextW API
#
def EnumWndProc(args):
	global g_index
	global g_buf
	
	hWnd = win32exts.arg(args, 1)
	
	win32exts.push_value(hWnd)
	win32exts.push_value(g_buf)
	win32exts.push_value(260)
	win32exts.func_call("GetWindowTextW")
	strText = win32exts.read_wstring(g_buf, 0, -1)
	
	win32exts.push_value(0)
	win32exts.push_wstring(strText)
	win32exts.push_value(g_buf)
	win32exts.push_value(1)
	win32exts.sym_call("MessageBoxW")

	#
	# return value is a string like: "retval, add_esp_bytes",
	#    for stdcall add_esp_bytes usually equals to 4 * arg_count,
	#    and cdecl add_esp_bytes equals to 0.
	#
	strRetVal = "1, 8"
	
	g_index = g_index + 1
	if g_index > 3:
		strRetVal = "0, 8"
	
	return strRetVal

win32exts.push_function("EnumWndProc")
win32exts.push_value(0)
win32exts.func_call("EnumWindows")

#
# sample: call MessageBoxW
#
win32exts.push_value(0)
win32exts.push_astring("Py_MessageBoxA11")
win32exts.push_value(0)
win32exts.push_value(0)
win32exts.sym_call("MessageBoxA")

#
# sample: call EnumWindows & GetWindowTextW API
#         You can also call it like this
#
g_index = 0
win32exts.func_call("EnumWindows(&EnumWndProc, 0)")

#
# sample: call MessageBoxW
#
win32exts.push_value(0)
win32exts.push_wstring("Py_MessageBoxA22")
win32exts.push_value(0)
win32exts.push_value(0)
win32exts.sym_call("MessageBoxW")
