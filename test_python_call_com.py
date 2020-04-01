import win32exts

#
# 测试 COM 组件, 打开计算器
#
wsh = win32exts.co_create_object("Wscript.Shell")

win32exts.va_invoke(wsh, "Run", "calc")

#以上等价于以下三行
win32exts.co_push_start()
win32exts.push_bstr("calc")
win32exts.co_invoke(wsh, "Run")

win32exts.co_release(wsh)
