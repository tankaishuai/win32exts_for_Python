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
iCount = win32exts.load_sym("*", "*")


#
# sample: call GetCurrentThreadId API
#
dwThreadId = win32exts.GetCurrentThreadId()


#
# sample: call EnumWindows & GetWindowTextW API
#
def EnumWndProc(args):
	global g_index
	global g_buf
	
	hWnd = win32exts.arg(args, 1)
	
	win32exts.GetWindowTextW(hWnd, g_buf, 260)
	strText = win32exts.read_wstring(g_buf, 0, -1)
	
	win32exts.MessageBoxW(0, win32exts.L(strText), g_buf, 1)

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

win32exts.EnumWindows(win32exts.callback("EnumWndProc"), 0)


#
# sample: call EnumWindows & GetWindowTextW API
#         【You can also call it like this】
#
g_index = 0
win32exts.func_call("EnumWindows(&EnumWndProc, 0)")


#
# sample: call MessageBoxW
#         【You can also call it like this】
#
win32exts.push_value(0)
win32exts.push_wstring("Py_MessageBoxW_V2")
win32exts.push_value(0)
win32exts.push_value(0)
win32exts.sym_call("MessageBoxW")
#
# Or:
#
win32exts.MessageBoxW(0, win32exts.L("Py_MessageBoxW_V2"), 0, 0)


#
# uninit
#
win32exts.uninit()
