# ARP Request / Reply Packet Analysis

## 1. Objective

ARP Request와 ARP Reply 패킷을 직접 캡처하여 IP 주소와 MAC 주소가 어떻게 매핑되는지 확인한다.

Wireshark와 tcpdump를 이용하여 ARP 패킷의 주요 필드를 분석하였다.

---

## 2. Packet Capture

Wireshark에서 다음 필터를 사용하였다.
`arp`

또한 CLI 환경에서는 tcpdump를 사용하여 패킷을 캡처하였다.
```bash
sudo tcpdump -i eth1 -vvv -e arp
```

---

## 3. ARP Request Packet Analysis

![ARP Request Packet](./images/arp-request.png)

| Field | Value |
| :--- | :--- |
| **Opcode** | Request (1) |
| **Sender MAC** | `00:0c:29:5a:c3:65` |
| **Sender IP** | `192.168.56.20` |
| **Target MAC** | `00:00:00:00:00:00` |
| **Target IP** | `192.168.56.10` |

Ubuntu(`192.168.56.20`)가 `192.168.56.10`의 MAC 주소를 알아내기 위해 ARP Request를 전송하였다.

Wireshark에서도 다음과 같이 확인할 수 있다.

`who has 192.168.56.10? Tell 192.168.56.20`

Sender는 자신의 MAC과 IP를 알고 있지만, Target의 MAC 주소는 아직 알지 못한다. 따라서 Target MAC Address는 `00:00:00:00:00:00`으로 설정되어있다.

---

## 4. ARP Reply Packet Analysis

![ARP Reply Packet](./images/arp-reply.png)

| Field | Value |
| :--- | :--- |
| **Opcode** | Reply (2) |
| **Sender MAC** | `00:0c:29:5a:c3:65` |
| **Sender IP** | `192.168.56.20` |
| **Target MAC** | `00:0c:29:54:b4:af` |
| **Target IP** | `192.168.56.10` |

캡처된 ARP Reply의 **Sender는 `192.168.56.20`**, **Target은 `192.168.56.10`**이다. Sender MAC(`00:0c:29:5a:c3:65`)은 응답을 보내는 장비의 MAC 주소이며, Target MAC(`00:0c:29:54:b4:af`)은 **응답을 받는 대상 장비의 MAC 주소**이다.

> **캡처 해석 주의:** 위 3절의 Request는 `192.168.56.20 → 192.168.56.10`의 MAC 주소를 묻고 있지만, 이 절의 Reply도 `192.168.56.20 → 192.168.56.10` 방향이다. 따라서 두 스크린샷을 **동일한 ARP 요청과 그 응답의 한 쌍이라고 단정할 수 없다.** `.20`이 `.10`의 MAC 주소를 요청한 경우 이에 대응하는 정상적인 Reply라면 일반적으로 Sender IP는 `.10`, Target IP는 `.20`이어야 한다. 원본 캡처의 실제 값은 변경하지 않았으며, 요청·응답의 대응 관계를 검증하려면 캡처 시각과 양쪽 필드를 대조해야 한다.

일반적인 ARP Reply는 요청자의 MAC 주소를 목적지로 하여 이더넷 **유니캐스트**로 전송된다. 다만 ARP 메시지 안의 `Target MAC` 필드와 이더넷 헤더의 목적지 MAC 필드는 별개이며, 이 스크린샷만으로 모든 ARP Reply가 항상 유니캐스트라고 결론 내릴 수는 없다.

---

## 5. ARP Request vs ARP Reply Comparison

| 항목 (Field) | ARP Request | ARP Reply |
| :--- | :--- | :--- |
| **Opcode** | `request (1)` | `reply (2)` |
| **전송 방식 (Destination)** | **Broadcast** (`ff:ff:ff:ff:ff:ff`) | **Unicast** (요청자의 MAC) |
| **전송 목적** | IP에 대응하는 MAC 주소 **요청** | 요청받은 IP의 MAC 주소 **응답** |
| **Target MAC** | `00:00:00:00:00:00` (조회 대상 MAC이 미상) | `00:0c:29:54:b4:af` (캡처된 Reply의 **수신 대상** MAC) |

---

## 6. Summary & Learned

ARP는 IPv4 주소를 기반으로 해당 장치의 MAC 주소를 확인하기 위해 사용된다.
ARP Request에서는 Target의 MAC 주소를 알 수 없기 때문에 Broadcast를 통해 특정 IP 주소의 MAC 주소를 요청한다.
ARP Reply에서는 확인된 MAC 주소 정보를 요청한 호스트에게 전달하며, 일반적으로 Unicast 방식으로 전송된다.
이번 실습에서는 Wireshark와 tcpdump를 이용하여 ARP Request와 ARP Reply의 Opcode, Sender/Target IP 및 MAC 주소를 직접 확인하면서 ARP의 IP-MAC 주소 매핑 과정을 패킷 수준에서 분석하였다. 다만 위 두 캡처가 서로 대응하는 요청·응답인지 추가 확인이 필요하다.




