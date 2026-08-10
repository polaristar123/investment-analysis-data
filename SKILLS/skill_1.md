# 🎯 Unified Investment Analysis Engine v10.1 (Part 1/3)
## Base Layer & Priority Hooks - Execution Rules & Validation
### Skill Module 1: Data Parsing → Hook 8-10 → Foundation Hooks 1-7

**버전**: v10.1 APEX Modular Standard  
**모듈**: Part 1/3 - Skill (실행 규칙 & 검증)  
**목적**: hook_1.md의 공식을 실제로 적용하는 **체크리스트 & 실행 순서**

---

## 🔄 UNIFIED AUTOMATION EXECUTION CONTRACT

사용자가 [analysis_ingredient.md] 형식으로 재무 데이터를 제공하면:

1. **Part 1 자동 로드** → Sector-Routing 실행
2. **Priority Hooks 8-10 즉시 실행** → WACC, CAP Decay, NWC 산출
3. **Foundation Hooks 1-7 순차 검증** → 최소 3/7 PASS 확인
4. **Part 2 로드 여부 결정** (5/7 이상 PASS 시 진행)

**⚠️ Binding Rule**: 1개 Hook이라도 누락 불가

---

## 📊 EXECUTION PIPELINE (Part 1)

### Phase 1: Data Input & Sector Detection (1-2분)

```
입력 체크리스트:
- [ ] Ticker 명시 (예: 005930.KS)
- [ ] Company Name 명시
- [ ] Sector 분류 (Financials / Manufacturing / Tech / Retail)
- [ ] 재무제표 완성 (Income / Balance / Cash Flow 모두)
- [ ] 통화 단위 명시 (KRW / USD / JPY)
- [ ] 회계연도 명시 (2025, 2026 등)
```

**자동 Sector 라우팅**:
```
if Sector in ["Banking", "Insurance", "Brokerage", "Financial Services"]:
    ROUTE = "Financials Branch" (NWC/CapEx Bypass)
    
elif Sector in ["Manufacturing", "Auto", "Semiconductor", "Chemical"]:
    ROUTE = "Standard Branch" (Hook 1-25 전체)
    
elif Sector in ["SaaS", "Software", "AI Platform"]:
    ROUTE = "Tech Branch" (CAC/LTV 강조)
    
elif Sector in ["Retail", "F&B", "E-commerce"]:
    ROUTE = "Retail Branch" (Working Capital 강조)
    
else:
    ROUTE = "Standard Branch" (기본값)
```

---

### Phase 2: Priority Hooks 8-10 (3~4분)

#### Step 2-1: Hook 8 Dynamic WACC 계산

**입력 데이터 수집**:
```
1. 시장 데이터
   - Rf (10년 국고채 금리): ___ %
   - Rm - Rf (시장 리스크프리미엄): ___ %
   
2. 기업 데이터
   - β (베타): ___
   - Current Market Cap: ___ (원)
   - Total Debt: ___ (원)
   - Cash & Equivalents: ___ (원)
   - Interest Expense (연): ___ (원)
   - Effective Tax Rate: ___ %
```

**계산 루틴**:
```python
# Step A: Ke 계산
Ke = Rf + Beta × (Rm - Rf)
# 예: Ke = 3.5 + 1.2 × 6.0 = 11.7%

# Step B: Kd 계산
Kd = Interest Expense / Total Debt
# 예: Kd = 2,000억 / 50,000억 = 4.0%

# Step C: E, D, V 계산
Market_Cap = Stock_Price × Shares_Outstanding
Net_Debt = Total_Debt - Cash
V = Market_Cap + Net_Debt
E_weight = Market_Cap / V
D_weight = Net_Debt / V

# Step D: WACC 최종
WACC = Ke × E_weight + Kd × (1 - Tax_Rate) × D_weight
# 예: WACC = 11.7% × 0.971 + 4.0% × (1-0.22) × 0.029 = 11.4%
```

**출력 형식**:
```
✓ Hook 8 Dynamic WACC: 11.4%
  - Ke (Cost of Equity): 11.7%
  - Kd (Cost of Debt): 4.0%
  - E/V: 97.1% | D/V: 2.9%
  - Tax Rate: 22%
```

---

#### Step 2-2: Hook 9 CAP Decay 계산

**입력 데이터**:
```
1. 경쟁우위기간 평가
   - 현재 Moat 강도: Strong / Moderate / Weak
   - 기본 CAP_base (추천): ___ 년
   
2. 감쇠 요인 평가
   - CEO 안정성: 우수 / 중간 / 낮음 (λ -30% / 0% / +50%)
   - R&D 투자율: ___ % (> 5%: -20% / < 2%: +30%)
   - 특허 만료: 향후 ___ 년 내 (만료 임박: +40%)
   - 산업 변화 속도: 급변 / 중간 / 안정 (λ 0.12~0.15 / 0.08~0.10 / 0.03~0.06)
```

**계산 루틴**:
```python
# Step A: 기본 λ 선택 (산업별)
if Industry in ["AI", "Biotech", "Mobile"]:
    Lambda_base = 0.13
elif Industry in ["Auto", "Chemical", "Manufacturing"]:
    Lambda_base = 0.08
elif Industry in ["Financial", "Utility", "Infrastructure"]:
    Lambda_base = 0.05
else:
    Lambda_base = 0.08  # 기본값

# Step B: 조정 계수 적용
Lambda = Lambda_base × (1 + CEO_Adjustment + RnD_Adjustment + Patent_Adjustment + ...)

# Step C: CAP(t) 시뮬레이션 (t = 3, 5, 10년)
for t in [3, 5, 10]:
    CAP_t = CAP_base × exp(-Lambda × t)
    print(f"Year {t}: CAP = {CAP_t:.1f}년")
```

**출력 형식**:
```
✓ Hook 9 CAP Decay:
  - CAP_base: 12.0년 (Strong Moat)
  - λ (Decay Rate): 0.08
  - Year 3: CAP = 9.4년
  - Year 5: CAP = 8.0년
  - Year 10: CAP = 5.4년
```

---

#### Step 2-3: Hook 10 Normalized NWC 계산

**입력 데이터 (5년 역사)**:
```
연도     | Current Assets | Curr Liab | Revenue
---------|----------------|-----------|--------
t-4      | ___ 억원       | ___ 억원  | ___ 억원
t-3      | ___ 억원       | ___ 억원  | ___ 억원
t-2      | ___ 억원       | ___ 억원  | ___ 억원
t-1      | ___ 억원       | ___ 억원  | ___ 억원
t        | ___ 억원       | ___ 억원  | ___ 억원
```

**계산 루틴**:
```python
# Step A: 5년 NWC/Sales 비율 계산
NWC_Sales_Ratios = []
for year in [t-4, t-3, t-2, t-1, t]:
    NWC_year = Current_Assets[year] - Current_Liabilities[year]
    Ratio = NWC_year / Revenue[year]
    NWC_Sales_Ratios.append(Ratio)

# Step B: 정규화된 비율 (평균)
Normalized_Ratio = mean(NWC_Sales_Ratios)

# Step C: 2025년 정규화 ∆NWC
Revenue_2025_Forecast = ___ 억원
NWC_Target_2025 = Revenue_2025_Forecast × Normalized_Ratio
NWC_Actual_2024 = ___ 억원
Delta_NWC_Normalized = NWC_Target_2025 - NWC_Actual_2024

# Step D: Owner Earnings 연산
Net_Income_2025 = ___ 억원
D_A_2025 = ___ 억원
Maintenance_CapEx_2025 = Total_CapEx_2025 × 0.85  # 또는 max(D&A, 0.85×CapEx)
Owner_Earnings_2025 = (Net_Income_2025 + D_A_2025 
                       - Maintenance_CapEx_2025 
                       - Delta_NWC_Normalized)
```

**출력 형식**:
```
✓ Hook 10 Normalized NWC:
  - 5년 평균 NWC/Sales: 14.7%
  - 2025 Revenue Forecast: 25,500억원
  - Target NWC (2025): 3,749억원
  - Normalized ∆NWC: +149억원
  - Owner Earnings (2025): 34,551억원
```

---

### Phase 3: Foundation Hooks 1-7 (4~5분)

#### Hook 1: Dynamic NCAV (체크리스트)

```
□ NCAV_dynamic = (Current Assets × 0.8) - Total Liabilities
  Result: ___ 억원
  
□ 조건 1: NCAV_dynamic > 0?  YES / NO
□ 조건 2: Debt/Equity < 100%?  YES / NO
□ 조건 3: Current Ratio > 1.5x?  YES / NO

□ 최종: PASS (3/3) / PARTIAL (2/3) / FAIL (≤1/3)

금융업 대체:
□ Capital Ratio = Equity / Total Assets > 8%?  YES / NO
```

**자동 감점**:
- NCAV 음수 + Debt/Equity > 150%: ⚠️ CRITICAL (내재가치 -40%)

---

#### Hook 2: Double-Path Moat (체크리스트)

```
□ 물리적 해자 평가
   - 브랜드/특허: 강함 / 중간 / 약함
   - 네트워크/규모: 강함 / 중간 / 약함
   - 점수: ___ / 10

□ 경제적 해자 평가
   - ROIC > WACC 확인 (Hook 11에서 상세 분석)
   - 지속 확률: ___ %

□ 결론: PASS (해자 확인) / WEAK (해자 미약) / FAIL (해자 없음)
```

---

#### Hooks 3-7: 요약 체크리스트

| Hook | 항목 | 기준 | 결과 | 상태 |
|------|------|------|------|------|
| 3 | Margin & Growth Stability | 75% 이상 통과 | ___ % | ✓/✗ |
| 4 | Governance & Compensation | WACC ±3.5% 범위 | ___ bps | ✓/✗ |
| 5-6 | L_score (SDI × PPI) | > 0 | ___ | ✓/✗ |
| 7 | Dynamic MoS Required | Current MoS ≥ Required | ___ % | ✓/✗ |

---

## ✅ PART 1 FINAL VALIDATION CHECKLIST

### 필수 검증 항목 (모두 완료해야 Part 2 진행)

```
Phase 1: Data Integrity
□ Income Statement: Revenue + EBITDA + Net Income + Operating Profit
□ Balance Sheet: Assets + Liabilities + Equity (검산: A = L + E)
□ Cash Flow: Operating CF + CapEx + Free CF (검산: FCF = OCF - CapEx)
□ 통화 단위 통일 (KRW / USD / JPY 혼재 없음)
□ 연도별 데이터 일관성 (5년 역사 완비)

Phase 2: Sector-Routing Confirmation
□ Sector 분류 완료
□ Financials 여부 판정 (YES → NWC/CapEx Bypass 확인)
□ 라우팅 결정: Standard / Financials / Tech / Retail

Phase 3: Priority Hooks 8-10 Completion
□ Hook 8 WACC: Ke + Kd + E/V + D/V + 최종값 모두 산출
  Output: WACC = ___ %
□ Hook 9 CAP: CAP_base + λ + t=3/5/10 시뮬레이션
  Output: Year 10 CAP = ___ 년
□ Hook 10 NWC: 5년 평균 + Normalized ∆NWC + Owner Earnings
  Output: Owner Earnings = ___ 억원

Phase 4: Foundation Hooks 1-7 Status
□ Hook 1 NCAV: PASS / PARTIAL / FAIL
□ Hook 2 Moat: PASS / WEAK / FAIL
□ Hooks 3-7: 최소 3/5 PASS (50% 통과율)

Phase 5: Part 2 Go/No-Go Decision
□ 모든 Priority Hooks (8-10) 완료
□ Foundation Hooks 최소 5/7 이상 PASS
□ 수치 오류 없음 (금융 계산 재검증)

Go/No-Go: ✓ PROCEED TO PART 2 / ✗ RETRY PART 1
```

---

## 🚨 NEGATIVE CATALYST PREVIEW (Part 3에서 상세)

Part 1 단계에서 감지해야 할 **위험 신호**:

```
Automatic Penalty (-30점 이상):
1. NCAV 음수 + Debt/Equity > 150%: CRITICAL_SOLVENCY_RISK
2. Normalized ∆NWC > 2배 증가 추세: CRITICAL_CASH_TRAP
3. Current Ratio < 1.2x + Interest Coverage < 1.5x: DEFAULT_RISK
4. Revenue Decline > 10% YoY 연속 2년: REVENUE_CLIFF

이 경우 내재가치 -30~50% 감점 + Part 2 조건부 진행
```

---

## <thought_process>

### Part 1 Skill 검증 완료 체크:

1. **Data Parsing**: 입력 데이터 완전성 + 통화/연도 일관성 ✓
2. **Sector Routing**: Financials vs Standard Branch 결정 ✓
3. **Priority Hooks 8-10**: WACC + CAP Decay + Owner Earnings 모두 산출 ✓
4. **Foundation Hooks 1-7**: 최소 5/7 PASS 확인 ✓
5. **Negative Catalyst Detection**: 위험 신호 감시 ✓
6. **Part 2 Go/No-Go**: 모든 선행 조건 충족 확인 ✓

### 최종 Output 전 순서:
1. Part 1의 모든 수치를 Thought Process 태그 내에서 재검증
2. Part 2 로드 여부 사용자 확인 후 진행
3. Part 2에서 Advanced Hooks 11-14 + Apex Hooks 21-25 상세 분석

</thought_process>

---

## 📌 Part 1 (Skill) 완료 사항

- [x] Execution Pipeline 명시 (Phase 1-4)
- [x] Hook 8-10 상세 계산 루틴 + 계산기
- [x] Foundation Hooks 1-7 체크리스트
- [x] PASS/FAIL 판정 기준 명확화
- [x] Negative Catalyst Preview (위험 신호)
- [x] Part 2 Go/No-Go Criteria 정의

---

## 🔜 Part 2 로드 조건

✅ Part 1 완료 후:
- Hooks 8-10 모두 산출 ✓
- Foundation Hooks 최소 5/7 PASS ✓
- 위험 신호 체크 ✓

**→ Part 2 (hook_2.md / skill_2.md) 로드 가능**

---

**작성 완료**: 2026-07-29  
**버전**: v10.1 APEX Modular  
**모듈**: Part 1/3 (Base Layer Skill Module)
