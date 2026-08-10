# 🔬 버크셔 해서웨이 스타일 통합 재무제표 분석 보고서 표준 (v10.1 APEX)
## Part 3: Adaptive Engine & Integrated Output Matrix (Modules 1~5)
### 적응형 안전마진 · 촉매 및 부정적 신호 · 최종 투자 보고서 표준 (Claude `.md` 규약)

---

## 1. 개요 및 실행 프로토콜

Part 1과 Part 2의 연산 결과(25 Hooks 및 3-Philosopher 점수)를 바탕으로, 본 Part 3에서는 동적 매크로 환경 및 기업 생애주기를 반영하는 **5대 Adaptive Modules**를 적용하고 버크셔 해서웨이 표준의 **최종 통합 분석 보고서(Integrated Output Matrix)**를 생성합니다.

---

## 2. Adaptive Modules (1–5) - v10.0+ Innovation

### Module 1: Regime & Life-Cycle Adaptive MoS (동적 요구 안전마진)
기업 성장률과 시장 환경 레짐에 따라 요구 안전마진(Required MoS)을 동적으로 조정합니다.

$$	ext{Required MoS}_{	ext{v10}} = 	ext{Base MoS} 	imes \left(1 - \ln(1 + 	ext{Revenue Growth Rate})ight) 	imes 	ext{Regime Multiplier}$$

* **Regime Multiplier**: 정상기($1.0$), 약세장/공황기($0.7$ - 적극 매수 완화), 경기 침체/급등기($1.3$ - 방어적 강화)

### Module 2: Soros Reflexivity & Catalyst Engine (촉매 및 부정적 신호 엔진)
* **Positive Catalysts (+)**: 신제품 출시, 자사주 소각, M&A, 사업부 스핀오프 (최대 +100점)
* **Negative Catalysts (-)**: 경영권 분쟁(-30), 규제/소송(-20), 기술 구식화(-25), 채무 급증(-30), 거래처 집중 위험(-15)

$$	ext{Adjusted Catalyst Score} = 	ext{Positive Score} - 	ext{Negative Penalties}$$

### Module 3: Volatility Clustering & Dynamic ATR Stop-Loss (변동성 손절선)
$$	ext{Stop-Loss Price} = 	ext{Current Price} - (k 	imes 	ext{ATR}_{20})$$
* 정상기 $k=1.5$, 고변동성 $k=2.0$, 극단 스트레스 $k=2.5$. (데이터 미제공 시 연간 변동성으로 추정)

### Module 4: Multi-Horizon Portfolio Bucketing (3계층 포트폴리오 자금 배분)
1. **Core Compounder (50%)**: 10년 이상 장기 보유, 25 Hooks 완벽 통과 (기업당 최대 30%)
2. **High-Beta Growth (30%)**: 3~5년 중기 성장, 매출 성장률 $\ge 30\%$ (기업당 최대 15%)
3. **Event-Driven Tactical (20%)**: 6개월~1년 단기 촉매, Catalyst Score $\ge 60$ (기업당 최대 5%)

### Module 5: Expert Market Fear & Sentiment (CMFI - 시장 공포/탐욕 지수)
$$CMFI = 0.30 \cdot FGI + 0.30 \cdot Score_{HY} + 0.20 \cdot Score_{PCR} + 0.20 \cdot Score_{AAII}$$
* $CMFI \ge 75$ (극단적 공포): Regime Multiplier $= 0.70$ 적용
* $CMFI < 35$ (극단적 탐욕): Regime Multiplier $= 1.30$ 적용

---

## 3. Integrated Output Matrix v10.1 (최종 재무제표 분석 보고서 표준)

Claude는 최종 출력 시 반드시 아래의 **버크셔 해서웨이 스타일 통합 보고서 서식**을 준수하여 작성해야 합니다.

```markdown
================================================================================
          🔬 BERKSHIRE HATHAWAY STYLE INTEGRATED FINANCIAL REPORT v10.1
                      [기업명 / Ticker 분석 보고서]
================================================================================

1. 기업 프로필 및 핵심 개요 (Company Profile)
--------------------------------------------------------------------------------
• 종목명 / Ticker: [기업명] ([Ticker])
• 산업군 (Sector): [산업 구분] (라우팅 Branch: [Standard/Financials/Tech/Retail])
• 분석 연도 / 통화: [2025] / [KRW 억원]
• 현재 주가 / 시가총액: [주가] 원 / [시가총액] 억원

2. 3-Philosopher 거장 합의 점수 (Consensus Score)
--------------------------------------------------------------------------------
• Benjamin Graham Defense Score : [ 70 / 100 ] (하방 자산 방어력)
• Warren Buffett Value Score    : [ 100 / 100 ] (주주이익 및 지속가능 해자)
• Charlie Munger Quality Score  : [ 100 / 100 ] (경영진 역량 및 가격 결정력)
--------------------------------------------------------------------------------
★ FINAL CONSENSUS SCORE         : [ 90.0 / 100 ] -> [ STRONG BUY / BUY / HOLD / SELL ]

3. 핵심 재무 지표 및 Priority Hooks (Hooks 8–10)
--------------------------------------------------------------------------------
• Dynamic WACC (Hook 8)          : [ 11.4% ] (Ke: 11.7%, Kd: 4.0%, Tax: 22%)
• CAP Decay 10Y (Hook 9)         : [ 12.0년 ] -> 10년 후 [ 5.4년 ] (λ = 0.08)
• Normalized Owner Earnings (H10): [ 34,551억원 ] (주당 주주이익: [ 12,500원 ])

4. 25 Hooks 검증 종합 현황 (Hook Filtration Matrix)
--------------------------------------------------------------------------------
• Base Layer (Hooks 1–10)       : [ 8 / 10 PASS ]
• Advanced Layer (Hooks 11–14)  : [ 4 / 4 PASS ] (PPI: 1.5, Monte Carlo Band: 55,000~95,000원)
• Apex Layer (Hooks 21–25)      : [ 5 / 5 PASS ] (Governance Discount: -8%, CCC: 정상)

5. Adaptive Modules & Dynamic Adjustment (v10.0 Engine)
--------------------------------------------------------------------------------
• Module 1 (Adaptive MoS)        : 요구 안전마진 [ 28.0% ] vs 현재 MoS [ 7.0% ]
• Module 2 (Catalyst Score)      : 긍정 [+68점] / 부정 [-18점] -> 최종 [+50점]
• Module 3 (Dynamic Stop-Loss)   : ATR₂₀ 기반 손절가 [ 65,750원 ]
• Module 4 (Portfolio Bucket)    : [ Core Compounder (50% 비중) ] 적합
• Module 5 (Market Sentiment)    : CMFI 지수 [ 67점 ] (정상~약간 탐욕)

6. Lollapalooza Override & Anti-Hooks 점검
--------------------------------------------------------------------------------
• Lollapalooza Triggers (4대 극단 신호) : [ SAFE ] (치명적 위반 없음)
• Anti-Hooks 금지표현 스캔             : [ CLEAN ] (무근거 낙관론 없음)

================================================================================
█ FINAL INVESTMENT RECOMMENDATION (최종 투자 판정)
================================================================================

  [ 최종 투자 신호 ]: BUY (조건부 매수)
  
  • 목표 주가 밴드 (Target Price) : 82,000원 ~ 88,000원 (상승여력: +18.6%)
  • 95% 내재가치 신뢰구간         : 55,000원 ~ 95,000원
  • 추천 포트폴리오 버킷          : Core Compounder (보유기간: 3~5년)
  • 권장 포지션 비중              : 전체 포트폴리오의 15% ~ 30%
  • 매수 대응 전략                : 65,000원 이하 분할 매수 / Stop-Loss 65,750원 설정

--------------------------------------------------------------------------------
[ 주요 리스크 및 핵심 추적 관찰 요인 (Risk & Catalysts) ]
1. 리스크: 반도체 시황 사이클 변동성, 미-중 기술 규제 및 공급망 이슈
2. 촉매: AI 반도체 파운드리 수주 확대, Galaxy 신제품 마진 개선, 자사주 소각
================================================================================
```

---

## 4. 실행 요약 및 Claude 모듈 연동 규칙

사용자는 분석 대상 기업의 재무 데이터(`analysis_ingredient.md`)를 입력한 후, `Part 1 -> Part 2 -> Part 3` 모듈을 순차적으로 호출하거나, 세 모듈의 표준 규칙에 맞춰 본 통합 보고서(Integrated Output Matrix)를 최종 생성하게 됩니다.
