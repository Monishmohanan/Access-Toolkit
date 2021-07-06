#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from cx_Freeze import setup, Executable
import sys,os

build_exe_options = {
      "packages": ["os"], 
      "includes":["tkinter", "tkinter.ttk"],  
      "include_files":["AccessToolkit-docs.pdf"]}
base=None

if sys.platform == "win32":
	base = "Win32GUI"

setup(name="Access Toolkit",
      version="1.1",
      description="Toolkit for mapping files and folders",
	  options = {"build_exe": build_exe_options},
      executables=[Executable("Access Toolkit.py", base=base, icon = "tool.ico")]
      )
