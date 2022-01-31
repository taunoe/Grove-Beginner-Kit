#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
import serial, serial.tools.list_ports
import sys

class MainWindow:

  def __init__(self, main):
    myFrame = Frame(main)
    #myFrame.pack()

    self.myButton = Button(main, text="Connnect!", command=self.cmd_connect)
    self.myButton.grid(column=0, row=1)

    ttk.Label(main, text="Select port:").grid(column=0, row=2, padx = 10, pady = 20)

    self.serial_ports = []
    self.find_serial_ports()
    self.selected_port = StringVar()
    self.selected_port = self.serial_ports[0] # initial value
    self.drop_select_port = ttk.Combobox(main, width=27, textvariable=self.selected_port)
    self.drop_select_port.grid(column=3, row=2)

    # Adding combobox drop down list
    self.monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')

  def cmd_connect(self):
    print("Connect!")

  def cmd_select_port(self):
    self.selected_port = self.drop_select_port.get()
    print("Selected port {}".format(self.selected_port))

  def find_serial_ports(self):
    print("find_serial_ports")
    try:
      ports = list(serial.tools.list_ports.comports())
      # Add to gui list
      for port in ports:
        self.serial_ports.append(port[0])
    except:
      print("Error")


def main():
  root = Tk()
  root.title("Window title")
  root.geometry("600x400")
  #root.iconbitmap('')
  w = MainWindow(root)
  root.mainloop()

if __name__ == '__main__':
  main()

# 冷血屠城烈士英魂不朽
# 誓殲豺狼民主星火不滅