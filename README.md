# Cybersecurity Study & Practice

**From Fundamentals to Hands-on Security Engineering**

네트워크, 리눅스, 사이버보안을 학습하며 이론을 실제 환경에서 검증하고 문제를 해결하는 과정을 기록하는 저장소입니다.

단순히 개념을 암기하는 것을 넘어 **Learn → Practice → Analyze → Document** 과정을 통해 실무 역량을 쌓는 것을 목표로 합니다.

---

## About Me

- **Major:** Cybersecurity
- **Interests:** Network Security, Linux, Security Infrastructure
- **Career Goal:** Security Infrastructure Engineer
- **Currently Learning:** Networking, Linux, Python, Security Fundamentals

보안 인프라 엔지니어를 목표로 네트워크와 시스템의 동작 원리를 이해하고, 직접 실습하며 기술적 문제 해결 능력을 발전시키고 있습니다.

장기적으로 보안 전문성을 확장하고 글로벌 IT 기업의 보안 직무에 도전하는 것이 목표입니다.

## Featured Labs & Projects

현재까지 진행한 주요 실습과 프로젝트입니다.

| Topic | Description | Documentation |
|---|---|---|
| ARP Analysis | ARP Request/Reply, Gratuitous ARP, ARP Cache 및 Linux NUD 분석 | [View Lab](./01-network/arp/00-README.md) |
| DHCP Security | DHCP DORA 과정, DHCP Starvation 실습 및 대응 기술 학습 | [View Lab](./01-network/dhcp/README.md) |
| IPv4 Packet Analysis | IPv4 헤더 파싱, Fragmentation, DSCP 및 PHB 분석 | [View Lab](./01-network/ip/README.md) |
| Python Typing Game | Python과 Tkinter를 활용한 GUI 타자 게임 개발 | [View Project](./04-programming/typing-game/README.md) |

각 실습에서는 가능한 한 환경 구성, 사용한 명령어, 실행 결과, 분석 및 시행착오를 함께 기록합니다.

## Repository Structure

```text
cybersecurity-study/
│
├── 01-network/         # Network protocols & packet analysis
│   ├── arp/
│   ├── dhcp/
│   └── ip/
│
├── 02-linux/           # Linux fundamentals
├── 03-security/        # Security concepts
├── 04-programming/     # Python & programming practice
│   └── typing-game/
│
├── 05-projects/        # Security projects
└── README.md
```

향후 CTF 학습을 시작하면 `06-ctf/` 영역을 추가할 예정입니다.

## Learning Roadmap

### 2026 — Building Foundations

**Goal: 네트워크·리눅스 기초 강화 및 CTF 입문**

- [x] ARP 패킷 분석
- [x] DHCP 동작 및 DHCP Starvation 실습
- [x] IPv4 헤더 분석
- [x] Python GUI 프로젝트 구현
- [ ] VLAN 및 Routing 실습 문서화
- [ ] Linux 권한 및 시스템 보안 실습
- [ ] CTF 입문 문제 해결 및 Write-up 작성

### 2027 H1 — Practical Security

**Goal: 기초 보안 문제를 독립적으로 분석하고 해결하기**

- [ ] Web Security 기초 학습
- [ ] Linux 및 System Security 실습
- [ ] Wireshark 기반 트래픽 분석 심화
- [ ] Python 보안 자동화 도구 개발
- [ ] CTF 기초 문제 독립 해결
- [ ] 개인 보안 프로젝트 완성

### 2027 H2 — Security Challenges

**Goal: 해킹 대회에 도전하고 팀에 실질적으로 기여하기**

- [ ] CTF 주요 분야 탐색 및 전문 분야 선정
- [ ] 중급 수준의 보안 문제 해결 연습
- [ ] 팀 기반 문제 해결 및 협업 경험
- [ ] 실제 해킹 대회 참가
- [ ] 대회 회고 및 학습 결과 문서화

## Long-term Goals

1. **Technical Foundation** — 네트워크·리눅스·시스템의 동작 원리 이해
2. **Hands-on Experience** — 보안 실습과 프로젝트를 통한 기술 적용
3. **Problem Solving** — CTF 및 보안 문제 분석 역량 향상
4. **Security Engineering** — 보안 인프라 구축·운영 역량 확보
5. **Continuous Growth** — 지속적인 학습을 통한 보안 전문성 확장

---

### Learning Philosophy

> Understand how it works. Practice how it behaves. Analyze why it happens.

기술이 어떻게 동작하는지 이해하고, 직접 검증하고, 그 결과를 설명할 수 있는 보안 엔지니어로 성장하는 것이 목표입니다.
