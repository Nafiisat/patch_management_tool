Patch Management Tool – Cross-Platform Security Updates with Python
📌 Overview
The Patch Management Tool is a cross-platform Python-based utility that automates the detection and installation of software and system updates on Windows, macOS, and Linux.
It is designed to help individuals and small teams maintain security hygiene by keeping their systems patched against vulnerabilities.
This tool detects available patches, installs them, and generates reports for audit and compliance purposes.

🚀 Features
Cross-platform support – Works on Windows, macOS, and Linux.
Automated update checks – Detects available OS and software patches.
One-click installation – Applies patches without manual intervention.
Logging and reporting – Generates a detailed patch history in a log file.
Customizable – Easily extend to monitor specific software packages.
🛠 Technology Stack
Language: Python 3
Libraries:
subprocess (to execute system commands)
os (for file and path management)
platform (to detect OS type)
datetime (for timestamps in logs)
⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/Nafiisat/patch_management_tool.git
cd patch_management_tool
2️⃣ Install Python 3
Ensure Python 3 is installed:
python3 --version
If not installed, download from: https://www.python.org/downloads/
3️⃣ Run the Script
python3 patch_manager.py
📋 Usage
Check for updates only:
The tool will list available updates without installing them.
Install updates automatically:
When run with the install flag, it applies all available updates.
View logs:
Generated in patch_log.txt with timestamps and details.
📄 Example Log Output
[2025-08-12 14:35:22] OS: macOS
Checked for updates: 5 available.
Installed 5 updates successfully.
🔮 Future Improvements
Add email notifications when updates are available.
Integration with vulnerability scanners for proactive patching.
Web dashboard to view patch status across multiple systems.
🤝 Contributing
Pull requests are welcome! For major changes, please open an issue to discuss your ideas.
