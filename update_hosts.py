import socket
import datetime
import os

def get_ip(domain):
    try:
        # Uses local system resolver (equivalent to local nslookup)
        ip = socket.gethostbyname(domain)
        return ip
    except socket.error:
        return None

def main():
    domains_file = 'domains.txt'
    hosts_output = 'hosts'
    readme_output = 'README.md'
    
    if not os.path.exists(domains_file):
        print(f"Error: {domains_file} not found.")
        return

    with open(domains_file, 'r') as f:
        domains = [line.strip() for line in f if line.strip()]

    hosts_content = []
    
    print("Resolving domains...")
    for domain in domains:
        ip = get_ip(domain)
        if ip:
            line = f"{ip.ljust(20)} {domain}"
            hosts_content.append(line)
            print(f"Resolved: {line}")
        else:
            print(f"Failed to resolve: {domain}")

    # Generate hosts file content with Beijing Time (UTC+8)
    tz_beijing = datetime.timezone(datetime.timedelta(hours=8))
    current_time = datetime.datetime.now(tz_beijing).strftime("%Y-%m-%d %H:%M:%S")
    
    header = f"""# Github Hosts
# Updated: {current_time} (Beijing Time)
# Repo: https://github.com/caolonghao/github-hosts-hongkong

"""
    
    full_content = header + "\n".join(hosts_content)
    
    with open(hosts_output, 'w') as f:
        f.write(full_content)
        
    # Generate README.md
    readme_content = f"""# Github Hosts (Hong Kong)

This repository provides a `hosts` file for GitHub domains, resolved locally to optimize connectivity.

**Last Updated:** {current_time} (Beijing Time)

## Usage

### Local Usage
Append the content of `hosts` to your system's hosts file.
- **Windows**: `C:\\Windows\\System32\\drivers\\etc\\hosts`
- **Linux/macOS**: `/etc/hosts`

### Content
```text
{full_content}
```
"""
    with open(readme_output, 'w') as f:
        f.write(readme_content)

    print("\nUpdate complete.")

if __name__ == "__main__":
    main()
