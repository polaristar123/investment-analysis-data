# 🎯 Unified Investment Analysis Engine v10.1 (Part 3/3 Final)
## Adaptive Modules 1-5 Execution + Negative Catalyst + Final Signal
### Skill Module 3: 자동 계산기 + 최종 판정 로직 + Output 생성

**버전**: v10.1 APEX Modular Standard  
**모듈**: Part 3/3 - Skill (최종 실행 & 신호 생성)  
**목적**: Adaptive Module 1-5 자동 계산 + 부정적 신호 차감 + 최종 투자 판정

---

## 🔄 ADAPTIVE MODULE EXECUTION PIPELINE (Part 3)

### Phase 1: Module 1 Calculation (2~3분)

#### Regime & Life-Cycle Adaptive MoS 자동 계산

```python
# 입력
Base_MoS = float(input("Base MoS Required (%) : "))  # 예: 30
Revenue_Growth_3Y_CAGR = float(input("3Y Revenue CAGR (%) : "))  # 예: 12
Current_VIX = float(input("Current VIX : "))  # 예: 18.5
Rate_Environment = input("금리 환경 (Rising/Neutral/Falling) : ")  # 예: Neutral

# Step 1: 성장률 기반 MoS 조정
Growth_Adjustment = 1 - math.log(1 + Revenue_Growth_3Y_CAGR/100)

# Step 2: 시장 사이클 Regime Multiplier
if Current_VIX < 20 and Rate_Environment == "Neutral":
    Regime_Multiplier = 1.0
elif Current_VIX >= 20 or Rate_Environment == "Rising":
    Regime_Multiplier = 1.3  # 보수적
elif Current_VIX < 15 or Rate_Environment == "Falling":
    Regime_Multiplier = 0.7  # 공격적

# Step 3: 최종 Adaptive MoS
Adaptive_MoS = Base_MoS * Growth_Adjustment * Regime_Multiplier

# Step 4: 판정
Current_Price = float(input("Current Price : "))
Intrinsic_Value = float(input("Intrinsic Value Base : "))
Current_MoS = (Intrinsic_Value - Current_Price) / Intrinsic_Value * 100

Signal_1 = "BUY" if Current_MoS >= Adaptive_MoS else "HOLD"

print(f"Base MoS: {Base_MoS}%")
print(f"Growth Adjustment: {Growth_Adjustment:.3f}")
print(f"Regime Multiplier: {Regime_Multiplier:.2f}")
print(f"Adaptive MoS Required (v10): {Adaptive_MoS:.1f}%")
print(f"Current MoS: {Current_MoS:.1f}%")
print(f"Module 1 Signal: {Signal_1}")
```

**체크리스트**:
```
□ Base MoS 입력: ___ %
□ 3Y Revenue CAGR: ___ %
□ Growth Adjustment 계산: ___
□ 시장 사이클 Regime Multiplier: ___
□ Adaptive MoS 최종: ___ %
□ Module 1 Signal (BUY/HOLD/AVOID): ___ ✓
```

---

### Phase 2: Module 2 Calculation (3~4분)

#### Catalyst Engine + Negative Catalyst 통합

```python
# ========== POSITIVE CATALYST ==========
Catalyst_1 = float(input("신제품/기술 (0~25) : "))  # 예: 15
Catalyst_2 = float(input("M&A 커버리지 (0~20) : "))  # 예: 12
Catalyst_3 = float(input("자사주 매입 (0~20) : "))  # 예: 18
Catalyst_4 = float(input("포트폴리오 개선 (0~15) : "))  # 예: 10
Catalyst_5 = float(input("신사업 (0~10) : "))  # 예: 8
Catalyst_6 = float(input("거버넌스/공시 (0~10) : "))  # 예: 5

Positive_Catalyst_Score = Catalyst_1 + Catalyst_2 + Catalyst_3 + Catalyst_4 + Catalyst_5 + Catalyst_6

# ========== NEGATIVE CATALYST (NEW SYSTEM) ==========
Negative_1 = float(input("경영권 분쟁 유무 (0 or -30) : "))  # 예: 0
Negative_2 = float(input("규제/소송 심각도 (0~-20) : "))  # 예: -8
Negative_3 = float(input("기술 구식화 위험 (0~-25) : "))  # 예: 0
Negative_4 = float(input("채무 급증 (0~-30) : "))  # 예: -10
Negative_5 = float(input("거래처 집중 위험 (0~-15) : "))  # 예: 0
Negative_6 = float(input("경영진 변동 리스크 (0~-20) : "))  # 예: 0

Negative_Catalyst_Score = Negative_1 + Negative_2 + Negative_3 + Negative_4 + Negative_5 + Negative_6

# ========== ADJUSTED CATALYST SCORE ==========
Adjusted_Catalyst_Score = max(0, Positive_Catalyst_Score + Negative_Catalyst_Score)

# ========== ALLOCATION MULTIPLIER ==========
if Adjusted_Catalyst_Score >= 80:
    Allocation_Multiplier = 1.3
elif Adjusted_Catalyst_Score >= 60:
    Allocation_Multiplier = 1.2
else:
    Allocation_Multiplier = 1.0

Signal_2 = f"Position Multiplier: ×{Allocation_Multiplier}"

print(f"Positive Catalyst Score: {Positive_Catalyst_Score}/100")
print(f"Negative Catalyst Score: {Negative_Catalyst_Score}")
print(f"Adjusted Catalyst Score: {Adjusted_Catalyst_Score}/100")
print(f"Module 2 Signal: {Signal_2}")
```

**체크리스트**:
```
□ 긍정적 촉매 6개 입력 (총점):
  - 신제품: ___ | 커버리지: ___ | 자사주: ___ 
  - 포트폴리오: ___ | 신사업: ___ | 거버넌스: ___
  - 합계: ___ /100

□ 부정적 촉매 6개 입력 (총점):
  - 경영권: ___ | 규제: ___ | 기술: ___
  - 채무: ___ | 거래처: ___ | 경영진: ___
  - 합계: ___ (음수)

□ 조정된 Catalyst Score: ___ /100
□ Allocation Multiplier: ×___ ✓
```

---

### Phase 3: Module 3 Calculation (2분)

#### Dynamic ATR Stop-Loss 계산

```python
# 입력
Current_Price = float(input("Current Price : "))
Realized_Volatility_20d = float(input("20-Day Realized Volatility (%) : "))
ATR_20 = float(input("ATR 20일 (일절값) : "))

# 변동성 레짐 결정
if Realized_Volatility_20d <= 15:
    k_value = 1.5
elif Realized_Volatility_20d <= 25:
    k_value = 2.0
else:
    k_value = 2.5

# Fallback Logic (ATR 미제공 시)
if ATR_20 == 0:
    ATR_20_approx = Current_Price * (Realized_Volatility_20d / 100 / math.sqrt(252))
    ATR_20 = ATR_20_approx
    print(f"ATR Approximated (Fallback): {ATR_20:.0f}")

# Stop-Loss 계산
Stop_Loss_Price = Current_Price - (k_value * ATR_20)

# 안전성 판정
if Current_Price > Stop_Loss_Price * 1.05:  # 5% 이상 마진
    Safety_Status = "✓ Safe"
else:
    Safety_Status = "⚠ At Risk"

print(f"Realized Volatility (20d): {Realized_Volatility_20d}%")
print(f"k-value (Volatility Regime): {k_value}")
print(f"ATR₂₀: {ATR_20:.0f}")
print(f"Stop-Loss Price: {Stop_Loss_Price:.0f}원")
print(f"Module 3 Signal: {Safety_Status}")
```

**체크리스트**:
```
□ 현재주가: ___ 원
□ 20일 변동성: ___ %
□ ATR 20: ___ 원 (또는 0 for Fallback)
□ 변동성 레짐: Normal / High / Extreme
□ k-value: ___
□ Stop-Loss Price: ___ 원 ✓
□ 안전도 판정: Safe / At Risk
```

---

### Phase 4: Module 4 Calculation (2분)

#### Portfolio Bucketing 배분 결정

```python
# 입력
Consensus_Score = float(input("Part 2 Consensus Score (100점 만점) : "))
Revenue_Growth = float(input("Revenue Growth (%) : "))
Downside_Risk = float(input("Downside Risk - 99% VaR (%) : "))
Portfolio_Value = float(input("Total Portfolio Value (원) : "))

# Step 1: 버킷 분류
if Consensus_Score > 80 and Revenue_Growth < 15:
    Assigned_Bucket = "Core Compounder"
    Max_Position_Pct = 30
    Bucket_Allocation_Pct = 50
elif Consensus_Score > 60 and Revenue_Growth >= 30:
    Assigned_Bucket = "High-Beta Growth"
    Max_Position_Pct = 15
    Bucket_Allocation_Pct = 30
elif Consensus_Score >= 50 and Downside_Risk <= 25:
    Assigned_Bucket = "Event-Driven Tactical"
    Max_Position_Pct = 5
    Bucket_Allocation_Pct = 20
else:
    Assigned_Bucket = "Not Qualified"
    Max_Position_Pct = 0
    Bucket_Allocation_Pct = 0

# Step 2: 포지션 크기 계산
if Assigned_Bucket != "Not Qualified":
    Bucket_Budget = Portfolio_Value * (Bucket_Allocation_Pct / 100)
    Max_Position_Size = Bucket_Budget * (Max_Position_Pct / 100)
    Recommendation = f"{Max_Position_Size:,.0f}원 이내"
else:
    Recommendation = "불적격 (투자 제외)"

print(f"Assigned Bucket: {Assigned_Bucket}")
print(f"Max Position %%: {Max_Position_Pct}%")
print(f"Bucket Budget: {Bucket_Budget:,.0f}원")
print(f"Max Position Size: {Recommendation}")
print(f"Module 4 Signal: {Assigned_Bucket}")
```

**체크리스트**:
```
□ Consensus Score: ___ /100
□ Revenue Growth: ___ %
□ Downside Risk: ___ %
□ Portfolio Value: ___ 원

□ 버킷 분류:
  - Core Compounder (50% 배분) / 
  - High-Beta Growth (30% 배분) / 
  - Tactical (20% 배분) / 
  - Not Qualified

□ Max Position Size: ___ 원 ✓
```

---

### Phase 5: Module 5 Calculation (2분)

#### CMFI Market Fear Index 계산

```python
# 입력
FGI_Index = float(input("CNN Fear & Greed Index (0~100) : "))  # 예: 45
HY_OAS_bps = float(input("HY OAS (bps) : "))  # 예: 520
PCR_10MA = float(input("Put/Call Ratio 10MA : "))  # 예: 0.85
AAII_Spread = float(input("AAII Bull-Bear Spread (%) : "))  # 예: 15

# Step 1: 각 지표 정규화
Score_FGI = 100 - FGI_Index  # 역순 (공포↑ = 점수↑)

# HY OAS (400bps 기준)
Z_HY = (HY_OAS_bps - 400) / 120
Score_HY = min(100, max(0, 50 + 25 * Z_HY))

# PCR (0.45~1.00 범위)
if PCR_10MA >= 1.00:
    Score_PCR = 100
elif PCR_10MA <= 0.45:
    Score_PCR = 0
else:
    Score_PCR = (PCR_10MA - 0.45) / (1.00 - 0.45) * 100

# AAII (±30% 범위)
Score_AAII = min(100, max(0, 50 - 1.25 * AAII_Spread))

# Step 2: CMFI 통합
CMFI = 0.30*Score_FGI + 0.30*Score_HY + 0.20*Score_PCR + 0.20*Score_AAII

# Step 3: 레짐 판정
if CMFI >= 75:
    Regime = "Extreme Fear"
    Regime_Multiplier = 0.70
elif CMFI >= 35:
    Regime = "Normal"
    Regime_Multiplier = 1.00
else:
    Regime = "Extreme Greed"
    Regime_Multiplier = 1.30

print(f"Score_FGI: {Score_FGI:.0f}")
print(f"Score_HY: {Score_HY:.0f}")
print(f"Score_PCR: {Score_PCR:.0f}")
print(f"Score_AAII: {Score_AAII:.0f}")
print(f"\nCMFI (Composite): {CMFI:.0f}/100")
print(f"Sentiment Regime: {Regime}")
print(f"Module 1 Multiplier Override: {Regime_Multiplier}x")
print(f"Module 5 Signal: {Regime}")
```

**체크리스트**:
```
□ CNN FGI: ___ /100
□ HY OAS: ___ bps
□ Put/Call Ratio: ___
□ AAII Spread: ___ %

□ 각 지표 정규화:
  - Score_FGI: ___ 
  - Score_HY: ___
  - Score_PCR: ___
  - Score_AAII: ___

□ CMFI 최종: ___ /100
□ Sentiment Regime: Extreme Fear / Normal / Extreme Greed
□ Module 1 Override: ×___ ✓
```

---

## 🎯 FINAL INTEGRATED SIGNAL GENERATION

### Investment Signal 판정 알고리즘

```python
# ========== 5개 Module Signal 통합 ==========
Module_1_Signal = "BUY" if Current_MoS >= Adaptive_MoS else "HOLD"
Module_2_Signal = f"×{Allocation_Multiplier}"
Module_3_Signal = "Safe" if Stop_Loss_Price < Current_Price else "At Risk"
Module_4_Signal = Assigned_Bucket
Module_5_Signal = Regime  # Extreme Fear / Normal / Extreme Greed

# ========== NEGATIVE CATALYST 차감 ==========
Base_Consensus_Score = 90  # Part 2에서 산출
Negative_Catalyst_Penalty = abs(Negative_Catalyst_Score)  # -18 → 18점 차감
Adjusted_Consensus = Base_Consensus_Score - Negative_Catalyst_Penalty

print(f"Base Consensus (v8.0): {Base_Consensus_Score}점")
print(f"Negative Catalyst Penalty: -{Negative_Catalyst_Penalty}점")
print(f"Adjusted Consensus (v10.1): {Adjusted_Consensus}점")

# ========== LOLLAPALOOZA CHECK ==========
Lollapalooza_Triggered = (
    (SDI > 1.0 and Revenue_Growth < 0) and
    (CEO_Option_3yr > 3 and Self_Stock_Buyback == 0) and
    (PER > 50 and Revenue_Growth < 10) and
    (PPI < 0.5 for 2 years)
)

if Lollapalooza_Triggered:
    Final_Signal = "CRITICAL_AVOID"
    Final_Score = 0
else:
    # ========== FINAL SIGNAL GENERATION ==========
    if Adjusted_Consensus > 80:
        if Module_1_Signal == "BUY" and Module_3_Signal == "Safe":
            Final_Signal = "STRONG BUY"
            Final_Score = 95
        else:
            Final_Signal = "BUY"
            Final_Score = 80
    elif Adjusted_Consensus > 60:
        Final_Signal = "BUY"
        Final_Score = 70
    elif Adjusted_Consensus > 40:
        Final_Signal = "HOLD"
        Final_Score = 50
    else:
        Final_Signal = "AVOID"
        Final_Score = 20

# ========== TARGET PRICE & POSITION SIZE ==========
Intrinsic_Value_Low = Intrinsic_Value * 0.75   # Bear
Intrinsic_Value_High = Intrinsic_Value * 1.25  # Bull
Target_Price_Mean = Intrinsic_Value

Expected_Return = (Target_Price_Mean - Current_Price) / Current_Price * 100
Downside_Risk_VaR = -abs(Downside_Risk)

# Risk-Adjusted Return (Sharpe Ratio)
Risk_Free_Rate = 3.5  # %
Sharpe_Ratio = (Expected_Return - Risk_Free_Rate) / abs(Downside_Risk_VaR)

# Position Size 제한
if Final_Signal == "STRONG BUY":
    Position_Size_Limit = Max_Position_Size * 1.2  # 120%
elif Final_Signal == "BUY":
    Position_Size_Limit = Max_Position_Size
elif Final_Signal == "HOLD":
    Position_Size_Limit = Max_Position_Size * 0.5  # 50%
else:
    Position_Size_Limit = 0

print(f"\n{'='*60}")
print(f"FINAL INVESTMENT DECISION (v10.1 APEX)")
print(f"{'='*60}")
print(f"Overall Signal: {Final_Signal}")
print(f"Confidence Score: {Adjusted_Consensus}/100")
print(f"\nPrice Target: {Target_Price_Mean:,.0f}원")
print(f"Target Range: {Intrinsic_Value_Low:,.0f} ~ {Intrinsic_Value_High:,.0f}원")
print(f"Expected 1Y Return: {Expected_Return:+.1f}%")
print(f"Downside Risk (99% VaR): {Downside_Risk_VaR:.1f}%")
print(f"Sharpe Ratio: {Sharpe_Ratio:.2f}")
print(f"\nPosition Size: {Position_Size_Limit:,.0f}원")
print(f"Holding Period: {'3-5년 (Core)' if Module_4_Signal == 'Core' else '1-3년' if Module_4_Signal == 'Growth' else '6-12개월'}")
print(f"Stop-Loss: {Stop_Loss_Price:,.0f}원")
print(f"{'='*60}")
```

---

## ✅ PART 3 FINAL VALIDATION CHECKLIST

```
Phase 1: Module 1-5 Complete
□ Module 1 Adaptive MoS: ___ %
□ Module 2 Catalyst Score & Multiplier: ___
□ Module 3 ATR Stop-Loss: ___ 원
□ Module 4 Bucket Assignment: ___
□ Module 5 CMFI & Regime: ___

Phase 2: Negative Catalyst Assessment Complete
□ 6개 부정적 신호 입력 완료
□ Adjusted Consensus: ___ /100 (차감 후)
□ Lollapalooza Check: Safe / Triggered

Phase 3: Final Signal Generation Complete
□ Overall Signal: STRONG BUY / BUY / HOLD / AVOID
□ Target Price: ___ 원
□ Expected Return: ___ %
□ Position Size Limit: ___ 원 ✓

FINAL STATUS: ✅ v10.1 APEX COMPLETE
```

---

## 📊 COMPLETE SYSTEM FLOW (Part 1 → 3)

```
사용자 입력 (재무 데이터)
        ↓
Part 1: Sector Routing → Priority Hooks 8-10 → Foundation Hooks 1-7
        ↓
Part 2: Advanced Hooks 11-14 → Apex Hooks 21-25 → 3-Philosopher Consensus
        ↓
Part 3: Adaptive Modules 1-5 → Negative Catalyst → Final Signal
        ↓
OUTPUT: Integrated Investment Matrix v10.1
        ↓
최종 투자 판정 (BUY/HOLD/AVOID) + 목표가 + 포지션 크기
```

---

## 🎊 v10.1 APEX UNIFIED SYSTEM COMPLETE!

**✅ 모든 3 Part 완료 (6개 파일)**:
- Part 1: Base Layer & Priority Hooks
- Part 2: Advanced & Institutional Apex + 3-Philosopher
- Part 3: Adaptive Modules + Output Matrix

**✅ 총 역할 수**:
- 25개 Hook ✓
- 5개 Adaptive Module ✓
- 3-Philosopher Consensus ✓
- Negative Catalyst System ✓
- Lollapalooza Override ✓
- Final Signal Generation ✓

---

**작성 완료**: 2026-07-29  
**버전**: v10.1 APEX Modular Standard (완성)  
**총 문서**: 6개 마크다운 파일 (~35,000 단어)  
**상태**: ✅ PRODUCTION READY
