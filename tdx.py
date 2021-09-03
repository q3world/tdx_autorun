import pywinauto
import pyautogui

_exe_name = r'D:\new_tdx\TdxW.exe'
_win_login = '通达信金融终端V.*'
_win_dlg = '通达信信息'
_win_main = '通达信金融终端V.* \- '
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

def connect(_exe_name):
    try:
        app = pywinauto.application.Application().connect(path=_exe_name)
    except:
        app = pywinauto.application.Application().start(_exe_name)

    return app

def lonin(app):
    app.top_window().child_window(control_id=0x80ba, class_name='SysTabControl32').select(1)
    app.top_window().child_window(control_id=1, class_name='Button').click()
    
def dlg_close(app):
    app.top_window().close()
    
def layout(app):
    app.top_window().set_focus()
    pyautogui.typewrite(_layout, interval=0.01)
    pyautogui.press('enter')
    
def run():
    app = start(_exe_name)
    result = app.window(title_re=_win_login).wait('enabled', timeout=30)
    if result:
        lonin(app)
    
    result = app.window(title_re=_win_dlg).wait('enabled', timeout=30)
    if result:
        dlg_close(app)

    result = app.window(title_re=_win_main).wait('enabled', timeout=30)
    if result:
        layout(app)

    print('Ok.')

if __name__ == '__main__':
    run()
