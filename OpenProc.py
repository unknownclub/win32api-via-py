import ctypes

k_handle = ctypes.WinDLL("Kernel32.dll")

PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)

# HANDLE OpenProcess(
#  DWORD dwDesiredAccess,
#  BOOL  bInheritHandle,
#  DWORD dwProcessId
# );

dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False
dwProcessId = 0x60C

response = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)
error = k_handle.GetLastError()
if error != 0:
    print("Error code: {0}".format(error))
    exit(1)

if response <= 0:
    print("Handle was not created.")
else:
    print("Handle was created.")
    
    
    
   