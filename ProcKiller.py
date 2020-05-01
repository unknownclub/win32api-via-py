import ctypes

user_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")

PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)

lpWindowName = ctypes.c_char_p(input("Enter Window Name to Kill: ").encode('utf-8'))
hWnd = user_handle.FindWindowA(None, lpWindowName)
if hWnd == 0:
    print("Error code: {0} - Could Not Grab Handle.".format(k_handle.GetLastError()))
    exit(1)
else:
    print("Got Handle.")


lpdwProcessId = ctypes.c_ulong()
response = user_handle.GetWindowThreadProcessId(hWnd, ctypes.byref(lpdwProcessId))

if response == 0:
    print("Error code: {0} - Could Not Grab PID.".format(k_handle.GetLastError()))
    exit(1)
else:
    print("Got PID.")

dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False
dwProcessId = lpdwProcessId

hProc = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)

if hProc <= 0:
    print("Error Code: {0} - Could Not Grab Priv Handle.".format(k_handle.GetLastError()))
else:
    print("Handle was created.")
    

uExitCode = 0x1
response = k_handle.TerminateProcess(hProc, uExitCode)
if response <= 0:
    print("Error Code: {0} - Could Not Terminate Process".format(k_handle.GetLastError()))
else:
    print("Process went Bye Bye.")



















