# Installation Guide

## System Requirements

- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- Windows 10/11, macOS, or Linux
- Internet connection for initial setup

## Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AbirMohanta/ML-Based-Ballistics-Recognition-Tool.git
   cd ML-Based-Ballistics-Recognition-Tool
   ```

2. **Set Up Virtual Environment (Recommended)**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Installation**
   ```bash
   streamlit run app.py
   ```

## Common Installation Issues

### Package Installation Errors
If you encounter package installation errors:
1. Upgrade pip: `python -m pip install --upgrade pip`
2. Install packages individually
3. Check system compatibility

### Streamlit Launch Issues
If Streamlit fails to launch:
1. Check Python version
2. Verify all dependencies are installed
3. Try running with `--server.port 8501` 