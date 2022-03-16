# Emre Sefer, CS 104, Fall 2021, LAB02
# This program prints the rents for different regions
t=1300
c=1500
u=1800
k=2000
		
t_total = t + t*0.1
c_total = c + c*0.1
u_total = u + u*0.1
k_total = k + k*0.1
		
tpay = t_total/3 
cpay = c_total/3
upay = u_total/3
kpay = k_total/3
		
print("Tasdelen: ",tpay)
print("Çekmeköy: ",cpay)
print("Üsküdar: ",upay)
print("Kadýköy: ",kpay)
