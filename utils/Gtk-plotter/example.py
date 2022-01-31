#!/usr/bin/env python3
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyApp:
  def __init__(self):
      self.column_names = False
      self.drop_nan = False
      self.df = None

      self.builder = Gtk.Builder()
      self.builder.add_from_file("example.glade")
      self.builder.connect_signals(self)

      self.window = self.builder.get_object("MainWindow")
      self.window.show_all()


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

  def on_destroy(self, event):
    Gtk.main_quit()

if __name__ == "__main__":
  MyApp()
  Gtk.main()
