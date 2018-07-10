from tkinter import *
	
b = "black"
f = "yellow"

w = 10
h = 5

class Game:
	def __init__(self):
		self.count = 0
		self.jan = Tk()
		self.jan["bg"] = "black"
		self.jan.geometry("240x250")
		self.jan.title("Jogo da velha")
		self.jan.resizable(False, False)

		self.bta1 = Button(self.jan,width=w, height=h, text="",bg=b ,fg=f ,command=self.a1)
		self.bta2 = Button(self.jan,width=w, height=h, text="",bg=b ,fg=f ,command=self.a2)
		self.bta3 = Button(self.jan,width=w, height=h, text="",bg=b ,fg=f ,command=self.a3)

		self.btb1 = Button(self.jan,width=w, height=h, text="",bg=b ,fg=f , command=self.b1)
		self.btb2 = Button(self.jan,width=w, height=h, text="",bg=b ,fg=f , command=self.b2)
		self.btb3 = Button(self.jan,width=w, height=h, text="",bg=b ,fg=f , command=self.b3)

		self.btc1 = Button(self.jan,width=w, height=h, text="",bg=b ,fg=f , command=self.c1)
		self.btc2 = Button(self.jan,width=w, height=h, text="",bg=b ,fg=f , command=self.c2)
		self.btc3 = Button(self.jan,width=w, height=h, text="",bg=b ,fg=f , command=self.c3)


	def tela(self,r):
		if r == 1:
			v = Tk()
			v["bg"] == "black"
			v.geometry("100x40")
			lb = Label(v, text="O VENCEU!!", fg=b).place(x=10,y=10)
			self.jan.destroy()
		else:
			v = Tk()
			v["bg"] == "black"
			v.geometry("100x40")
			lb = Label(v, text="X VENCEU!!", fg=b).place(x=10,y=10)
			self.jan.destroy()

	def buttons(self):
		self.bta1.grid(column=0, row=0)
		self.bta2.grid(column=1, row=0)
		self.bta3.grid(column=2, row=0)

		self.btb1.grid(column=0, row=1)
		self.btb2.grid(column=1, row=1)
		self.btb3.grid(column=2, row=1)

		self.btc1.grid(column=0, row=2)
		self.btc2.grid(column=1, row=2)
		self.btc3.grid(column=2, row=2)

	def vit(self):
		if self.bta1["text"] == "O" and self.bta2["text"] == "O" and self.bta3["text"] == "O" or self.btb1["text"] == "O" and self.btb2["text"] == "O" and self.btb3["text"] == "O" or self.btc1["text"] == "O" and self.btc2["text"] == "O" and self.btc3["text"] == "O" or self.bta1["text"] == "O" and self.btb1["text"] == "O" and self.btc1["text"] == "O" or self.bta2["text"] == "O" and self.btb2["text"] == "O" and self.btc2["text"] == "O" or self.bta3["text"] == "O" and self.btb3["text"] == "O" and self.btc3["text"] == "O" or self.bta1["text"] == "O" and self.btb2["text"] == "O" and self.btc3["text"] == "O" or self.bta3["text"] == "O" and self.btb2["text"] == "O" and self.btc1["text"] == "O":
			self.tela(1)

		elif self.bta1["text"] == "X" and self.bta2["text"] == "X" and self.bta3["text"] == "X" or self.btb1["text"] == "X" and self.btb2["text"] == "X" and self.btb3["text"] == "X" or self.btc1["text"] == "X" and self.btc2["text"] == "X" and self.btc3["text"] == "X" or self.bta1["text"] == "X" and self.btb1["text"] == "X" and self.btc1["text"] == "X" or self.bta2["text"] == "X" and self.btb2["text"] == "X" and self.btc2["text"] == "X" or self.bta3["text"] == "X" and self.btb3["text"] == "X" and self.btc3["text"] == "X" or self.bta1["text"] == "X" and self.btb2["text"] == "X" and self.btc3["text"] == "X" or self.bta3["text"] == "X" and self.btb2["text"] == "X" and self.btc1["text"] == "X":
			self.tela(2)



	def a1(self):
		if self.bta1["text"] == "":
			if self.count % 2 == 0:
				self.bta1["text"] = "X"
			else:
				self.bta1["text"] = "O"
			self.count+=1
			self.vit()
		else:
			print("A1 Já tem")

	def a2(self):
		if self.bta2["text"] == "":
			if self.count % 2 == 0:
				self.bta2["text"] = "X"
			else:
				self.bta2["text"] = "O"
			self.count+=1
			self.vit()
		else:
			print("A2 Já tem")

	def a3(self):
		if self.bta3["text"] == "":
			if self.count % 2 == 0:
				self.bta3["text"] = "X"
			else:
				self.bta3["text"] = "O"
			self.count+=1
			self.vit()
		else:
			print("A3 Já tem")

	def b1(self):
		if self.btb1["text"] == "":
			if self.count % 2 == 0:
				self.btb1["text"] = "X"
			else:
				self.btb1["text"] = "O"
			self.count+=1
			self.vit()
		else:
			print("B1 Já tem")

	def b2(self):
		if self.btb2["text"] == "":
			if self.count % 2 == 0:
				self.btb2["text"] = "X"
			else:
				self.btb2["text"] = "O"
			self.count+=1
			self.vit()
		else:
			print("B2 Já tem")

	def b3(self):
		if self.btb3["text"] == "":
			if self.count % 2 == 0:
				self.btb3["text"] = "X"
			else:
				self.btb3["text"] = "O"
			self.count+=1
			self.vit()
		else:
			print("B3 Já tem")

	def c1(self):
		if self.btc1["text"] == "":
			if self.count % 2 == 0:
				self.btc1["text"] = "X"
			else:
				self.btc1["text"] = "O"
			self.count+=1
			self.vit()
		else:
			print("C1 Já tem")

	def c2(self):
		if self.btc2["text"] == "":
			if self.count % 2 == 0:
				self.btc2["text"] = "X"
			else:
				self.btc2["text"] = "O"
			self.count+=1
			self.vit()
		else:
			print('C2 Já tem')

	def c3(self):
		if self.btc3["text"] == "":
			if self.count % 2 == 0:
				self.btc3["text"] = "X"
			else:
				self.btc3["text"] = "O"
			self.count+=1
			self.vit()
		else:
			print("C3 Já tem")





	def run(self):
		self.buttons()
		self.jan.mainloop()

g = Game()
g.run()












