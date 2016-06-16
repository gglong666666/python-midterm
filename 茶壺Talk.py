from  OpenGL.GL import  *
from  OpenGL.GLU import  *
from  OpenGL.GLUT import  *

def  drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)  #這個很厲害
		#把先前的畫面清除，每次重繪之前都要把原來的畫面擦掉，不然疊加起來什麼都看不出了
    
	#glRotatef(1, 0, 1, 0)
			  (0, 0, 0, 0)
		#四個參數第一個是角度，後三個是向量，就是繞著這個向量旋轉，這裡是繞著Y軸旋轉1°
	
    glutWireTeapot( 0.5 )
		#glut提供的繪製"猶他茶壺"的工具函數，那個0.5是大小
		
    glFlush()
		#刷新顯示
	
glutInit()
#是用glut來初始化OpenGL的

glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
#這裡告訴系統我們需要一個怎樣顯示的模式
#參數GLUT_RGBA就是使用(red, green, blue)的顏色系統

glutInitWindowSize( 400 , 400 )
#設置出現視窗的大小

glutCreateWindow( "First" )
#打這個指令，就出現一個窗口了，First就是窗口的標題

glutDisplayFunc(drawFunc)
#它是一個函數，用來繪製OpenGL窗口，這個函數裡有很多OpenGL的繪圖操作等命令

glutMainLoop()
#主循環，一旦使用了，我們的OpenGL就一直運行下去了
#和很多程序中的主循環一樣，不停的運行，畫出即時的圖像，處理輸入等
