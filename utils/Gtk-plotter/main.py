#!/usr/bin/env python3

"""
Tauno Erik
30.01.2022 - 04.02.2022

Build GUI Apps with Python and GTK: https://www.youtube.com/watch?v=Ko0NTS0IpfI
https://pygobject.readthedocs.io/en/latest/
https://python-gtk-3-tutorial.readthedocs.io/en/latest/
http://lazka.github.io/pgi-docs/
https://matplotlib.org/3.1.3/tutorials/introductory/customizing.html
# https://stackoverflow.com/questions/31012645/properly-structure-and-highlight-a-gtkpopovermenu-using-pygobject
"""

from urllib import response
import gi
from gi.repository import Gio
import sys
import pandas as pd
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg
import matplotlib.pyplot as plt
# matplotlib dark theme:
from ing_theme_matplotlib import mpl_style  # pip install ing_theme_matplotlib

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyApp:
  def __init__(self):
    self.column_names = False
    self.drop_nan = False
    self.df = None

    self.builder = Gtk.Builder()
    self.builder.add_from_file("window2.glade")
    self.builder.connect_signals(self)

    self.window = self.builder.get_object("JuunWindow") #GtkApplicationWindow name
    self.window.show_all()

    ## Menu
    # https://github.com/alexhuntley/Plots/blob/main/plots/plots.py
    menu_button = self.builder.get_object("menu_btn")
    self.menu = Gio.Menu()
    self.menu.append("Help", "app.help")
    self.menu.append("About Plots", "app.about")
    menu_button.set_menu_model(self.menu)

    #print(self.get_style_context().get_color())
    #print(self.get_style_context().get_border_color())
    #print(self.get_style_context().get_background_color())

    #####
    """
    # Create an empty style context
    style_ctx = Gtk.StyleContext()
    # Create an empty widget path
    widget_path =  Gtk.WidgetPath()
    # Specify the widget class type you want to get colors from
    widget_path.append_type(Gtk.Button)
    style_ctx.set_path(widget_path)
    # Print style context colors of widget class Gtk.Button
    print('Gtk.Button: Normal:')
    print('foreground color: ', style_ctx.get_color(Gtk.StateFlags.NORMAL) )
    print('color:            ', style_ctx.get_property('color', Gtk.StateFlags.NORMAL) )
    print('background color: ', style_ctx.get_property('background-color', Gtk.StateFlags.NORMAL) )
    print('outline color:    ', style_ctx.get_property('outline-color', Gtk.StateFlags.NORMAL) )
    print('Gtk.Button: Link:')
    print('foreground color: ', style_ctx.get_color(Gtk.StateFlags.LINK) )
    print('color:            ', style_ctx.get_property('color', Gtk.StateFlags.LINK) )
    print('background color: ', style_ctx.get_property('background-color', Gtk.StateFlags.LINK) )
    print('outline color:    ', style_ctx.get_property('outline-color', Gtk.StateFlags.LINK) )
    ####
    """


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
    response = dialog.run()
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

    mpl_style(dark=True)
    canvas_window = self.builder.get_object("plot1")

    if canvas_window.get_child():
      canvas_window.show_all()
      return
    fig = plt.figure()
    df = self.df
    x = list(df.columns)[1]
    y = list(df.columns)[1]
    fig.add_subplot().scatter(df[x], df[y])
    plt.xlabel(x)
    plt.ylabel(y)

    # draw plot
    canvas = FigureCanvasGTK3Agg(fig)
    canvas.set_size_request(800, 600)
    canvas_window.add(canvas)
    canvas_window.show_all()


  def on_plot_close(self, widget, event):
    print("on_plot_close")
    return self.builder.get_object("plot1").hide_on_delete()


  def on_destroy(self, event):
    Gtk.main_quit()


if __name__ == "__main__":
  MyApp()
  Gtk.main()
