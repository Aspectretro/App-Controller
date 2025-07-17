import winreg

def get_default_browser_windows():
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                           r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice") as key:
            browser = winreg.QueryValueEx(key, 'ProgId')[0]
            return browser
    except Exception as e:
        print(f"Error accessing registry: {e}")
        return None

# Example usage
browser = get_default_browser_windows()
print(f"Default browser (Windows): {browser}")