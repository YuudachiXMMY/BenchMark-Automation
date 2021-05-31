# Name	FINAL FANTASY XIV: Stormblood Benchmark


import uiautomation as auto


cm = auto.WindowControl(searchDepth=1,Name='ComputeMark')
cm.SetTopmost(True)

# Choose Resolution: 1920x1080
cm.ComboBoxControl(foundIndex=1, Name='').Click()
cm.ListControl(foundIndex=1, Name='').Click()

cm.SetTopmost(True)
# Choose Preset: Extreme
cm.ComboBoxControl(foundIndex=2, Name='').Click()
cm.ListControl(foundIndex=1, Name='').Click()

# Choose Fullscreen
cm.CheckBoxControl(Name='Fullscreen').Click()

# Run
cm.ButtonControl(Name='Run benchmark').Click()