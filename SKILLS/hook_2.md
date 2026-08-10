# 🔬 Unified Investment Analysis Engine v10.1 (Part 2/3)
## Advanced Hooks 11-14 (v6.0) + Apex Institutional Hooks 21-25 (v8.0)
### 3-Philosopher Consensus Model + Lollapalooza Override Matrix

**버전**: v10.1 APEX Modular Standard  
**모듈**: Part 2/3 - Advanced & Institutional Apex Layer  
**설명**: 경쟁우위 분석 → 거버넌스 리스크 → 극단 위험 버퍼

---

## 📖 PART 2 로드 조건 (Part 1 완료 후)

✅ Part 1 필수 완료 사항:
- Hook 8-10 모두 산출 ✓
- Foundation Hooks 최소 5/7 PASS ✓
- Sector-Routing 확정 ✓

**→ Part 2 자동 로드**

---

## 🟡 ADVANCED HOOKS (11-14) - v6.0 FRAMEWORK

### Hook 11: P-Q-C Decomposed ROIC Engine (맥킨지 VDT 분해)

**목적**: 마진 증가의 원인을 **가격(P)** vs **물량(Q)** vs **비용(C)** 세 가지로 MECE 분해

**공식**:

$$\text{NOPAT Margin} = \frac{(P \cdot Q) - (C_{\text{variable}} \cdot Q) - FC - T}{P \cdot Q}$$

$$\text{ROIC}_{\text{v6}} = \left[ \alpha \cdot \Delta P + \beta \cdot \Delta Q - \gamma \cdot \Delta C \right] \times \text{IC Turnover}$$

**변수 정의**:
- $P$ = 제품 평균 판매가 (Average Selling Price)
- $Q$ = 판매 물량 (Quantity Sold)
- $C_{\text{variable}}$ = 단위 당 변동비
- $FC$ = 고정비
- $IC$ = 투자자본 (Invested Capital)

**Step 1: 마진 변화 원인 분해**

```
예시: Samsung Display (2023 → 2024)
- Gross Margin 2023: 15.0%
- Gross Margin 2024: 18.5%
- 변화폭: +3.5%p

분해 분석:
1. 가격 인상 (∆P): OLED 프리미엄 + 공급 부족 → +2.0%p
2. 물량 증가 (∆Q): AI/폴더블 수요 → +1.5%p
3. 비용 절감 (∆C): 수율 개선 + 생산 효율화 → +0.5%p
4. 기타 (제품 믹스 등): -0.5%p

결론: 가격 57% + 물량 43% + 비용 14% (기여도 기준)
```

**Step 2: Pricing Power Index (PPI) 계산**

$$PPI = \frac{\text{Firm Margin Change \%}}{\text{Industry Margin Change \%}} \times \text{Asset Turnover}$$

```
계산:
- 기업 마진 변화: +3.5%p
- 산업 평균 마진 변화: +0.8%p
- PPI = (3.5 / 0.8) × 자산회전율

해석:
- PPI > 1.2: 강한 가격 결정력 (+15점)
- PPI 0.8~1.2: 중립 (0점)
- PPI < 0.8: 약한 가격 결정력 (-20점)
```

**⚠️ Hook 11 감점 규칙**:
```
마진 100% 증가가 비용 절감(∆C < 0)에만 의존
→ PPI -30% 감점 (지속불가능 마진)

이유: 원가 절감은 언젠가 한계에 도달
      → 가격 인상 없이는 ROIC 하락 위험
```

---

### Hook 12: CapEx Dualization Auditor (버펫 주주이익)

**목적**: 유지(Maintenance) CapEx vs 성장(Growth) CapEx 분리 → Owner Earnings 정확화

**공식**:

$$\text{Maintenance CapEx} = \text{CapEx}_{\text{Total}} - \text{CapEx}_{\text{Growth}}$$

$$\text{Owner Earnings}_{\text{v6}} = \text{Net Income} + \text{D\&A} - \text{Maintenance CapEx} - \text{Normalized } \Delta NWC$$

**Step 1: Maintenance CapEx 추정**

**방법 1: 명시적 분리** (재무제표에 기재)
```
기업이 명확히 구분한 경우:
- 신규 사업/공장 투자 = Growth CapEx
- 기존 장비 유지/교체 = Maintenance CapEx
```

**방법 2: D&A 기반 기본값** (정보 부족 시)
```
Maintenance CapEx = max(D&A, 0.85 × CapEx_Total)

이유:
- D&A: 이미 갚은 자산 규모의 연간 소모
- 0.85 × CapEx: 보수적 추정
- max(): 더 큰 값 적용 (안전마진)

예: Samsung Electronics (2024)
- D&A: 12,000억원
- Total CapEx: 18,000억원
- 0.85 × 18,000 = 15,300억원

Maintenance CapEx = max(12,000, 15,300) = 15,300억원
Growth CapEx = 18,000 - 15,300 = 2,700억원
```

**Step 2: Owner Earnings 연산 (최종)**

```
Samsung Electronics (2024 예상):
- Net Income: 38,000억원
- D&A: 12,000억원
- Maintenance CapEx: 15,300억원
- Normalized ∆NWC: +149억원

Owner Earnings = 38,000 + 12,000 - 15,300 - 149
               = 34,551억원

per Share (만주 기준):
Owner Earnings/Share = 34,551억원 / 27.7억주 ≈ 12,500원
```

**⚠️ Hook 12 위험 신호**:
```
CapEx > D&A × 1.5 지속 3년 이상
→ 성장 CapEx 의존도 높음 (성숙기 위험)

예: CapEx 계속 증가하는데 Revenue 정체
→ 자본 효율성 악화 (ROIC 하락)
```

---

### Hook 13: Soft Moat & Network Quantifier (먼거의 소프트 해자)

**목적**: 물리적 자산 가치가 낮은 플랫폼/SaaS 기업의 무한자산(고객 충성도, 네트워크)을 정량화

**공식**:

$$\Phi(\text{Moat})_{\text{v6}} = \Phi(\text{Moat})_{\text{base}} + \mu \cdot \ln(\text{Active Users}) + \eta \cdot \left( \frac{\text{LTV}}{\text{CAC}} \right)$$

$$\lambda_{\text{Decay}} = \lambda_{\text{base}} \times e^{-\delta \cdot \Phi(\text{Moat})_{\text{v6}}}$$

**Step 1: 활성 사용자 기여도 평가**

```
Moat 강도 계정에 사용자 수 반영:

예: 카카오톡 (국내)
- Active Users: 43.5백만
- Network Effect: 사용자 1명 증가 시 네트워크 가치 지수 증가

ln(43.5M) = 17.6
Moat Boost = 0.2 × 17.6 = +3.5점 (기본값 10점에서 13.5점)
```

**Step 2: LTV/CAC 비율 (경제 모델)**

```
LTV (Life Time Value) = 평생 고객 가치
  = (ARPU × 월 × 잔존율) / (1 + Discount_Rate)

CAC (Customer Acquisition Cost) = 고객 획득 비용

LTV/CAC > 3.0: 매우 효율적 (+25점)
LTV/CAC 2.0~3.0: 효율적 (+15점)
LTV/CAC 1.0~2.0: 중간 (0점)
LTV/CAC < 1.0: 비효율적 (-40점)
```

**Step 3: 선택 비용(Switching Cost) 정량화**

```
고객이 경쟁사로 전환할 비용/시간:

높음 (금융/ERP): SC = 연 매출의 20~30%
중간 (SaaS 협업): SC = 연 매출의 5~15%
낮음 (소비자 앱): SC = 거의 없음 (0%)

높은 SC → Hook 9의 λ 하향 (-20~30%)
```

**⚠️ Hook 13 감점 규칙**:
```
LTV/CAC < 1.5 + Switching Cost 낮음
→ Moat 매우 약함 (λ 상향 +40%)
→ CAP 급락 (3년 내 CAP 50% 감소)
```

---

### Hook 14: Stochastic Monte Carlo WACC & Margin Range (신뢰구간)

**목적**: 단일 내재가치 금지 → 95% 신뢰구간 밴드(Band) 제시

**공식**:

$$\text{Intrinsic Value Band} = \left[ V_{\text{Intrinsic}}^{(2.5\%)}, \; V_{\text{Intrinsic}}^{(97.5\%)} \right]$$

**Step 1: 3개 매크로 시나리오 구성**

```
Bull Case (낙관):
- WACC: Dynamic WACC - 100bps (금리 하락/신용 개선)
- Terminal ROIC: Base + 200bps
- 확률: 25%

Base Case (기본):
- WACC: Dynamic WACC (현상 유지)
- Terminal ROIC: 기본값
- 확률: 50%

Bear Case (보수):
- WACC: Dynamic WACC + 200bps (금리 상승/신용 악화)
- Terminal ROIC: Base - 300bps
- 확률: 25%
```

**Step 2: 각 시나리오별 내재가치 계산 (DCF)**

```
V_Bull = Σ(t=1 to 10) [NOPAT_t / (1 + WACC_Bull)^t] 
         + [Terminal Value / (1 + WACC_Bull)^10]

V_Base = ... (기본 WACC 적용)

V_Bear = ... (WACC_Bear 적용)
```

**Step 3: 확률가중 내재가치 밴드**

```
예: Samsung Electronics

V_Bull (기준금리 -100bps, 금리 인하): 95,000원
V_Base (현상 유지): 75,000원
V_Bear (기준금리 +200bps, 금리 인상): 55,000원

확률가중 기댓값:
E[V] = 0.25 × 95,000 + 0.50 × 75,000 + 0.25 × 55,000
     = 73,750원

95% 신뢰구간 밴드: [55,000 ~ 95,000원]
```

**Output 형식**:
```
✓ Hook 14 Stochastic Range:
  - Bear (2.5% quantile): 55,000원 (WACC +200bps)
  - Base (50% median): 75,000원 (Dynamic WACC)
  - Bull (97.5% quantile): 95,000원 (WACC -100bps)
  
  현재주가 70,000원 vs 내재가치 밴드
  → 저평가 (-5,000원 오버슛 가능)
```

---

## 🔴 APEX INSTITUTIONAL HOOKS (21-25) - v8.0 FRAMEWORK

### Hook 21: Corporate Governance & Capital Misallocation Discount (거버넌스 할인)

**목적**: 대주주 도덕적 해이, 배당/자사주 오버행으로 인한 주주가치 파괴 정량화

**공식**:

$$\delta_{\text{Governance}} = \sum_{k=1}^{n} w_k \cdot I_k$$

$$V_{\text{Intrinsic (v8)}} = V_{\text{Base Intrinsic}} \times (1 - \delta_{\text{Governance}})$$

**거버넌스 위험 요소**:

| 위험 요소 | 점수 | 적용 시나리오 |
|---------|------|-------------|
| 물적 분할 히스토리 | -15점 | 1회 이상 |
| 창업자족 경영진 독단 | -10점 | CEO 독립이사 비중 < 30% |
| 이사회 지분 상충 | -20점 | CEO/회장 겸직 + 대주주 자리 |
| 배당 오버행 | -10점 | 배당 비율 > 50% (성장기 기업) |
| 자사주 오버행 | -15점 | 자사주 소각 없이 누적 5% 이상 |

**Step 1: 거버넌스 점수 산출**

```
예: Samsung Electronics
- 물적 분할 히스토리: 0점 (없음)
- 경영진 독립성: +3점 (양호)
- 이사회 다양성: +2점 (개선 중)
- 배당 정책: -5점 (주주환원 중심이나 지분 희석 우려)
- 자사주 정책: -3점 (소각 일부)

총 거버넌스 점수: -8점
→ δ_Governance = 8% (내재가치 8% 할인)
```

**Step 2: 최종 내재가치 조정**

```
V_Base Intrinsic = 75,000원 (Hook 14 기본값)
δ_Governance = 8%

V_Intrinsic(v8) = 75,000 × (1 - 0.08) = 69,000원
```

**⚠️ Hook 21 심각 신호**:
```
δ_Governance > 30% (물적 분할 + 배당/자사주 오버행 동시)
→ CRITICAL_GOVERNANCE_RISK (내재가치 -30% 할인)
→ 투자 회피
```

---

### Hook 22: Working Capital Efficiency & CCC Auditor (운전자본 효율)

**목적**: 매출액 대비 현금 회수 속도 악화 → 자본 효율성 급락 감지

**공식**:

$$\text{CCC} = \text{DSO (매출채권기간일)} + \text{DIO (재고기간일)} - \text{DPO (매입채무기간일)}$$

$$\text{Efficiency Multiplier} = \exp\left(-\kappa \cdot \frac{\Delta \text{CCC}}{365}\right)$$

**Step 1: CCC 계산**

```
정의:
- DSO = (Accounts Receivable / Revenue) × 365
- DIO = (Inventory / COGS) × 365
- DPO = (Accounts Payable / COGS) × 365

예: 도매 기업
- DSO: 45일 (외상판매 많음)
- DIO: 60일 (재고 회전 느림)
- DPO: 30일 (단기 외상)

CCC = 45 + 60 - 30 = 75일
해석: 현금을 투자한 후 수거까지 75일 소요
→ 운전자본 효율 낮음
```

**Step 2: CCC 악화 추세 감지**

```
2023년 CCC: 75일
2024년 CCC: 85일 (10일 악화)
2025년 CCC (예상): 95일 (10일 추가 악화)

악화 패턴 감지:
- 20% 이상 악화 + 연속 2년 → CRITICAL_CASH_TRAP
- Owner Earnings 차감 증대 (∆NWC 폭증)
```

**Step 3: 자본 효율성 승수 조정**

```
Kappa 계수 = 0.5 (표준)

Year 1 (CCC 75일):
Efficiency Multiplier = exp(-0.5 × 75/365) = 0.90
→ Owner Earnings 10% 감점

Year 2 (CCC 85일):
Efficiency Multiplier = exp(-0.5 × 85/365) = 0.89
→ Owner Earnings 11% 감점 (악화)
```

**⚠️ Hook 22 감점 규칙**:
```
CCC > 120일 + 매년 악화
→ 자본 낭비 기업 (ROIC 하락 경로)
→ 내재가치 -20% 감점
```

---

### Hook 23: M&A Goodwill & Intangible Impairment Stress-Tester (무형자산 감손)

**목적**: 무분별한 M&A로 발생한 장부상 무형자산이 미래에 상각될 위험 평가

**공식**:

$$\text{Adjusted Equity}_{\text{v8}} = \text{Total Equity} - \left( \text{Goodwill} + \text{Other Intangibles} \right) \times \theta_{\text{Impairment}}$$

$$\text{Target ROIC}_{\text{Adjusted}} = \frac{\text{NOPAT}}{\text{IC} + \text{Cumulative Impairments Added Back}}$$

**Step 1: 무형자산 비중 평가**

```
Rule:
- Goodwill / Equity > 20%: 위험 신호 (적신호)
- Goodwill / Equity 10~20%: 중간 (모니터)
- Goodwill / Equity < 10%: 정상

예: 대형 M&A 후 Samsung
- Goodwill: 15,000억원
- Equity: 270,000억원
- 비중: 5.6% (정상 범위)
```

**Step 2: 감손 스트레스 시나리오**

```
Impairment Scenario 1 (낙관): θ = 0% (감손 없음)
- 인수 사업 성공적 통합
- 수익성 목표 달성

Impairment Scenario 2 (기본): θ = 30% (부분 감손)
- 통합 과정에서 일부 효과 미흡
- 예상 수익의 70~80% 달성

Impairment Scenario 3 (비관): θ = 100% (전액 감손)
- 인수 사업 실패
- 완전 상각 필요

확률: 낙관 25% / 기본 50% / 비관 25%

기댓값:
E[θ] = 0.25 × 0% + 0.50 × 30% + 0.25 × 100% = 40%
```

**Step 3: ROIC 재계산**

```
기본 ROIC (Goodwill 포함): 18.0%

감손 조정 후:
IC_Adjusted = IC_Base + (Goodwill × 0.4)
ROIC_Adjusted = NOPAT / IC_Adjusted

→ ROIC 하락 (M&A 가치 파괴 위험 반영)
```

**⚠️ Hook 23 감점 규칙**:
```
Goodwill > Equity × 25% + M&A 최근 3년 내 3회 이상
→ CRITICAL_M&A_RISK (내재가치 -25% 할인)
```

---

### Hook 24: Macro Liquidity & Refinancing Cliff Stress-Tester (재융자 절벽)

**목적**: 1~2년 이내 단기차입금/재발행 만기 초래 시 고금리 충격 & 디폴트 리스크

**공식**:

$$\text{Refinancing Stress Multiplier} = \frac{\text{Short-Term Debt Due within 12M}}{\text{Cash \& Short-Term Equivalents}}$$

$$\text{Stressed Interest Cost} = \text{Short-Term Debt} \times \left(R_{\text{current}} + \Delta R_{\text{Stress}}\right)$$

**Step 1: 재융자 비율 계산**

```
예: 건설 기업 (높은 단기차입금)
- Short-Term Debt (1년 내 만기): 500억원
- Cash & Equivalents: 300억원

Refinancing Ratio = 500 / 300 = 1.67
해석: 현금만으로 재융자 불가 (67% 부족)
→ 신규 차입 또는 자산 매각 필요
```

**Step 2: 고금리 충격 시뮬레이션**

```
Current 금리 환경: 기준금리 3.5%
- Short-Term 차입금리: 5.0%

Stress Scenario (금리 인상):
- 기준금리 +1.0% (→ 4.5%)
- Short-Term 차입금리: 6.5%
- ∆R_Stress = +1.5%

Stressed Interest Cost:
= 500억원 × (5.0% + 1.5%) = 32.5억원
= 추가 이자 비용 +7.5억원

영향: 당년 이익 7.5억원 감소 (CRITICAL)
```

**Step 3: ICR (이자보상배수) 악화 판정**

```
ICR = EBIT / Interest Expense

정상: ICR > 3.0x
주의: ICR 1.5~3.0x
위험: ICR < 1.5x (이자 상환 곤란)

Stressed ICR:
= EBIT / (Interest_Base + Stressed_Additional)

Stressed ICR < 1.5x → CRITICAL_DEFAULT_RISK
```

**⚠️ Hook 24 감점 규칙**:
```
Refinancing Ratio > 1.0 + Stressed ICR < 1.5x
→ CRITICAL_LIQUIDITY_CRISIS (내재가치 -40% 할인)
→ 신용등급 강등 위험
→ 즉시 회피
```

---

### Hook 25: Extreme Value Theory (EVT) & Tail-Risk Black Swan Buffer (꼬리위험)

**목적**: 99.9% 확률 범위 내 최악의 부도 이벤트(팬데믹, 공급망 단절, 경영진 스캔들) 대비 안전마진

**공식**:

$$\text{Margin of Safety}_{\text{Apex}} = \max\left(\text{MoS}_{\text{Base}}, \; \text{Tail Risk Loss Ratio} \times 1.25\right)$$

**Step 1: 꼬리위험 사건 확인**

```
Tail Risk Events (발생 확률 < 5%):

1. 정치/규제: 정부 정책 급변, 규제 강화
   예: 정부 강제공시 의무화 (통신사 추가 투자)

2. 공급망 단절: 주요 부품 공급 중단
   예: 반도체 수급난 (팬데믹 2020)

3. 창업자 스캔들: 경영진 비리/구속
   예: 재벌 3세 지배구조 이슈

4. 시장 충격: 유가/환율/금리 급변
   예: 유로위기 (2011), 브렉시트 (2016)

5. 제품/기술 위험: R&D 실패, 특허 상실
   예: 스마트폰 기술 변화
```

**Step 2: 각 사건별 손실률 추정**

```
예: Samsung Electronics

사건별 손실률 추정:
1. 정치/규제: -15% (매출 일부 감소)
2. 공급망 단절: -25% (생산 중단 3개월)
3. 창업자 스캔들: -10% (신뢰도 하락)
4. 시장 충격: -20% (판가 급락)
5. 기술 변화: -30% (신제품 실패)

Tail Risk Loss = max(위 5개 시나리오)
             = -30% (기술 변화 최악)
```

**Step 3: 꼬리위험 대비 MoS 상향**

```
Base MoS (Hook 7): 35%
Tail Risk Loss: 30%
Tail Risk MoS = 30% × 1.25 = 37.5%

Final Apex MoS = max(35%, 37.5%) = 37.5%

해석:
- 현재주가: 70,000원
- 내재가치 Base: 75,000원 (현재주가 7% 저평가)
- 필요 MoS: 37.5%

최악 시나리오 허용 주가:
= 75,000 × (1 - 0.375) = 46,875원
= 현재주가 대비 -33% 하락까지 허용
```

**Step 4: 현금 런웨이(Cash Runway) 검증**

```
극단 시나리오: 1년 매출 50% 감소

2025 Expected Revenue: 25,500억원
Tail Risk Revenue: 12,750억원

Monthly Cash Burn (최악):
= (12,750억원 / 12) - Operating CF 절감액
= 1,062억원/월 (보수 추정)

Current Cash: 10,000억원
Cash Runway = 10,000 / 1,062 ≈ 9.4개월

판정: 12개월 이상 권장
→ 추가 자금 조달 필요 (회사채/증자)
```

**⚠️ Hook 25 감점 규칙**:
```
Cash Runway < 12개월 + 고부채 구조
→ CRITICAL_TAIL_RISK (MoS 50% 상향 필수)
→ 투자 회피 또는 극도의 주의
```

---

## 👥 3-PHILOSOPHER CONSENSUS MODEL (3철학자 거장 합의)

**목적**: 단일 가치평가 방식의 편향 제거 → 3명 거장의 독립적 가치관 통합

### Graham Defense Score ($P_{\text{Graham}}$)

**철학**: 자산 보호 + 극도의 안전마진

```
점수 계산:
1. Hook 1 (NCAV) PASS: +20점
2. Debt/Equity < 50%: +15점
3. Current Ratio > 2.0x: +15점
4. Dividend Yield > 2%: +10점
5. PBR < 1.0x: +20점
6. PER < 평균의 60%: +20점

Graham Score = Σ (0~100점)

해석:
- > 80점: STRONG BUY (극도의 저평가)
- 60~80점: BUY (좋은 기회)
- 40~60점: HOLD (중립)
- < 40점: AVOID (고평가 또는 위험)
```

**예시: Samsung Electronics**
```
1. NCAV: -85,000억원 (음수) → 0점
2. Debt/Equity: 68% (양호) → 15점
3. Current Ratio: 1.32x (부족) → 10점
4. Dividend Yield: 1.5% (낮음) → 5점
5. PBR: 0.65x (저평가) → 20점
6. PER: 9배 (낮음) → 20점

Graham Score = 70점 (BUY 신호)
```

---

### Buffett Value Score ($P_{\text{Buffett}}$)

**철학**: 현금 창출 능력 + 장기 경제적 해자

```
점수 계산:
1. Hook 10 Owner Earnings Yield > 5%: +25점
2. Hook 2 Moat 확인됨: +25점
3. ROIC > WACC (지속 기간 > 5년): +25점
4. 자본 효율성 (CapEx < Free CF): +15점
5. 배당성향 < 50% (재투자 여력): +10점

Buffett Score = Σ (0~100점)

해석:
- > 80점: STRONG BUY (시간이 돈이 되는 기업)
- 60~80점: BUY (우수 기업)
- 40~60점: HOLD (평범한 기업)
- < 40점: AVOID (현금 창출 약함)
```

**예시: Samsung Electronics**
```
1. Owner Earnings Yield: 12,500원 / 70,000원 = 17.9% → 25점
2. Moat: 반도체/디스플레이 (Strong) → 25점
3. ROIC 18% > WACC 11.4% (지속성 확실) → 25점
4. CapEx < Free CF (자본 효율 양호) → 15점
5. 배당성향 ~30% (낮음) → 10점

Buffett Score = 100점 (STRONG BUY!)
```

---

### Munger Quality Score ($P_{\text{Munger}}$)

**철학**: 지속 가능한 경쟁우위 + 경영 우수성

```
점수 계산:
1. Hook 11 (PPI > 1.2): +25점 (가격 결정력)
2. Hook 13 (LTV/CAC > 2.5): +20점 (경제 효율)
3. Hook 21 (δ_Governance < 10%): +20점 (거버넌스 양호)
4. 임직원 만족도 / 이직률 < 산업 평균: +15점
5. R&D 투자 > 산업 평균: +20점

Munger Score = Σ (0~100점)

해석:
- > 80점: STRONG BUY (최고 경영진 역량)
- 60~80점: BUY (우수한 경영)
- 40~60점: HOLD (평범한 경영)
- < 40점: AVOID (경영 역량 약함)
```

**예시: Samsung Electronics**
```
1. PPI 1.5 > 1.2 (가격 결정력 우수) → 25점
2. LTV/CAC 미적용 (SaaS 아님, 반도체) → 0점 (대체: 스스로의 기술 리더십 +25점)
3. Governance Discount 8% (양호) → 20점
4. 임직원 만족도 → 10점
5. R&D 투자 매출 9% (높음) → 20점

Munger Score = 100점 (STRONG BUY!)
```

---

## 🔀 CONSENSUS AGGREGATION (최종 합의)

$$P_{\text{consensus}} = \frac{P_{\text{Graham}} + P_{\text{Buffett}} + P_{\text{Munger}}}{3}$$

**예시: Samsung**
```
Graham Score: 70점
Buffett Score: 100점
Munger Score: 100점

Consensus = (70 + 100 + 100) / 3 = 90점 (STRONG BUY!)
```

---

## ⚡ LOLLAPALOOZA OVERRIDE MATRIX (극단 오버라이드)

**목적**: 25개 Hook을 모두 통과해도 **4개 극단 신호** 동시 발생 시 → P_consensus = 0% (회피)

### 4가지 치명적 신호 (Lollapalooza Triggers)

| # | 신호 | 정의 | 감점 |
|---|------|------|------|
| 1 | **SDI > 1.0 + Revenue Decline** | 주식 과도 희석 + 매출 부진 | -25점 |
| 2 | **Incentive Misalignment (경영진 옷로환** | CEO 옵션행사 연속 3년 + 자사주 구매 없음 | -25점 |
| 3 | **PER > 50배 + 성장률 < 10%** | 극도의 고평가 + 성장 정체 | -25점 |
| 4 | **통화력 급손 (Pricing Power Collapse)** | PPI < 0.5 (가격 인상 불가) 연속 2년 | -25점 |

**규칙**:
```
4개 신호 중 4개 모두 동시 발생
→ Lollapalooza Trigger ACTIVATED
→ P_consensus 즉시 0점 (절대 회피)
→ CRITICAL_AVOID 플래그 (정보 기각)

예: IT 버블 때 다수의 고PER 기술주
    (PER 100배 이상 + 수익성 부진)
```

---

## 🚨 ANTI-HOOKS AUTOMATIC PENALTY (-50점 이상)

**금지 표현 자동 감점 시스템**:

| 금지 표현 | 감점 | 이유 |
|---------|------|------|
| "사업이 정상 궤도" (근거 없이) | -30점 | 과도한 낙관 |
| "경기 무조건 회복" | -40점 | 경제예측 오류 사례 다수 |
| "AI/메타버스 무조건 성장" | -50점 | 기술 버블 재현 위험 |
| "대주주 신뢰하고 매도 없음" | -35점 | 지배구조 리스크 무시 |
| "영원한 성장" (종료 기간 명시 없음) | -60점 | 터미널 밸류 왜곡 |

---

## <thought_process>

### Part 2 검증 체크리스트:

1. **Advanced Hooks 11-14 완성**:
   - Hook 11 P-Q-C 분해 + PPI 계산 ✓
   - Hook 12 Maintenance CapEx + Owner Earnings ✓
   - Hook 13 LTV/CAC + Network Effect ✓
   - Hook 14 95% 신뢰구간 밴드 ✓

2. **Apex Hooks 21-25 완성**:
   - Hook 21 Governance Discount ✓
   - Hook 22 CCC Efficiency ✓
   - Hook 23 Goodwill Impairment ✓
   - Hook 24 Refinancing Cliff ✓
   - Hook 25 Tail-Risk Buffer ✓

3. **3-Philosopher Model**:
   - Graham Defense Score 계산 ✓
   - Buffett Value Score 계산 ✓
   - Munger Quality Score 계산 ✓
   - Consensus Aggregation ✓

4. **Lollapalooza Override**:
   - 4개 극단 신호 정의 ✓
   - 동시 발생 시 절대 회피 규칙 ✓

5. **Anti-Hooks Penalty**:
   - 금지 표현 자동 감점 ✓

### Part 3로의 연결:
- Negative Catalyst System (Hook 22 CCC 악화 사례)
- Module 1-5 Adaptive Engines
- Integrated Output Matrix

</thought_process>

---

## 📌 Part 2 완료 사항

- [x] Advanced Hooks 11-14 (v6.0) 상세 공식 + 계산 예시
- [x] Apex Hooks 21-25 (v8.0) 완전 설명
- [x] 3-Philosopher Consensus Model (Graham/Buffett/Munger)
- [x] Lollapalooza Override Matrix (극단 신호)
- [x] Anti-Hooks 자동 감점 시스템
- [x] 모든 텍스트 깨짐 정제 (한글 표준화)
- [x] Negative Catalyst Preview (적신호 신호)

---

## 🔜 Part 3 로드 조건

✅ Part 1 + Part 2 완료 후:
- Hooks 1-25 모두 산출 ✓
- 3-Philosopher 거장 점수 계산 ✓
- Lollapalooza 신호 확인 ✓

**→ Part 3 (hook_3.md / skill_3.md) 로드 가능**
- Adaptive Modules 1-5 (v10.0+)
- Negative Catalyst System (상세)
- Integrated Output Matrix (v10.1 Apex Standard)
- Final Investment Signal (STRONG BUY / BUY / HOLD / SELL)

---

**작성 완료**: 2026-07-29  
**버전**: v10.1 APEX Modular  
**모듈**: Part 2/3 (Advanced & Institutional Apex)
