import platform
import psutil
import cpuinfo
import wmi

#64 or 32 bit
print(f"Architecture: {platform.architecture()}")
print(f"Network Name: {platform.node()}")
print(f"Operating System: {platform.platform()}")
print(f"Processor: {platform.processor()}")

my_cpuinfo = cpuinfo.get_cpu_info()
print(f"Full CPU Name: {my_cpuinfo['brand_raw']}")
print(f"Full CPU Name: {my_cpuinfo['hz_actual_friendly']}")
print(f"Full CPU Name: {my_cpuinfo['hz_advertised_friendly']}")
print(my_cpuinfo)

print(f"Total RAM: {psutil.virtual_memory().total/ 1024 / 1024 / 1024:.2f} GB")

#Cache size amongst other findings
pc = wmi.WMI()
os_info = pc.Win32_OperatingSystem()[0]
print(f"OS Info {os_info}")
print(pc.Win32_Processor()[0])
print(f"GPU info: {pc.Win32_VideoController()[0]}")

#print(my_cpuinfo.keys()) for more options
