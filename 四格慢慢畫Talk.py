from  OpenGL.GL import  *
from  OpenGL.GLU import  *
from  OpenGL.GLUT import  *

def  init():	

    glClearColor( 0.5 , 0.5 , 0.5 , 1.0 )	
	#背景顏色(紅、綠、藍、透明)
	
    gluOrtho2D( - 1.0 , 1.0 , - 1.0 , 1.0 )	#定義一個二維圖像	zzzzzzzz

def  drawFunc():

    glClear(GL_COLOR_BUFFER_BIT)	#把先前的畫面清除，每次重繪之前都要把原來的畫面擦掉，不然疊加起來什麼都看不出了
	
	#分割線
    glBegin(GL_LINES)
    glVertex2f( - 1.0 , 0.0 )	#位置
    glVertex2f( 1.0 , 0.0 )
    glVertex2f( 0.0 , 1.0 )
    glVertex2f( 0.0 , - 1.0 )
    glEnd()
	#分割線
	
	
	#右上區
    glPointSize( 5.0 )		#宣告每個點的大小為5個像素
    glBegin(GL_POINTS)
	#glColor3f(R, G, B)指定了繪製的顏色，這裡的RGB都是0~1之間的浮點數
    glColor3f( 1.0 , 0.0 , 0.0 )	#顏色
    glVertex2f( 0.3 , 0.3 )			#位置
    glColor3f( 0.0 , 1.0 , 0.0 )
    glVertex2f( 0.6 , 0.6 )
    glColor3f( 0.0 , 0.0 , 1.0 )
    glVertex2f( 0.9 , 0.9 )
    glEnd()
	#右上區
	
	
	#左上
    glColor3f( 1.0 , 1.0 , 0 )	#紅+綠
    glBegin(GL_QUADS)	#四邊形
    glVertex2f( - 0.2 , 0.2 )
    glVertex2f( - 0.2 , 0.5 )
    glVertex2f( - 0.5 , 0.5 )
    glVertex2f( - 0.5 , 0.2 )
    glEnd()
	#左上
	
	
	#左下(先畫線再填充)
    glColor3f( 0.0 , 1.0 , 1.0 )
    glPolygonMode(GL_FRONT, GL_LINE)
    glPolygonMode(GL_BACK, GL_FILL)
    glBegin(GL_POLYGON)	#多邊形
    glVertex2f( - 0.5 , - 0.1 )
    glVertex2f( - 0.8 , - 0.3 )
    glVertex2f( - 0.8 , - 0.6 )
    glVertex2f( - 0.5 , - 0.8 )
    glVertex2f( - 0.2 , - 0.6 )
    glVertex2f( - 0.2 , - 0.3 )
    glEnd()
	#左下
	
	
	#右下(先填充再畫線)
    glPolygonMode(GL_FRONT, GL_FILL)
    glPolygonMode(GL_BACK, GL_LINE)
    glBegin(GL_POLYGON)
    glVertex2f( 0.5 , - 0.1 )
    glVertex2f( 0.2 , - 0.3 )
    glVertex2f( 0.2 , - 0.6 )
    glVertex2f( 0.5 , - 0.8 )
    glVertex2f( 0.8 , - 0.6 )
    glVertex2f( 0.8 , - 0.3 )
    glEnd()
	#右下
	
	#GL_LINE是只畫線
	#GL_FILL是默認的填充

    glFlush()


glutInit()
#是用glut來初始化OpenGL的

glutInitDisplayMode(GLUT_RGBA|GLUT_SINGLE)
#這裡告訴系統我們需要一個怎樣顯示的模式
#參數GLUT_RGBA就是使用(red, green, blue)的顏色系統

glutInitWindowSize( 400 , 400 )
#設置出現視窗的大小

glutCreateWindow( "I am a good boy" )
#打這個指令，就出現一個窗口了，參數就是窗口的標題

glutDisplayFunc(drawFunc)
#它是一個函數，用來繪製OpenGL窗口

glutMainLoop()
#主循環，一旦調用了，我們的OpenGL就一直運行下去了
#和很多程序中的主循環一樣，不停的運行，畫出即時的圖像，處理輸入等