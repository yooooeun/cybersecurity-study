# ARP Cache Analysis

## 1. Objective

ARP Cache에 저장되는 IP-MAC 매핑 정보를 확인하고,
Cache의 상태 변화 및 삭제 동작을 실험을 통해 분석한다.

---

## 2. Check ARP Cache

`arp -n` 명령어를 통해 현재 시스템에 저장된 ARP 캐시 테이블을 확인하였다.

```bash
arp -n

---

## 3. ARP Cache Fields

| Field | Meaning |
| :--- | :--- |
| **Address** | 상대방 장비의 IP 주소 |
| **HWtype** | 물리적 네트워크 타입 (이더넷의 경우 `ether`) |
| **HWaddress** | 상대방 장비의 MAC 주소 |
| **Flags Mask** | 캐시 상태 (`C`: Valid/Completed, `I`: Invalid/Incomplete) |
| **Iface** | 패킷이 입출력되는 본인 PC의 네트워크 인터페이스 이름 |


