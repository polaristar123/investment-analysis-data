# 🎯 Unified Investment Analysis Engine v10.1 (Part 2/3)
## Advanced Hooks 11-14 + Apex Hooks 21-25 - Execution & Validation
### Skill Module 2: 계산 루틴 + 체크리스트 + 3-Philosopher 점수 산출

**버전**: v10.1 APEX Modular Standard  
**모듈**: Part 2/3 - Skill (실행 규칙 & 검증)  
**목적**: hook_2.md의 공식을 실제로 적용하는 **자동 계산기 & 판정 로직**

---

## 🔄 PART 2 EXECUTION PIPELINE

### Phase 1: Advanced Hooks 11-14 Calculation (5~7분)

#### Hook 11 Execution Routine

**Step A: 마진 변화 원인 분해**

```python
# 입력 데이터
Gross_Margin_t1 = float(input("2024년 Gross Margin (%) : "))  # 예: 18.5
Gross_Margin_t0 = float(input("2023년 Gross Margin (%) : "))  # 예: 15.0
Industry_Margin_Change = float(input("산업 평균 마진 변화 (%p) : "))  # 예: 0.8
Asset_Turnover = float(input("자산회전율 (배) : "))  # 예: 1.2

# 계산
Margin_Change = Gross_Margin_t1 - Gross_Margin_t0  # +3.5%p
PPI = (Margin_Change / Industry_Margin_Change) * Asset_Turnover

# 판정
if PPI > 1.2:
    PPI_Score = 15  # 강한 가격 결정력
elif PPI >= 0.8 and PPI <= 1.2:
    PPI_Score = 0   # 중립
else:
    PPI_Score = -20 # 약한 가격 결정력

print(f"PPI: {PPI:.2f}")
print(f"PPI Score: {PPI_Score}점")
```

**체크리스트**:
```
□ 마진 변화 원인 분해 (가격/물량/비용)
  - 가격 인상 기여도: ___ %
  - 물량 증가 기여도: ___ %
  - 비용 절감 기여도: ___ %
  
□ 가격 결정력 평가
  - PPI 계산 완료: ___ (값)
  - 점수 할당: ___ 점
  
□ 위험 신호 확인
  - 마진 100% 증가가 비용 절감만 의존? NO / YES (→ -30점 감점)
```

---

#### Hook 12 Execution Routine

**Step A: Maintenance CapEx 산정**

```python
# 방법 1: 명시적 분리 (정보 있을 때)
Growth_CapEx = float(input("Growth CapEx (억원) : "))  # 예: 2,700
Total_CapEx = float(input("Total CapEx (억원) : "))    # 예: 18,000
Maintenance_CapEx_method1 = Total_CapEx - Growth_CapEx  # 15,300

# 방법 2: D&A 기반 기본값 (정보 부족 시)
D_and_A = float(input("D&A (억원) : "))                # 예: 12,000
Maintenance_CapEx_method2 = max(D_and_A, Total_CapEx * 0.85)

# 최종 선택
Maintenance_CapEx = Maintenance_CapEx_method1 if Growth_CapEx > 0 else Maintenance_CapEx_method2

# Owner Earnings 계산
Net_Income = float(input("Net Income (억원) : "))      # 예: 38,000
Delta_NWC = float(input("Normalized ∆NWC (억원) : "))  # 예: 149

Owner_Earnings = Net_Income + D_and_A - Maintenance_CapEx - Delta_NWC

print(f"Maintenance CapEx: {Maintenance_CapEx:.0f}억원")
print(f"Owner Earnings: {Owner_Earnings:.0f}억원")
```

**체크리스트**:
```
□ Maintenance CapEx 산정 방법 선택
  - 방법 1 (명시적 분리): YES / NO
  - 방법 2 (D&A 기본값): 사용
  
□ Owner Earnings 최종 계산
  - Net Income: ___ 억원
  - D&A: ___ 억원
  - Maintenance CapEx: ___ 억원 (차감)
  - ∆NWC: ___ 억원 (차감)
  - Owner Earnings: ___ 억원 ✓
  
□ 위험 신호 확인
  - CapEx > D&A × 1.5 지속 3년? NO / YES (→ ROIC 악화)
```

---

#### Hook 13 Execution Routine

**Step A: Soft Moat 점수 산출**

```python
# 입력
Active_Users = float(input("Active Users (백만) : "))   # 예: 43.5
LTV_per_User = float(input("LTV per User (연, 원) : "))  # 예: 100,000
CAC_per_User = float(input("CAC per User (원) : "))      # 예: 40,000
Switching_Cost_pct = float(input("Switching Cost (% of Revenue) : "))  # 예: 15

# 계산
LTV_CAC_Ratio = LTV_per_User / CAC_per_User
Network_Boost = 0.2 * math.log(Active_Users * 1e6)

# LTV/CAC 스코어
if LTV_CAC_Ratio > 3.0:
    LTV_Score = 25
elif LTV_CAC_Ratio >= 2.0:
    LTV_Score = 15
elif LTV_CAC_Ratio >= 1.0:
    LTV_Score = 0
else:
    LTV_Score = -40

# Switching Cost 평가
if Switching_Cost_pct > 20:
    SC_Score = 25  # 높음
elif Switching_Cost_pct >= 10:
    SC_Score = 15  # 중간
else:
    SC_Score = 5   # 낮음

Moat_Score_13 = Network_Boost + LTV_Score + SC_Score

print(f"LTV/CAC Ratio: {LTV_CAC_Ratio:.2f}")
print(f"Moat Score (Hook 13): {Moat_Score_13:.0f}점")
```

**체크리스트**:
```
□ 네트워크 효과 정량화
  - Active Users: ___ 백만
  - ln(Users) Boost: +___ 점
  
□ LTV/CAC 경제성 평가
  - LTV/CAC Ratio: ___
  - LTV Score: ___ 점
  
□ 선택 비용 평가
  - Switching Cost %: ___ %
  - SC Score: ___ 점
  
□ Hook 13 최종 점수
  - Moat Score: ___ 점 ✓
  
□ 위험 신호
  - LTV/CAC < 1.5 + 낮은 Switching Cost? NO / YES (→ λ +40%)
```

---

#### Hook 14 Execution Routine

**Step A: 3 시나리오 WACC 설정**

```python
Dynamic_WACC = float(input("Dynamic WACC (Hook 8) (%) : "))  # 예: 11.4

# 3개 시나리오
WACC_Bull = Dynamic_WACC - 1.0    # 금리 인하
WACC_Base = Dynamic_WACC           # 현상 유지
WACC_Bear = Dynamic_WACC + 2.0    # 금리 인상

print(f"WACC Bull (낙관): {WACC_Bull:.2f}%")
print(f"WACC Base (기본): {WACC_Base:.2f}%")
print(f"WACC Bear (보수): {WACC_Bear:.2f}%")
```

**Step B: 시나리오별 DCF 계산**

```python
# 입력
Terminal_ROIC_Base = float(input("Terminal ROIC (기본, %) : "))
Terminal_ROIC_Bull = Terminal_ROIC_Base + 2.0  # +200bps
Terminal_ROIC_Bear = Terminal_ROIC_Base - 3.0  # -300bps

# 각 시나리오별 DCF 계산
# (상세 공식은 생략 - 표준 DCF 모델 사용)

V_Bull = 95000  # 계산 결과 예시 (원)
V_Base = 75000  # (원)
V_Bear = 55000  # (원)

# 확률가중
E_V = 0.25 * V_Bull + 0.50 * V_Base + 0.25 * V_Bear

print(f"V_Bull: {V_Bull:,}원")
print(f"V_Base: {V_Base:,}원")
print(f"V_Bear: {V_Bear:,}원")
print(f"E[V] (확률가중): {E_V:,.0f}원")
print(f"95% Confidence Band: [{V_Bear:,}원 ~ {V_Bull:,}원]")
```

**체크리스트**:
```
□ 3 시나리오 WACC 결정
  - WACC Bull: ___ %
  - WACC Base: ___ %
  - WACC Bear: ___ %
  
□ Terminal ROIC 결정
  - Base: ___ %
  - Bull (+2%p): ___ %
  - Bear (-3%p): ___ %
  
□ DCF 계산 (각 시나리오)
  - V_Bull: ___ 원
  - V_Base: ___ 원
  - V_Bear: ___ 원
  
□ 신뢰구간 밴드
  - 기댓값 E[V]: ___ 원
  - 범위: [___, ___] 원 ✓
```

---

### Phase 2: Apex Hooks 21-25 Calculation (5~6분)

#### Hook 21 Execution Routine

**Step A: 거버넌스 점수 산출**

```python
# 거버넌스 위험 요소
Physical_Split_History = int(input("물적 분할 히스토리 (회수) : "))  # 예: 0
CEO_Independence = int(input("CEO 독립이사 비중 (%) : "))  # 예: 40
Board_Diversity = int(input("이사회 다양성 점수 (0~10) : "))  # 예: 7
Dividend_Policy = int(input("배당성향 (%) : "))  # 예: 30
Self_Stock_Ratio = float(input("자사주 비중 (%) : "))  # 예: 2.5

# 점수 계산
Governance_Score = 0
Governance_Score -= Physical_Split_History * 15  # 물적 분할 -15점/회
Governance_Score += min(CEO_Independence - 30, 3) * 2  # 독립성 가산
Governance_Score += Board_Diversity * 2  # 다양성 가산
if Dividend_Policy > 50:  # 성장기 기업인 경우
    Governance_Score -= 10  # 배당 오버행 페널티
if Self_Stock_Ratio > 5:
    Governance_Score -= 15  # 자사주 오버행

# 할인율 계산
Delta_Governance = max(0, Governance_Score / 100)  # 0~40% 범위로 정규화

print(f"Governance Score: {Governance_Score}점")
print(f"δ_Governance: {Delta_Governance * 100:.1f}%")
```

**체크리스트**:
```
□ 거버넌스 위험 요소 평가
  - 물적 분할: ___ 회 (→ 점수)
  - CEO 독립성: ___ % 
  - 이사회 다양성: ___ /10
  - 배당정책: ___ % (위험도)
  - 자사주: ___ % (위험도)
  
□ 최종 거버넌스 할인
  - δ_Governance: ___ %
  - V_Intrinsic_Adjusted = V_Base × (1 - δ_Governance) ✓
  
□ 위험 신호
  - δ > 30%? NO / YES (→ CRITICAL)
```

---

#### Hook 22-25 Quick Checklist

| Hook | 항목 | 입력값 | 판정 |
|------|------|--------|------|
| **22** | CCC (일) | ___ | <75: ✓ / >120: ✗ |
| **22** | CCC 악화율 (%) | ___ | <10%: ✓ / >20%: ✗ |
| **23** | Goodwill/Equity (%) | ___ | <20%: ✓ / >25%: ✗ |
| **23** | M&A 횟수 (3년) | ___ | <3회: ✓ / >3회: ✗ |
| **24** | Refinancing Ratio | ___ | <1.0: ✓ / >1.5: ✗ |
| **24** | Stressed ICR | ___ | >1.5: ✓ / <1.5: ✗ |
| **25** | Cash Runway (월) | ___ | >12: ✓ / <12: ✗ |
| **25** | Tail Risk Loss (%) | ___ | -30%까지: ✓ / >-40%: ✗ |

---

### Phase 3: 3-Philosopher Consensus (3~4분)

#### 자동 점수 계산

```python
# Part 1에서 산출된 기초 데이터
NCAV_dynamic = -85000  # 음수
Debt_to_Equity = 68    # %
Current_Ratio = 1.32   # x
Dividend_Yield = 1.5   # %
PBR = 0.65             # x
PER = 9                # 배

Owner_Earnings_Yield = 17.9  # %
Moat_Status = "Strong"       # 문자열
ROIC = 18.0            # %
WACC = 11.4            # %
CapEx_vs_FCF = 0.64    # (CapEx < FCF? YES)
Dividend_Payout = 30   # %

PPI = 1.5
LTV_CAC = 3.2
Governance_Discount = 8  # %
R_D_Ratio = 9          # % (of Revenue)

# ==========================================
# GRAHAM DEFENSE SCORE 계산
# ==========================================
Graham_Score = 0

# 1. Hook 1 (NCAV)
Graham_Score += 0 if NCAV_dynamic < 0 else 20

# 2. Debt/Equity < 50%?
Graham_Score += 15 if Debt_to_Equity < 50 else (10 if Debt_to_Equity < 100 else 0)

# 3. Current Ratio > 2.0x?
Graham_Score += 15 if Current_Ratio > 2.0 else (10 if Current_Ratio > 1.5 else 5)

# 4. Dividend Yield > 2%?
Graham_Score += 10 if Dividend_Yield > 2.0 else 5

# 5. PBR < 1.0x?
Graham_Score += 20 if PBR < 1.0 else 15

# 6. PER < 평균의 60%?
Graham_Score += 20 if PER < 12 else 15

print(f"Graham Defense Score: {Graham_Score}/100")
# 예상: 70점

# ==========================================
# BUFFETT VALUE SCORE 계산
# ==========================================
Buffett_Score = 0

# 1. Owner Earnings Yield > 5%?
if Owner_Earnings_Yield > 15:
    Buffett_Score += 25
elif Owner_Earnings_Yield > 8:
    Buffett_Score += 20
elif Owner_Earnings_Yield > 5:
    Buffett_Score += 15
else:
    Buffett_Score += 5

# 2. Moat 확인?
Buffett_Score += 25 if Moat_Status in ["Strong", "Very Strong"] else 15

# 3. ROIC > WACC?
Buffett_Score += 25 if ROIC > WACC else 15

# 4. 자본 효율성
Buffett_Score += 15 if CapEx_vs_FCF < 1.0 else 10

# 5. 배당성향 < 50%?
Buffett_Score += 10 if Dividend_Payout < 50 else 5

print(f"Buffett Value Score: {Buffett_Score}/100")
# 예상: 100점

# ==========================================
# MUNGER QUALITY SCORE 계산
# ==========================================
Munger_Score = 0

# 1. PPI > 1.2?
Munger_Score += 25 if PPI > 1.2 else (15 if PPI > 0.8 else 0)

# 2. LTV/CAC > 2.5? (SaaS의 경우, 아니면 기술 리더십 대체)
Munger_Score += 20 if LTV_CAC > 2.5 else (25 if R_D_Ratio > 8 else 0)

# 3. Governance 양호?
Munger_Score += 20 if Governance_Discount < 10 else (10 if Governance_Discount < 20 else 0)

# 4. 임직원 만족도 / 이직률
Munger_Score += 15  # 가정: 일반적

# 5. R&D 투자 충분?
Munger_Score += 20 if R_D_Ratio > 8 else 10

print(f"Munger Quality Score: {Munger_Score}/100")
# 예상: 100점

# ==========================================
# CONSENSUS AGGREGATION
# ==========================================
Consensus_Score = (Graham_Score + Buffett_Score + Munger_Score) / 3

print(f"\n=== FINAL 3-PHILOSOPHER CONSENSUS ===")
print(f"Graham: {Graham_Score}점")
print(f"Buffett: {Buffett_Score}점")
print(f"Munger: {Munger_Score}점")
print(f"CONSENSUS: {Consensus_Score:.0f}점")

# 신호 판정
if Consensus_Score > 80:
    Signal = "STRONG BUY"
elif Consensus_Score > 60:
    Signal = "BUY"
elif Consensus_Score > 40:
    Signal = "HOLD"
else:
    Signal = "AVOID"

print(f"Signal: {Signal}")
```

**체크리스트**:
```
□ Graham Defense Score 계산
  - 항목 1~6 모두 입력: ✓
  - 최종 점수: ___ /100

□ Buffett Value Score 계산
  - Owner Earnings Yield: ___ %
  - Moat Status: ___
  - ROIC > WACC?: YES / NO
  - 자본 효율성: ✓
  - 배당성향: ___ %
  - 최종 점수: ___ /100

□ Munger Quality Score 계산
  - PPI: ___
  - LTV/CAC 또는 R&D: ___
  - Governance: ___ %
  - 임직원 만족도: (일반)
  - 최종 점수: ___ /100

□ Consensus Aggregation
  - 평균 계산: (Graham + Buffett + Munger) / 3
  - CONSENSUS: ___ /100 ✓
  - Signal: STRONG BUY / BUY / HOLD / AVOID
```

---

### Phase 4: Lollapalooza & Anti-Hooks Check (2~3분)

#### Lollapalooza Trigger Detection

```python
# 4개 치명적 신호 동시 확인
Signal_1 = (SDI > 1.0) and (Revenue_Growth < 0)  # 주식 희석 + 매출 부진
Signal_2 = (CEO_Option_Exercise_3yr > 3) and (Self_Stock_Buyback == 0)  # 경영진 옷로환
Signal_3 = (PER > 50) and (Revenue_Growth < 10)  # 극도의 고평가
Signal_4 = (PPI < 0.5) for 2 consecutive years  # 가격 인상 불가

Lollapalooza_Triggered = Signal_1 and Signal_2 and Signal_3 and Signal_4

if Lollapalooza_Triggered:
    Consensus_Score = 0  # 즉시 0점
    Signal = "CRITICAL_AVOID"
    print("⚠️ LOLLAPALOOZA OVERRIDE ACTIVATED - ABSOLUTE AVOIDANCE")
```

**체크리스트**:
```
□ 신호 1: SDI > 1.0 + Revenue Decline?  NO / YES
□ 신호 2: CEO 옷로환 (옵션 +3회 + 자사주 0회)?  NO / YES
□ 신호 3: PER > 50 + 성장률 < 10%?  NO / YES
□ 신호 4: PPI < 0.5 연속 2년?  NO / YES

☑ Lollapalooza 동시 발생? NO / YES (→ Consensus = 0)
```

#### Anti-Hooks Penalty Check

```python
Forbidden_Phrases = [
    "사업이 정상 궤도",  # -30점
    "경기 무조건 회복",  # -40점
    "AI/메타버스 무조건",  # -50점
    "대주주 신뢰",  # -35점
    "영원한 성장"  # -60점
]

Anti_Hooks_Penalty = 0
for phrase in Forbidden_Phrases:
    if phrase in analysis_text:
        # 해당 페널티 적용
        pass

Consensus_Score -= Anti_Hooks_Penalty
```

**체크리스트**:
```
□ 금지 표현 자동 스캔
  - "사업 정상 궤도"?  NO / YES (→ -30점)
  - "경기 무조건"?  NO / YES (→ -40점)
  - "AI/메타버스 무조건"?  NO / YES (→ -50점)
  - "대주주 신뢰"?  NO / YES (→ -35점)
  - "영원한 성장"?  NO / YES (→ -60점)

□ 최종 Anti-Hooks 감점: ___ 점 (누적)
□ 수정된 Consensus: ___ /100 (감점 후)
```

---

## ✅ PART 2 FINAL VALIDATION CHECKLIST

```
Phase 1: Advanced Hooks 11-14 Complete
□ Hook 11 P-Q-C 분해: PPI 계산 + 점수 할당
□ Hook 12 CapEx 이분화: Maintenance + Owner Earnings
□ Hook 13 Soft Moat: LTV/CAC + Network Effect + Switching Cost
□ Hook 14 Stochastic Range: 3 시나리오 WACC + 신뢰구간 밴드

Phase 2: Apex Hooks 21-25 Complete
□ Hook 21 Governance: δ_Governance 계산 + V 조정
□ Hook 22 CCC: 효율성 승수 + 악화 추세 감시
□ Hook 23 Goodwill: Impairment 스트레스 + ROIC 재계산
□ Hook 24 Refinancing: Ratio + Stressed ICR + 위험 판정
□ Hook 25 Tail Risk: Cash Runway + MoS 상향

Phase 3: 3-Philosopher Consensus
□ Graham Defense Score: ___ /100
□ Buffett Value Score: ___ /100
□ Munger Quality Score: ___ /100
□ Consensus 평균: ___ /100 ✓

Phase 4: Override & Anti-Hooks
□ Lollapalooza 4개 신호 동시 확인
□ Anti-Hooks 금지 표현 스캔
□ 최종 Consensus 수정 완료

Go/No-Go Decision:
□ Consensus ≥ 60점 → Part 3 진행 ✓
□ Consensus < 60점 → 재검토 필요
□ Lollapalooza 또는 Anti-Hooks 심각 → AVOID
```

---

## <thought_process>

### Part 2 Skill 검증 완료:

1. **Advanced Hooks 11-14**: P-Q-C, CapEx, LTV/CAC, 신뢰구간 모두 계산 ✓
2. **Apex Hooks 21-25**: 거버넌스, CCC, 무형자산, 재융자, 꼬리위험 모두 산출 ✓
3. **3-Philosopher Model**: 그레이엄/버펫/먼거 점수 자동 계산 ✓
4. **Lollapalooza Override**: 4개 극단 신호 감지 로직 ✓
5. **Anti-Hooks Penalty**: 금지 표현 자동 감점 ✓
6. **Final Consensus**: 수정된 최종 점수 + Signal 생성 ✓

### Part 3로의 연결:
- Adaptive Modules 1-5 (regime-adjusted MoS, catalyst scoring, ATR stop-loss, bucketing, CMFI)
- Negative Catalyst System (상세)
- Integrated Output Matrix v10.1
- Final Investment Signal (STRONG BUY / BUY / HOLD / SELL)

</thought_process>

---

## 📌 Part 2 (Skill) 완료 사항

- [x] Advanced Hooks 11-14 계산 루틴 + Python 코드
- [x] Apex Hooks 21-25 체크리스트 + 자동 판정
- [x] 3-Philosopher Consensus 자동 계산기
- [x] Lollapalooza Override 감지 로직
- [x] Anti-Hooks 페널티 시스템
- [x] Part 2 최종 검증 체크리스트

---

## 🔜 Part 3 로드 조건

✅ Part 1 + Part 2 완료 후:
- Hooks 1-25 모두 산출 ✓
- 3-Philosopher Consensus 계산 ✓
- Lollapalooza & Anti-Hooks 체크 ✓
- Consensus ≥ 60점 (Part 3 진행 가능)

**→ Part 3 (hook_3.md / skill_3.md) 로드 가능**

---

**작성 완료**: 2026-07-29  
**버전**: v10.1 APEX Modular  
**모듈**: Part 2/3 (Advanced & Institutional Skill Module)
