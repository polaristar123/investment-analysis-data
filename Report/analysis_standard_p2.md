# 🔬 버크셔 해서웨이 스타일 통합 재무제표 분석 보고서 표준 (v10.1 APEX)
## Part 2: Advanced & Institutional Apex Layer (Hook 11~25)
### 심화 경쟁우위 분석 · 거버넌스 리스크 · 3대 거장 합의 모델 (Claude `.md` 규약)

---

## 1. 개요 및 로드 조건

Part 1의 기초 연산 및 우선 실행 항목(Priority Hooks 8-10) 검증이 성공적으로 완료된 후 본 모듈이 호출됩니다. Part 2에서는 **DuPont/McKinsey 분해**, **거버넌스 할인**, **극단적 Tail Risk** 및 **3-Philosopher Consensus Model**을 실행합니다.

---

## 2. Advanced Hooks (11–14) - v6.0 Framework

### Hook 11: P-Q-C Decomposed ROIC Engine (맥킨지 VDT 분해)
ROIC 및 마진의 변동 원인을 가격(Price), 물량(Quantity), 비용(Cost)으로 MECE 분해합니다.

$$	ext{NOPAT Margin} = rac{(P \cdot Q) - (C_{	ext{variable}} \cdot Q) - FC - T}{P \cdot Q}$$

$$	ext{Pricing Power Index (PPI)} = rac{\Delta 	ext{Firm Margin \%}}{\Delta 	ext{Industry Margin \%}} 	imes 	ext{Asset Turnover}$$

* **감점 규칙**: 마진 개선의 $100\%$가 단순 비용 절감($\Delta C < 0$)에만 의존하는 경우, 지속 불가능 마진으로 판단하여 **PPI -30% 감점**을 적용합니다.

### Hook 12: CapEx Dualization Auditor (버펫 주주이익 정밀화)
CapEx를 유지(Maintenance)와 성장(Growth)으로 엄밀히 분리합니다.

$$	ext{Maintenance CapEx} = \max(	ext{D\&A}, \; 0.85 	imes 	ext{CapEx}_{	ext{Total}})$$

$$	ext{Owner Earnings}_{	ext{v6}} = 	ext{Net Income} + 	ext{D\&A} - 	ext{Maintenance CapEx} - 	ext{Normalized } \Delta 	ext{NWC}$$

### Hook 13: Soft Moat & Network Quantifier (먼거의 소프트 해자 정량화)
플랫폼, SaaS 및 브랜드 자산의 무형 해자를 정량화합니다.

$$\Phi(	ext{Moat})_{	ext{v6}} = \Phi(	ext{Moat})_{	ext{base}} + \mu \cdot \ln(	ext{Active Users}) + \eta \cdot \left( rac{	ext{LTV}}{	ext{CAC}} ight)$$

* $rac{	ext{LTV}}{	ext{CAC}} > 3.0$: 우수 (+25점), $rac{	ext{LTV}}{	ext{CAC}} < 1.0$: 비효율 (-40점 및 CAP Decay $\lambda$ +40% 가중).

### Hook 14: Stochastic Monte Carlo WACC & Margin Range (확률론적 내재가치 밴드)
단일 내재가치 제시를 금지하고 매크로 시나리오별 $95\%$ 신뢰구간 밴드를 산출합니다.

$$	ext{Intrinsic Value Band} = \left[ V_{	ext{Intrinsic}}^{(2.5\%)}, \; V_{	ext{Intrinsic}}^{(97.5\%)} ight]$$

```
[시나리오별 WACC 및 내재가치 예시 (삼성전자)]
- Bull Case (25%): WACC 10.4% → 내재가치 95,000원
- Base Case (50%): WACC 11.4% → 내재가치 75,000원
- Bear Case (25%): WACC 13.4% → 내재가치 55,000원
☞ 확률가중 기댓값 E[V] = 73,750원 (밴드: 55,000원 ~ 95,000원)
```

---

## 3. Apex Institutional Hooks (21–25) - v8.0 Framework

### Hook 21: Corporate Governance & Capital Misallocation Discount (거버넌스 할인)
대주주 도덕적 해이, 물적 분할, 배당/자사주 오버행 리스크를 내재가치에 직접 할인 적용합니다.

$$\delta_{	ext{Governance}} = \sum_{k=1}^{n} w_k \cdot I_k \quad \implies \quad V_{	ext{Intrinsic (v8)}} = V_{	ext{Base Intrinsic}} 	imes (1 - \delta_{	ext{Governance}})$$

| 거버넌스 위험 요인 | 감점 가중치 ($w_k$) |
| :--- | :--- |
| 물적 분할 히스토리 (주주가치 침해) | $-15\%$ |
| 이사회 독립성 결여 (CEO/의장 겸직) | $-15\%$ |
| 자사주 소각 없는 누적 보유 ($> 5\%$) | $-10\%$ |
| 경영진 옵션 행사와 주가 불일치 | $-10\%$ |

### Hook 22: Working Capital Efficiency & CCC Auditor (현금전환주기 평가)
$$	ext{CCC} = 	ext{DSO (매출채권회전일)} + 	ext{DIO (재고회전일)} - 	ext{DPO (매입채무회전일)}$$
* CCC가 2년 연속 $20\%$ 이상 증가 시 **CRITICAL_CASH_TRAP** 플래그를 발동하고 내재가치를 $-20\%$ 추가 감점합니다.

### Hook 23: M&A Goodwill & Intangible Impairment Stress-Tester (무형자산 감손)
$$	ext{Adjusted Equity} = 	ext{Total Equity} - (	ext{Goodwill} + 	ext{Other Intangibles}) 	imes 	heta_{	ext{Impairment}}$$
* $	ext{Goodwill} / 	ext{Equity} > 20\%$ 초과 기업에 대해 스트레스 테스트($	heta = 40\%$)를 실시하여 조정한 ROIC를 재계산합니다.

### Hook 24: Macro Liquidity & Refinancing Cliff Stress-Tester (재융자 절벽)
$$	ext{Refinancing Stress Multiplier} = rac{	ext{Short-Term Debt Due within 12M}}{	ext{Cash \& Cash Equivalents}}$$
* 재융자 비율 $> 1.0$ 및 Stressed ICR $< 1.5	ext{x}$ 인 경우 유동성 위기 경보를 발동합니다.

### Hook 25: Extreme Value Theory & Tail-Risk Black Swan Buffer (꼬리위험 버퍼)
$$	ext{Margin of Safety}_{	ext{Apex}} = \max\left(	ext{MoS}_{	ext{Base}}, \; 	ext{Tail Risk Loss Ratio} 	imes 1.25ight)$$

---

## 4. 3-Philosopher Consensus Model (3대 거장 합의 모델)

가치평가의 단일 편향을 방지하기 위해 투자 거장 3인의 시각을 종합 정량화합니다.

```
1. Benjamin Graham Defense Score (P_Graham): 자산 안전성 및 밸류에이션 하방 방어
   - NCAV, 부채비율(<50%), 유동비율(>2.0x), PER/PBR 수준 평가 (100점 만점)

2. Warren Buffett Value Score (P_Buffett): 주주이익 창출력 및 지속가능 해자
   - Owner Earnings Yield(>5%), ROIC-WACC 격차, CapEx 효율성 평가 (100점 만점)

3. Charlie Munger Quality Score (P_Munger): 최고 경영진 역량 및 가격 결정력
   - PPI지수, Soft Moat, 거버넌스 건전성, R&D 효율성 평가 (100점 만점)
```

$$	ext{Consensus Score } (P_{	ext{consensus}}) = rac{P_{	ext{Graham}} + P_{	ext{Buffett}} + P_{	ext{Munger}}}{3}$$

---

## 5. Lollapalooza Override Matrix (극단 오버라이드)

25개 Hook 평가 결과와 무관하게, 아래 **4가지 치명적 신호**가 동시에 발동할 경우 합의 점수를 강제로 $0\%$ 처리하고 **CRITICAL_AVOID (절대 매수 금지)**를 출력합니다.

1. **SDI $> 1.0$ & Revenue Decline**: 주식 과도 희석 및 매출 정체/하락 동시 발생
2. **Incentive Misalignment**: 경영진 주식 매도/옵션 행사 지속 & 자사주 매입 부재
3. **Hyper-Valuation**: PER $> 50$배 & 매출 성장률 $< 10\%$
4. **Pricing Power Collapse**: PPI $< 0.5$ (가격 인상 능력 상실) 2년 연속 지속

---

## 6. Part 2 검증 및 통과 체크리스트

```markdown
[ Part 2 필수 검증 체크리스트 ]
- [ ] Hook 11 P-Q-C 분해 및 PPI 지수 산출 완료
- [ ] Hook 12 Owner Earnings v6 정밀 연산 완료
- [ ] Hook 14 Monte Carlo 95% 내재가치 밴드 구성 완료
- [ ] Hook 21~25 Institutional Apex Hooks 리스크 산출 완료
- [ ] 3-Philosopher 점수 산출 및 합의 점수(P_consensus) 집계 완료
- [ ] Lollapalooza 4대 오버라이드 트리거 점검 완료

☞ 위 조건이 확인되면 'Part 3: Adaptive Engine & Final Output'으로 진행합니다.
```
