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
