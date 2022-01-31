#!/usr/bin/env python3

"""
30.01.2022

Build GUI Apps with Python and GTK: https://www.youtube.com/watch?v=Ko0NTS0IpfI
https://pygobject.readthedocs.io/en/latest/
https://python-gtk-3-tutorial.readthedocs.io/en/latest/
http://lazka.github.io/pgi-docs/
"""

from urllib import response
import gi
import sys
import pandas as pd
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg
import matplotlib.pyplot as plt


gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyApp:
  def __init__(self):
      self.column_names = False
      self.drop_nan = False
      self.df = None

      self.builder = Gtk.Builder()
      self.builder.add_from_file("uus.glade")  # Glade file
      self.builder.connect_signals(self)

      self.window = self.builder.get_object("JuunWindow") #GtkApplicationWindow name
      self.window.show_all()


  def load_table(self, filename):
    if filename is not None:
      fn = filename.split("/")[-1] # last one
      if self.column_names:
        df = pd.read_csv(filename, engine="python")
      else:
        df = pd.read_csv(filename, engine="python", header=None)
        header_list = ["column" + str(x) for x in range(len(df.iloc[0]))]
        df.columns = header_list
      if self.drop_nan:
        df = df.dropna()

      self.df = df # dataframe

  def menu_btn_pressed(self, widget):
    print("menu_btn_pressed")


  def on_open_dialog(self, widget):
    dialog = self.builder.get_object("open_file_dialog")
    response = dialog.run
    if response == Gtk.ResponseType.OK:
      print("ok btn")
      filename = dialog.get_filename()
      self.load_table(filename)
    elif response == Gtk.ResponseType.CANCEL:
      print("cancel btn")
      dialog.close()
    dialog.close()
    print("on_open_dialog")

  def on_close_dialog(self, widget, event):
    print("on_close_dialog")
    return self.builder.get_object("open_file_dialog").hide_on_delete()

  def on_column_switch(self, switch, gparam):
    print("on_column_switch")
    self.column_names = bool(switch.get_active())

  def on_nan_switch(self, switch, gparam):
    print("on_nan_switch")
    self.drop_nan = bool(switch.get_active())

  def on_plot(self, button):
    print("on_plot")
    if self.df is None:
      return
    canvas_window = self.builder.get_object("plot1")
    if canvas_window.get_child():
      canvas_window.show_all()
      return
    fig = plt.figure()
    df = self.df
    x = list(df.columns)[3]
    y = list(df.columns)[5]
    fig.add_subplot().scatter(df[x], df[y])
    plt.xlabel(x)
    plt.ylabel(y)

    # draw plot
    canvas = FigureCanvasGTK3Agg(fig)
    canvas.set_size_request(800, 600)
    canvas_window.add(canvas)
    canvas_window.show_all()


  def on_plot_close(self, widget, event):
    return self.builder.get_object("plot1").hide_on_delete()

  def on_destroy(self, event):
    Gtk.main_quit()

if __name__ == "__main__":
  MyApp()
  Gtk.main()
