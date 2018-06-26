import pymysql.cursors
import time
import subprocess
import sys
#connect to database two

conn = pymysql.connect(host='10.14.88.224', user='root', password='sensor_cloud', db='neutron')
try:
	with conn.cursor() as cur1:
		sql = "select status,floating_ip_address from floatingips where status=%s"
		res1 = cur1.execute(sql,('DOWN'))
		Regions=cur1.fetchone()
		conn.commit()
		#print Regions[1]
		r=str(Regions[1])
	
finally:
	
	conn.close()

k=subprocess.check_output(["bash","/home/devstack/Desktop/login/create.sh"])
#print type(k)
#print type(r)
#print len(k)
k=str(k)
k=k[0:k.find('\n')]
time.sleep(5)
subprocess.call(["openstack","--os-project-id","1360aeef80294e5e90e3a3cc74c3e2ae","--os-username","admin","--os-password","sensor_cloud","--os-auth-url","http://10.14.88.224/identity/v3","--os-project-domain-name","default","--os-identity-api-version","3","server add floating ip",k,r])

#subprocess.call(["bash","/home/devstack/Desktop/login/ins.sh",k,r])
#subprocess.call(["sudo","openstack","server add floating ip",k,r])
#print k
#print(sys.version)
