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

- **IP 충돌 감지**: 호스트가 네트워크에 연결될 때 동일한 IP 주소를 사용하는 장비가 있는지 확인한다.
- **ARP Cache 갱신**: MAC 주소가 변경되었을 때 네트워크 내 다른 장비들의 ARP 캐시 테이블을 최신 정보로 갱신시킨다.
- **주소 정보 알림**: 네트워크 인터페이스 교체 및 교환 시 자신의 최신 주소 정보를 자발적으로 광고한다.

---

## 4. Security Perspective

ARP 프로토콜은 패킷에 대한 **인증(Authentication) 메커니즘이 존재하지 않는다**. 

따라서 공격자가 위조된 IP-MAC 매핑 정보를 담은 GARP/ARP Reply 패킷을 지속적으로 전송할 경우, 타겟 장비의 캐시 테이블을 변조하는 **ARP Spoofing** 또는 **ARP Cache Poisoning** 공격에 악용될 수 있다.




