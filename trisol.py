import tkinter
import math
import numpy as np
root = tkinter.Tk()

root.title('Triangle Solver')
root.geometry("1280x1000")
root.configure(bg="white")
root.resizable(0,0)
####################################################################Header##########################################################
####################################################################Header##########################################################
####################################################################Header##########################################################
label_heading = tkinter.Label(root, text="Triangle Solver ",bg="white")
label_heading.config(font=("OpenSans", 15))
label_heading.pack()

label_blank1 = tkinter.Label(root,bg="white")
label_blank1.config()
label_blank1.pack()
#creating top frame
frame = tkinter.Frame(root,bg="white")
frame.config()
frame.pack()

frameLeft = tkinter.Frame(frame,bg="white")
frameLeft.config()
frameLeft.pack(side=tkinter.LEFT)

label_blank2 = tkinter.Label(frame,bg="white",text="  ")
label_blank2.config()
label_blank2.pack(side=tkinter.LEFT)
		
frameCenter = tkinter.Frame(frame,bg="white")
frameCenter.config()
frameCenter.pack(side=tkinter.LEFT)

label_blank3 = tkinter.Label(frame,bg="white",text="  ")
label_blank3.config()
label_blank3.pack(side=tkinter.LEFT)

frameRight = tkinter.Frame(frame,bg="white")
frameRight.config()
frameRight.pack(side=tkinter.LEFT)
####################################################################Header##########################################################
####################################################################Header##########################################################
####################################################################Header##########################################################
canvas = tkinter.Canvas(frameCenter, width=700, height=500)
def draw(a, b, c):
	canvas.delete('all')
	A = (0, 0) ############Set xA,yA = (0,0)
	B = (c, 0) ############Set xB,yB = (c,0)
	# Calculate coordinates of C
	hc = (2 * (a**2*b**2 + b**2*c**2 + c**2*a**2) - (a**4 + b**4 + c**4))**0.5 / (2.*c)
	dx = (b**2 - hc**2)**0.5
	if abs((c - dx)**2 + hc**2 - a**2) > 0.01: dx = -dx 
	C = (dx, hc) ###########################  Coordinates of C
	coords = [int((x + 1) * 40) for x in A+B+C] ############### Translation A(0,0) -> A(40,40) B(c,0)-> ((c+1)*40,40) ,....
	canvas.create_polygon(*coords,tags="triagle",fill="white",outline='black')
	xA, yA = coords[:2]          
	xB, yB = coords[2:4]
	xC, yC = coords[4:]
	mxa,mya = [(xC+xB)/2,(yB+yC)/2]     ################## coordinates of middle BC
	mxb,myb = [(xA+xC)/2,(yA+yC)/2]     ################## coordinates of middle AC
	mxc,myc = [(xA+xB)/2,(yA+yB)/2]     ################## coordinates of middle AB
	#######################Solve coordinates of H,K,I######################################
	LHA = np.array([[yC-yB , xB-xC] , [xC-xB , yC-yB]])
	RHA = np.array([xB*yC-xC*yB , xA*(xC-xB)+yA*(yC-yB)])
	LHB = np.array([[yC-yA , xA-xC] , [xC-xA , yC-yA]])
	RHB = np.array([xA*yC - yA*xC , xB*(xC-xA)+yB*(yC-yA)])
	xhA,yhA = np.linalg.solve(LHA,RHA) ########################xH,yH
	xhB,yhB = np.linalg.solve(LHB,RHB) ########################xK,yK
	xhC,yhC = [xC,yA] #########################################xI,yI
	########################draw ah,bk,ci#######################################################
	canvas.create_line(xA,yA,xhA,yhA,tags='ha',dash='-')
	canvas.create_line(xB,yB,xhB,yhB,tags='hb',dash='-')
	canvas.create_line(xC,yC,xhC,yhC,tags='hc',dash='-')
	##################################addition ah,bk,ci##########################################
	canvas.create_line(xC,yC,xhB,yhB,tags='hhc1',dash='-')
	canvas.create_line(xC,yC,xhA,yhA,tags='hhc2',dash='-')
	##################################addition ah,bk,ci##########################################
	canvas.create_line(xA,yA,xhB,yhB,tags='hhc1',dash='-')
	canvas.create_line(xA,yA,xhC,yhC,tags='hhc2',dash='-')
	##################################addition ah,bk,ci##########################################
	canvas.create_line(xB,yB,xhA,yhA,tags='hhc1',dash='-')
	canvas.create_line(xB,yB,xhC,yhC,tags='hhc2',dash='-')
	##############################################################################################
	
	#########################Name HEK #####################################################
	canvas.create_text(xhA+15,yhA,font="Purisa",
					   text="H")
	canvas.create_text(xhB-15,yhB,font="Purisa",
					   text="K")
	canvas.create_text(xhC,yhC-15,font="Purisa",
					   text="E")
	########################Name h1,h2,h3 #####################################################
	canvas.create_text((xhC+xC)/2,(yhC+yC)/2.5,font="Purisa",
					   text="h3")
	canvas.create_text((xhA+xA)/2,(yhA+yA)/2,font="Purisa",
					   text="h1")
	canvas.create_text((xhB+xB)/2 + 15,(yhB+yB)/2-15,font="Purisa",
					   text="h2")
	######################Name edge #####################################################
	canvas.create_text(mxa+15,mya,font="Purisa",
					   text="a",tags='ma')
	canvas.create_text(mxb-15,myb,font="Purisa",
					   text="b",tags='mb')
	canvas.create_text(mxc,myc-15,font="Purisa",
					   text="c",tags='mc')
	#####################Name angle A,B,C
	canvas.create_text(xA-10,yA-10,font="Purisa",
					   text="A")
	canvas.create_text(xB+10,yB-10,font="Purisa",
					   text="B",tags='B')
	canvas.create_text(xC,yC+10,font="Purisa",
					   text="C",tags='C')
	
	canvas.pack()
def triangle_result():
	a = side1.get()
	b = side2.get()
	c = side3.get()
	if (a+b>c) & (b+c>a) & (a+c>b) & (a>0) & (b>0) & (c>0):
		if (a==b)&(b==c):
			tritype.config(text = "Tam giác đều ")
		elif (a==b)& (a!=c) | (a==c)&(a!=b) | (b==c) & (b!=a):
			tritype.config(text = "Tam giác cân ")
		elif (a*a==b*b+c*c)|(b*b==a*a+c*c)|(c*c==a*a+b*b):
			tritype.config(text = "Tam giác vuông ")
		elif (a*a==b*b+c*c)|(b*b==a*a+c*c)|(c*c==a*a+b*b) & (a==b)& (a!=c) | (a==c)&(a!=b) | (b==c) & (b!=a):
			tritype.config(text = "Tam giác vuông cân ")
		elif (c**2)>(b**2+a**2):
			tritype.config(text = "Tam giác tù ")
		else:
			tritype.config(text = "Tam giác nhọn ")
	cv = a+ b + c
	p = cv/2
	dt = math.sqrt(p*(p-a)*(p-b)*(p-c))
	h1 = 2*dt/a
	h2 = 2*dt/b
	h3 = 2*dt/c
	na = (b*b+c*c-a*a) / (2*b*c)
	nb = (c*c+a*a-b*b) / (2*a*c)
	nc = (a*a+b*b-c*c) / (2*a*b)
	goc_a_r = math.acos(na)
	goc_a = goc_a_r * 180 / math.pi
	goc_b_r = math.acos(nb)
	goc_b = goc_b_r * 180 / math.pi
	goc_c_r = math.acos(nc)
	goc_c = goc_c_r * 180 / math.pi
	#####################################################Out put result###########################################################	
	#####################################################Out put result###########################################################	
	#####################################################Out put result###########################################################	
	label_area.config(text = "Diện tích:  "+str(round(dt,2)))
	label_cv.config(text="Chu vi: "+str(round(cv,2)))
	heigth_label.config(text= "Đường cao: " + "h1:" + str(round(h1,2)) + "\n" + "h2:" + str(round(h2,2)) +"\n" "h3:" + str(round(h3,2)))
	angle_label.config(text = "Góc: " + "Alpha:" + str(round(goc_a,2)) +  "\n" + "Beta:" + str(round(goc_b,2)) +"\n" "Gamma:" + str(round(goc_c,2)))
	draw(a,b,c)
############################################# Controller to get input ##################################################
side1 = tkinter.DoubleVar()
side2 = tkinter.DoubleVar()
side3 = tkinter.DoubleVar()
#adding controls to left frame
label_left = tkinter.Label(frameLeft, text="Nhập cạnh a(BC):",bg="white")
label_left.config(font=("OpenSans", 15))
label_left.pack()
entry1 = tkinter.Entry(frameLeft, textvariable=side1)
entry1.pack()
label_center = tkinter.Label(frameLeft, text="Nhập cạnh b(AC):",bg="white")
label_center.config(font=("OpenSans", 15))
label_center.pack()
entry2 = tkinter.Entry(frameLeft, textvariable=side2)
entry2.pack()      
label_3 = tkinter.Label(frameLeft, text="Nhập cạnh c(AB):",bg="white")
label_3.config(font=("OpenSans", 15))
label_3.pack()
entry3 = tkinter.Entry(frameLeft, textvariable=side3)
entry3.pack()  
######################################## First Output (haven't click button yet)###########################################

label_area = tkinter.Label(frameRight, text="Diện tích: ?",bg="white",width = 20)
label_area.config(font=("OpenSans", 15))
label_area.pack()
##################################################################
label_cv = tkinter.Label(frameRight, text="Chu vi: ?",bg="white",width = 20)
label_cv.config(font=("OpenSans", 15))
label_cv.pack()
############################################
tritype = tkinter.Label(frameRight, text="Đây là tam giác: ?",bg="white",width = 20)
tritype.config(font=("OpenSans", 15))
tritype.pack()
########################################################
heigth_label = tkinter.Label(frameRight, text="Chiều cao của tam giác: ?",bg="white",width = 20)
heigth_label.config(font=("OpenSans", 15))
heigth_label.pack()
##################################################################
angle_label = tkinter.Label(frameRight, text="Các góc của tam giác: ?",bg="white",width = 20)
angle_label.config(font=("OpenSans", 15))
angle_label.pack()
########################################################
label_right = tkinter.Button(frameRight, text="Tìm kết quả", bg="white",fg="blue",command = triangle_result)
label_right.config(font=("OpenSans", 15))
label_right.pack(pady = 30)

root.mainloop()