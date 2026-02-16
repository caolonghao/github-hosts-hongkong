# Github Hosts (Hong Kong)

[English](./README.md) | [中文](./README.md)

This repository provides a `hosts` file for GitHub domains, resolved locally to optimize connectivity. It is specifically updated based on the local network resolution (Hong Kong).

本项目提供 GitHub 相关域名的 `hosts` 解析内容，由本地网络 (香港) 通过 `nslookup` 实时获取解析地址，旨在优化 GitHub 的访问速度。

---

**Last Updated (最后更新):** 2026-02-17 04:00:01 (Beijing Time / 北京时间)

## Usage / 使用方法

### Local Usage / 本地使用
Append the content of `hosts` to your system's hosts file.
将 `hosts` 文件中的内容添加到系统 hosts 文件末尾：

- **Windows**: `C:\Windows\System32\drivers\etc\hosts`
- **Linux / macOS**: `/etc/hosts`

### Automation / 自动更新
The repository is updated daily at 4:00 AM.
本项目每日凌晨 4:00 自动执行更新。

## Content / 解析内容
```text
# Github Hosts
# Updated: 2026-02-17 04:00:01 (Beijing Time)
# Repo: https://github.com/caolonghao/github-hosts-hongkong

140.82.114.25        alive.github.com
140.82.114.25        live.github.com
185.199.111.154      github.githubassets.com
140.82.113.21        central.github.com
185.199.108.133      desktop.githubusercontent.com
185.199.109.133      camo.githubusercontent.com
185.199.109.133      github.map.fastly.net
151.101.1.194        github.global.ssl.fastly.net
140.82.116.4         gist.github.com
185.199.111.153      github.io
140.82.116.4         github.com
192.0.66.2           github.blog
140.82.116.6         api.github.com
185.199.111.133      raw.githubusercontent.com
185.199.111.133      user-images.githubusercontent.com
185.199.111.133      favicons.githubusercontent.com
185.199.110.133      avatars5.githubusercontent.com
185.199.111.133      avatars4.githubusercontent.com
185.199.109.133      avatars3.githubusercontent.com
185.199.111.133      avatars2.githubusercontent.com
185.199.109.133      avatars1.githubusercontent.com
185.199.110.133      avatars0.githubusercontent.com
185.199.110.133      avatars.githubusercontent.com
140.82.116.9         codeload.github.com
16.15.179.222        github-cloud.s3.amazonaws.com
16.15.223.194        github-com.s3.amazonaws.com
3.5.30.180           github-production-release-asset-2e65be.s3.amazonaws.com
52.216.44.33         github-production-user-asset-6210df.s3.amazonaws.com
52.217.75.164        github-production-repository-file-5c1aeb.s3.amazonaws.com
185.199.111.153      githubstatus.com
140.82.112.17        github.community
20.43.185.14         github.dev
140.82.113.21        collector.github.com
13.107.42.16         pipelines.actions.githubusercontent.com
185.199.110.133      media.githubusercontent.com
185.199.111.133      cloud.githubusercontent.com
185.199.111.133      objects.githubusercontent.com
```
