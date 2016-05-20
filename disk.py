import os
import time
sleepTime = 1
  

def disk_usage(path):  
    disk = {}  
    st = os.statvfs(path)  
    free = (st.f_bavail * st.f_frsize)  
    total = (st.f_blocks * st.f_frsize)  
    used = (st.f_blocks - st.f_bfree) * st.f_frsize  
    disk['total'] = total
    disk['used'] = used
    disk['free'] = free
    return disk  

if __name__ == '__main__':
	# while (1):
		time.sleep(sleepTime)
		begin = time.time()
		disk = disk_usage('/')
		print '------------------'
		print "total: %f" %(disk['total'])
		print "free: %f" %(disk['free'])
		print "used: %f"  %(disk['used'])
		rate = (float(disk['used']) / disk['total']) * 100 
		end = time.time()
		print ("disk usage:%.2f%%" %(rate))
		print ("time:%f" %(end- begin))
		print '------------------'
