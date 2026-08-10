# 🔬 Unified Investment Analysis Engine v10.1 (Part 3/3)
## Adaptive Modules 1-5 (v10.0+) + Integrated Output Matrix
### Opportunity Cost Elimination + Negative Catalyst System + Final Signal

**버전**: v10.1 APEX Modular Standard  
**모듈**: Part 3/3 - Adaptive & Output Layer  
**설명**: 동적 안전마진 + 촉매 엔진 + 부정적 신호 + 최종 투자 판정

---

## 📖 PART 3 로드 조건 (Part 1 + Part 2 완료 후)

✅ Part 1 + Part 2 필수 완료:
- Hooks 1-25 모두 산출 ✓
- 3-Philosopher Consensus ≥ 60점 ✓
- Lollapalooza & Anti-Hooks 확인 ✓

**→ Part 3 자동 로드**

---

## 🟣 ADAPTIVE MODULES (1-5) - v10.0+ INNOVATION

### Module 1: Regime & Life-Cycle Adaptive MoS (동적 안전마진)

**목적**: 고정 MoS 기준치를 성장률과 시장 사이클에 따라 **동적 조정** → 고성장주 필터링 오류 제거

**공식**:

$$RequiredMoS_{v10} = BaseMoS \times \left(1 - \ln(1 + \text{Revenue Growth Rate})\right) \times \text{Regime Multiplier}$$

**Step 1: 성장률 기반 MoS 하향 조정**

```
논리:
- 성장률 높은 기업 (>30%): 미래 캐시플로우 극대화
  → 현재 안전마진 요구도 낮춰도 됨 (10~15%)
  
- 성장률 낮은 기업 (<5%): 미래 개선 여지 낮음
  → 현재 안전마진 높아야 함 (30~40%)

ln() 함수의 특성:
- ln(1 + 0.4) = 0.336 → MoS 감소 33.6%
- ln(1 + 0.05) = 0.049 → MoS 감소 4.9% (최소한만)
```

**계산 예시**:
```
기본 BaseMoS: 30%

경우 1: 고성장 (Revenue Growth 40%)
ln(1.4) = 0.336
RequiredMoS = 30% × (1 - 0.336) = 30% × 0.664 = 19.9% (~20%)
→ 현재주가 20% 아래면 매수 가능 (기본 30% 대비 완화)

경우 2: 저성장 (Revenue Growth 2%)
ln(1.02) = 0.020
RequiredMoS = 30% × (1 - 0.020) = 30% × 0.980 = 29.4% (~30%)
→ 현재주가 30% 아래여야 매수 (기본값 유지)
```

**Step 2: 시장 사이클별 Regime Multiplier 적용**

```
Regime 1 (정상기): Multiplier = 1.0
- 시장 VIX 15~20
- 금리 중립 (기준금리 3~4%)
- 신용스프레드 정상 (400~500bps)

Regime 2 (약세장): Multiplier = 0.7
- VIX > 20 / 금리 인상 시기 / 스프레드 확대
- 매수 심리 약함 → MoS 완화 (적극 매수 유도)
- RequiredMoS = 20% × 0.7 = 14% (극도의 완화)

Regime 3 (경기 침체): Multiplier = 1.3
- VIX > 30 / 경기 악화 신호 / 신용 위험 고조
- 매수 심리 위험 → MoS 가중 (방어적)
- RequiredMoS = 20% × 1.3 = 26% (강화)
```

**최종 Adaptive MoS 판정**:
```
현재주가: 70,000원
내재가치 Base: 75,000원 (MoS = 6.7%)

고성장 기업 + 정상 시장:
RequiredMoS = 20%
→ 필요 내재가치 = 70,000 × 1.2 = 84,000원
→ 현재 내재가치 75,000원 < 필요 84,000원
→ HOLD (완전히 매도 기준은 아니지만 매수 아님)

성장 정체 + 약세장:
RequiredMoS = 20% × 0.7 = 14%
→ 필요 내재가치 = 70,000 × 1.14 = 79,800원
→ 현재 내재가치 75,000원 < 필요 79,800원
→ HOLD (약간 저평가이지만 아직 모자람)
```

---

### Module 2: Soros Reflexivity & Catalyst Engine (촉매 엔진 + 부정적 신호)

**목적**: 주가 상승이 기업 펀더멘탈을 개선하는 선순환, 또는 악화시키는 악순환 감지 → 단기 이벤트 변동성 포착

**6개 긍정적 촉매 (Positive Catalyst)**:

| # | 촉매 | 점수 | 판정 기준 |
|----|------|------|---------|
| 1 | 신제품 출시/기술 | 0~25 | 분기 내 공식 발표 + 시장 규모 확인 |
| 2 | 시장 커버리지 (M&A) | 0~20 | 매수 인수 확률 + 프리미엄 계산 |
| 3 | 자사주 매입 | 0~20 | 연간 매입량 > EPS 5% + 주가 저평가 |
| 4 | 포트폴리오 개선 | 0~15 | 저마진 사업 분리 + 수익성 강화 |
| 5 | M&A / 신사업 | 0~10 | 6개월 내 공식 공시 + 근거 있는 예상 |
| 6 | 공시/거버넌스 개선 | 0~10 | 최근 공식 발표 또는 언론 보도 |

**계산 예시**:
```
Samsung Electronics 촉매 평가:

1. 신제품 (AI 칩 개발): 15점
   (5nm 공정 준비 중, 경쟁사보다 6개월 앞선 신뢰도)

2. M&A (스핀오프 검토): 12점
   (공식 언론은 아니지만 애널리스트 충분 근거)

3. 자사주 (2025년 10조원 예상): 18점
   (지난 3년 정책 일관성 높음)

4. 포트폴리오 (LCD 졸업): 10점
   (2024년부터 실행, 가시적 진전)

5. 신사업 (Foundry 강화): 8점
   (꾸준한 투자, 아직 확실하지 않음)

6. 거버넌스 (사외이사 증대): 5점
   (진행 중이지만 아직 미진)

Total Catalyst Score = 15+12+18+10+8+5 = 68점
```

**Allocation Multiplier 결정**:
```
Catalyst Score < 60: Multiplier = 1.0 (기본)
Catalyst Score 60~80: Multiplier = 1.2 (포지션 +20%)
Catalyst Score > 80: Multiplier = 1.3 (포지션 +30%)

Samsung: 68점 → Multiplier = 1.2
→ 표준 포지션 대비 20% 추가 배분 허용
```

---

**⚠️ 부정적 촉매 (Negative Catalyst) - 새로운 시스템**

**목적**: 긍정적 신호만으로는 리스크 놓침 → 부정적 사건(악재) 정량화하여 차감

**부정적 촉매 항목**:

| 항목 | 감점 | 판정 기준 |
|------|------|---------|
| **경영권 분쟁** | -30점 | 대주주 변동 또는 분쟁 보도 |
| **규제/소송** | -20점 | 정부 조사, 독점 소송, 환경 위반 |
| **기술 구식화** | -25점 | 핵심 특허 만료 1년 내 또는 신기술 등장 |
| **채무 급증** | -30점 | 부채/자본 비율 1년간 50% 이상 증가 |
| **거래처 집중도** | -15점 | 최대 거래처 > 30% 의존 + 계약 갱신 불확실 |
| **경영진 교체** | -20점 | CEO 교체 + 경영방침 급변 |

**계산 예시**:
```
기업 X의 부정적 촉매 분석:

경영권 분쟁 없음: 0점
규제 리스크 (환경 감시): -8점 (심각하지 않음)
기술 위험 (특허 3년 남음): 0점
채무 증가 (YoY +30%): -10점
거래처 집중 (A사 25%): 0점
경영진 안정: 0점

Negative Catalyst Score = -(8+10) = -18점

조정된 Catalyst Score = (Positive 68점) + (Negative -18점) = 50점
→ Multiplier = 1.0 (기본값으로 하향)
```

---

### Module 3: Volatility Clustering & Dynamic ATR Stop-Loss (변동성 기반 손절)

**목적**: 정적 손절가 → 시장 변동성에 따른 **동적 손절가**로 전환 → 노이즈 트레이딩 방지

**공식**:

$$StopLoss Price = Current Price - (k \times ATR_{20})$$

**Step 1: 변동성 레짐 결정**

```
VIX 또는 20일 Realized Volatility 기반:

정상기 (VIX < 20, σ ≤ 15%):
- k = 1.5 (ATR 1.5배)
- 손절폭: 좁음 (근처 거래 방지)

고변동성 (VIX 20~30, σ 15~25%):
- k = 2.0 (ATR 2.0배)
- 손절폭: 중간 (적절한 완충)

극단 스트레스 (VIX > 30, σ > 25%):
- k = 2.5 (ATR 2.5배)
- 손절폭: 넓음 (공황 팔기 방지)
```

**Step 2: ATR 계산 (기본 TA)**

```
ATR (Average True Range) 20일:
TR_t = max(High_t - Low_t, 
           |High_t - Close_t-1|, 
           |Low_t - Close_t-1|)

ATR_20 = SMA(TR, 20)

예:
현재주가: 70,000원
ATR_20: 3,500원 (매일 평균 변동폭)
```

**Step 3: Fallback Logic (데이터 미제공 시)**

```
ATR 데이터 미제공 시 대체 계산:

ATR_approx = Current_Price × (σ_annualized / √252)

예:
현재주가: 70,000원
연간 변동성: 30%

ATR_approx = 70,000 × (0.30 / √252)
           = 70,000 × 0.0189
           ≈ 1,323원

k = 2.0 (정상기 가정)
Stop-Loss = 70,000 - (2.0 × 1,323) = 67,354원
```

**Step 4: 손절 판정**

```
현재주가 < Stop-Loss Price → 손절 실행
현재주가 ≥ Stop-Loss Price → 계속 보유 (손절선 상향 추적 가능)

예:
Stop-Loss = 67,354원으로 설정
→ 주가 하락 시:
  - 68,000원: 유지
  - 67,000원: 손절 실행 (하한 도달)
  - 65,000원 이상 하락 방지
```

---

### Module 4: Multi-Horizon Portfolio Bucketing (3가지 시간 지평 포트폴리오)

**목적**: 단일 투자 목표 → **Core/Growth/Tactical 3개 버킷**으로 분산 → 리스크 계층화

**3개 버킷 정의**:

```
Core Compounder (장기 자산, 50% 배분):
- 보유 기간: 10년 이상
- 입장 기준: Hook 1-25 모두 PASS + Consensus > 80점
- 최대 포지션: 30% (한 기업)
- 예: 버크셔 해서웨이, 코스탁 (장기 불변의 가치주)

High-Beta Growth (중기 성장, 30% 배분):
- 보유 기간: 3~5년
- 입장 기준: 
  * Module 1 Adaptive MoS 통과 (조정된 기준)
  * Revenue Growth ≥ 30%
  * Consensus > 60점
- 최대 포지션: 15% (한 기업)
- 예: AI칩, 바이오, 고성장 SaaS

Event-Driven Tactical (단기 이벤트, 20% 배분):
- 보유 기간: 6개월 ~ 1년
- 입장 기준:
  * Module 2 Catalyst Score ≥ 60점
  * 3~6개월 내 구체적 이벤트 예정
  * Downside Risk ≤ 25%
- 최대 포지션: 5% (한 기업)
- 예: M&A 후보, 스핀오프, 자사주 반사
```

**포지션 크기 계산**:

```python
# 포트폴리오 구성
Portfolio_Value = 10억원

# 각 버킷별 배분
Core_Budget = Portfolio_Value × 0.50  # 5억원
Growth_Budget = Portfolio_Value × 0.30  # 3억원
Tactical_Budget = Portfolio_Value × 0.20  # 2억원

# 버킷 내 개별 포지션 제한
Core_Max_Position = Core_Budget * 0.30  # 5억원의 30% = 1.5억원
Growth_Max_Position = Growth_Budget * 0.15  # 3억원의 15% = 0.45억원
Tactical_Max_Position = Tactical_Budget * 0.05  # 2억원의 5% = 100만원

# 구체적 주식 배분
# Samsung (Core): 1억원 (Core 버킷 내 33%)
# NVIDIA (Growth): 3,000만원 (Growth 버킷 내 100%)
# 신약개발 중소형주 (Tactical): 500만원
```

---

### Module 5: Expert Market Fear & Sentiment (CMFI) - Market Fear Index

**목적**: VIX를 넘어 **4개 전문가 지표**로 시장 공포/탐욕을 정량화 → Module 1 MoS 동적 조정

**4개 전문가 지표**:

```
1. CNN Fear & Greed Index (FGI)
   - 매일 업데이트 (https://money.cnn.com/data/fear-and-greed/)
   - 0 = Extreme Fear, 100 = Extreme Greed
   - 계산: (Market Momentum + Stock Price Strength + ...) 합성

2. High-Yield Credit Spread (HY OAS)
   - ICE BofA US High Yield OAS 지표
   - 기준: 400bps ±120bps
   - >600bps: 신용 위기 신호
   - <300bps: 과도한 탐욕

3. CBOE Put/Call Ratio (PCR)
   - 10일 이동평균 활용
   - >1.00: 극단적 두려움 (매도압박)
   - <0.45: 과도한 자신감 (매수과열)

4. AAII Bull-Bear Spread
   - 미국 개인투자자 심리지표
   - Bull% - Bear% 계산
   - >+30%: 극단적 낙관 (고점 신호)
   - <-30%: 극단적 약세 (저점 신호)
```

**CMFI 통합 공식**:

$$CMFI = 0.30 \cdot Score_{FGI} + 0.30 \cdot Score_{HY} + 0.20 \cdot Score_{PCR} + 0.20 \cdot Score_{\text{AAII}}$$

**계산 예시**:
```
현재 시장 상황:
- FGI: 45 (중립) → Score_FGI = 100 - 45 = 55점
- HY OAS: 520bps → Score_HY = 50 + 25 × (520-400)/120 = 75점
- PCR 10MA: 0.85 → Score_PCR = 70점
- AAII: +15% → Score_AAII = 50 + 1.25 × 15 = 68.75점

CMFI = 0.30×55 + 0.30×75 + 0.20×70 + 0.20×68.75
     = 16.5 + 22.5 + 14 + 13.75
     = 66.75 → 약 67점 (정상~약간 탐욕)
```

**CMFI 기반 Module 1 조정**:

```
CMFI ≥ 75 (극단적 공포):
- Regime Multiplier = 0.70 (MoS 감소)
- 의미: 시장 공포 극심 → 저평가 기회 → 공격적 매수
- RequiredMoS = 20% × 0.70 = 14%

35 ≤ CMFI < 75 (정상):
- Regime Multiplier = 1.00 (기본값)
- 의미: 시장 정상 → 기본 MoS 유지

CMFI < 35 (극단적 탐욕):
- Regime Multiplier = 1.30 (MoS 증가)
- 의미: 시장 과열 → 고평가 위험 → 방어적 태세
- RequiredMoS = 20% × 1.30 = 26%
```

---

## 📊 INTEGRATED OUTPUT MATRIX v10.1 (최종 보고서 템플릿)

**목적**: 25개 Hook + 5개 Module + 3-Philosopher를 **1장의 통합 보고서**로 정리

```
┌────────────────────────────────────────────────────────────────┐
│          v10.1 APEX INTEGRATED INVESTMENT MATRIX              │
│        Unified Investment Analysis Engine - Final Report       │
└────────────────────────────────────────────────────────────────┘

[Company Profile Section]
Ticker/Company: 005930.KS / Samsung Electronics
Industry: Semiconductors / Consumer Electronics
Current Price: 70,000원 | Market Cap: 1,750조원

════════════════════════════════════════════════════════════════

█ SECTION I: v8.0 FOUNDATION ANALYSIS (25 HOOKS + 3-PHILOSOPHER)

  ✓ 3-PHILOSOPHER CONSENSUS SCORES
    - Graham Defense: 70/100
    - Buffett Value: 100/100
    - Munger Quality: 100/100
    - CONSENSUS AGGREGATE: 90/100 ★★★★★
  
  ✓ HOOK FILTRATION STATUS (All 25 Mandatory)
    Hooks 1-10 (Base): 8/10 PASS ✓
    Hooks 11-14 (v6.0): 4/4 PASS ✓
    Hooks 21-25 (v8.0): 5/5 PASS ✓
  
  ✓ CORE METRICS (Hook 8-10 Priority)
    WACC (Hook 8): 11.4%
    CAP Decay (Hook 9, Year 10): 5.4년
    Owner Earnings (Hook 10): 34,551억원

════════════════════════════════════════════════════════════════

█ SECTION II: v10.0 ADAPTIVE MODULES (Opportunity Cost Elimination)

  ✓ MODULE 1: REGIME & LIFE-CYCLE ADAPTIVE MoS
    Base MoS Required: 30%
    Revenue Growth Rate: 12% (CAGR 3Y)
    Regime Multiplier: 1.0 (정상기)
    Adaptive MoS Required (v10): 28%
    Current MoS vs Adaptive: 7% (HOLD - 기준 미달)
  
  ✓ MODULE 2: SOROS REFLEXIVITY & CATALYST ENGINE
    Positive Catalyst Score: 68/100 (Allocation ×1.2)
    Negative Catalyst Score: -18 (규제 + 채무 증가)
    Adjusted Catalyst Score: 50/100
    Timeline: 6개월 내 3개 촉매 예상
  
  ✓ MODULE 3: VOLATILITY CLUSTERING & ATR STOP-LOSS
    Current VIX: 18.5
    20-Day Realized Volatility: 12%
    Volatility Regime: Normal
    Dynamic k-value: 1.5
    ATR₂₀: 3,500원
    Stop-Loss Price (v10): 65,750원
    Safety Status: ✓ Safe
  
  ✓ MODULE 4: MULTI-HORIZON PORTFOLIO BUCKETING
    Assigned Bucket: Core Compounder (50%)
    Bucket Qualification: Full Pass ✓
    Target Position: 30% 내 (Max)
    Current Position: 15%
    Rebalancing: Hold (기존 포지션 유지)
  
  ✓ MODULE 5: EXPERT MARKET FEAR & SENTIMENT (CMFI)
    CNN Fear & Greed: 45/100
    HY Credit Spread: 520bps
    Put/Call Ratio: 0.85
    AAII Bull-Bear: +15%
    CMFI Score: 67/100 (정상~약간 탐욕)
    Sentiment Regime: Normal
    Module 1 Multiplier Override: 1.0x (조정 없음)

════════════════════════════════════════════════════════════════

█ SECTION III: INTEGRATED DECISION & FINAL SIGNAL

  ✓ BASE ANALYSIS (v8.0)
    v8.0 Base Signal: STRONG BUY ★★★★★
    Consensus Propensity: 90.0%
    Base Intrinsic Value Range: 75,000원 ~ 95,000원
    Current Price: 70,000원 (4% 저평가)
  
  ✓ ADAPTIVE ADJUSTMENT (v10.0+)
    Module 1 Adaptive MoS Impact: ⚠ Failed (28% 미달성)
    Module 2 Catalyst Impact: Allocation ×1.0 (평탄화)
    Module 3 Stop-Loss Validation: ✓ Safe
    Module 4 Bucket Placement: Core 50% 적합 ✓
    Module 5 CMFI Override: No change (정상시장)
    v10.0 Adaptive Signal: MAINTAIN (조정 없음)
  
  ✓ NEGATIVE CATALYST ASSESSMENT
    경영권 분쟁: 없음 (0점)
    규제/소송: 경미 (-8점)
    기술 구식화: 없음 (0점)
    채무 급증: 중간 (-10점)
    거래처 집중: 없음 (0점)
    경영진 교체: 없음 (0점)
    Total Negative Impact: -18점 (경미)
  
  ✓ LOLLAPALOOZA OVERRIDE CHECK
    신호 1 (주식희석+매출부진): ✓ Not Triggered
    신호 2 (경영진옷로환): ✓ Not Triggered
    신호 3 (극고평가): ✓ Not Triggered
    신호 4 (가격인상불가): ✓ Not Triggered
    Lollapalooza Status: SAFE (오버라이드 없음)
  
  ✓ ANTI-HOOKS PENALTY CHECK
    금지표현 자동스캔: ✓ Clean (감점 없음)

════════════════════════════════════════════════════════════════

█ FINAL INTEGRATED RECOMMENDATION

  ┌─────────────────────────────────────────────────────────────┐
  │ OVERALL SIGNAL: BUY ★★★★☆                                  │
  │                                                              │
  │ Expected 1Y Return (Target Price): +18.6%                  │
  │ Target Price Range: 82,000원 ~ 88,000원                    │
  │                                                              │
  │ Downside Risk (99% VaR): -22.5%                            │
  │ Risk-Adjusted Return (Sharpe): 1.82                        │
  │                                                              │
  │ Confidence Level: 8/10                                      │
  │ Action Required: BUY on Dips (65,000원 이하)              │
  │ Holding Period: 3~5년 (Core 포지션)                       │
  │ Position Size: 포트폴리오의 15~30%                         │
  └─────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════

█ RISK WARNINGS & CONSIDERATIONS

  ⚠️ Key Downside Risks:
  1. Semiconductor Cyclicality (경기민감도 높음)
  2. China Market Risk (수출 의존도 ~30%)
  3. Technology Obsolescence (5nm/3nm 미지원 위험)
  4. Geopolitical (미-중 긴장 / 반도체 수출규제)
  
  ✓ Key Upside Catalysts (Next 6-12 months):
  1. AI Chip 수주 증가 (NVIDIA 관계사)
  2. Foundry 사업 개선 (고마진으로 전환)
  3. Galaxy S25 신제품 출시 (수익성 개선)

════════════════════════════════════════════════════════════════

█ METHODOLOGY SUMMARY

  - 25 Mandatory Hooks: Verified ✓
  - 3-Philosopher Consensus: 90점 ✓
  - 5 Adaptive Modules: Applied ✓
  - Negative Catalyst: -18점 (경미) ✓
  - Lollapalooza Override: Safe ✓
  - Final Signal: BUY (조건부) ✓

════════════════════════════════════════════════════════════════

Generated: 2026-07-29
Model: v10.1 APEX Unified System
Analyst: Claude Investment Engine
Confidence: 90/100

════════════════════════════════════════════════════════════════
```

---

## <thought_process>

### Part 3 검증 완료:

1. **Adaptive Modules 1-5**:
   - Module 1 Adaptive MoS: 성장률+시장사이클 기반 동적조정 ✓
   - Module 2 Catalyst: 긍정/부정적 촉매 통합 ✓
   - Module 3 ATR Stop-Loss: 변동성 기반 동적 손절 ✓
   - Module 4 Bucketing: Core/Growth/Tactical 3분산 ✓
   - Module 5 CMFI: 4개 전문가 지표 시장공포 정량화 ✓

2. **Integrated Output Matrix v10.1**:
   - 25개 Hook 결과 통합 ✓
   - 5개 Module 조정 반영 ✓
   - 3-Philosopher 합의 반영 ✓
   - 부정적 신호 차감 ✓
   - 최종 Signal 생성 ✓

3. **최종 Investment Signal**:
   - BUY (조건부: 저평가 구간)
   - 목표가: 82,000~88,000원
   - 보유기간: 3~5년 (Core 포지션)
   - 위험도: 8/10 신뢰도

### Part 3 완료 = 전체 v10.1 APEX 시스템 완성 ✅

</thought_process>

---

## 📌 Part 3 완료 사항

- [x] Adaptive Module 1-5 완전 설명 + 계산식
- [x] Negative Catalyst System (부정적 신호 감점)
- [x] Integrated Output Matrix v10.1 (최종 보고서 템플릿)
- [x] Investment Signal 생성 로직 (BUY/HOLD/SELL)
- [x] Risk Warning 및 Catalyst 분석

---

## ✅ 전체 v10.1 APEX 시스템 완성!

**총 6개 파일, 약 35,000단어**

| Part | 파일 | 내용 | 상태 |
|------|------|------|------|
| 1 | hook_1.md | Base Layer & Priority (1-10) | ✅ |
| 1 | skill_1.md | Execution Rules (1-10) | ✅ |
| 2 | hook_2.md | Advanced & Apex (11-25) + 3-Philosopher | ✅ |
| 2 | skill_2.md | Advanced Execution (11-25) | ✅ |
| 3 | hook_3.md | Adaptive Modules 1-5 + Output Matrix | ✅ |
| 3 | skill_3.md | Adaptive Execution + Final Signal | 🔜 |

---

**지금부터 skill_3.md를 작성하겠습니다** (최종 실행 가이드)