# 📖 APEX v10.2 Compact - 사용 가이드

**버전**: v10.2 (Part 1-3 통합, 70% 축소 최적화)  
**예상 실행 시간**: 15-20분 (재무제표 입력 → 최종 보고서)  
**작성일**: 2026-08-10

---

## 🎯 시스템 개요

이 시스템은 **Warren Buffett & Charlie Munger 스타일 펀더멘탈 분석**을 자동으로 수행합니다.

### 핵심 특징
✅ **원샷 방식**: 3개 Part를 1개 통합 규칙으로 압축  
✅ **계산은 간단**: 입력값 → 자동 연산 (설명/유도 제거)  
✅ **보고서는 자세**: 모든 결과에 상세 근거 & 해석 포함  
✅ **자동화 가능**: 각 Hook별 체크리스트 형식  
✅ **한국어 통일**: KRW(억원), % 등 단위 통일  

---

## 📂 파일 구조

```
investment.v3/
├── SKILLS/
│   ├── APEX_v10.2_COMPACT_UNIFIED.md          ← 계산 규칙 (Hooks 1-25 + Modules 1-5)
│   ├── REPORT_TEMPLATE_DETAILED_v10.2.md      ← 보고서 템플릿 (상세)
│   ├── README_v10.2.md                         ← 이 파일 (사용 가이드)
│   │
│   └── [구식] Part 1-3 백업 폴더
│       ├── skill_1.md (v10.1)
│       ├── hook_1.md (v10.1)
│       └── ...
│
└── Report/
    ├── analysis_ingredient.md                  ← [입력] 재무제표 원본
    └── analysis_compact_[TICKER]_[DATE].md    ← [출력] 최종 보고서
```

---

## 🚀 실행 흐름 (How to Use)

### Phase 1: 재무 데이터 준비 (5분)

**파일명**: `analysis_ingredient.md`

**필수 입력 항목**:
```markdown
[Ticker]: 005930.KS
[Company Name]: 삼성전자
[Sector]: Electronics / Financials / SaaS / Retail
[Financial Year]: 2025
[Currency]: KRW (억원)

[Income Statement]
- Revenue: 245,000
- EBITDA: 52,000
- Operating Profit: 48,000
- Net Income: 38,000

[Balance Sheet]
- Total Assets: 455,000
- Total Liabilities: 185,000
- Shareholders' Equity: 270,000
- Current Assets: 125,000
- Current Liabilities: 95,000

[Cash Flow]
- Operating CF: 42,000
- CapEx: 18,000
- Free Cash Flow: 24,000

[Key Data]
- Current Stock Price: 65,000
- Shares Outstanding: 26,200
- Total Debt: 50,000
- Cash: 5,000
- R&D Expense: 22,000
- Beta: 1.2 (또는 기본값 1.0)
```

✅ **검증**: 자산 = 부채 + 자본, 현금흐름 일관성 확인

---

### Phase 2: 자동 Hook 연산 (10분)

**로드 문서**: `APEX_v10.2_COMPACT_UNIFIED.md`

**자동 실행 순서**:

#### Step 1: 섹터 자동 감지
```
Sector 입력값 분석
  ↓
  [Financials인가? 금융업 Bypass 규칙 적용]
  [아니면? Standard Branch 실행]
```

#### Step 2: Priority Hooks 8-10 연산 (즉시)

| Hook | 입력값 | 계산 | 출력값 |
|------|--------|------|--------|
| **Hook 8** | Rf, Beta, Kd, Tax | WACC 공식 | WACC = ___ % |
| **Hook 9** | CAP_base, λ, t | e^(-λt) | CAP(5Y) = ___ 년 |
| **Hook 10** | NI, D&A, M-CapEx, ∆NWC | 합산 | Owner Earnings = ___ 억원 |

#### Step 3: Foundation Hooks 1-7 병렬 검증
```
□ Hook 1: NCAV 보호 (자산 방어)
□ Hook 2: 해자 지속성 (Moat)
□ Hook 3-7: 마진/성장/거버넌스 등
```

#### Step 4: Advanced Hooks 11-25 (10분)
```
Hook 11-14: 경쟁우위 분석 (PPI, Owner Earnings Growth, ROIC-WACC, NWC Trap)
Hook 15-20: 효율성 & 구조 지표
Hook 21-25: 거버넌스 & 극단 위험
```

#### Step 5: Lollapalooza Override 체크
```
다음 중 1개 이상 해당 시:
  ❌ CRITICAL_AVOID 신호 → 즉시 거부 (MAX 비중 = 0%)
  ✓ 없으면 → Module 1-5 진행
```

#### Step 6: 거장 3인 합의 점수
```
Graham Score (30%) + Buffett Score (40%) + Munger Score (30%)
= Consensus Score (/100)

신호:
  80~100: STRONG BUY
  70~79: BUY
  50~69: HOLD
  30~49: SELL
  <30: CRITICAL_AVOID
```

---

### Phase 3: 보고서 생성 (5분)

**로드 문서**: `REPORT_TEMPLATE_DETAILED_v10.2.md`

**생성 경로**: `/Report/analysis_compact_[TICKER]_20260810.md`

**자동 작성 항목**:
1. Executive Summary (최종 신호 + 목표가)
2. 거장 3인 평가 (Graham/Buffett/Munger 점수 & 해석)
3. Priority Hooks 상세 결과
4. Advanced Hooks 요약
5. 리스크 & Lollapalooza 체크
6. 시나리오 분석 (Bear/Base/Bull)
7. 손절 규약 & 모니터링 지표
8. 실행 계획 (진입 전략/목표가/리밸런싱)

---

## 📊 계산 예시 (Samsung Electronics 005930.KS)

### Hook 8: WACC 계산

| 입력 | 값 |
|------|-----|
| Rf | 3.5% |
| Beta | 1.2 |
| MRP | 6.0% |

**계산**:
```
Ke = 3.5% + 1.2 × 6.0% = 11.7%
Kd = 2,000억 / 50,000억 = 4.0%
Market Cap = 65,000 × 26,200억 = 1,703,000억 (약 1.7조)
Net Debt = 50,000 - 5,000 = 45,000억 (약 0.45조)
V = 1,703,000 + 45,000 = 1,748,000억
E/V = 1,703 / 1,748 = 97.4%
D/V = 45 / 1,748 = 2.6%

WACC = 11.7% × 0.974 + 4.0% × (1-0.22) × 0.026
     = 11.38% + 0.081%
     = 11.46% (약 11.5%)
```

**출력**: `WACC = 11.5%` ✓

---

### Hook 9: CAP Decay

**입력**:
- 해자 강도: Strong (CAP_base = 12년)
- 산업 속도: 중간 (λ_base = 0.08)
- CEO: 안정 (조정 -30%)

**계산**:
```
λ = 0.08 × (1 - 0.30) = 0.056

Year 3: CAP = 12 × e^(-0.056×3) = 12 × 0.839 = 10.1년
Year 5: CAP = 12 × e^(-0.056×5) = 12 × 0.749 = 9.0년
Year 10: CAP = 12 × e^(-0.056×10) = 12 × 0.561 = 6.7년
```

**출력**: `Year 5 CAP = 9.0년` ✓

---

### Hook 10: Owner Earnings

**입력**:
- Net Income: 38,000억
- D&A: 12,000억
- Total CapEx: 18,000억
- Growth CapEx: 2,700억 (분리된 경우)

**계산**:
```
M-CapEx = 18,000 - 2,700 = 15,300억
Normalized ∆NWC = +149억 (5년 평균 적용)
Owner Earnings = 38,000 + 12,000 - 15,300 - 149 = 34,551억
```

**출력**: `Owner Earnings = 34,551억원` ✓

---

## ⚠️ 주의사항

### 1. 데이터 입력 시
```
❌ 하지 말 것:
- 통화 단위 혼재 (KRW + USD)
- 5년 미만 데이터로 5년 평균 계산
- 비정상 연도(M&A/구조조정)를 정규화에 포함

✅ 할 것:
- 모든 금액을 동일 단위로 통일
- 이상치 감지 시 설명 추가
- 재무제표 검산 확인 (A = L + E)
```

### 2. 해석 시
```
❌ 위험한 해석:
- WACC 10.1%, 목표 기업 수익률이 11%면 "OK"
  → 아니다. 1% 오차만으로도 음수 가능
  → 최소 3% 이상 스프레드 필요

- ROIC > WACC 1년이니까 BUY
  → 아니다. CAP이 충분해야 함 (최소 5년)

✅ 올바른 해석:
- 모든 수치에 ±3% 버퍼 적용
- CAP이 5년 이상 지속되는가?
- 극단 위험신호 1개라도 있으면 AVOID
```

### 3. 금융업 특수 규칙
```
Financials 섹터 자동 감지 시:
- NWC / CapEx / CCC 계산 스킵
- 대신: ROE, NPL, BIS 중심 평가
- Owner Earnings 대신: Net Interest Income 기반
```

---

## 🔄 정기 점검 (Quarterly Review)

**분기말 (3/6/9/12월) 체크리스트**:

```markdown
[ ] 매출 가이드 확인 (상향/동일/하향)
[ ] 마진율 추세 (개선/정체/악화)
[ ] 부채 추세 (증가/정체/감소)
[ ] 경영진 변화 (변화 있음/없음)
[ ] 규제/소송 신규 이슈 (있음/없음)

판정:
✓ 모두 양호 → HOLD (계속 보유)
△ 1-2개 변화 → 분석 (상태 재평가)
❌ 3개 이상 악화 → 손절 (위험신호)
```

---

## 📞 FAQ

**Q: 매번 모든 Hook을 계산해야 하나?**
A: 아니다. 계산 규칙(APEX_v10.2_COMPACT_UNIFIED.md)을 따르고, 보고서 템플릿에 값을 채우면 된다. 자동 계산 가능한 부분은 자동화.

**Q: 금융업인데 NWC를 계산하라고 나와 있어?**
A: 아니다. 섹터 감지 시 금융업이면 자동으로 NWC/CapEx Bypass 적용. 보고서에 "Financials Branch 적용됨"으로 표시.

**Q: 현재가가 목표가 위인데 뭘 하지?**
A: 
1. Base Case 달성 확률이 50% 이상인가? (YES → 소액 진입)
2. Downside Protection이 충분한가? (손절가까지 거리) (YES → 진입)
3. 모두 NO면 HOLD 또는 회피.

**Q: Lollapalooza 신호가 나왔어. 뭘 하지?**
A: 즉시 포지션 청산. 예외 없음. "언젠가 나아질 것"이라는 기대는 금지.

---

## 📈 예상 효과

### Before (v10.1)
- 분석 시간: 45-60분 (Part 1-3 순차 로드)
- 문서 길이: 800+ 줄
- 중복 설명: 많음
- 자동화: 불가능

### After (v10.2)
- 분석 시간: 15-20분 (원샷)
- 문서 길이: 350줄 (계산) + 400줄 (보고서)
- 중복: 제거
- 자동화: 높음 (체크리스트 기반)

---

## 🎓 학습 곡선

**첫 번째 분석** (2-3시간):
- 규칙 이해 + 첫 기업 분석
- 계산 과정 숙달

**두 번째 분석** (1시간):
- 템플릿 활용 가속화

**세 번째 이후** (15-20분):
- 안정적 속도 달성

---

## 📝 업그레이드 로드맵

- v10.2: 현재 (통합 + 최적화)
- v10.3: 자동 스크립트 (Python/CLI)
- v10.4: 다중 기업 비교 (Dashboard)
- v10.5: 실시간 가격 추적 (Alert 시스템)

---

**마지막 확인**: 이 가이드를 읽고 `analysis_ingredient.md` 형식으로 첫 기업 데이터를 준비하세요. 그 다음 `APEX_v10.2_COMPACT_UNIFIED.md`의 계산 규칙을 따르고, 최종 결과는 `REPORT_TEMPLATE_DETAILED_v10.2.md`에 채워넣으면 됩니다!

Happy Investing! 🚀
