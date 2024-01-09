import pyautogui as pag
import time

time.sleep(2)
m_posi_x, m_posi_y = pag.position()
print('現在のマウスカーソル位置 x：',m_posi_x)
print('現在のマウスカーソル位置 y：',m_posi_y)
