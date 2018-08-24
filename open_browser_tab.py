"""
Opens a new browser tab

NOTE: Only browsers, which are part of the PATH variable can be found
"""
import webbrowser


controller = webbrowser.get("firefox")
controller.open_new_tab("https://stackoverflow.com")
