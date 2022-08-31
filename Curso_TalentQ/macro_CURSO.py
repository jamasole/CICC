import numpy as np
from IPython.display import display,Markdown,Latex
import matplotlib.pyplot as plt


##############################################################################################################
# Definimos funciones auxiliares para printear

def MatrixToLatex(A):
    a="\\begin{bmatrix}"
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if ((j+1)%A.shape[1])==0:           
                a=a+"{0:.2f}".format(A[i,j])
            else:
                a=a+"%s&"%"{0:.2f}".format(A[i,j])
        if ((i+1)%A.shape[0])!=0:
            a=a+"\\\\"
    a=a+"\\end{bmatrix}"

    return(a)

def Display(string):
    display(Markdown(string))

    
def DisplayMatrix(A):
    A_Latex = MatrixToLatex(A)
    display(Markdown(A_Latex))
   
    
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
  

'''Para dibujar vectores '''

def plot_2D_plane(right=1,up=1,left=-1,down=-1,fsize=(8,8)):
    hpoints, vpoints = [],[]
    for i in range(left,right+1):
        if i!=0: hpoints.append(i)
    for i in range(down,up+1):
        if i!=0: vpoints.append(i)
    
    ax = plt.figure(figsize=fsize).gca()

    # Establece escalas iguales para ambos ejes
    ax.set(xlim=(left-0.5,right+0.5), ylim=(down-0.5, up+0.5), aspect='equal')
    # Elimina los bordes superior e inferior
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # Establece los bordes inferior e izquierdo como ejes de coordenadas
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    # Crea ticks en cada entero para habilitar dibujo de un retículo menor
    # Create minor ticks placed at each integer to enable drawing of minor grid
    ax.set_xticks(hpoints)
    ax.set_yticks(vpoints)
    # Dibuja retículo
    ax.grid(which='both', color='green', linewidth=1, linestyle='-', alpha=0.2)
    # Crea etiquetas 'x' e 'y' al final de cada eje
    ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)
    # Dibuja flechas
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (0), marker='<', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
    ax.plot((0), (0), marker='v', transform=ax.get_xaxis_transform(), **arrow_fmt)


def draw_sides(x=1,y=2,side_color="b",lwidth=1):
    plt.arrow(x,0,0,y,color=side_color,linestyle="dotted",width=0.001*lwidth)
    plt.arrow(0,y,x,0,color=side_color,linestyle="dotted",width=0.001*lwidth)
        
def draw_vector(x=1,y=0,vname="v",show_name=False,vcolor="b",sides=False,side_color="b",lwidth=1):
    plt.quiver(0,0,x,y,scale=1,scale_units='xy',angles = 'xy',color=vcolor,width=0.008*lwidth)
    dx = x
    if y<0: dy=y-0.3
    else: dy = y+0.3
        
    if show_name:
        vector_name="$"+vname+"=("+str(x)+","+str(y)+")$"
        plt.text(dx,dy,vector_name,color=vcolor)
    
    if sides:
        draw_sides(x,y,side_color)

def place_text(x,y,text,tcolor="blue"):
    plt.text(x,y,text,color=tcolor)
    

def show_plt():
    plt.show()
    



# drawing used for quantum
def draw_axes():
	points = [ [1.2,0], [0,1.2], [-1.2,0], [0,-1.2] ] # dummy points for zooming out
	arrows = [ [1.1,0], [0,1.1], [-1.1,0], [0,-1.1] ] # coordinates for the axes
	for p in points: 
		plt.plot(p[0],p[1]+0.1) # drawing dummy points
	for a in arrows: 
		plt.arrow(0,0,a[0],a[1],head_width=0.04, head_length=0.08) # drawing the axes


def draw_unit_circle():
    unit_circle= plt.Circle((0,0),1,color='black',fill=False)
    plt.gca().add_patch(unit_circle)
	

def Expande_Ket(u):
    a=r'$| u \rangle $  ='
    for i in range(len(u)):
        if (i+1)%len(u)!=0:
            a+=r' %s |$e_%i \rangle  $ + ' %(u[i][0],i)  
        elif (i+1)%len(u)==0:
            a+= r" %s |$e_%i\rangle $ " %(u[i][0],i)
    display(Markdown(a))


