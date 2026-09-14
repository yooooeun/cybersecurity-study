# DHCP & DHCP Starvation Analysis

## 1. Objective

DHCP(Dynamic Host Configuration Protocol)의 기본적인 동작 과정을 이해하고,
Yersinia를 활용하여 DHCP Starvation 공격이 발생하는 원리와 DHCP 서버의 IP 자원이 고갈되는 과정을 실습을 통해 확인한다.

---

## 2. What is DHCP?

DHCP(Dynamic Host Configuration Protocol)는 
네트워크에 연결된 장치에 IP 주소와 같은 네트워크 설정을
자동으로 할당해 주는 프로토콜이다.

DHCP의 기본적인 IP 할당 과정은 **DORA**라고 하며,
다음과 같은 순서로 동작한다.

```text
Client                         DHCP Server

   |                                |
   |-------- DHCP Discover -------->|
   |                                |
   |<--------- DHCP Offer ----------|
   |                                |
   |-------- DHCP Request --------->|
   |                                |
   |<---------- DHCP ACK -----------|
   |                                |
```


| Message           | Direction       | Purpose                       |
| :---------------- | :-------------- | :---------------------------- |
| **DHCP Discover** | Client → Server | DHCP 서버를 찾기 위한 요청             |
| **DHCP Offer**    | Server → Client | DHCP 서버가 IP 주소 등의 설정을 제안      |
| **DHCP Request**  | Client → Server | 제안받은 설정을 사용하겠다는 요청            |
| **DHCP ACK**      | Server → Client | DHCP 서버가 요청을 승인하고 네트워크 설정을 할당 |

---

### 3. DHCP Starvation

>>What is DHCP Starvation?

DHCP Starvation Attack은 DHCP 서버가 보유하고 있는
IP 주소를 반복적으로 할당하게 만들어 IP Pool을 고갈시키고,
정상적인 사용자가 IP 주소를 할당받지 못하도록 방해하는 공격이다.

공격자는 여러 개의 가짜 MAC 주소를 사용하여
DHCP Discover 또는 Request를 반복적으로 발생시킨다.

DHCP 서버는 서로 다른 MAC 주소를 사용하는 요청을
서로 다른 클라이언트의 요청으로 인식할 수 있으며,
이 과정에서 IP 주소가 계속 할당되면서 DHCP 서버의
사용 가능한 IP Pool이 감소하게 된다.

```
가짜 MAC 주소 생성
        ↓
DHCP Discover / Request 반복
        ↓
DHCP Server가 새로운 클라이언트로 인식
        ↓
IP Lease 할당
        ↓
IP Pool 감소
        ↓
IP Pool 고갈
        ↓
정상 사용자의 IP 할당 방해
```
