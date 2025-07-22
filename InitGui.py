#***************************************************************************
#*    Copyright (C) 2023 
#*    This library is free software
#***************************************************************************
import inspect
import os
import sys
import FreeCAD
import FreeCADGui

class flightCvShowCommand:
    def GetResources(self):
        file_path = inspect.getfile(inspect.currentframe())
        module_path=os.path.dirname(file_path)
        return { 
          'Pixmap': os.path.join(module_path, "icons", "flight.svg"),
          'MenuText': "flightCv",
          'ToolTip': "Show/Hide flightCv"}

    def IsActive(self):
        import flightCv
        flightCv
        return True

    def Activated(self):
        try:
          import flightCv
          flightCv.main.d.show()
        except Exception as e:
          FreeCAD.Console.PrintError(str(e) + "\n")

    def IsActive(self):
        import flightCv
        return not FreeCAD.ActiveDocument is None

class flightCvWB(FreeCADGui.Workbench):
    def __init__(self):
        file_path = inspect.getfile(inspect.currentframe())
        module_path=os.path.dirname(file_path)
        self.__class__.Icon = os.path.join(module_path, "icons", "flight.svg")
        self.__class__.MenuText = "flightCv"
        self.__class__.ToolTip = "flightCv by Pascal"

    def Initialize(self):
        self.commandList = ["flightCv_Show"]
        self.appendToolbar("&flightCv", self.commandList)
        self.appendMenu("&flightCv", self.commandList)

    def Activated(self):
        import flightCv
        flightCv
        return

    def Deactivated(self):
        return

    def ContextMenu(self, recipient):
        return

    def GetClassName(self): 
        return "Gui::PythonWorkbench"
FreeCADGui.addWorkbench(flightCvWB())
FreeCADGui.addCommand("flightCv_Show", flightCvShowCommand())

