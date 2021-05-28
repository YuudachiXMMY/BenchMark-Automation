# Name	FINAL FANTASY XIV: Stormblood Benchmark


import uiautomation as auto


fallout4 = auto.PaneControl(searchDepth=1,Name='FINAL FANTASY XIV: Stormblood Benchmark')
fallout4.SetTopmost(True)
fallout4.ButtonControl(foundIndex=16, Name='').Click()
