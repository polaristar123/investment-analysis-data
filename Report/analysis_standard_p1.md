# 🔬 버크셔 해서웨이 스타일 통합 재무제표 분석 보고서 표준 (v10.1 APEX)
## Part 1: Base Layer & Priority Hooks (Hook 1~10)
### 데이터 파싱 · 우선 실행 모듈 · 기초 검증 표준 (Claude `.md` 규약)

---

## 1. 개요 및 실행 프로토콜 (Module Loading Protocol)

본 가이드는 **Lost in the Middle** 방지 및 대규모 데이터의 엄밀한 처리를 위해 3단계 독립 모듈 구조로 구성됩니다. 사용자가 입력한 재무제표 데이터를 바탕으로 우선 실행 항목(Priority Hooks 8-10)을 선제 연산한 후, 기초 검증(Foundation Hooks 1-7)을 진행합니다.

### 1.1 문서 분할 및 실행 순서
| 단계 | 모듈 파일 | 담당 영역 | 대상 Hooks | 권장 로딩 및 연산 시간 |
| :--- | :--- | :--- | :--- | :--- |
| **Part 1** | `analysis_standard_p1.md` | Base Layer & Priority | Hooks 1–10 | 5~7분 |
| **Part 2** | `analysis_standard_p2.md` | Advanced & Institutional | Hooks 11–25 | 8~10분 |
| **Part 3** | `analysis_standard_p3.md` | Adaptive Engine & Final Output | Modules 1–5 & Output Matrix | 6~8분 |

---

## 2. 데이터 파싱 및 섹터 라우팅 프로토콜 (Data Parsing & Sector Routing)

### 2.1 표준 데이터 입력 형식 (`analysis_ingredient.md`)
분석 실행 시 아래와 같은 형식으로 재무제표 기본 정보가 공급되어야 합니다.

```markdown
[Ticker]: 005930.KS
[Company Name]: 삼성전자 (Samsung Electronics)
[Sector]: Electronics (Technology Hardware / Semiconductor)
[Financial Year]: 2025
[Currency]: KRW (억원)

[Income Statement]
- Revenue (매출액): 245,000
- EBITDA: 52,000
- Operating Profit (영업이익): 48,000
- Net Income (당기순이익): 38,000

[Balance Sheet]
- Total Assets (총자산): 455,000
- Total Liabilities (총부채): 185,000
- Shareholders' Equity (자기자본): 270,000
- Current Assets (유동자산): 125,000
- Current Liabilities (유동부채): 95,000

[Cash Flow]
- Operating Cash Flow (영업활동현금흐름): 42,000
- CapEx (자본적지출): 18,000
- Free Cash Flow (잉여현금흐름): 24,000

[Key Metrics & Context]
- Employees: 267,000명
- R&D Expense: 22,000 (매출의 9.0%)
```

### 2.2 섹터 라우팅 디시전 트리 (Sector-Routing Decision Tree)
```
입력 데이터 섹터 감지
  │
  ├─→ [Financials (금융업): 은행 / 보험 / 증권]
  │    └─→ Financials Branch 실행 (NWC, CapEx, CCC Bypass 연산 적용)
  │
  ├─→ [Manufacturing (제조업): 반도체 / 자동차 / 화학 / 철강]
  │    └─→ Standard Branch 실행 (Hook 1–25 전 과정 표준 연산)
  │
  ├─→ [Software / Tech (기술/플랫폼): SaaS / AI / App]
  │    └─→ Tech Branch 실행 (CAC, LTV, Soft Moat 가중치 부여)
  │
  └─→ [Retail / Consumer (유통/소비재): 소매 / F&B / 이커머스]
       └─→ Retail Branch 실행 (운전자본 efficiency 및 회전율 집중)
```

### 2.3 금융업 예외 처리 핸들러 (Financials Sector Exception Handler)
* **Bypass 항목**: NWC(순운전자본), CapEx(자본적 지출), CCC(현금전환주기)는 개념 구조상 산출 대상에서 제외합니다.
* **대체 검증 경로**:
  1. **ROE 중심 평가**: $ROE = rac{	ext{Net Income}}{	ext{Shareholders' Equity}}$ (기준: $> 12\%$ 정상, $> 15\%$ 우수)
  2. **자산건전성**: NPL Ratio $< 1.0\%$, 대손충당금적립률(LLR) $> 2.0\%$
  3. **규제자본비율**: BIS 비율 $> 8\%$, K-ICS 비율 $> 100\%$
  4. **순이자마진(NIM)**: NIM $> 2.0\%$ 및 금리 변동 시나리오 분석

---

## 3. 우선 실행 항목: Priority Hooks (8, 9, 10)

### ⚡ Hook 8: Dynamic WACC Modulator (동적 가중평균자본비용 엔진)
시간의 흐름 및 금리 환경 변화에 따른 자본비용을 동적으로 반영합니다.

$$	ext{WACC} = K_e \cdot rac{E}{V} + K_d \cdot (1 - T_c) \cdot rac{D}{V}$$

* **자기자본비용 ($K_e$) (CAPM)**:
  $$K_e = R_f + eta \cdot (R_m - R_f)$$
  * $R_f$: 10년 만기 국고채 금리 (기본값: $3.5\%$)
  * $eta$: 주가 변동성 베타 계수 (업종/기업 고유값)
  * $R_m - R_f$: 시장 리스크 프리미엄 (기본값: $6.0\%$)
* **타인자본비용 ($K_d$)**:
  $$K_d = rac{	ext{Interest Expense}}{	ext{Total Debt}}$$
* **기업가치 ($V$)**: $V = E + D = 	ext{Market Cap} + 	ext{Net Debt}$

```python
# WACC 연산 예시 (삼성전자 기준)
Rf = 0.035
Beta = 1.2
MRP = 0.060
Ke = Rf + Beta * MRP  # 11.7%

Kd = 0.040  # 평균 차입금리 4.0%
Market_Cap = 17000000  # 시가총액 (억원)
Net_Debt = 500000     # 순채무 (억원)
V = Market_Cap + Net_Debt

E_weight = Market_Cap / V  # 97.1%
D_weight = Net_Debt / V    # 2.9%
Tc = 0.22                  # Effective Tax Rate 22%

WACC = (Ke * E_weight) + (Kd * (1 - Tc) * D_weight)
# WACC = 11.36% (보수적 적용: 11.4%)
```

---

### ⚡ Hook 9: Exponential CAP Decay Engine (지수적 경쟁우위기간 감쇠 엔진)
경쟁자 침입에 의해 기업의 경제적 해자(Moat)가 감쇠하는 유기적 과정을 모델링합니다.

$$	ext{CAP}(t) = 	ext{CAP}_{	ext{base}} 	imes e^{-\lambda \cdot t}$$

* $	ext{CAP}_{	ext{base}}$: 현재 해자 수준에 따른 기준 기간 (Strong Moat: 15~20년, Moderate: 8~12년, Weak: 3~6년)
* $\lambda$ (감쇠 속도): $\lambda = 0.08 	imes (1 + \Delta_{	ext{management}} + \Delta_{	ext{RnD}} + \Delta_{	ext{patent}} + \Delta_{	ext{tech}})$

```
[감쇠 계수 조정 가이드]
- 경영진 안정성: 장기 근속(-30%) / 자주 교체(+50%)
- R&D 비중: 매출 대비 > 5% (-20%) / < 2% (+30%)
- 특허 만료: 5년 이내 핵심 특허 만료 (+40%)
- 기술 변화 속도: 급변 급속(AI/바이오, λ=0.12~0.15) / 고전적 안정(기반시설/금융, λ=0.03~0.06)
```

---

### ⚡ Hook 10: Normalized NWC Synchronizer (정규화 운전자본 동기화 및 주주이익 연산)
경기 사이클에 따른 순운전자본(NWC) 왜곡을 제거하여 버크셔 해서웨이 방식의 주주이익(Owner Earnings)을 산출합니다.

$$	ext{Normalized NWC/Sales Ratio} = rac{1}{5} \sum_{k=1}^{5} rac{	ext{NWC}_{t-k}}{	ext{Revenue}_{t-k}}$$

$$	ext{Normalized } \Delta 	ext{NWC}_t = (	ext{Normalized Ratio}) 	imes 	ext{Revenue}_t - 	ext{NWC}_{t-1}$$

$$	ext{Owner Earnings} = 	ext{Net Income} + 	ext{D\&A} - 	ext{Maintenance CapEx} - 	ext{Normalized } \Delta 	ext{NWC}$$

```
[Owner Earnings 산출 예시]
- Net Income: 38,000억원
- D&A: 12,000억원
- Maintenance CapEx (추정): 15,300억원 (= max(D&A, 0.85 × Total CapEx))
- Normalized ∆NWC: +149억원

Owner Earnings = 38,000 + 12,000 - 15,300 - 149 = 34,551억원
```

---

## 4. 기초 검증 항목: Foundation Hooks (1–7)

1. **Hook 1: Dynamic Net Current Asset Value (동적 보유가치 검증)**
   $$	ext{NCAV}_{	ext{dynamic}} = (	ext{Current Assets} 	imes 0.8) - 	ext{Total Liabilities}$$
   * PASS 조건: $	ext{NCAV}_{	ext{dynamic}} > 0$ 또는 $	ext{ROIC} > 	ext{WACC}$ 보상 구조 충족.
2. **Hook 2: Double-Path Consensual Moat Evaluation (이중경로 해자 검증)**
   $$rac{d(	ext{ROIC})}{dt} = -\kappa(	ext{ROIC}(t) - 	ext{WACC}) + \Phi(	ext{Moat})$$
   * PASS 조건: 해자의 지속력 $\Phi(	ext{Moat})$이 침식 속도 $\kappa$ 이상일 것.
3. **Hook 3: Qualitative Margin & Growth Stability (마진/성장 안정성)**: 과거 5년 마진 변동성 계수(CV) $< 0.25$ 검증.
4. **Hook 4: Governance & Executive Alignment (거버넌스 체계)**: 경영진 보상 체계의 ROIC/EBITDA 연동성 검증.
5. **Hook 5–6: L_score Structural Coupling (구조적 결합도)**: 주식 희석 지수(SDI) 및 가격 결정력 지수(PPI) 검증.
6. **Hook 7: Volatility-Adjusted Margin of Safety (변동성 조정 안전마진)**: 요구 안전마진과 현재 주가 격차 비교.

---

## 5. Part 1 검증 및 통과 체크리스트

```markdown
[ Part 1 필수 검증 체크리스트 ]
- [ ] 입력 데이터 완전성 및 3대 재무제표 수치 합치성 확인
- [ ] 금융업 여부에 따른 Sector-Routing 적용 완료
- [ ] Hook 8 WACC 연산 완료 (Ke, Kd, E/V, D/V 확정)
- [ ] Hook 9 CAP Decay 시뮬레이션 완료 (t=3, 5, 10)
- [ ] Hook 10 Normalized NWC 및 Owner Earnings 연산 완료
- [ ] Foundation Hooks 1–7 최소 5개 이상 PASS 판정 확인

☞ 위 조건이 모두 완결되면 'Part 2: Advanced & Institutional Layer'를 로드합니다.
```
