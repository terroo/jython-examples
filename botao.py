from javax.swing import JButton, JFrame
import random

frame = JFrame('Gerar numeros aleatorios',
            defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
            size = (300, 150)
        )

def change_text(event):
    for i in range( 10 ):
        print( random.randint(0,9) )
    print("----------------------------")
button = JButton('Gerar', actionPerformed=change_text)
frame.add(button)
frame.visible = True
