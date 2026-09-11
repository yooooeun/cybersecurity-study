# Gratuitous ARP Analysis

## 1. What is Gratuitous ARP?

Gratuitous ARP(GARP)는 다른 호스트의 MAC 주소를 조회하기 위한 일반적인 ARP Request와 달리, 자신의 IP-MAC 주소 정보를 네트워크에 광고하기 위해 **자발적(Gratuitous)으로 전송되는 ARP 패킷**이다.

---

## 2. Packet Structure & Differences

### Packet Comparison

- **Normal ARP Request**: 상대방의 주소를 알아내기 위한 목적이므로 `Sender IP != Target IP` 관계를 가진다.
- **Gratuitous ARP**: 본인의 주소를 알리기 위한 목적이므로 **`Sender IP == Target IP`** 관계를 가진다.

### Captured GARP Field

실습 패킷 분석에서 다음과 같이 **Sender IP와 Target IP가 동일한 특성**을 확인하였다[cite: 1].

| Field | Value |
| :--- | :--- |
| **Opcode** | `request (1)` |
| **Sender IP** | `192.168.56.10` |
| **Target IP** | `192.168.56.10` |
| **Target MAC** | `ff:ff:ff:ff:ff:ff` (Broadcast) |

![Gratuitous ARP Packet](./images/gratuitous-arp.png)

---

## 3. Why is Gratuitous ARP used?





