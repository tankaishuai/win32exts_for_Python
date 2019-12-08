
import win32exts

win32exts.load_sym("*", "*")
ax = win32exts.co_create_object("vb6com.vb6test")
print win32exts.co_list_sym(ax)

# Function up_str(ByVal x As String, ByRef a As String) As Long



# 通常以传值方式调用，但无法获取修改后的参数结果
print win32exts.va_invoke(ax, "up_str", "e", "abcd")



# up_str() 第2个参数 以引用方式调用
win32exts.co_push_start()
win32exts.push_bstr("e")
win32exts.push_bstr("abcd")
i = win32exts.co_convert_by_ref()     #声明该参数以引用方式调用
print win32exts.co_invoke(ax, "up_str")

# 获取修改过的参数值
print win32exts.co_get_by_ref(i)
