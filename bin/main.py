import os
import subprocess
import sys
import platform
from datetime import datetime

class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

class ShellPrompt:
    def __init__(self):
        self.show_time = True
        self.show_git = True
        self.show_virtualenv = True

    def get_git_info(self):
        """
        Retrieve git branch and status information.
        
        Returns:
            str: Git branch name with '+' if there are uncommitted changes, or None if not in a git repository.
        """
        try:
            branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stderr=subprocess.DEVNULL).decode('utf-8').strip()
            status = subprocess.check_output(['git', 'status', '--porcelain'], stderr=subprocess.DEVNULL).decode('utf-8').strip()
            return f"{branch} +" if status else branch
        except subprocess.CalledProcessError:
            return None

    def get_time(self):
        """
        Get current time in HH:MM:SS format.
        
        Returns:
            str: Current time.
        """
        return datetime.now().strftime("%H:%M:%S")

    def get_virtualenv(self):
        """
        Get the name of the current virtual environment.
        
        Returns:
            str: Name of the virtual environment, or None if not in a virtual environment.
        """
        if 'VIRTUAL_ENV' in os.environ:
            return os.path.basename(os.environ['VIRTUAL_ENV'])
        return None

    def shorten_path(self, path, max_length=40):
        """
        Shorten the given path if it exceeds the maximum length.
        
        Args:
            path (str): The path to shorten.
            max_length (int): Maximum length of the path.
        
        Returns:
            str: Shortened path.
        """
        if len(path) <= max_length:
            return path
        
        parts = path.split(os.sep)
        if len(parts) > 3:
            return os.sep.join([parts[0], '...'] + parts[-2:])
        else:
            return '...' + path[-(max_length-3):]

    def get_prompt(self):
        """
        Generate the shell prompt string.
        
        Returns:
            str: Formatted shell prompt.
        """
        segments = []
        user = os.getenv('USER', os.getenv('USERNAME', 'user'))
        hostname = platform.node()
        segments.append(f"{Colors.BRIGHT_GREEN}{user}@{hostname}{Colors.RESET}")
        
        cwd = self.shorten_path(os.getcwd())
        segments.append(f"{Colors.BRIGHT_BLUE}{cwd}{Colors.RESET}")
        
        if self.show_git:
            git_info = self.get_git_info()
            if git_info:
                segments.append(f"{Colors.YELLOW}{git_info}{Colors.RESET}")
        
        if self.show_virtualenv:
            venv = self.get_virtualenv()
            if venv:
                segments.append(f"{Colors.BRIGHT_MAGENTA}{venv}{Colors.RESET}")
        
        if self.show_time:
            current_time = self.get_time()
            segments.append(f"{Colors.BRIGHT_BLACK}{current_time}{Colors.RESET}")
        
        prompt = f"{Colors.BOLD}{Colors.BRIGHT_WHITE}╭─{Colors.RESET} " + f" {Colors.BRIGHT_WHITE}│{Colors.RESET} ".join(segments)
        prompt += f"\n{Colors.BOLD}{Colors.BRIGHT_WHITE}╰─❯{Colors.RESET} "
        return prompt

if __name__ == "__main__":
    prompt = ShellPrompt()
    sys.stdout.write(prompt.get_prompt())
