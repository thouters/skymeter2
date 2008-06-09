#!/usr/bin/env python
#       PySkymeter 2.1.0, 2008/03/25
#	Skymeter, raadpleegt de Volumepagina van skynet selfcare,
#	verwerkt deze en bekomt de nuttige informatie.
#	
#	Copyright (C) 2005 Thomas Langewouters. 
#	
#	This program is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; either version 2 of the License, or
#	(at your option) any later version.
#	
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#	You should have received a copy of the GNU General Public License
#	along with this program; if not, write to the Free Software
#	Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#   FIXME: use true MVC
import Tkinter
import tkSimpleDialog
import tkMessageBox
import tkSimpleDialog
from skymeter import *
import time

class SimpleBar:
    width = 400
    height = 25

    def __init__(self, parentwidget):
        self.widget = Tkinter.Canvas(parentwidget, width=self.width, height="25")
        self.SetState(False)

    def SetState(self, state):
        self.widget.create_rectangle(0,0,self.width, self.height, fill="black")
        if state:
            self.widget.create_rectangle(1,1,self.width-2, self.height-2, fill="yellow")
        else:
            self.widget.create_rectangle(1,1,self.width-2, self.height-2, fill="grey")

    def SetValue(self, decimal):
        self.SetState(True)
        self.widget.create_rectangle(1,1,(self.width - 2)* decimal, self.height - 2, fill="blue")
    def destroy(self):
        return self.widget.destroy()


class ConfDialog(tkSimpleDialog.Dialog):
    def body(self, master):
        Tkinter.Label(master, text="Username:").grid(row=0)
        Tkinter.Label(master, text="Password:").grid(row=1)
        self.e1 = Tkinter.Entry(master)
        self.e2 = Tkinter.Entry(master)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.changed = False
        return self.e1 # initial focus

    def apply(self):
        self.username = self.e1.get()
        self.password = self.e2.get()
        self.changed = True

class TkMeter:
    widgets = []
    def __init__(self,skymeter,meter):
        if (    (skymeter.__class__ != TkSkymeter) 
            or  (not isinstance(meter,Meter))  ):
            raise Exception("Invalid argument(s)")

        row = len(skymeter.widgets)

        lblname = Tkinter.Label(skymeter.root, text=meter.__class__.__name__)
        lblname.grid(row=row)
        self.widgets.append(lblname)

        bar = SimpleBar(skymeter.root)
        bar.SetValue(meter.value/meter.total)
        bar.widget.grid(row=row, column=1)
        self.widgets.append(bar)

        strVal= Tkinter.StringVar()
        strVal.set(" of ".join(map(meter.num2string,[meter.value,meter.total])))
        lblVal = Tkinter.Label(skymeter.root, textvariable=strVal)
        lblVal.grid(row=row, column=2)
        self.widgets.append(lblVal)

    def __del__(self):
        for w in self.widgets:
            w.destroy()

class TkMeterMsg:
    widget = None
    def __init__(self,skymeter,msg):
        self.widget = Tkinter.Label(skymeter.root, text=msg)
        self.widget.grid(column=1,row=len(skymeter.widgets),sticky=Tkinter.N+Tkinter.S)
    def __del__(self):
        self.widget.destroy()

class TkSkymeter(skymeter):
    widgets = []
    def mnu_PollMeter(self):
        self.widgets = []

        try:
            result = self.GetData()
            msg = "Volume meters for %s on %s\n" % (
                    self.username, 
                    time.strftime(self.timeformat, self.time))
            self.widgets = [TkMeterMsg(self,msg)]

            for meter in result:
                self.widgets.append(TkMeter(self,meter))                
        except SkymeterError, result:
            msg = "Fout bij het raadplegen van skymeter: %s" % result.error
            self.widgets = [TkMeterMsg(self,msg)]

    def mnu_Settings(self):
        Cdia = ConfDialog(self.root)
        if Cdia.changed:
            self.username = Cdia.username
            self.password = Cdia.password
            try:
                self.savecred()
            except SkymeterError, result:
                tkMessageBox.showwarning("Fout",result.error)

    def mnu_About(self):
        msg =   "Skymeter versie %s \n" \
                "Geschreven door Thomas Langewouters\nGebruik op eigen risico" \
                % self._version
        tkMessageBox.showinfo("Over...",msg)

    def main(self):
        self.root = Tkinter.Tk()		
        self.root.title("Skynet Volume Meters")
        self.menubar = Tkinter.Menu(self.root)
        self.menubar.add_command(label="Verversen", command=self.mnu_PollMeter)
        self.menubar.add_command(label="Instellingen", command=self.mnu_Settings)
        self.menubar.add_command(label="Over", command=self.mnu_About)
        self.root.columnconfigure(1,minsize=400)
        self.root.rowconfigure(1,minsize=25)
        self.root.config(menu=self.menubar)
        self.widgets = [TkMeterMsg(self,"No Data")]
        self.root.mainloop()

if __name__ == "__main__":
    main = TkSkymeter()
    main.main()
