# 🔬 Unified Investment Analysis Engine v10.1 (Part 1/3)
## Base Layer & Priority Hooks (Hook 1-10)
### Data Parsing → Priority Execution → Foundation Verification

**버전**: v10.1 APEX Modular Standard  
**모듈**: Part 1/3 - Base Layer & Priority Hooks  
**설명**: 재무 데이터 파싱 규약 → Priority Hooks (8,9,10) 실행 → Foundation Hooks (1-7) 검증

---

## 📋 MODULE LOADING PROTOCOL (문서 3분할 구조)

이 시스템은 **Lost in the Middle 문제를 해결**하기 위해 3개 독립 모듈로 분할됨:

| Part | 파일명 | 담당 영역 | Hooks | 예상 로딩 시간 |
|------|-------|---------|-------|-------------|
| **Part 1** | `hook_1.md` / `skill_1.md` | Base Layer | 1-10 | 5~7min |
| **Part 2** | `hook_2.md` / `skill_2.md` | Advanced Apex | 11-25 | 8~10min |
| **Part 3** | `hook_3.md` / `skill_3.md` | Adaptive & Output | Modules 1-5 | 6~8min |

**사용 규칙**: 
- 사용자 데이터 입력 → Part 1 로드 (Priority Hooks 8-10 즉시 실행)
- Part 1 검증 완료 → Part 2 로드 (Advanced Hooks 11-25)
- Part 2 완료 → Part 3 로드 (Adaptive Modules + Output Matrix 생성)

---

## 🎯 DATA PARSING & SECTOR-ROUTING PROTOCOL

### Step 1: Data Ingestion & Validation

사용자가 `analysis_ingredient.md` 형식으로 재무 데이터를 제공하면:

```markdown
[Ticker]: 005930.KS
[Company Name]: Samsung Electronics
[Sector]: Electronics (Technology Hardware)
[Financial Year]: 2025
[Currency]: KRW (한국원)

[Income Statement]
- Revenue: 245,000억원
- EBITDA: 52,000억원
- Net Income: 38,000억원
- Operating Profit: 48,000억원

[Balance Sheet]
- Total Assets: 455,000억원
- Total Liabilities: 185,000억원
- Shareholders' Equity: 270,000억원
- Current Assets: 125,000억원
- Current Liabilities: 95,000억원

[Cash Flow]
- Operating Cash Flow: 42,000억원
- CapEx (Capital Expenditure): 18,000억원
- Free Cash Flow: 24,000억원

[Key Metrics]
- Employees: 267,000명
- R&D Spending: 22,000억원 (매출의 9%)
```

### Step 2: Sector-Routing Decision Tree

```
입력 Sector 분석
  │
  ├─→ [Financials 분기 (금융업)]
  │    └─ 은행 (Banking) / 보험 (Insurance) / 증권 (Brokerage)
  │       → Financials-Specific Branch 실행 (NWC/CapEx Bypass)
  │
  ├─→ [Manufacturing 분기]
  │    └─ 자동차 / 반도체 / 화학 / 철강
  │       → Standard Branch 실행 (Hook 1-25 전체)
  │
  ├─→ [Software/Tech 분기]
  │    └─ SaaS / App / AI Platform
  │       → Tech-Specific Branch 실행 (CAC/LTV 강조)
  │
  └─→ [Retail/Consumer 분기]
       └─ 소매 / F&B / 온라인 커머스
          → Retail-Specific Branch 실행 (Working Capital 중심)
```

### Step 3: Financials Sector Exception Handler

**금융업 파싱 시 BYPASS 항목**:
- ❌ NWC (Net Working Capital): 금융업은 매출채권/재고 개념 없음
- ❌ CapEx: 금융기관의 물리적 자산투자는 ROIC 연산 외
- ❌ CCC (Cash Conversion Cycle): 금융업 비즈니스 모델 불부합

**금융업 대체 연산 경로**:

```
Financials 라우팅 규칙:

1. ROE (자기자본이익률) 중심 평가
   ROE = Net Income / Shareholders' Equity
   PASS 기준: ROE > 12% (정상) / > 15% (우수)

2. 자산건전성 지표 (Asset Quality)
   - NPL Ratio (부실채권비율) < 1% (양호)
   - LLR (Loan Loss Reserve) / Total Loans > 2% (충분)
   
3. 규제자본비율 (BIS Ratio / K-ICS)
   은행: BIS > 8% (법정 최소)
   보험: K-ICS > 100% (건전성)
   
4. NIM (순이자마진) / FLR (fixed-rate loan ratio)
   - NIM > 2.0%: 이자소득 충분
   - 금리상승 시나리오: FLR 분석
   
5. 그 외 연산: Hook 1-7, 21-25는 동일 적용
   (단, 매출액 대비 자산 규모 조정)
```

---

## 🔴 PRIORITY HOOKS (8, 9, 10) - IMMEDIATE EXECUTION

### ⚡ Hook 8: Dynamic WACC Modulator (동적 가중평균자본비용)

**목적**: 시간에 따라 변하는 자본비용을 정확히 반영하여 현재가치(DCF) 할인율 정의

**공식**:
$$WACC = K_e \cdot \frac{E}{V} + K_d \cdot (1 - T_c) \cdot \frac{D}{V}$$

**변수 정의**:
- $K_e$ = 자기자본비용 (Cost of Equity)
- $K_d$ = 타인자본비용 (Cost of Debt)  
- $T_c$ = 법인세율 (Corporate Tax Rate)
- $E$ = 자기자본 시장가치 (Equity Market Value)
- $D$ = 타인자본 시장가값 (Debt Market Value)
- $V$ = 기업 전체 가치 ($E + D$)

**Step 1: $K_e$ 계산 (CAPM)**

$$K_e = R_f + \beta \cdot (R_m - R_f)$$

**입력값 결정**:
- $R_f$ = 10년 만기 국고채 금리 (현재 대한민국: ~3.5%)
- $\beta$ = 주가 수익성 변동율 (과거 10년 회귀 분석)
- $R_m - R_f$ = 시장 리스크 프리미엄 (일반적으로 5~7%)

**계산 예시**:
```
Samsung Electronics (005930.KS):
- Rf = 3.5% (10년 국고채)
- β = 1.2 (반도체 업종 / 신흥국 프리미엄)
- (Rm - Rf) = 6.0% (한국 장기 평균)

Ke = 3.5% + 1.2 × 6.0% = 11.7%
```

**Step 2: $K_d$ 계산 (차입금 이자율)**

$$K_d = \frac{\text{Interest Expense}}{\text{Total Debt}}$$

**또는 (신용등급 기반)**:
```
Credit Rating → Spread 대입:
- AAA: 기준금리 + 100bps
- AA: 기준금리 + 150bps
- A: 기준금리 + 250bps
- BBB: 기준금리 + 400bps
- BB 이하: 기준금리 + 600bps 이상
```

**금융비용 조정** (ALM/이자율 구조 복잡도):
- 구조화 채권 / 하이브리드 채권 → 별도 분석
- 변동금리 부채 비중 높음 → 이자율 시나리오 분석 (선택)

**Step 3: E/V, D/V 계산**

```
V = Market Cap (주식 시가총액) + Net Debt (순채무)
   = 주가 × 발행주식수 + (총차입금 - 현금)

E/V = Market Cap / V
D/V = Net Debt / V
```

**Step 4: 법인세율 조정**

```
Tc = Effective Tax Rate (유효 법인세율)
   = Income Tax Paid / Pre-tax Income
   
또는
Tc = 법정 법인세율 (대한민국 기본: 22%)
   - 중소기업 할인 / 투자 세액공제 조정
```

**최종 WACC 계산**:

```
예시: Samsung Electronics
- Ke = 11.7%
- Kd = 3.8% (기업 평균 차입금리)
- Market Cap = 1,700조원
- Net Debt = 50조원
- V = 1,750조원
- E/V = 1,700/1,750 = 97.1%
- D/V = 50/1,750 = 2.9%
- Tc = 22% (법정)

WACC = 11.7% × 0.971 + 3.8% × (1-0.22) × 0.029
     = 11.36% + 0.086% 
     ≈ 11.4% (또는 11.5%)
```

**⚠️ 주의사항**:
- **고정 WACC 금지**: 매년 또는 시나리오별로 재계산 필수
- **금융업 적용 불가**: Financials Branch에서는 3-Banker Approach 사용
- **대출 이자율 변동 심한 경우**: Sensitivity Analysis 추가 필수

---

### ⚡ Hook 9: Exponential CAP Decay Engine (지수적 경쟁우위기간 감쇠기)

**목적**: 경제 해자(Moat)가 시간 경과에 따라 점진적으로 소멸되는 과정을 모델링

**공식**:
$$CAP(t) = CAP_{\text{base}} \times e^{-\lambda \cdot t}$$

**변수 정의**:
- $CAP(t)$ = $t$년 후의 경쟁우위 기간 (Competitive Advantage Period)
- $CAP_{\text{base}}$ = 현재 경쟁우위 기간 (기본값: 10~20년)
- $\lambda$ = 감쇠 속도 (Decay Rate) (기본값: 0.05~0.15 연 단위)
- $t$ = 연수 (1년, 2년, ... 10년)

**Step 1: $CAP_{\text{base}}$ 결정**

업종 및 해자 강도별 기본값:

```
강한 해자 (Strong Moat):
- 브랜드/특허 (Apple, Coca-Cola): 15~20년
- 네트워크효과 (Meta, 카카오톡): 12~18년

중간 해자 (Moderate Moat):
- 규모의 경제 (삼성, LG): 8~12년
- 고객 전환비용 (금융 서비스): 7~10년

약한 해자 (Weak Moat):
- 상품 차별화 낮음 (도매/유통): 3~6년
- 경쟁 심함 (명확한 해자 없음): 1~3년
```

**Step 2: $\lambda$ (감쇠율) 결정**

```
결정 요인:
1. 경영 지속성 (Management Stability)
   - CEO 장기근속: λ 하향 (-30%)
   - 경영진 자주 교체: λ 상향 (+50%)

2. R&D 투자 효율성
   - 매출 대비 R&D > 5%: λ 하향 (-20%)
   - 매출 대비 R&D < 2%: λ 상향 (+30%)

3. 특허 만료 스케줄
   - 핵심 특허 5년 내 만료: λ 상향 (+40%)
   - 특허 갱신/연장 계획: λ 유지

4. 산업 기술 변화 속도
   - 급변 (AI/바이오): λ = 0.12~0.15
   - 중간 (화학/자동차): λ = 0.08~0.10
   - 안정 (금융/기반시설): λ = 0.03~0.06

기본 공식:
λ = 0.08 × (1 + Adjustment Factors)
```

**Step 3: CAP 감쇠 시뮬레이션**

```
예시: Samsung Electronics
- CAP_base = 12년 (강-중간 해자)
- λ = 0.08 (표준)

연도별 CAP(t):
- t=0: CAP = 12.0년
- t=1: CAP = 12.0 × e^(-0.08×1) = 11.1년
- t=3: CAP = 12.0 × e^(-0.08×3) = 9.4년
- t=5: CAP = 12.0 × e^(-0.08×5) = 8.0년
- t=10: CAP = 12.0 × e^(-0.08×10) = 5.4년

해석: 
- 현재 해자 강도(12년) → 5년 후 약화(8년) → 10년 후 크게 약화(5.4년)
- NOPAT 감소 경로 설정: CAP 기간 동안만 ROIC > WACC, 이후 ROIC = WACC
```

**Step 4: NOPAT 급락 구간 설정 (Value Destruction)**

```
해자 급락 시 내재가치 손실 계산:
V_moat_loss = Σ(t=CAP_end to 10) 
              [NOPAT(t) × (ROIC(t) - WACC) / (1+WACC)^t]

예: CAP 종료(t=8) 이후
- t=8~10: ROIC = WACC → 추가 초과수익 없음
- DCF 할인현재가치 하락
```

**⚠️ 주의사항**:
- **해자 없는 기업은 λ를 대폭 상향** (0.15~0.20)
- **특허 기반 기업**: 특허 만료일 명시적 반영
- **10년 이상 CAP 금지**: 최소 가정은 t=10년에 CAP → 0 (모든 해자 소멸)

---

### ⚡ Hook 10: Normalized NWC Synchronizer (정규화 운전자본 동기화기)

**목적**: 경기 사이클 변동을 제거한 평년 기준 운전자본(Net Working Capital) 산정 → Owner Earnings 정확화

**공식 1: 정규화 NWC 비율 계산**

$$\text{Normalized NWC/Sales Ratio} = \frac{1}{5} \sum_{k=1}^{5} \frac{NWC_{t-k}}{Revenue_{t-k}}$$

**변수 정의**:
- $NWC_t$ = Current Assets − Current Liabilities − Cash
- $Revenue_t$ = 매출액 (연간)
- $t$ = 현재연도
- $k$ = 1, 2, 3, 4, 5 (과거 5년)

**Step 1: 역사 NWC 데이터 수집 (5년)**

```
예시: Samsung Electronics (KRW 100억 기준)

연도     |  Current Assets | Current Liabilities | NWC | Revenue | NWC/Sales %
---------|-----------------|---------------------|-----|---------|------------
2020     |  12,500         |  9,500              | 3,000| 22,200  | 13.5%
2021     |  13,200         |  9,800              | 3,400| 23,500  | 14.5%
2022     |  14,100         |  10,200             | 3,900| 24,200  | 16.1%
2023     |  13,800         |  10,100             | 3,700| 24,800  | 14.9%
2024     |  13,500         |  9,900              | 3,600| 24,500  | 14.7%

Normalized NWC/Sales = (13.5+14.5+16.1+14.9+14.7) / 5 = 14.7%
```

**Step 2: 정규화된 ∆NWC 계산**

$$\text{Normalized } \Delta NWC_t = (\text{정규화 비율}) \times \text{Revenue}_t - NWC_{t-1}$$

```
예시 (2025년 전망):
- 2025 Revenue Forecast: 25,500억원
- Normalized NWC/Sales = 14.7%
- Target NWC (2025) = 25,500 × 14.7% = 3,749억원
- NWC (2024 실제) = 3,600억원

Normalized ∆NWC(2025) = 3,749 - 3,600 = +149억원
(= 2025 free cash flow에서 차감)
```

**Step 3: Owner Earnings 연산 (Buffett 공식)**

$$\text{Owner Earnings} = \text{Net Income} + \text{D\&A} - \text{Maintenance CapEx} - \text{Normalized } \Delta NWC$$

```
Samsung Electronics (2025 예상):
- Net Income: 38,000억원
- D&A (감가상각): 12,000억원
- Maintenance CapEx (추정): 15,300억원 (= 0.85 × 18,000)
- Normalized ∆NWC: +149억원

Owner Earnings = 38,000 + 12,000 - 15,300 - 149
               = 34,551억원
```

**Step 4: ∆NWC 트랩 감지 (Value Trap Override)**

```
위험 신호 (∆NWC 폭증):
- Normalized ∆NWC > Normalized ∆NWC(t-1) × 1.5: 적신호
- 2년 연속 ∆NWC > 0: 운전자본 악화 경향

예: 2024년 +200억원 → 2025년 +500억원 (2.5배 증가)
    → CRITICAL_CASH_TRAP 플래그 (내재가치 -30% 감점)
```

**⚠️ 주의사항**:
- **비정상적 연도는 제외**: 대규모 M&A/구조조정 연도 제외 후 재계산
- **산업 특성 고려**: 외상매출금/재고 수준이 높은 산업 (도매/유통) 특별히 모니터
- **통화 변동 조정**: 다국적 기업은 연결 대차대조표 기준으로 환산

---

## 🟢 FOUNDATION HOOKS (1-7) - SEQUENTIAL VERIFICATION

### Hook 1: Dual-Mode Capital Adequacy & Asset Degradation (동적 보유가치)

**목적**: 기업의 장부 가치 왜곡과 불경기 마진 함수를 통한 하방 경고치(보수적 안전마진) 검증

**공식 1: 제조/소매업**

$$NCAV_{\text{dynamic}} = (CurrentAssets \times 0.8) - TotalLiabilities$$

**공식 2: 금융업 (Bypass)**

$$CapitalRatio = \frac{Equity}{TotalAssets} \geq 8\%$$

**PASS 조건**:
```
1. NCAV_dynamic > 0 (유동자산이 채무 커버 가능)
2. Debt/Equity < 100% (레버리지 과도하지 않음)
3. Current Ratio > 1.5x (단기 유동성 충분)
```

**계산 예시**:
```
Samsung Electronics:
- Current Assets: 125,000억원
- Total Liabilities: 185,000억원

NCAV = (125,000 × 0.8) - 185,000
     = 100,000 - 185,000 = -85,000억원 (음수)

→ FAIL (극도의 차용 과다)

하지만 Samsung은 ROIC > WACC로 보상되므로 예외 처리
```

---

### Hook 2: Double-Path Consensual Moat Evaluation (이중경로 해자 검증)

**목적**: 경제적 해자의 물리적 소멸 과정 & 경제적 가치 소멸 추적

**공식**:

$$\frac{d(ROIC)}{dt} = -\kappa(ROIC(t) - WACC) + \Phi(\text{Moat})$$

**PASS 조건**:
$$\Phi(\text{Moat}) \geq \kappa(ROIC - WACC)$$

해석: 해자의 지속력($\Phi$)이 경쟁 침식 속도($\kappa$)를 상쇄하면 PASS

---

### Hook 3-7: (Part 1 요약 생략)

* Hook 3: 정성적 MECE 마진 & 성장 안정성 (75% 이상 통과)
* Hook 4: 경영 & 거버넌스 정렬 (EBITDA 기반 보수 체계)
* Hook 5-6: L_score 커플링 (SDI & PPI 분석)
* Hook 7: 변동성 조정 안전마진 (MoS_required ≥ Current MoS)

---

## <thought_process>

**Part 1 검증 체크리스트** (최종 Output 생성 전 필수):

### Phase 1: Data Parsing & Sector-Routing ✓
- [ ] 입력 데이터 완전성 확인 (Income/Balance/Cash Flow 모두 존재)
- [ ] Sector 분류 완료 (Financials vs Non-Financials)
- [ ] 금융업 라우팅 여부 판단

### Phase 2: Priority Hooks 8-10 ✓
- [ ] Hook 8 WACC: Ke 계산 + Kd 조정 + E/V, D/V 결정 + 최종 WACC 산출
  * 예시: WACC = 11.4% ✓
- [ ] Hook 9 CAP Decay: CAP_base 선정 + λ 결정 + t=3,5,10 시뮬레이션
  * 예시: t=5년 후 CAP = 8.0년 ✓
- [ ] Hook 10 NWC: 5년 역사 평균 + ∆NWC 정규화 + Owner Earnings 계산
  * 예시: Normalized ∆NWC = +149억원 → Owner Earnings = 34,551억원 ✓

### Phase 3: Foundation Hooks 1-7 ✓
- [ ] Hook 1 NCAV: PASS/FAIL 판정
- [ ] Hook 2 Moat: Φ vs κ 비교
- [ ] Hooks 3-7: 각 지표 산출 (최종 예비 저장)

### Phase 4: Output Formatting ✓
- [ ] Part 2 로드 여부 사용자에게 확인
- [ ] 모든 수치 한국어 통화(억원) 또는 % 표기 통일

</thought_process>

---

## 📌 Part 1 완료 체크리스트

- [x] Data Parsing & Validation 규약 명시
- [x] Sector-Routing Tree (금융업 예외 처리) 완성
- [x] Hook 8 (Dynamic WACC) 상세 연산
- [x] Hook 9 (CAP Decay) 수식 + 시뮬레이션
- [x] Hook 10 (Normalized NWC) Owner Earnings 연동
- [x] Foundation Hooks 1-7 요약 (상세는 별도)
- [x] Chain-of-Thought 검증 태그 추가

---

## 🔜 다음 단계

**Part 2 로드 조건**:
- Part 1의 Hooks 8-10 모두 완료
- Foundation Hooks 1-7 상태 확인 (최소 3/7 PASS)

**Part 2 내용** (hook_2.md / skill_2.md):
- Advanced Hooks 11-14 (v6.0)
- Institutional Apex Hooks 21-25 (v8.0)
- 3-Philosopher Consensus Model
- Lollapalooza Override Matrix

---

**작성 완료**: 2026-07-29  
**버전**: v10.1 APEX Modular  
**모듈**: Part 1/3 (Base Layer & Priority Hooks)
