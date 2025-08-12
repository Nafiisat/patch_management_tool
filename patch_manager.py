import subprocess
import platform
import requests

NVD_API = "https://services.nvd.nist.gov/rest/json/cves/2.0"

def search_cves(product, version):
    params = {"keywordSearch": f"{product} {version}"}
    response = requests.get(NVD_API, params=params)
    
    if response.status_code == 200:
        data = response.json()
        total_cves = data.get("totalResults", 0)
        if total_cves > 0:
            print(f"⚠ Found {total_cves} CVEs for {product} {version}")
        else:
            print(f"No CVEs found for {product} {version}")
    else:
        print(f"[ERROR] Failed to fetch CVEs for {product} {version}")

def list_installed_packages():
    system = platform.system()

    if system == "Darwin":  # macOS
        result = subprocess.run(["brew", "list", "--versions"], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            pkg, ver = line.split(" ", 1)
            search_cves(pkg, ver)

    elif system == "Linux":
        result = subprocess.run(["dpkg", "-l"], capture_output=True, text=True)
        for line in result.stdout.splitlines()[5:]:
            parts = line.split()
            if len(parts) >= 3:
                pkg, ver = parts[1], parts[2]
                search_cves(pkg, ver)

    elif system == "Windows":
        print("[TODO] Add Windows CVE checking")
    else:
        print("[ERROR] Unsupported OS")

if __name__ == "__main__":
    list_installed_packages()
