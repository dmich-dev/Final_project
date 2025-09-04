# Running NASA APOD Viewer on WSL (Windows Subsystem for Linux)

This guide provides detailed instructions for setting up and running the NASA APOD Viewer application on Windows Subsystem for Linux (WSL).

## Prerequisites

1. WSL installed on your Windows system (preferably WSL2)
2. An X server for Windows (to display GUI applications)
3. Basic familiarity with Linux commands

## Setting Up the X Server

To run graphical applications on WSL, you need an X server running on Windows:

1. **Install an X server for Windows**. Here are some popular options:
   - [VcXsrv](https://sourceforge.net/projects/vcxsrv/) (recommended)
   - [Xming](https://sourceforge.net/projects/xming/)
   - [X410](https://x410.dev/) (paid option)

2. **Configure the X server**:

   For VcXsrv:
   - Launch XLaunch
   - Select "Multiple windows" and set "Display number" to 0
   - Select "Start no client"
   - Check "Disable access control"
   - Save the configuration for future use

3. **Configure Windows Firewall**:
   - Open Windows Defender Firewall
   - Go to "Allow an app or feature through Windows Defender Firewall"
   - Find VcXsrv or your X server in the list
   - Make sure it's checked for both "Private" and "Public" networks

## Running the Application

1. **Start your X server** (VcXsrv, Xming, etc.) on Windows

2. **Open WSL terminal** and navigate to your project directory:
   ```bash
   cd /path/to/Final-project
   ```

3. **Run the WSL script**:
   ```bash
   ./wsl_run_app.sh
   ```

   This script will:
   - Configure the DISPLAY environment variable
   - Verify that Python and Tkinter are installed
   - Set up a virtual environment if needed
   - Install required packages
   - Run the application

## Troubleshooting

If you encounter issues:

1. **No display or "Can't open display" error**:
   - Verify your X server is running on Windows
   - Check that DISPLAY is set correctly:
     ```bash
     echo $DISPLAY
     ```
   - If not set correctly, manually set it:
     ```bash
     export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0
     ```
   - Make sure your Windows firewall allows the X server

2. **Missing Tkinter**:
   - Install it with:
     ```bash
     sudo apt update && sudo apt install -y python3-tk
     ```

3. **Other GUI issues**:
   - Some WSL distributions might need additional packages:
     ```bash
     sudo apt install -y libgtk-3-0
     ```

4. **Performance issues**:
   - WSL2 generally has better performance than WSL1 for GUI applications
   - Consider running the app natively on Windows if performance is inadequate

## Running Without the Script

If you prefer to set things up manually:

1. Start your X server on Windows
2. In WSL, set the DISPLAY variable:
   ```bash
   export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0
   ```
3. Navigate to the FinalCopy directory:
   ```bash
   cd /path/to/Final-project/FinalCopy
   ```
4. Set up and activate a virtual environment:
   ```bash
   python3 -m venv ../.venv
   source ../.venv/bin/activate
   ```
5. Install dependencies:
   ```bash
   pip install -r Requirements.txt
   ```
6. Run the application:
   ```bash
   python3 -m src.main
   ```

## Additional Resources

- [Microsoft's Guide to GUI Apps in WSL](https://docs.microsoft.com/en-us/windows/wsl/tutorials/gui-apps)
- [VcXsrv Documentation](https://sourceforge.net/projects/vcxsrv/)
- [Ubuntu GUI on WSL2 Tutorial](https://ubuntu.com/tutorials/ubuntu-on-windows#1-overview)
