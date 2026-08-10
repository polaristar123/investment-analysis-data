# 🚀 APEX v10.3 Ultimate Master Engine - 실행 가이드

## 📋 시스템 구성 (System Architecture)

```
[최종 통합 v10.3 투자 분석 엔진]
│
├─ INPUT: analysis_ingredient_extended.md
│  ├─ PART 0~0.9: 최적화 규칙 + Forensics (v10.3)
│  ├─ PART I~VIII: 기본 재무데이터 입력
│  └─ PART XIII: Hook 26-35 (기관등급 정밀)
│
├─ EXECUTION: 3단계 순차 분석
│  ├─ Phase 1: Fast-Pass Scan (Hook 1, 8, 10, 24)
│  ├─ Phase 2: Foundation Hooks (1-7)
│  └─ Phase 3: Deep-Dive Analysis (8-35)
│
└─ OUTPUT: 통합 투자 보고서
   ├─ 3-Philosopher Consensus Score
   ├─ 25 Hooks 종합 평가
   ├─ Adaptive Modules 1-5
   └─ Final Investment Recommendation
```

---

## ⚡ 3단계 실행 프로토콜

### **Step 1: 데이터 입력 (2-3분)**

`analysis_ingredient_extended.md`의 PART I-VIII에 기업 재무데이터 입력:

```markdown
[필수 입력 항목]
- 10년 매출/EBITDA/영업이익/순이익
- 10년 자산/부채/자본
- 10년 영업현금흐름/CapEx/자유현금흐름
- 현재주가, 유통주식수, 섹터 분류
```

**✓ 섹터 자동 라우팅** (PART 0.9):
- Financials: NWC/CapEx/CCC Bypass
- SaaS/IT: CAC/LTV 강조, CapEx Bypass
- Manufacturing: 모든 Hook 적용
- Biotech/Pharma: 특화 지표 적용

---

### **Step 2: Forensics Gate 검증 (2분)**

**PART 0.8 즉시 실행:**

```
[M-Score > -1.78?] 
├─ YES → 🔴 FRAUD ALERT (분석 중단)
└─ NO  → Z-Score 검사로 진행

[Z-Score < 1.81?]
├─ YES → 🔴 BANKRUPTCY RISK (분석 중단)
└─ NO  → ✅ FORENSICS GATE PASSED → Full Analysis
```

**토큰 효율성:** 부정/파산 검출 시 **60% 절감**

---

### **Step 3: 3단계 Hook 분석 (8-12분)**

#### **Phase 3A: Priority Hooks 8-10** (4분)

| Hook | 항목 | 공식 |
|------|------|------|
| **8** | Dynamic WACC | $WACC = K_e \cdot (E/V) + K_d(1-T_c) \cdot (D/V)$ |
| **9** | CAP Decay | $CAP(t) = CAP_{base} \times e^{-\lambda t}$ |
| **10** | Owner Earnings | $NI + D\&A - Maint. CapEx - \Delta NWC$ |

**실행:** Chain-of-Thought 5단계 프로토콜 (PART 0.5 Rule 2)
```
[Step 1] 공식 정의
[Step 2] 데이터 입력
[Step 3] 중간항 계산
[Step 4] 분자 합계
[Step 5] 최종값 + 해석
```

#### **Phase 3B: Foundation Hooks 1-7** (2분)

✅ PASS 기준: 최소 5/7 (Foundation Quality 검증)

#### **Phase 3C: Advanced + Apex Hooks 11-25** (4분)

- **Hook 11-14**: P-Q-C 분해, Owner Earnings, Monte Carlo
- **Hook 21-25**: 거버넌스, CCC, Goodwill, 유동성, Tail Risk

**✓ Rule 1 적용** (Sector-Based Bypass):
- Financials: Hook 3-7, 9-20 Skip → ~25% 토큰 절감
- SaaS: Hook 3-7, 9-10, 12, 14-25 Skip → ~20% 절감
- Manufacturing: Hook 33, 35만 Skip → ~8% 절감

---

### **Step 4: 3-Philosopher Consensus 모델** (2분)

```
1️⃣  Benjamin Graham Score  (0-100)
    → 자산 방어력, 채무비율, 유동성

2️⃣  Warren Buffett Score   (0-100)
    → 주주이익 창출력, 지속가능 해자

3️⃣  Charlie Munger Score   (0-100)
    → 경영진 역량, 가격 결정력

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⭐ CONSENSUS = (Graham + Buffett + Munger) / 3
```

---

### **Step 5: Adaptive Modules 1-5** (2분)

| Module | 항목 | 조정내용 |
|--------|------|---------|
| **1** | 동적 안전마진 | 성장률 & 거시환경 조정 |
| **2** | 촉매 점수 | +긍정 / -부정 신호 |
| **3** | 동적 손절가 | ATR 기반 자동 조정 |
| **4** | 포트폴리오 버킷 | Core / Growth / Tactical |
| **5** | 시장 심리 | CMFI 지수 반영 |

---

### **Step 6: 최종 보고서 생성** (1분)

**PART XIII Hook 26-35 정밀 분석 결과 통합:**

```markdown
================================================================================
🏛️  APEX v10.3 INTEGRATED INVESTMENT REPORT
================================================================================

[기업명] / Ticker
【sector】 | 【현재주가】 / 【시가총액】

1️⃣  3-PHILOSOPHER CONSENSUS SCORE
────────────────────────────────────────────────────────────────
  • Graham Score      : [ __ / 100 ]
  • Buffett Score     : [ __ / 100 ]
  • Munger Score      : [ __ / 100 ]
  ─────────────────────────────────
  ⭐ CONSENSUS        : [ __ / 100 ] → [STRONG BUY / BUY / HOLD / SELL]

2️⃣  CORE METRICS (Hook 8-10)
────────────────────────────────────────────────────────────────
  • Dynamic WACC      : [ __ % ] (Ke: __%, Kd: __%, Tax: __%)
  • CAP Decay (10Y)   : [ __ 년 ] (현재 → 10년후 [ __ 년 ])
  • Owner Earnings    : [ __ 억원 ] (주당 [ __ 원 ])

3️⃣  VALUATION
────────────────────────────────────────────────────────────────
  • 95% 신뢰구간      : [ __ 원 ] ~ [ __ 원 ]
  • 목표주가 (12M)    : [ __ 원 ] (상승여력: __%)
  • 현재 MoS          : __% (요구 MoS: __%)

4️⃣  RISK & CATALYSTS
────────────────────────────────────────────────────────────────
  • 주요 리스크       : [ 1) ___ 2) ___ 3) ___ ]
  • 주요 촉매         : [ 1) ___ 2) ___ 3) ___ ]
  • Lollapalooza      : ✅ SAFE (치명적 신호 없음)

5️⃣  RECOMMENDATION
────────────────────────────────────────────────────────────────
  • 최종 신호         : [STRONG BUY / BUY / HOLD / SELL / STRONG SELL]
  • 추천 버킷         : [Core Compounder / Growth / Tactical]
  • 권장 비중         : __% of Portfolio (최대 __%)
  • 매수 가격대       : [ __ 원 이하 분할매수 ]
  • Stop-Loss 설정    : [ __ 원 ]

================================================================================
```

---

## 🎯 주요 개선 사항 (v10.3 vs v10.1)

| 항목 | v10.1 | v10.3 |
|------|-------|-------|
| **Hook 범위** | 1-25 | 1-35 (새로운 10개) |
| **정밀도** | 기본 수식 | LaTeX 89개 + 예시 |
| **Chain-of-Thought** | 부분 적용 | 모든 Hook 5단계 의무화 |
| **Forensics** | 미포함 | M-Score + Z-Score (조기종료) |
| **Sector Bypass** | 4개 | 5개 + 동적 토큰 효율 |
| **Institutional Grade** | Hook 21-25 | Hook 26-35 추가 (CAE, ROIC_adj, EV_precision 등) |
| **보고서 형식** | 기본 | 3-Philosopher + Adaptive 통합 |

---

## ⏱️ 전체 분석 소요 시간

```
입력 (3분) + Fast-Pass (2분) + Forensics (2분) 
+ Priority (4분) + Foundation (2분) + Advanced (4분) 
+ Consensus (2분) + Adaptive (2분) + 보고서 (1분) 
= 👉 약 22분 소요 (섹터별 Bypass 시 15-18분)
```

---

## 📊 실행 체크리스트

```markdown
✅ 데이터 입력 완료
✅ 섹터 분류 및 라우팅 결정
✅ Forensics Gate (M-Score / Z-Score) 검증
✅ Priority Hooks 8-10 계산
✅ Foundation Hooks 1-7 검증 (5/7 이상)
✅ Advanced Hooks 11-25 분석
✅ 3-Philosopher 스코어 계산
✅ Adaptive Modules 1-5 조정
✅ Lollapalooza 4대 극단 신호 검사
✅ 최종 보고서 생성 및 검증
```

---

## 🚀 즉시 시작 (Quick Start)

1. **입력 파일 준비**: `analysis_ingredient_extended.md`의 PART I-VIII 작성
2. **Sector 선택**: PART 0.9에서 업종 자동 검출
3. **Forensics 검증**: M-Score > -1.78? Z-Score < 1.81? 확인
4. **Hook 분석 실행**: Chain-of-Thought 프로토콜 따라 단계별 계산
5. **보고서 생성**: 위 템플릿 사용하여 최종 리포트 작성

---

**버전**: APEX v10.3  
**상태**: 🎯 PRODUCTION READY  
**마지막 업데이트**: 2026-08-10
