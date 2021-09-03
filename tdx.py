import pywinauto
import pyautogui

_exe_name = r'D:\new_tdx\TdxW.exe'
_win_login = '通达信金融终端V7.49'
_win_dlg = '通达信信息'
_win_main = '通达信金融终端V7.49 - [行情报价-沪深Ａ股]'
_layout = 'q2'

def start(_exe_name):
    kill(_exe_name)
    app = pywinauto.application.Application().start(_exe_name)

    return app

def kill(_exe_name):
    try:
        app = pywinauto.application.Application().connect(path=_exe_name)
        app.kill()
    except:
        pass

def lonin(window):
    window.child_window(control_id=0x80ba, class_name='SysTabControl32').select(1)
    window.child_window(control_id=1, class_name='Button').click()
    
def dlg_close(window):
    window.close()
    
def dlg_close(window):
    window.close()
    
def layout(window):
    pyautogui.typewrite(_layout, interval=0.01)
    pyautogui.press('enter')
    
def run():
    app = start(_exe_name)
    app[_win_login].wait('enabled', timeout=30)
    window = app.top_window()
    #print(window.window_text())
    if window.window_text() == _win_login:
        lonin(window)
    
    try:
        app[_win_dlg].wait('enabled', timeout=30)
        window = app.top_window()
        if window.window_text() == _win_dlg:
            dlg_close(window)
            
    except:
        pass

    app[_win_main].wait('enabled', timeout=30)
    window = app.top_window()
    if window.window_text() == _win_main:
        layout(window)

    print('Ok.')

if __name__ == '__main__':
    run()
