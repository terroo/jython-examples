import javax.swing as libswing 

pnumero = libswing.JOptionPane.showInputDialog("Digite um Numero Inteiro: ") 
snumero = libswing.JOptionPane.showInputDialog("Digite OUTRO Numero Inteiro: ") 

soma = int(pnumero) + int(snumero) 

libswing.JOptionPane.showMessageDialog(None, "A soma eh %d " % soma)
