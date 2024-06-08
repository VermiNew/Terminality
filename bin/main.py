import os
import subprocess
import sys
import platform

def get_git_branch():
    try:
        output = subprocess.check_output(['git', 'branch', '--show-current'], stderr=subprocess.DEVNULL).decode('utf-8').strip()
        return output if output else None
    except subprocess.CalledProcessError:
        return None

def get_prompt():
    user = os.getenv('USERNAME', 'user')
    hostname = platform.node()
    cwd = os.getcwd()
    git_branch = get_git_branch()
    
    # Check if we are in a virtual environment
    venv_indicator = ''
    if 'VIRTUAL_ENV' in os.environ:
        venv_indicator = f"({os.path.basename(os.environ['VIRTUAL_ENV'])}) "

    # Building the prompt
    prompt = f"\033[1;36m{user}@{hostname}\033[1;30m:\033[0m \033[1;30m{venv_indicator}\033[1;34m{cwd}\033[0m"
    if git_branch:
        prompt += f" (\033[1;32m{git_branch}\033[0m)"
    prompt += " \033[1;30m#\033[0m "
        
    return prompt

if __name__ == "__main__":
    sys.stdout.write(get_prompt())
