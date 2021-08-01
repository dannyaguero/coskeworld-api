import scratch2py
import time
s2py = scratch2py.s2py('username', 'password')
s2py.cloudConnect('COSKEWorld Project ID')
s2py.setCloudVar('coskeworld.APIconnect', 0)
apiConnect = s2py.readCloudVar('coskeworld.APIconnect')
print (apiConnect)
