# 📊 APEX v10.2 COMPACT - 통합 투자 분석 엔진
**원샷 방식: 재무제표 입력 → 자동 모든 Hook 연산 → 최종 보고서**  
**버전**: v10.2 (Part 1-3 통합, 70% 축소)

---

## 🎯 ONE-SHOT EXECUTION FLOW

```
[Step 1] 재무 데이터 입력 (analysis_ingredient.md)
    ↓
[Step 2] 섹터 자동 감지 & Bypass 규칙 적용
    ↓
[Step 3] Priority Hooks 8-10 즉시 연산 (WACC, CAP Decay, Owner Earnings)
    ↓
[Step 4] Foundation Hooks 1-7 병렬 검증 (5분)
    ↓
[Step 5] Advanced Hooks 11-25 & Modules 1-5 (10분)
    ↓
[Step 6] 최종 보고서 한 번에 생성
```

---

## 📋 입력 데이터 형식 (필수)

```markdown
[Ticker]: 005930.KS
[Company Name]: 삼성전자
[Sector]: Electronics / Financials / SaaS / Retail
[Financial Year]: 2025
[Currency]: KRW (억원)

[Income Statement]
- Revenue: ___ / EBITDA: ___ / Operating Profit: ___ / Net Income: ___

[Balance Sheet]
- Total Assets: ___ / Total Liabilities: ___ / Equity: ___
- Current Assets: ___ / Current Liabilities: ___

[Cash Flow]
- Operating CF: ___ / CapEx: ___ / Free Cash Flow: ___

[Key Data]
- Current Stock Price: ___ / Shares Outstanding: ___
- Total Debt: ___ / Cash: ___ / R&D Expense: ___
- Employees: ___ / Beta: ___ (기본값: 1.0)
```

---

## ⚡ PRIORITY HOOKS 8-10 (자동 연산)

### Hook 8: WACC 계산기

| 입력값 | 값 | 기본값 |
|--------|-----|--------|
| Rf (10Y 국고채) | ___ % | 3.5% |
| Beta | ___ | 1.0 |
| Market Risk Premium | ___ % | 6.0% |
| Interest Expense | ___ 억원 | 자동 |
| Total Debt | ___ 억원 | 자동 |
| Market Cap | ___ 억원 | 자동 |
| Tax Rate | ___ % | 22% |

**자동 계산**:
```
Ke = Rf + Beta × (Rm - Rf)
Kd = Interest Expense / Total Debt
V = Market Cap + (Total Debt - Cash)
WACC = Ke × (E/V) + Kd × (1-Tax) × (D/V)
```

**Output**: `WACC = ___ %` ✓

---

### Hook 9: CAP Decay 시뮬레이터

| 입력값 | 선택 |
|--------|------|
| 현재 해자 강도 | Strong(15y) / Moderate(10y) / Weak(5y) |
| 산업 변화 속도 | 급변(0.13) / 중간(0.08) / 안정(0.05) |
| CEO 안정성 | 우수(-30%) / 중간(0%) / 낮음(+50%) |

**자동 시뮬레이션**:
```
λ = 산업기본값 × (1 + 조정계수)
CAP(t) = CAP_base × e^(-λ×t) for t=1,3,5,10
```

**Output**:
```
Year 3: CAP = ___ 년
Year 5: CAP = ___ 년
Year 10: CAP = ___ 년
```

---

### Hook 10: 정규화 Owner Earnings

| 입력값 | 값 |
|--------|-----|
| Net Income (당기순이익) | ___ 억원 |
| D&A (감가상각) | ___ 억원 |
| Total CapEx | ___ 억원 |
| Growth CapEx (분리된 경우) | ___ 억원 |
| Current Assets (5년 평균) | ___ 억원 |
| Current Liabilities (5년 평균) | ___ 억원 |
| Revenue (5년 평균) | ___ 억원 |

**자동 계산**:
```
Maintenance CapEx = max(D&A, Total CapEx × 0.85)
Normalized NWC/Sales = 5년 평균 비율
Normalized ∆NWC = Target NWC - Prior NWC
Owner Earnings = NI + D&A - M-CapEx - ∆NWC
```

**Output**: `Owner Earnings = ___ 억원` ✓

---

## 🟢 FOUNDATION HOOKS 1-7 (체크리스트)

### Hook 1: NCAV 보호 (자산 방어)
```
□ NCAV = (Current Assets × 0.8) - Total Liabilities > 0?
  ❌ NO & Debt/Equity > 150% → CRITICAL (-30점)
  ✓ YES → PASS (+0점)
```

### Hook 2: 해자 지속성 (Moat Sustainability)
```
□ ROIC > WACC 지속 가능? (CAP 기간 동안)
  ✓ YES → PASS (+5점)
  ❌ NO → FAIL (-20점)
```

### Hook 3: 마진/성장 안정성
```
□ 지난 5년 Gross Margin CV < 0.25?
□ Revenue Growth 편차 < 2배?
  ✓ 2개 이상 → PASS (+0점)
  ❌ 1개 이하 → WEAK (-10점)
```

### Hook 4: 거버넌스 정렬
```
□ CEO 보수와 EBIT 변동 연관성?
  ✓ 상관계수 > 0.6 → PASS (+0점)
  ❌ < 0.6 → WEAK (-15점)
```

### Hook 5-6: 가격 결정력 (PPI) & 투자 효율성 (SDI)
```
□ PPI = (기업 마진변화 / 산업 마진변화) × 자산회전율 > 1.0?
  ✓ YES → PASS (+10점)
  ❌ NO → WEAK (0점)

□ SDI = NI / Revenue (Sustainable) > 5%?
  ✓ YES → PASS (+5점)
  ❌ NO → WEAK (-10점)
```

### Hook 7: 변동성 조정 MoS
```
□ Required MoS = Base MoS + (Volatility × 0.05)?
□ Current Price MoS ≥ Required MoS?
  ✓ YES → PASS (+0점)
  ❌ NO → RISKY (-20점)
```

**Foundation Score = Σ(점수) / 최대값**

---

## 🟡 ADVANCED HOOKS 11-25 (병렬 연산)

### Hook 11-14: 경쟁우위 분석

| Hook | 항목 | 계산 | 판정 |
|------|------|------|------|
| 11 | PPI (가격 결정력) | (기업마진변화 / 산업마진) × 자산회전율 | >1.2: +15점 / <0.8: -20점 |
| 12 | Owner Earnings (정규화) | NI + D&A - M-CapEx - ∆NWC | 성장율 계산 |
| 13 | ROIC-WACC Spread | ROIC - WACC | >3%: 우수 / <0%: 악화 |
| 14 | NWC Trap 감지 | ∆NWC 추세 | 2년 연속 증가? -30점 |

---

### Hook 15-20: 효율성 & 구조 지표

```
Hook 15: 자산 회전율 (Asset Turnover) = Revenue / Total Assets
Hook 16: 부채 비율 (Debt/Equity) 추세
Hook 17: 유동성 비율 (Current Ratio) > 1.5x?
Hook 18: CCC (현금전환주기) 개선 추세?
Hook 19: 고객집중도 (Top 3 customers % of revenue)
Hook 20: R&D 강도 (R&D / Revenue %)
```

---

### Hook 21-25: 거버넌스 & 극단 위험

| Hook | 항목 | 위험 신호 | 감점 |
|------|------|---------|------|
| 21 | 경영진 안정성 | CEO 1년 내 3명 이상 교체 | -40점 |
| 22 | 관련자거래 | 연간 총 매출 10% 초과 | -35점 |
| 23 | 규제 위험 | 진행 중 조사/소송 3건 이상 | -30점 |
| 24 | 유동성 위험 | 12M 만기 부채 > 보유 현금 × 1.5 | -25점 |
| 25 | 공급망 집중도 | Top 3 suppliers % > 40% | -20점 |

---

## 🔴 LOLLAPALOOZA ANTI-HOOK (자동 Override)

**다음 중 1개 이상 해당 시 즉시 CRITICAL_AVOID 신호**:

```
1. NCAV < 0 AND Debt/Equity > 150%
2. ∆NWC 급증 (2배 이상 1년 내)
3. Interest Coverage < 1.5x AND Rising Debt Trend
4. Revenue Decline > 10% YoY 연속 2년
5. 실행 중인 규제 조사 + NPL Ratio > 3% (금융업)
6. CEO 교체 + 주요 거래처 이탈 동시 발생
```

**결과**: `SIGNAL = CRITICAL_AVOID` → **Max Allocation = 0%**

---

## 📊 MODULES 1-5 (최종 합의)

### Module 1: 동적 안전마진 요구치
```
Base MoS = 15% (기준)
Risk Premium:
  - High Volatility (>40% annual): +10%
  - Concentration Risk (>30%): +5%
  - Governance Risk (점수 <50): +10%
  
Required MoS = Base + All Premiums
```

### Module 2: 거시경제 정렬 (CMFI)
```
Current Regime: Recession / Recovery / Expansion / Overheating
Firm Sensitivity: High / Medium / Low
Score = Regime Impact × Firm Sensitivity
```

### Module 3: ATR 손절 규약
```
ATR (14일) = ___
Trailing Stop = Current Price - (2 × ATR)
```

### Module 4-5: 거장 3인 합의 (Graham, Buffett, Munger)

**Graham (Asset Defense Score)**
```
점수 = 50 × (NCAV/Market Cap) + 50 × (Current Ratio / 1.5)
기준: <0 → 0점 / >0.5 → 100점
```

**Buffett (Owner Yield Score)**
```
점수 = (Owner Earnings / Market Cap) / (WACC/100) × 100
기준: <0.5 → 0점 / >1.0 → 100점
```

**Munger (Pricing Power Score)**
```
점수 = PPI × 50 + (Gross Margin Trend) × 50
기준: 0~100점
```

**통합 합의 점수**:
```
Consensus = 0.30 × Graham + 0.40 × Buffett + 0.30 × Munger
최종 신호:
  - >70: BUY
  - 50-70: HOLD
  - 30-50: SELL
  - <30: AVOID
```

---

## 📄 최종 보고서 템플릿 (4페이지)

생성 파일: `/Report/analysis_compact_[TICKER]_[DATE].md`

```markdown
# [기업명] 투자 분석 보고서 v10.2 Compact

## 1. 최종 신호 & 목표가 (Executive Summary)

| 항목 | 값 |
|------|-----|
| **최종 신호** | BUY / HOLD / SELL / CRITICAL_AVOID |
| **합의 점수** | ___ / 100 |
| **목표가** | ___ ~ ___ 원 |
| **안전마진** | ___ % |
| **권장 비중** | ___ % |

**핵심 논거** (3줄):
- [Point 1]
- [Point 2]
- [Point 3]

---

## 2. 거장 3인 평가 (Masters Consensus)

| 모델 | 점수 | 주요 지표 | 판정 |
|------|------|---------|------|
| Graham (자산) | ___ / 100 | NCAV, Liquidity Ratio | [진단] |
| Buffett (주주이익) | ___ / 100 | Owner Earnings, ROIC-WACC | [진단] |
| Munger (가격결정력) | ___ / 100 | PPI, Gross Margin | [진단] |

---

## 3. Priority Hooks 연산 결과 (Hook 8-10)

### Hook 8: WACC
- Ke = ___ % (= Rf + β × MRP)
- Kd = ___ %
- WACC = **___ %**

### Hook 9: CAP Decay
- 현재 해자 기간: ___ 년
- Year 5 CAP: ___ 년
- Year 10 CAP: ___ 년

### Hook 10: Owner Earnings
- Normalized ∆NWC: ___ 억원
- **Owner Earnings = ___ 억원**

---

## 4. 리스크 & 손절 (Risk Management)

| 항목 | 값 |
|------|-----|
| ATR (14일) | ___ 원 |
| 손절가 | ___ 원 (-___ %) |
| 핵심 모니터 지표 | [3개] |

**Lollapalooza 위험 신호**:
- [ ] 없음
- [x] 있음: [신호 명시]

---

## 5. 3-Scenario Valuation

| 시나리오 | 보수적 | 기본 | 낙관적 |
|---------|--------|------|--------|
| Revenue CAGR | ___ % | ___ % | ___ % |
| EBIT Margin | ___ % | ___ % | ___ % |
| Terminal Multiple | ___ x | ___ x | ___ x |
| **내재가치** | **$___** | **$___** | **$___** |
| 확률 | 25% | 50% | 25% |

**확률가중평균 목표가 = $___ (~___% upside)**

---

## 6. 실행 계획 (Action Plan)

분할 매수: $___ (100% 신규)
포트폴리오 비중: ___% (최대)
점검 주기: 분기(90일)
리밸런싱: 목표가 ±15% 도달 시
```

---

## 🚀 사용법

1. **재무 데이터 준비**: `analysis_ingredient.md` 형식으로 정리
2. **이 문서 로드**: Hooks 1-25 자동 실행
3. **최종 보고서 생성**: `/Report/analysis_compact_[TICKER]_[DATE].md`
4. **의사결정**: 보고서 섹션 1 참조 → 매매/회피

---

**버전**: v10.2 Compact (통합형, 70% 축소)  
**작성일**: 2026-08-10  
**예상 실행시간**: 15-20분 (전체 Hook + Report)
