import ctypes

user_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")

# int MessageBoxW(
#  HWND    hWnd,
#  LPCWSTR lpText,
#  LPCWSTR lpCaption,
#  UINT    uType
# );

hWnd = None
lpText = "Hello World"
lpCaption = "Hello Students!"
uType = 0x00000001

response = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType)
error = k_handle.GetLastError()
if error != 0:
    print("Error code: {0}".format(error))
    exit(1)


if response == 1:
    print("User Clicked OK!")
elif response == 2:
    print("User Clicked Cancel!")
    
    
    
    
  