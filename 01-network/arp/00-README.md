# ARP (Address Resolution Protocol)

ARP(Address Resolution Protocol)의 동작 원리를 이해하고,
실제 네트워크 환경에서 ARP 패킷과 ARP Cache를 분석하였다.

## Environment

- VirtualBox
- Host-only Network
- Victim: Ubuntu
- Attacker: Kali Linux
- Packet Analysis: Wireshark, tcpdump

### Network Configuration

| Host | IP Address |
|---|---|
| Ubuntu | 192.168.56.20 |
| Kali Linux | 192.168.56.10 |

## Objectives

- ARP Request / Reply 패킷 분석
- ARP Header 주요 필드 확인
- Gratuitous ARP 구조 및 동작 분석
- ARP Cache 확인 및 삭제 실습
- Linux의 ARP Cache 관리 방식 확인

## Contents

1. [ARP Request / Reply 분석](./01-ARP-Request-Reply.md)
2. [Gratuitous ARP 분석](./02-Gratuitous-ARP.md)
3. [ARP Cache 분석](./03-ARP-Cache.md)

## Key Concepts

- ARP Request
- ARP Reply
- Opcode
- Sender MAC / IP
- Target MAC / IP
- Gratuitous ARP
- ARP Cache
- Neighbor Unreachability Detection (NUD)

## Security Perspective

ARP는 별도의 인증 절차 없이 IP 주소와 MAC 주소의 
매핑 정보를 전달하기 때문에 ARP Spoofing 및
ARP Cache Poisoning과 같은 공격에 악용될 수 있다.
