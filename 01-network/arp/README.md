# ARP (Address Resolution Protocol)

네트워크 환경에서 IP 주소를 MAC 주소로 변환하는
ARP 프로토콜의 동작 원리를 학습하고 패킷을 직접 분석하였다.

## Environment

- VirtualBox
- Host-only Network
- Victim: Ubuntu
- Attacker: Kali Linux
- Packet Analysis: Wireshark, tcpdump
- Network:
  - Ubuntu: 192.168.56.20
  - Kali: 192.168.56.10

## Objectives

- ARP Request / Reply 패킷 분석
- ARP 패킷의 주요 필드 확인
- Gratuitous ARP의 구조와 동작 이해
- ARP Cache 확인 및 삭제 실습
- Wireshark와 tcpdump를 이용한 패킷 분석

## Contents

1. [ARP Request / Reply 분석](./arp-request-reply.md)
2. [Gratuitous ARP 분석](./gratuitous-arp.md)
3. [ARP Cache 실습](./arp-cache.md)

## Key Concepts

- ARP Request
- ARP Reply
- Sender MAC Address
- Sender IP Address
- Target MAC Address
- Target IP Address
- Gratuitous ARP
- ARP Cache
