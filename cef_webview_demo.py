
#初始化加载库
import win32exts
win32exts.load_sym("*", "*")
global cef
global root_wnd
global buf


#分配一块内存
buf = win32exts.malloc(520)

#创建cef对象
init_url = None
cef = win32exts.cef_webview_createA("cef", None, 0, 0, 1080, 720, init_url)
print(cef)


def OnViewCreated():
    #cef 创建好了，显示出来
    ret = win32exts.cef_webview_show(cef, True)

    #加载url
    ret = win32exts.cef_webview_load_urlA(cef, "D:\\src\\temp_src\\win32exts_for_Python\\cef_webview_demo.html")
    
    #获取cef根窗口
    root_wnd = win32exts.cef_webview_get_attr_intA(cef, "root_window")
    print("root_wnd = ", root_wnd)

    #注册一个扩展接口给cef： external.get_pid()
    win32exts.cef_webview_registerA(cef, "get_pid", win32exts.callback("OnWebViewEvent"))

def OnViewDestroy():
    pass

def OnDocumentReady():
    #页面已经加载完成，下面我们演示调用一下js脚本：eval("alert(...)") 弹一个框
    pfnCallback = None
    dwTimeout = 0
    #注意 cef_webview_execA() 为变参数目函数，最后要以一个 None 结尾表示参数结束！
    win32exts.cef_webview_execA(cef, "eval", pfnCallback, dwTimeout, "alert(\"test-Javascript!\")", None)
    pass

def OnLoadingFailed(url, desc):
    pass

def OnUrlChanged(url):
    #页面加载中
    print("Loading: " + url)
    pass

def OnTitleChanged(title):
    pass

def OnNewView(url):
    pass

def OnExecute(ret_ptr, func_name, args_and_count):
    #实现我们先前注册给cef的函数：external.get_pid()
    if "get_pid" == func_name:
        #win32exts.MessageBoxW(None, win32exts.L("get_pid() is called"), None, 0)
        dwProcessId = win32exts.GetCurrentProcessId()
        pRet = win32exts.SysMsprintfW(win32exts.L("%u"), dwProcessId)
        win32exts.write_value(ret_ptr, 0, 4, pRet)
    pass

def FreeResult(ret_ptr):
    pass

def OnExecuteCallback(ret_code, exec_id, ret_val):
    pass



#cef事件通知函数
def OnWebViewEvent(args):
    #取参数包
    event = win32exts.read_wstring(win32exts.arg(args, 2))
    status = win32exts.arg(args, 3)
    param1 = win32exts.arg(args, 4)
    if param1 > 0:
        param1 = win32exts.read_wstring(param1)
    param2 = win32exts.arg(args, 5)
    if param2 > 0:
        param2 = win32exts.read_wstring(param2)
    print(event, status, param1, param2)

    #事件分流
    if "OnViewCreated" == event:
        OnViewCreated()
    elif "OnViewDestroy" == event:
        OnViewDestroy()
    elif "OnDocumentReady" == event:
        OnDocumentReady()
    elif "OnLoadingFailed" == event:
        OnLoadingFailed(param1, param2)
    elif "OnUrlChanged" == event:
        OnUrlChanged(param1)
    elif "OnTitleChanged" == event:
        OnTitleChanged(param1)
    elif "OnNewView" == event:
        OnNewView(param1)
    elif "OnExecute" == event:
        OnExecute(status, param1, param2)
    elif "FreeResult" == event:
        FreeResult(status)
    elif "OnExecuteCallback" == event:
        OnExecuteCallback(status, param1, param2)
    
    return "0, 0"


#消息循环初始化函数
def Main(args):
    #cef初始化，指定事件通知函数
    ret = win32exts.cef_webview_init(cef, win32exts.callback("OnWebViewEvent"))
    if 0 == ret:
        return "-1, 4"
    return "0, 4"


#进入消息循环，指定初始化函数
win32exts.cef_webview_message_loop(win32exts.callback("Main"))

