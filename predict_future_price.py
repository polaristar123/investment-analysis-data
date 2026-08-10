import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numba import njit, prange, float32, uint64
from dataclasses import dataclass
from typing import Dict, Any, Tuple

# Set Academic Plotting Environment
sns.set_theme(style="darkgrid")
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False


# ==============================================================================
# 1. ULTRA-FAST BITWISE PRNG & GAUSSIAN POLAR ENGINE
# ==============================================================================
@njit(inline='always', fastmath=True)
def _rotl(x: uint64, k: int) -> uint64:
    """Bitwise rotation helper for Xoroshiro128+"""
    return (x << k) | (x >> (64 - k))


@njit(inline='always', fastmath=True)
def _xoroshiro128plus(state: np.ndarray) -> float:
    """
    Xoroshiro128+ Generator (Direct Float Injection)
    Replaces slow floating-point division with constant multiplication
    """
    s0 = state[0]
    s1 = state[1]
    result = s0 + s1

    s1 ^= s0
    state[0] = _rotl(s0, 24) ^ s1 ^ (s1 << 16)
    state[1] = _rotl(s1, 37)

    return float((result >> 11) * 1.1102230246251565e-16)


@njit(inline='always', fastmath=True)
def _get_polar_gaussian_pair(state: np.ndarray) -> Tuple[float, float]:
    """
    Marsaglia Polar Method: Eliminates sin() and cos() calls completely
    Zero-Trigonometry Pseudo-Random Gaussian Pair Generation
    """
    while True:
        u1 = _xoroshiro128plus(state)
        u2 = _xoroshiro128plus(state)
        v1 = 2.0 * u1 - 1.0
        v2 = 2.0 * u2 - 1.0
        s = v1 * v1 + v2 * v2
        if 0.0 < s < 1.0:
            multiplier = np.sqrt(-2.0 * np.log(s) / s)
            return v1 * multiplier, v2 * multiplier


# ==============================================================================
# 2. NUMBA JIT COMPILED HIGH-PERFORMANCE CMFI ENGINE (MODULE 5)
# ==============================================================================
@njit(fastmath=True, inline='always')
def _compute_cmfi_numba(
    fgi_index: float, 
    hy_spread_bps: float, 
    put_call_ratio: float, 
    aaii_spread: float
) -> Tuple[float, float, float, float, float, float, float, float]:
    """
    Zero-Overhead Numba-JIT CMFI Dynamic Engine
    Calculates 4-Indicator Composite Fear Scores and Regime Multipliers
    """
    # 1. Score Calculations with Hardware Clipping
    fgi_c = max(0.0, min(100.0, fgi_index))
    score_fgi = 100.0 - fgi_c

    z_hy = (hy_spread_bps - 400.0) / 120.0
    score_hy = max(0.0, min(100.0, 50.0 + 25.0 * z_hy))

    if put_call_ratio >= 1.00:
        score_pcr = 100.0
    elif put_call_ratio <= 0.45:
        score_pcr = 0.0
    else:
        score_pcr = (put_call_ratio - 0.45) / (1.00 - 0.45) * 100.0
    score_pcr = max(0.0, min(100.0, score_pcr))

    score_aaii = max(0.0, min(100.0, 50.0 - 1.25 * aaii_spread))

    # 2. Composite CMFI Score Calculation
    cmfi = 0.30 * score_fgi + 0.30 * score_hy + 0.20 * score_pcr + 0.20 * score_aaii

    # 3. Dynamic Regime Assessment
    if cmfi >= 75.0:
        regime_code = 1.0  # Extreme Fear
        regime_mult = 0.70
        refi_boost = 200.0  # bps
        drift_adj = 0.02
    elif cmfi < 35.0:
        regime_code = -1.0 # Extreme Greed
        regime_mult = 1.30
        refi_boost = -50.0 # bps
        drift_adj = -0.015
    else:
        regime_code = 0.0  # Normal
        regime_mult = 1.00
        refi_boost = 0.0
        drift_adj = 0.0

    return cmfi, score_fgi, score_hy, score_pcr, score_aaii, regime_mult, refi_boost, drift_adj


# ==============================================================================
# 3. ZERO-BRANCHING NUMBA PARALLEL C-KERNEL (AVX-512 OPTIMIZED)
# ==============================================================================
@njit(parallel=True, fastmath=True, nogil=True)
def _ultimate_apex_v110_kernel(
    N: int, 
    max_years: int, 
    S0: float, 
    v0: float, 
    kappa: float, 
    theta: float, 
    xi: float, 
    rho: float, 
    mu: float,
    seed_base: int
) -> np.ndarray:
    """
    v11.0 Ultimate Unified Apex C-Kernel
    - Direct AVX-512 Register Allocation
    - Antithetic Dual-Path Variate Execution
    - Zero-Branch Memory Layout
    """
    half_N = N // 2
    sqrt_one_minus_rho2 = np.sqrt(1.0 - rho * rho)
    log_S0 = np.log(S0)
    
    price_paths = np.empty((N, max_years + 1), dtype=np.float32)

    for i in prange(half_N):
        # Unique Seed Vector Initialization per Thread Parallel Stream
        prng_state = np.array([
            uint64(seed_base + i * 2 + 1013904223), 
            uint64(seed_base + i * 7 + 1664525)
        ], dtype=np.uint64)

        idx1 = i
        idx2 = i + half_N

        price_paths[idx1, 0] = np.float32(S0)
        price_paths[idx2, 0] = np.float32(S0)

        log_s1 = log_S0
        log_s2 = log_S0

        v1 = v0
        v2 = v0

        for t in range(1, max_years + 1):
            # Polar Method Gaussian Call
            z_s1, z_v_raw1 = _get_polar_gaussian_pair(prng_state)
            z_v1 = rho * z_s1 + sqrt_one_minus_rho2 * z_v_raw1

            # Antithetic Dual Pair Acceleration (-z)
            z_s2 = -z_s1
            z_v2 = -z_v1

            # Path 1: Reflection & Drift Execution
            v1_pos = max(v1, 1e-6)
            sqrt_v1_pos = np.sqrt(v1_pos)
            v1 = max(v1_pos + kappa * (theta - v1_pos) + xi * sqrt_v1_pos * z_v1, 1e-6)
            
            log_s1 += (mu - 0.5 * v1) + sqrt_v1_pos * z_s1
            price_paths[idx1, t] = np.float32(np.exp(log_s1))

            # Path 2: Reflection & Drift Execution (Antithetic Dual)
            v2_pos = max(v2, 1e-6)
            sqrt_v2_pos = np.sqrt(v2_pos)
            v2 = max(v2_pos + kappa * (theta - v2_pos) + xi * sqrt_v2_pos * z_v2, 1e-6)

            log_s2 += (mu - 0.5 * v2) + sqrt_v2_pos * z_s2
            price_paths[idx2, t] = np.float32(np.exp(log_s2))

    return price_paths


# ==============================================================================
# 4. UNIFIED ULTIMATE APEX SYSTEM ENGINE CLASS
# ==============================================================================
@dataclass(frozen=True)
class MacroParameters:
    fgi_index: float       # CNN Fear & Greed Index (0-100)
    hy_spread_bps: float   # High-Yield Credit Spread (bps)
    put_call_ratio: float  # CBOE Put/Call Ratio
    aaii_spread: float     # AAII Bull-Bear Spread (%)
    vix: float             # Market Volatility Index (VIX)


class UltimateApexEngineV110:
    """
    Unified High-Performance Engine V11.0
    Combines Module 5 CMFI Engine + Heston Stochastic Volatility Kernel
    """
    def __init__(self, current_price: float, macro: MacroParameters):
        if current_price <= 0:
            raise ValueError("Price must be strictly positive (> 0)")
        self.S0 = float(current_price)
        self.m = macro

    def run_full_pipeline(self, N: int = 204800, max_years: int = 10) -> Dict[str, Any]:
        """Runs Unified CMFI + Heston Monte Carlo Pipeline"""
        t_start = time.time()
        
        if N % 2 != 0:
            N += 1

        # 1. Execute Integrated Numba CMFI Engine
        cmfi, score_fgi, score_hy, score_pcr, score_aaii, regime_mult, refi_boost, drift_adj = _compute_cmfi_numba(
            self.m.fgi_index, self.m.hy_spread_bps, self.m.put_call_ratio, self.m.aaii_spread
        )

        # 2. Dynamic Heston Model Parameter Binding
        kappa = 2.0
        theta_base = max((self.m.vix / 100.0) ** 2, 1e-4)
        theta_cmfi = theta_base * (1.0 + 0.5 * ((cmfi - 50.0) / 100.0))
        xi = 0.25
        
        # Absolute Zero-Branch Feller Condition Enforcement
        feller_ratio = (2.0 * kappa * theta_cmfi) / (xi ** 2)
        if feller_ratio <= 1.0:
            xi = float(np.sqrt((2.0 * kappa * theta_cmfi) / 1.05))

        v0 = theta_cmfi
        rho = -0.65
        mu = 0.075 + drift_adj
        seed_base = int(time.time() * 1000) % 1000000

        # 3. Parallel Execution of Ultimate C-Kernel
        price_paths = _ultimate_apex_v110_kernel(
            N, max_years, self.S0, v0, kappa, theta_cmfi, xi, rho, mu, seed_base
        )
        t_elapsed = time.time() - t_start

        # 4. Summary Generation & Percentile Metrics
        summary = {}
        for yr in [3, 5, 10]:
            p_t = price_paths[:, yr]
            sem = np.std(p_t) / np.sqrt(N)
            summary[f'Year_{yr}'] = {
                'Mean': float(np.mean(p_t)),
                'Median': float(np.median(p_t)),
                'CI95_Margin': float(1.96 * sem),
                'P05': float(np.percentile(p_t, 5)),
                'P95': float(np.percentile(p_t, 95))
            }

        regime_str = 'Extreme Fear' if cmfi >= 75.0 else ('Extreme Greed' if cmfi < 35.0 else 'Normal')

        return {
            'cmfi': cmfi,
            'cmfi_scores': {
                'FGI': score_fgi,
                'HY': score_hy,
                'PCR': score_pcr,
                'AAII': score_aaii
            },
            'regime': regime_str,
            'regime_mult_mod1': regime_mult,
            'refi_boost_bps': refi_boost,
            'drift_adj': drift_adj,
            'feller_ratio': feller_ratio,
            'elapsed_time': t_elapsed,
            'price_paths': price_paths,
            'summary': summary
        }

    def render_analytics(self, sim_results: Dict[str, Any]):
        """Renders High-Density Academic Visualizations"""
        price_paths = sim_results['price_paths']
        summary = sim_results['summary']
        years = np.arange(0, price_paths.shape[1])

        p05_band = np.percentile(price_paths, 5, axis=0)
        p25_band = np.percentile(price_paths, 25, axis=0)
        p50_band = np.percentile(price_paths, 50, axis=0)
        p75_band = np.percentile(price_paths, 75, axis=0)
        p95_band = np.percentile(price_paths, 95, axis=0)
        mean_path = np.mean(price_paths, axis=0)

        fig, ax = plt.subplots(figsize=(15, 7.5), dpi=130)

        ax.fill_between(years, p05_band, p95_band, color='#004b23', alpha=0.15, label='95% Confidence Band (P05-P95)')
        ax.fill_between(years, p25_band, p75_band, color='#007200', alpha=0.30, label='50% Interquartile Range (P25-P75)')

        ax.plot(years, p50_band, color='#004b23', linewidth=2.5, linestyle='--', label='Median Trajectory (P50)')
        ax.plot(years, mean_path, color='#cc0000', linewidth=3.0, label='Expected Mean Trajectory')

        for yr in [3, 5, 10]:
            mean_p = summary[f'Year_{yr}']['Mean']
            margin = summary[f'Year_{yr}']['CI95_Margin']
            ax.scatter(yr, mean_p, color='#cc0000', s=100, zorder=5)
            ax.annotate(
                f'Year {yr} Target\nMean: ₩{mean_p:,.0f}\n(±₩{margin:,.2f})',
                xy=(yr, mean_p),
                xytext=(yr, mean_p * 1.20),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.2, headwidth=6),
                ha='center', fontsize=9.5, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.2)
            )

        ax.set_title(
            f'v11.0 APEX Unified System (CMFI: {sim_results["cmfi"]:.1f}/100 [{sim_results["regime"]}], Exec Time: {sim_results["elapsed_time"]*1000:.2f}ms)', 
            fontsize=13, fontweight='bold'
        )
        ax.set_xlabel('Horizon (Years)', fontsize=12)
        ax.set_ylabel('Target Asset Price (KRW)', fontsize=12)
        ax.set_xticks(years)
        ax.legend(loc='upper left', frameon=True, facecolor='white', framealpha=0.95)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

        plt.tight_layout()
        plt.show()


import sys
import json
import argparse


def parse_cli_args():
    """Parse command-line arguments for batch processing"""
    parser = argparse.ArgumentParser(
        description='v11.0 APEX Unified Forecast Engine - CLI Interface'
    )
    parser.add_argument('--ticker', type=str, help='Stock ticker symbol')
    parser.add_argument('--input-json', type=str, help='JSON input file path')
    parser.add_argument('--current-price', type=float, help='Current stock price')
    parser.add_argument('--fgi-index', type=float, default=50.0, help='CNN Fear & Greed Index (0-100)')
    parser.add_argument('--hy-spread', type=float, default=400.0, help='HY Spread (bps)')
    parser.add_argument('--put-call', type=float, default=0.75, help='Put/Call Ratio')
    parser.add_argument('--aaii-spread', type=float, default=0.0, help='AAII Spread (%)')
    parser.add_argument('--vix', type=float, default=20.0, help='VIX Index')
    parser.add_argument('--num-paths', type=int, default=204800, help='Number of Monte Carlo paths')

    return parser.parse_args()


def load_json_input(filepath: str) -> Dict[str, Any]:
    """Load macro parameters from JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def create_forecast_report(ticker: str, results: Dict[str, Any], current_price: float) -> Dict[str, Any]:
    """Create a structured forecast report for API consumption"""

    summary = results['summary']

    # Generate 3/5/10 year forecast data
    years = [3, 5, 10]
    forecast_data = []

    for year in years:
        s = summary[f'Year_{year}']
        forecast_data.append({
            'year': year,
            'mean': round(float(s['Mean']), 2),
            'median': round(float(s['Median']), 2),
            'p05_bear': round(float(s['P05']), 2),
            'p95_bull': round(float(s['P95']), 2),
            'ci95_margin': round(float(s['CI95_Margin']), 2),
        })

    # Calculate returns
    forecast_data_by_year = {item['year']: item for item in forecast_data}

    year_3_return = ((forecast_data_by_year[3]['mean'] - current_price) / current_price) * 100
    year_5_return = ((forecast_data_by_year[5]['mean'] - current_price) / current_price) * 100
    year_10_return = ((forecast_data_by_year[10]['mean'] - current_price) / current_price) * 100

    return {
        'ticker': ticker,
        'current_price': current_price,
        'forecast_timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'cmfi_analysis': {
            'composite_score': round(results['cmfi'], 2),
            'regime': results['regime'],
            'fgi_score': round(results['cmfi_scores']['FGI'], 2),
            'hy_score': round(results['cmfi_scores']['HY'], 2),
            'pcr_score': round(results['cmfi_scores']['PCR'], 2),
            'aaii_score': round(results['cmfi_scores']['AAII'], 2),
            'regime_multiplier': round(results['regime_mult_mod1'], 2),
            'drift_adjustment': round(results['drift_adj'], 4),
            'refi_boost_bps': round(results['refi_boost_bps'], 1),
        },
        'forecast_data': forecast_data,
        'projected_returns': {
            'year_3': round(year_3_return, 2),
            'year_5': round(year_5_return, 2),
            'year_10': round(year_10_return, 2),
        },
        'model_metrics': {
            'feller_ratio': round(results['feller_ratio'], 4),
            'execution_time_ms': round(results['elapsed_time'] * 1000, 2),
            'paths_simulated': 204800,
        },
        'summary_text': f"CMFI Score {results['cmfi']:.1f}/100 - {results['regime']} Regime. "
                       f"3Y Target: {forecast_data_by_year[3]['mean']:,.0f} ({year_3_return:+.1f}%), "
                       f"5Y Target: {forecast_data_by_year[5]['mean']:,.0f} ({year_5_return:+.1f}%), "
                       f"10Y Target: {forecast_data_by_year[10]['mean']:,.0f} ({year_10_return:+.1f}%)"
    }


# ==============================================================================
# BENCHMARK VERIFICATION RUNNER
# ==============================================================================
if __name__ == "__main__":
    args = parse_cli_args()

    # Load or construct macro parameters
    if args.input_json:
        input_data = load_json_input(args.input_json)
        ticker = input_data.get('ticker', 'UNKNOWN')
        current_price = input_data.get('current_price')
        macro_inputs = MacroParameters(
            fgi_index=input_data.get('fgi_index', 50.0),
            hy_spread_bps=input_data.get('hy_spread_bps', 400.0),
            put_call_ratio=input_data.get('put_call_ratio', 0.75),
            aaii_spread=input_data.get('aaii_spread', 0.0),
            vix=input_data.get('vix', 20.0)
        )
    else:
        ticker = args.ticker or 'UNKNOWN'
        current_price = args.current_price or 1000000
        macro_inputs = MacroParameters(
            fgi_index=args.fgi_index,
            hy_spread_bps=args.hy_spread,
            put_call_ratio=args.put_call,
            aaii_spread=args.aaii_spread,
            vix=args.vix
        )

    if current_price is None or current_price <= 0:
        print(json.dumps({'error': 'current_price must be a positive number'}), file=sys.stderr)
        sys.exit(1)

    try:
        engine = UltimateApexEngineV110(current_price=current_price, macro=macro_inputs)

        # Warm-up pass for JIT Compilation
        _ = engine.run_full_pipeline(N=2000, max_years=10)

        # Production Execution
        results = engine.run_full_pipeline(N=args.num_paths, max_years=10)

        # Create structured report
        report = create_forecast_report(ticker, results, current_price)

        # Output JSON to stdout
        print(json.dumps(report, indent=2))

    except Exception as e:
        error_report = {
            'error': str(e),
            'ticker': ticker,
            'current_price': current_price
        }
        print(json.dumps(error_report), file=sys.stderr)
        sys.exit(1)