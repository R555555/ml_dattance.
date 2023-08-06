import win32api

# Get the current working directory
cwd = win32api.GetCurrentDirectory()
print(cwd)