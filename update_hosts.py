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
        
    # Generate README.md with Chinese introduction
    readme_content = f"""# Github Hosts (Hong Kong)

[English](./README.md) | [中文](./README.md)

This repository provides a `hosts` file for GitHub domains, resolved locally to optimize connectivity. It is specifically updated based on the local network resolution (Hong Kong).

本项目提供 GitHub 相关域名的 `hosts` 解析内容，由本地网络 (香港) 通过 `nslookup` 实时获取解析地址，旨在优化 GitHub 的访问速度。

---

**Last Updated (最后更新):** {current_time} (Beijing Time / 北京时间)

## Usage / 使用方法

### Local Usage / 本地使用
Append the content of `hosts` to your system's hosts file.
将 `hosts` 文件中的内容添加到系统 hosts 文件末尾：

- **Windows**: `C:\\Windows\\System32\\drivers\\etc\\hosts`
- **Linux / macOS**: `/etc/hosts`

### Automation / 自动更新
The repository is updated daily at 4:00 AM.
本项目每日凌晨 4:00 自动执行更新。

## Content / 解析内容
```text
{full_content}
```
"""
    with open(readme_output, 'w') as f:
        f.write(readme_content)

    print("\nUpdate complete.")

if __name__ == "__main__":
    main()