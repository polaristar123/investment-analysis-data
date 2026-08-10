# [v10.2 APEX INSTITUTIONAL STANDARD INPUT TEMPLATE]

**이 문서 전체를 Claude Code 프롬프트로 붙여넣으면 v10.2 파이프라인 엔진이 실행되어 분석이 시작됩니다.**

> **[SYSTEM EXECUTION DIRECTIVE - v10.2 PROTOCOL]**
> "내가 세계 최고 수준의 투자 IB 팀의 선임 디렉터다. 
> [기업이름 / 티커 입력]에 대하여 **'Unified Investment Analysis Engine v10.2 (Fast-Pass + Sector Bypass + Dynamic Depth Engine)'**를 가동한다.
>
> **[가동 규칙]**
> 1. **2단계 파이프라인 적용**: Data 파싱 완료 후 반드시 **[Step 1: Fast-Pass Scan]**을 먼저 수행하라. 
>    - Hook 1, Hook 8, Hook 10, Hook 24, Lollapalooza 4대 극단 위험을 우선 스캔한다.
>    - 치명적 결격 사유(파산, 자본잠식, 유동성 위기 등) 발견 시 **즉시 분석을 중단(Early Exit)**하고 [Fast-Pass 탈락 보고서]만 출력하라.
>    - PASS 시에만 **[Step 2: Deep-Dive Analysis]**로 자동 전환하여 이하 전체 모듈 연산을 완성하라.
> 2. **업종별 Bypass 적용**: 입력된 대상 기업의 산업군(Sector)을 자동 판별하여 지정된 Bypass 지표(금융: NWC/CapEx/CCC Skip, IT/SaaS: CapEx/CCC Skip 등)의 계산 연산을 효율적으로 Skip하라.
>
> 아래 명시된 마크다운 템플릿 구조를 절대 변경하지 말고, 각 꺾쇠괄호 [ ] 안에 실제 사업보고서, 주요 공시, 시장 매크로 지표 검증된 데이터 값을 정확하게 기입해 주라. 정확한 값이 없는 주요 항목은 업계 평균 가이드라인이나 합리적인 추정치를 보고 (EST)라고 기입해 주라. 값을 기입할 때는 통일 단위(USD, KRW 등)를 명확히 써야 한다."

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## PART 0: EXECUTION MODE & SECTOR OVERRIDE (엔진 제어 파라미터 - NEW)
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 0. Execution Settings

**Execution Mode:** [/auto (기본값: Fast-Pass PASS 시 Deep-Dive 자동 진입) / /quick (Fast-Pass만 검증) / /full (Fast-Pass 생략 후 전체 연산)]

**Target Sector Category:** [Auto-Detect / Financials / Manufacturing / SaaS & IT / Biotech / FMCG]

*(선택한 Sector에 따라 Engine이 불필요한 Hook 연산을 자동 Bypass합니다.)*

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## PART I: CORE FINANCIAL DATA (기본 재무 데이터)
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### [Ticker / Company Name]:

### 1. Macro & Market Variables

**10Y Govt Bond Rate ($R_f$):** [ %]

**10Y Market Return ($R_m$):** [ %]

**Dynamic Beta (10Y):** [ ]

**Effective Tax Rate ($T_c$):** [ %]

**Current Stock Price ($P$):** [ (반드시 현재 오늘 기준 실시간 주가 기입) ]

**Total Shares Outstanding:** [ (반드시 현재 오늘 기준 실시간 유통주식수 기입) ]

**Current Market Cap:** [ $= P \times \text{Total Shares}$ (자동 계산)]

---

### 2. 10-Year Income Statement Checklist

| Metric | Year 1 | Year 2 | Year 3 | ... | Year 10 |
|--------|--------|--------|--------|-----|----------|
| **Revenue** | [ ] | [ ] | [ ] | ... | [ ] |
| **COGS** | [ ] | [ ] | [ ] | ... | [ ] |
| **Variable Costs** | [ EST] | [ EST] | [ EST] | ... | [ EST] |
| **Fixed Costs** | [ EST] | [ EST] | [ EST] | ... | [ EST] |
| **Gross Profit** | [ ] | [ ] | [ ] | ... | [ ] |
| **Gross Margin %** | [ %] | [ %] | [ %] | ... | [ %] |
| **SG&A Expenses** | [ ] | [ ] | [ ] | ... | [ ] |
| **R&D Expense** | [ ] | [ ] | [ ] | ... | [ ] |
| **Operating Income (EBIT)** | [ ] | [ ] | [ ] | ... | [ ] |
| **EBIT Margin %** | [ %] | [ %] | [ %] | ... | [ %] |
| **D&A** | [ ] | [ ] | [ ] | ... | [ ] |
| **Interest Expense** | [ ] | [ ] | [ ] | ... | [ ] |
| **Tax Expense** | [ ] | [ ] | [ ] | ... | [ ] |
| **Net Income** | [ ] | [ ] | [ ] | ... | [ ] |
| **Net Margin %** | [ %] | [ %] | [ %] | ... | [ %] |

---

### 3. 10-Year Balance Sheet Checklist

| Metric | Year 1 | Year 2 | Year 3 | ... | Year 10 |
|--------|--------|--------|--------|-----|----------|
| **Cash & Equivalents** | [ ] | [ ] | [ ] | ... | [ ] |
| **Accounts Receivable** | [ ] | [ ] | [ ] | ... | [ ] |
| **Inventories** | [ ] | [ ] | [ ] | ... | [ ] |
| **PPE (Net)** | [ ] | [ ] | [ ] | ... | [ ] |
| **Total Assets** | [ ] | [ ] | [ ] | ... | [ ] |
| **Short-Term Debt** | [ ] | [ ] | [ ] | ... | [ ] |
| **Long-Term Debt** | [ ] | [ ] | [ ] | ... | [ ] |
| **Total Liabilities** | [ ] | [ ] | [ ] | ... | [ ] |
| **Total Equity** | [ ] | [ ] | [ ] | ... | [ ] |

---

### 4. 10-Year Cash Flow & Capital Allocation

| Metric | Year 1 | Year 2 | Year 3 | ... | Year 10 |
|--------|--------|--------|--------|-----|----------|
| **Operating Cash Flow (OCF)** | [ ] | [ ] | [ ] | ... | [ ] |
| **Capital Expenditure (CapEx)** | [ ] | [ ] | [ ] | ... | [ ] |
| **Free Cash Flow** | [ ] | [ ] | [ ] | ... | [ ] |
| **Dividends Paid** | [ ] | [ ] | [ ] | ... | [ ] |

**10Y Revenue CAGR:** [ %]

**10Y FCF CAGR:** [ %]

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## PART II: EFFICIENCY & STRUCTURAL METRICS (효율성 및 구조 지표)
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 5. Working Capital Efficiency & Cash Conversion Cycle (Hook 22)
*(Financial Sector 선택 시 자동 Bypass)*

**Days Sales Outstanding (DSO):** [ Days]

**Days Inventory Outstanding (DIO):** [ Days]

**Days Payable Outstanding (DPO):** [ Days]

**Cash Conversion Cycle (CCC):** [ Days]

**3Y Trend (CCC):** [Improving / Stable / Deteriorating]

---

### 6. Debt & Liquidity Metrics (Hook 24 & Hook 25 - Fast-Pass Core)

**Total Debt Outstanding:** [ ]

**Short-Term Debt Due (within 12M):** [ ]

**Cash & Equivalents:** [ ]

**Net Debt / EBITDA:** [ x]

**Interest Coverage Ratio:** [ x]

**Refinancing Cliff (12-24M due / Total Debt):** [ %]

**Cash Runway (Months):** [ Months]

---

### 7. Capital Structure & ROI Metrics

**Invested Capital:** [ ]

**ROIC:** [ %]

**WACC (Hook 8):** [ %]

**ROIC - WACC Spread:** [ %]

**Liquidity Ratio:** [ x]

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## PART III: GOVERNANCE & OWNERSHIP (지배구조 및 소유권)
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 8. Corporate Governance & Ownership Structure (Hook 21)

**Major Shareholder Stake (>5%):** [ %]

**Board Independence Ratio:** [ %]

**Management Ownership:** [ %]

**CEO Tenure:** [ Years]

**Governance Issues:** [YES / NO]

**Governance Discount Rate:** [ %]

---

### 9. Soft Moat & Network Metrics (Hook 13 - Sector Targeted)

#### For IT/SaaS/Platform:
**Customer Lifetime Value (LTV):** [ ]
**Customer Acquisition Cost (CAC):** [ ]
**LTV / CAC Ratio:** [ x]
**Customer Churn Rate (Annual):** [ %]
**Net Revenue Retention (NRR):** [ %]

#### For Manufacturing:
**Patent Portfolio:** [ ]
**Supply Chain Concentration:** [ %]

#### For Financials:
**NPL Ratio:** [ %]
**BIS Capital Ratio:** [ %]
**ROA:** [ %]
**Net Interest Margin (NIM):** [ %]

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## PART IV: R&D & INTANGIBLE CAPITALIZATION
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 10. R&D Asset Capitalization

**R&D Expense (Annual):** [ ]

**Capitalization Rate (Amortization Period):** [ Years]

**Cumulative Capitalized R&D:** [ ]

**R&D Intensity (R&D / Revenue):** [ %]

**Adjusted ROIC (post-capitalization):** [ %]

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## PART V: CATALYSTS & VALUATION TRIGGERS
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 11. Upcoming Catalysts (향후 12-24개월)

| Catalyst | Timing | Expected Impact | Probability |
|----------|--------|-----------------|-------------|
| **Event 1** | [Month/Quarter] | [ %] | [ %] |
| **Event 2** | [Month/Quarter] | [ %] | [ %] |
| **Event 3** | [Month/Quarter] | [ %] | [ %] |

**Catalyst Confidence Level:** [HIGH / MEDIUM / LOW]

**Catalyst Multiplier:** [ x]

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## PART VI: MARKET REFLEXIVITY & LIQUIDITY
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 12. Market Multiples & Valuation Context

**Current PER:** [ x]

**Current PBR:** [ x]

**Current EV/EBITDA:** [ x]

**3Y Historical Average PER:** [ x]

**Sector Average PER:** [ x]

**Valuation Assessment:** [UNDERVALUED / FAIRLY-VALUED / OVERVALUED]

---

### 13. Stock Liquidity & Market Microstructure

**10Y Historical Volatility:** [ %]

**Average Daily Volume (ADV):** [ ]

**Bid-Ask Spread:** [ %]

**Market Cap Ranking (Sector):** [Top 5 / 5-10 / 10-20 / >20]

**Short Interest (% of Float):** [ %]

**Liquidity Discount:** [ %]

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## PART VII: MACRO REGIME & SCENARIO ANALYSIS
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 15. Current & Expected Macro Regime

**Current Macro Regime:** [RECESSION / RECOVERY / EXPANSION / OVERHEATING]

**Expected 12M Regime:** [RECESSION / RECOVERY / EXPANSION / OVERHEATING]

**Interest Rate Environment:** [RISING / STABLE / FALLING]

---

### 16. Three Scenario Analysis (Bull / Base / Bear)

#### **BEAR CASE**

| Metric | Value |
|--------|-------|
| **Revenue CAGR (3Y)** | [ %] |
| **Terminal EBIT Margin** | [ %] |
| **Terminal ROIC** | [ %] |
| **WACC (Stress)** | [ %] |
| **Terminal Multiple** | [ x] |
| **Intrinsic Value Per Share** | [ ] |
| **Downside Risk** | [ %] |

#### **BASE CASE**

| Metric | Value |
|--------|-------|
| **Revenue CAGR (3Y)** | [ %] |
| **Terminal EBIT Margin** | [ %] |
| **Terminal ROIC** | [ %] |
| **WACC** | [ %] |
| **Terminal Multiple** | [ x] |
| **Intrinsic Value Per Share** | [ ] |
| **Upside/Downside** | [ %] |

#### **BULL CASE**

| Metric | Value |
|--------|-------|
| **Revenue CAGR (3Y)** | [ %] |
| **Terminal EBIT Margin** | [ %] |
| **Terminal ROIC** | [ %] |
| **WACC (Compression)** | [ %] |
| **Terminal Multiple** | [ x] |
| **Intrinsic Value Per Share** | [ ] |
| **Upside** | [ %] |

**Probability-Weighted Fair Value:** [ ]

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## PART VIII: KELLY SIZING & PORTFOLIO RECOMMENDATION
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 17. Probability-Weighted Valuation & Risk Assessment

**Probability of Reaching Base Case (12M):** [ %]

**Probability of Bull Case:** [ %]

**Probability of Bear Case:** [ %]

**Confidence Level:** [HIGH (90%+) / MEDIUM (70~90%) / LOW (<70%)]

**Expected Return:** [ %]

**Expected Risk (Downside Volatility):** [ %]

**Sharpe Ratio:** [ ]

---

### 18. Kelly Criterion Position Sizing

**Win Probability:** [ %]

**Win / Loss Ratio:** [ x]

**Optimal Kelly %:** [ %]

**Half-Kelly Recommendation:** [ %] ← **권장 포트폴리오 비중**

**Maximum Position Size:** [ % of Capital]

**Stop-Loss Price:** [ ]

**Take-Profit Level (1차):** [ ]

**Take-Profit Level (2차):** [ ]

**Hold Duration:** [ Months]

---

### 19. Investment Decision & Summary

**Overall Investment Thesis:**
[ ]

**Primary Investment Drivers:**
1. [ ]
2. [ ]
3. [ ]

**Key Risks:**
1. [ ]
2. [ ]
3. [ ]

**Price Targets:**
- **12-Month Target:** [ ]
- **24-Month Target:** [ ]
- **5-Year Target:** [ ]

**Final Recommendation:** 
**[STRONG BUY / BUY / HOLD / SELL]**

**Confidence:** [ /10]

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## PART IX: STRESS TESTERS (Hook 26-29)
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 20. Hook 26: FX Stress-Tester

**Currency Exposure:** [ ]

**FX Volatility (3Y):** [ %]

**Hedging Cost:** [ %]

**FX Impact on NOPAT (±20%):** [ %]

**FX-Adjusted WACC:** [ %]

---

### 21. Hook 27: Supply Chain Concentration Risk

**Top 3 Customers Revenue:** [ %]

**HHI Index:** [ ]

**Top 3 Suppliers Concentration:** [ %]

**Supply Chain Disruption Impact:** [ %]

**WACC Premium:** [ bps]

---

### 22. Hook 28: Regulatory, ESG & Carbon Penalty

**Regulatory Risk Score:** [ /100]

**ESG Risk Score:** [ /100]

**Expected Annual Penalty:** [ ]

**Carbon Intensity:** [ tCO₂/Revenue$]

**Valuation Discount (ESG):** [ %]

---

### 23. Hook 29: Liquidity Stress & Market Impact

**Average Daily Volume (ADV):** [ ]

**Bid-Ask Spread:** [ %]

**Liquidity Discount:** [ %]

**Adjusted Intrinsic Value:** [ ]

**Market Impact (10% position):** [ %]

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## PART X: ADAPTIVE MODULES (Module 6-7)
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 24. Module 6: Multi-Scenario Macro Stress Testing

**Base Case (3Y Forward):**
- Revenue Growth: [ %] CAGR
- EBIT Margin: [ %]
- Terminal ROIC: [ %]
- WACC: [ %]

**Stress Scenarios:**

| Metric | Bear (25%) | Base (50%) | Bull (25%) |
|--------|-----------|-----------|-----------|
| **GDP Growth** | [ %] | [ %] | [ %] |
| **Interest Rates (Δ)** | +[ %p] | 0% | -[ %p] |
| **Firm Revenue** | [ %] | [ %] | [ %] |
| **EBIT Margin** | [ %] | [ %] | [ %] |

**Scenario-Weighted Fair Value:**
- V_Bear: [ ]
- V_Base: [ ]
- V_Bull: [ ]

**Probability-Weighted Value:** [ ]

**Confidence Band (95%):** [ to [ ]

---

### 25. Module 7: Short-Squeeze & Tail-Risk Index

**Short Interest (% of Float):** [ %]

**Days-to-Cover:** [ ]

**Squeeze Risk Index:** [ ] (0-100)

**Tail-Risk Events (5 scenarios):**
- Event 1: -[ %] probability [ %]
- Event 2: -[ %] probability [ %]

**Tail-Risk Adjusted MoS:** [ %]

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## PART XI: NEGATIVE CATALYST SYSTEM
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 26. Negative Catalyst Detail (6개 위험 신호)

**1. Management & Governance Risk:** [ -30 to 0 points]
- CEO/CFO Change: [Yes / No]
- Related-Party Transactions: [Yes / No]

**2. Regulatory & Compliance Risk:** [ -30 to 0 points]
- Active Investigations: [Count: ___]
- Fine Probability: [ %]

**3. Technology & Competitive Risk:** [ -30 to 0 points]
- Patent Expiration: [Yes / No]
- Disruptive Threat: [ /10]

**4. Financial Stress & Debt Risk:** [ -30 to 0 points]
- Debt/EBITDA: [ x]
- Interest Coverage: [ x]

**5. Customer Concentration Risk:** [ -30 to 0 points]
- Top Customer Revenue: [ %]
- HHI Index: [ ]

**6. Operational & Supply Chain Risk:** [ -30 to 0 points]
- Supplier Concentration: [ %]
- WC Deterioration: [ %]

**Total Negative Catalyst Score:** [ -180 to 0 points]

**Adjusted Consensus:** [ %]

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## PART XII: MULTI-AGENT DEBATE & CROSS-CHECK
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 27. Bull Case Advocate

**Bull Thesis:** [ ]

**Key Arguments:** 1. [ ] 2. [ ] 3. [ ]

**Bull Parameters:**
- Revenue CAGR: [ %]
- Terminal ROIC: [ %]
- Exit Multiple: [ x]

**Bull Fair Value:** $[ ] | **Upside**: [ %]

---

### 28. Bear Case Advocate

**Bear Thesis:** [ ]

**Key Arguments:** 1. [ ] 2. [ ] 3. [ ]

**Bear Parameters:**
- Revenue CAGR: [ %]
- Terminal ROIC: [ %]
- Exit Multiple: [ x]

**Bear Fair Value:** $[ ] | **Downside**: [ %]

---

### 29. Risk Manager's Perspective

**Key Risk Factors (Ranked):**

| Risk | Probability | Impact | Mitigant |
|------|-------------|--------|----------|
| [ ] | [ %] | -[ %] | [ ] |
| [ ] | [ %] | -[ %] | [ ] |
| [ ] | [ %] | -[ %] | [ ] |

**Required MoS:** [ %]

**Risk Manager Signal:** [SUFFICIENT / MARGINAL / INSUFFICIENT]

---

### 30. 5-Point Cross-Check & Final Verification

**#1: Valuation Consensus**
- Hook 1-7: [ %]
- Hook 11-25: [ %]
- Module 1-7: [ %]
- Match: [YES / NO]

**#2: Catalyst Timing Alignment**
- Roadmap Events: [Q /  Year]
- Timing Alignment: [YES / NO]

**#3: Risk Factor Correlation**
- Negative Catalysts Penalty: [ pts]
- Hook 21-25 Penalty: [ pts]
- Correlation: [Aligned / Divergent]

**#4: Stop-Loss & Tail-Risk Coherence**
- ATR Stop-Loss: $[ ]
- Tail-Risk MoS: [ %]
- Coherence: [Aligned / Inconsistent]

**#5: Final Investment Signal Consensus**
- Bull Advocate: [STRONG BUY / BUY / HOLD / SELL]
- Bear Advocate: [STRONG BUY / BUY / HOLD / SELL]
- Risk Manager: [STRONG BUY / BUY / HOLD / SELL]
- **3-Agent Consensus:** [STRONG BUY / BUY / HOLD / SELL]

**Final Override Check:**
- Lollapalooza Trigger: [YES / NO]
- Result: [CRITICAL_AVOID / Proceed]

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## FINAL CHECKLIST (v10.2 VERIFICATION)
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- [ ] Part 0: Execution Mode 지정 완료
- [ ] Part I: 10Y 재무제표 입력 완성 (Fast-Pass 핵심 포함)
- [ ] Part II: 효율성 지표 완성
- [ ] Part III: 지배구조 평가 완성
- [ ] Part IV: R&D 자본화 완성
- [ ] Part V: 촉매 분석 완성
- [ ] Part VI: 시장 지표 완성
- [ ] Part VII: 거시경제 시나리오 완성
- [ ] Part VIII: Kelly Sizing & 최종 추천 완성
- [ ] Part IX: Hook 26-29 Stress Tester 완성
- [ ] Part X: Module 6-7 완성
- [ ] Part XI: Negative Catalyst 시스템 완성
- [ ] Part XII: Multi-Agent Debate 완성
- [ ] 현재가 및 유통주식수 실시간 확인 완료

---

**문서 작성 일시:** [ 2026-08-09 ]

**분석가:** [ Claude Investment Engine v10.2 APEX Pipeline ]

**다음 단계:** 이 v10.2 템플릿에 기업 데이터를 입력 → /auto (또는 /quick, /full) 모드로 자동 분석 시작
