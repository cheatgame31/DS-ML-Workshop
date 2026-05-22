import io
import time
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st


# =========================================================
# Red Bull Data Cleaning Studio - Premium Single File Version
# =========================================================

st.set_page_config(
    page_title="Red Bull Data Cleaning Studio",
    page_icon="🐂",
    layout="wide",
    initial_sidebar_state="expanded",
)


# -----------------------------
# Theme / CSS
# -----------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --rb-navy: #061A33;
        --rb-blue: #0B3A75;
        --rb-sky: #1E88E5;
        --rb-red: #E30613;
        --rb-yellow: #FFC400;
        --rb-cream: #FFF7E6;
        --rb-bg: #F4F7FB;
        --rb-card: rgba(255,255,255,0.88);
        --rb-text: #102033;
        --rb-muted: #64748B;
        --rb-border: rgba(15, 23, 42, 0.10);
        --rb-shadow: 0 20px 55px rgba(6, 26, 51, 0.12);
    }

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 12% 10%, rgba(255,196,0,0.22), transparent 25%),
            radial-gradient(circle at 88% 0%, rgba(227,6,19,0.12), transparent 22%),
            linear-gradient(180deg, #F7FAFF 0%, #EEF3FA 100%);
        color: var(--rb-text);
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #061A33 0%, #09284D 55%, #04111F 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    section[data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stAlert"] {
        background: rgba(255,255,255,0.10);
        border: 1px solid rgba(255,255,255,0.16);
        border-radius: 18px;
    }

    .block-container {
        padding-top: 1.4rem;
        padding-bottom: 2.5rem;
        max-width: 1440px;
    }

    .hero {
        position: relative;
        overflow: hidden;
        border-radius: 34px;
        padding: 34px 38px;
        min-height: 245px;
        background:
            linear-gradient(135deg, rgba(6,26,51,0.98) 0%, rgba(11,58,117,0.96) 54%, rgba(227,6,19,0.88) 100%);
        box-shadow: var(--rb-shadow);
        color: #FFFFFF;
        border: 1px solid rgba(255,255,255,0.14);
    }

    .hero::before {
        content: "";
        position: absolute;
        width: 460px;
        height: 460px;
        right: -130px;
        top: -180px;
        background: radial-gradient(circle, rgba(255,196,0,0.48) 0%, rgba(255,196,0,0.14) 42%, transparent 70%);
        filter: blur(3px);
    }

    .hero::after {
        content: "";
        position: absolute;
        width: 220px;
        height: 220px;
        right: 130px;
        bottom: -90px;
        background: radial-gradient(circle, rgba(255,255,255,0.23), transparent 65%);
    }

    .hero-content {
        position: relative;
        z-index: 2;
        max-width: 860px;
    }

    .eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 13px;
        border-radius: 999px;
        background: rgba(255,255,255,0.14);
        border: 1px solid rgba(255,255,255,0.20);
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.04em;
        text-transform: uppercase;
    }

    .hero h1 {
        margin: 20px 0 10px 0;
        font-size: clamp(2.1rem, 4.6vw, 4.6rem);
        line-height: 0.96;
        letter-spacing: -0.06em;
        font-weight: 850;
    }

    .hero p {
        color: rgba(255,255,255,0.82);
        font-size: 1.03rem;
        line-height: 1.65;
        margin: 0;
        max-width: 720px;
    }

    .hero-badges {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        margin-top: 23px;
    }

    .hero-badge {
        padding: 10px 14px;
        border-radius: 14px;
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.16);
        color: #fff;
        font-weight: 650;
        font-size: 0.87rem;
    }

    .glass-card {
        background: var(--rb-card);
        border: 1px solid rgba(255,255,255,0.72);
        border-radius: 24px;
        padding: 22px;
        box-shadow: 0 14px 38px rgba(6,26,51,0.08);
        backdrop-filter: blur(18px);
        height: 100%;
    }

    .metric-card {
        position: relative;
        overflow: hidden;
        background: rgba(255,255,255,0.92);
        border: 1px solid rgba(255,255,255,0.78);
        border-radius: 24px;
        padding: 22px 22px 20px 22px;
        min-height: 138px;
        box-shadow: 0 16px 35px rgba(6,26,51,0.08);
    }

    .metric-card::before {
        content: "";
        position: absolute;
        inset: 0 0 auto 0;
        height: 5px;
        background: var(--accent);
    }

    .metric-label {
        color: var(--rb-muted);
        font-size: 0.82rem;
        font-weight: 760;
        letter-spacing: 0.055em;
        text-transform: uppercase;
        margin-bottom: 12px;
    }

    .metric-value {
        color: var(--rb-navy);
        font-size: 2.25rem;
        line-height: 1;
        letter-spacing: -0.04em;
        font-weight: 850;
    }

    .metric-caption {
        margin-top: 12px;
        color: var(--rb-muted);
        font-size: 0.88rem;
        font-weight: 500;
    }

    .section-title {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 14px;
        margin: 28px 0 12px 0;
    }

    .section-title h2 {
        font-size: 1.35rem;
        margin: 0;
        color: var(--rb-navy);
        letter-spacing: -0.03em;
    }

    .section-title span {
        color: var(--rb-muted);
        font-size: 0.92rem;
        font-weight: 600;
    }

    .pipeline {
        display: grid;
        grid-template-columns: repeat(6, minmax(130px, 1fr));
        gap: 12px;
        margin: 16px 0 6px 0;
    }

    .pipe-step {
        background: rgba(255,255,255,0.90);
        border: 1px solid rgba(15,23,42,0.08);
        border-radius: 20px;
        padding: 16px 14px;
        box-shadow: 0 12px 25px rgba(6,26,51,0.06);
        min-height: 115px;
    }

    .pipe-no {
        width: 32px;
        height: 32px;
        border-radius: 11px;
        display: grid;
        place-items: center;
        background: linear-gradient(135deg, var(--rb-red), #FF7A00);
        color: white;
        font-weight: 850;
        margin-bottom: 12px;
    }

    .pipe-title {
        color: var(--rb-navy);
        font-weight: 800;
        font-size: 0.95rem;
        line-height: 1.25;
        margin-bottom: 6px;
    }

    .pipe-desc {
        color: var(--rb-muted);
        font-size: 0.78rem;
        line-height: 1.38;
    }

    .upload-zone {
        border-radius: 24px;
        padding: 18px;
        background: rgba(255,255,255,0.78);
        border: 1px dashed rgba(11,58,117,0.26);
    }

    div[data-testid="stFileUploader"] section {
        border-radius: 22px !important;
        border: 1px dashed rgba(11,58,117,0.32) !important;
        background: rgba(255,255,255,0.74) !important;
    }

    .stButton > button, .stDownloadButton > button {
        width: 100%;
        min-height: 3.35rem;
        border-radius: 17px !important;
        border: 0 !important;
        font-weight: 850 !important;
        letter-spacing: 0.01em;
        background: linear-gradient(135deg, #E30613 0%, #FF5A00 52%, #FFC400 130%) !important;
        color: #FFFFFF !important;
        box-shadow: 0 18px 35px rgba(227,6,19,0.22) !important;
        transition: all 0.20s ease-in-out;
    }

    .stButton > button:hover, .stDownloadButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 22px 45px rgba(227,6,19,0.30) !important;
    }

    div[data-testid="stDataFrame"] {
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 12px 28px rgba(6,26,51,0.06);
    }

    div[data-testid="stStatus"] {
        border-radius: 24px;
        border: 1px solid rgba(15,23,42,0.08);
        box-shadow: 0 15px 38px rgba(6,26,51,0.08);
    }

    div[data-testid="stAlert"] {
        border-radius: 20px;
        border: 1px solid rgba(15,23,42,0.08);
    }

    .quality-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 9px 12px;
        border-radius: 999px;
        background: #EEF6FF;
        color: #0B3A75;
        border: 1px solid rgba(30,136,229,0.18);
        font-weight: 750;
        font-size: 0.84rem;
        margin-right: 7px;
        margin-bottom: 7px;
    }

    .footer-note {
        margin-top: 26px;
        color: var(--rb-muted);
        font-size: 0.86rem;
        text-align: center;
    }

    @media (max-width: 1100px) {
        .pipeline { grid-template-columns: repeat(3, minmax(130px, 1fr)); }
    }

    @media (max-width: 720px) {
        .pipeline { grid-template-columns: 1fr; }
        .hero { padding: 26px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# Helper functions
# -----------------------------
def safe_numeric_cols(df: pd.DataFrame) -> List[str]:
    return df.select_dtypes(include=[np.number]).columns.tolist()


def safe_object_cols(df: pd.DataFrame) -> List[str]:
    return df.select_dtypes(include=["object", "string", "category"]).columns.tolist()


def metric_card(label: str, value: str, caption: str, accent: str) -> None:
    st.markdown(
        f"""
        <div class="metric-card" style="--accent:{accent};">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-caption">{caption}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def pipeline_step(no: int, title: str, desc: str) -> str:
    return f"""
    <div class="pipe-step">
        <div class="pipe-no">{no}</div>
        <div class="pipe-title">{title}</div>
        <div class="pipe-desc">{desc}</div>
    </div>
    """


def build_quality_score(df: pd.DataFrame) -> Tuple[int, Dict[str, float]]:
    if df.empty:
        return 0, {"missing_rate": 1, "duplicate_rate": 1, "validity_rate": 0}

    total_cells = max(df.shape[0] * df.shape[1], 1)
    missing_rate = df.isna().sum().sum() / total_cells
    duplicate_rate = df.duplicated().sum() / max(len(df), 1)

    validity_rate = 1.0
    checks = []
    for col in ["Unit_Price", "Units_Sold"]:
        if col in df.columns:
            checks.append((pd.to_numeric(df[col], errors="coerce") > 0).mean())
    if "Customer_Score" in df.columns:
        checks.append((pd.to_numeric(df["Customer_Score"], errors="coerce") <= 10).mean())
    if checks:
        validity_rate = float(np.nanmean(checks))

    score = int(round((1 - missing_rate) * 42 + (1 - duplicate_rate) * 28 + validity_rate * 30))
    return max(0, min(100, score)), {
        "missing_rate": float(missing_rate),
        "duplicate_rate": float(duplicate_rate),
        "validity_rate": float(validity_rate),
    }


def standardize_known_columns(df: pd.DataFrame) -> Tuple[pd.DataFrame, List[str]]:
    df = df.copy()
    logs = []

    if "Region" in df.columns:
        df["Region"] = (
            df["Region"]
            .astype("string")
            .str.strip()
            .str.upper()
            .replace({
                "USA EAST": "USA-EAST",
                "USA_EAST": "USA-EAST",
                "US EAST": "USA-EAST",
                "EU": "EUROPE-EU",
                "APAC": "ASIA-PACIFIC",
            })
        )
        logs.append("Region standardized")

    if "Product_Variant" in df.columns:
        df["Product_Variant"] = df["Product_Variant"].astype("string").str.strip().str.title()
        logs.append("Product_Variant standardized")

    if "Channel" in df.columns:
        df["Channel"] = df["Channel"].astype("string").str.strip().str.replace("_", " ", regex=False).str.title()
        logs.append("Channel standardized")

    # General cleanup for all text columns
    for col in safe_object_cols(df):
        df[col] = df[col].astype("string").str.strip()

    if not logs:
        logs.append("General text trimming applied")

    return df, logs


def fill_missing_values(df: pd.DataFrame) -> Tuple[pd.DataFrame, List[str]]:
    df = df.copy()
    logs = []

    for col in df.columns:
        missing = df[col].isna().sum()
        if missing == 0:
            continue

        if pd.api.types.is_numeric_dtype(df[col]):
            median_value = df[col].median()
            df[col] = df[col].fillna(median_value)
            logs.append(f"{col}: filled {missing:,} missing values with median")
        else:
            mode_value = df[col].mode(dropna=True)
            fill_value = mode_value.iloc[0] if not mode_value.empty else "Unknown"
            df[col] = df[col].fillna(fill_value)
            logs.append(f"{col}: filled {missing:,} missing values with most frequent value")

    if not logs:
        logs.append("No missing values found")
    return df, logs


def apply_logic_checks(df: pd.DataFrame) -> Tuple[pd.DataFrame, List[str]]:
    df = df.copy()
    logs = []
    before = len(df)

    if "Unit_Price" in df.columns:
        df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce")
        df = df[df["Unit_Price"] > 0]
        logs.append("Unit_Price > 0")

    if "Units_Sold" in df.columns:
        df["Units_Sold"] = pd.to_numeric(df["Units_Sold"], errors="coerce")
        df = df[df["Units_Sold"] > 0]
        logs.append("Units_Sold > 0")

    if "Customer_Score" in df.columns:
        df["Customer_Score"] = pd.to_numeric(df["Customer_Score"], errors="coerce")
        df = df[df["Customer_Score"] <= 10]
        logs.append("Customer_Score <= 10")

    removed = before - len(df)
    if logs:
        logs.insert(0, f"Removed {removed:,} rows that violated business rules")
    else:
        logs.append("No known business-rule columns found; skipped safely")

    return df, logs


def make_missing_chart(df: pd.DataFrame):
    missing = df.isna().sum().sort_values(ascending=False)
    missing = missing[missing > 0].head(10)

    fig, ax = plt.subplots(figsize=(10, 4.2))
    if missing.empty:
        ax.text(0.5, 0.5, "No missing values", ha="center", va="center", fontsize=16, weight="bold")
        ax.set_axis_off()
    else:
        ax.barh(missing.index[::-1], missing.values[::-1])
        ax.set_title("Top Missing Value Columns", fontsize=14, weight="bold", pad=14)
        ax.set_xlabel("Missing Count")
        ax.grid(axis="x", alpha=0.22)
        for spine in ax.spines.values():
            spine.set_visible(False)
    fig.tight_layout()
    return fig


def make_distribution_chart(df: pd.DataFrame):
    numeric_cols = safe_numeric_cols(df)
    preferred = [c for c in ["Units_Sold", "Marketing_Spend", "Unit_Price", "Customer_Score"] if c in numeric_cols]
    selected = preferred[:2] if preferred else numeric_cols[:2]

    fig, ax = plt.subplots(figsize=(10, 4.2))
    if not selected:
        ax.text(0.5, 0.5, "No numeric columns available", ha="center", va="center", fontsize=16, weight="bold")
        ax.set_axis_off()
    else:
        data = [pd.to_numeric(df[col], errors="coerce").dropna() for col in selected]
        ax.boxplot(data, vert=False, labels=selected, patch_artist=True)
        ax.set_title("Outlier Profile", fontsize=14, weight="bold", pad=14)
        ax.grid(axis="x", alpha=0.22)
        for spine in ax.spines.values():
            spine.set_visible(False)
    fig.tight_layout()
    return fig


def convert_df_to_csv(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode("utf-8-sig")


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.markdown(
        """
        <div style="padding: 8px 4px 18px 4px;">
            <div style="font-size: 0.78rem; font-weight: 800; letter-spacing: .08em; opacity:.72; text-transform:uppercase;">Control Center</div>
            <div style="font-size: 1.55rem; font-weight: 850; letter-spacing:-.04em; margin-top:4px;">Cleaning Studio</div>
            <div style="font-size: .88rem; opacity:.72; line-height:1.5; margin-top:8px;">Select modules, upload CSV, then execute the pipeline.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    steps = st.multiselect(
        "Pipeline modules",
        [
            "Data Audit",
            "Deduplication",
            "Text Standardization",
            "Missing Value Treatment",
            "Business Logic Check",
            "Outlier Profile",
        ],
        default=[
            "Data Audit",
            "Deduplication",
            "Text Standardization",
            "Missing Value Treatment",
            "Business Logic Check",
            "Outlier Profile",
        ],
    )

    st.divider()
    preview_rows = st.slider("Preview rows", min_value=5, max_value=50, value=12, step=5)
    enable_animation = st.toggle("Premium progress animation", value=True)

    st.info("Designed for executive-style data preparation: clean, clear, and decision-ready.")


# -----------------------------
# Hero
# -----------------------------
st.markdown(
    """
    <div class="hero">
        <div class="hero-content">
            <div class="eyebrow">Red Bull Data Platform | Premium Cleaning Experience</div>
            <h1>Data Cleaning<br/>Command Center</h1>
            <p>
                Transform raw sales data into a clean, trusted and analysis-ready dataset through a guided pipeline with quality score, validation checkpoints and visual diagnostics.
            </p>
            <div class="hero-badges">
                <div class="hero-badge">Quality Score</div>
                <div class="hero-badge">Business Rule Validation</div>
                <div class="hero-badge">Missing Value Treatment</div>
                <div class="hero-badge">Download Ready CSV</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-title">
        <h2>Cleaning Pipeline</h2>
        <span>6-step data preparation workflow</span>
    </div>
    <div class="pipeline">
    """
    + pipeline_step(1, "Audit", "Profile columns, data types, missing values and descriptive statistics.")
    + pipeline_step(2, "Remove Duplicates", "Identify and remove repeated records to reduce noise.")
    + pipeline_step(3, "Standardize", "Clean category names, trim text and align known business labels.")
    + pipeline_step(4, "Treat Missing", "Fill numeric columns with median and text columns with mode.")
    + pipeline_step(5, "Validate", "Apply known business constraints for price, volume and score fields.")
    + pipeline_step(6, "Diagnose", "Visualize missing values and outlier distribution for quick review.")
    + "</div>",
    unsafe_allow_html=True,
)


# -----------------------------
# Upload
# -----------------------------
st.markdown('<div class="section-title"><h2>Upload Dataset</h2><span>CSV file only</span></div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Drag and drop your CSV file here",
    type=["csv"],
    label_visibility="collapsed",
)


if uploaded_file is None:
    left, right = st.columns([1.4, 1])
    with left:
        st.markdown(
            """
            <div class="glass-card">
                <h3 style="margin-top:0; color:#061A33; letter-spacing:-.03em;">Ready for your dataset</h3>
                <p style="color:#64748B; line-height:1.7; margin-bottom: 16px;">
                    Upload a CSV file to unlock the quality dashboard, run the cleaning workflow and download the optimized result.
                </p>
                <span class="quality-pill">Fast audit</span>
                <span class="quality-pill">Safe cleaning</span>
                <span class="quality-pill">Modern UX</span>
                <span class="quality-pill">Single-file app</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.markdown(
            """
            <div class="glass-card">
                <h3 style="margin-top:0; color:#061A33; letter-spacing:-.03em;">Recommended columns</h3>
                <p style="color:#64748B; line-height:1.65;">
                    The app works with any CSV, but provides richer checks when these fields exist:
                </p>
                <div class="quality-pill">Region</div>
                <div class="quality-pill">Product_Variant</div>
                <div class="quality-pill">Channel</div>
                <div class="quality-pill">Unit_Price</div>
                <div class="quality-pill">Units_Sold</div>
                <div class="quality-pill">Customer_Score</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="footer-note">Red Bull Data Cleaning Studio · Premium UI version</div>', unsafe_allow_html=True)
    st.stop()


# -----------------------------
# Read file safely
# -----------------------------
try:
    df_raw = pd.read_csv(uploaded_file)
except UnicodeDecodeError:
    uploaded_file.seek(0)
    df_raw = pd.read_csv(uploaded_file, encoding="latin1")
except Exception as exc:
    st.error(f"Unable to read CSV file: {exc}")
    st.stop()

if df_raw.empty:
    st.warning("The uploaded file has no rows. Please upload a dataset with data.")
    st.stop()

if "cleaned_df" not in st.session_state:
    st.session_state.cleaned_df = None
if "cleaning_logs" not in st.session_state:
    st.session_state.cleaning_logs = []

quality_score, rates = build_quality_score(df_raw)

st.markdown('<div class="section-title"><h2>Dataset Quality Snapshot</h2><span>Before cleaning</span></div>', unsafe_allow_html=True)

m1, m2, m3, m4, m5 = st.columns(5)
with m1:
    metric_card("Quality Score", f"{quality_score}%", "Initial readiness", "#E30613")
with m2:
    metric_card("Records", f"{len(df_raw):,}", "Rows detected", "#0B3A75")
with m3:
    metric_card("Columns", f"{len(df_raw.columns):,}", "Features available", "#FFC400")
with m4:
    metric_card("Missing Cells", f"{int(df_raw.isna().sum().sum()):,}", f"{rates['missing_rate']:.1%} of all cells", "#FF7A00")
with m5:
    metric_card("Duplicates", f"{int(df_raw.duplicated().sum()):,}", f"{rates['duplicate_rate']:.1%} of records", "#10B981")

st.markdown('<div class="section-title"><h2>Raw Data Preview</h2><span>First rows from uploaded file</span></div>', unsafe_allow_html=True)
st.dataframe(df_raw.head(preview_rows), use_container_width=True, height=360)

chart_left, chart_right = st.columns(2)
with chart_left:
    st.markdown('<div class="section-title"><h2>Missing Value Map</h2><span>Top affected columns</span></div>', unsafe_allow_html=True)
    st.pyplot(make_missing_chart(df_raw), use_container_width=True)
with chart_right:
    st.markdown('<div class="section-title"><h2>Numeric Distribution</h2><span>Outlier overview</span></div>', unsafe_allow_html=True)
    st.pyplot(make_distribution_chart(df_raw), use_container_width=True)

st.markdown('<div class="section-title"><h2>Execute Pipeline</h2><span>Apply selected modules</span></div>', unsafe_allow_html=True)

run_col, info_col = st.columns([1.15, 1])
with run_col:
    run_pipeline = st.button("Run Premium Data Cleaning Pipeline", use_container_width=True)
with info_col:
    st.markdown(
        """
        <div class="glass-card" style="padding:16px 18px;">
            <b style="color:#061A33;">Safe mode enabled</b>
            <div style="color:#64748B; margin-top:5px; font-size:.9rem; line-height:1.55;">
                Missing or unavailable columns are skipped automatically to prevent app crashes.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


if run_pipeline:
    df = df_raw.copy()
    logs: List[str] = []

    with st.status("Running premium cleaning workflow...", expanded=True) as status:
        if "Data Audit" in steps:
            st.write("1. Data audit completed")
            numeric = safe_numeric_cols(df)
            if numeric:
                st.dataframe(df[numeric].describe().T, use_container_width=True)
            else:
                st.caption("No numeric columns found for descriptive statistics.")
            logs.append("Data audit completed")
            if enable_animation:
                time.sleep(0.25)

        if "Deduplication" in steps:
            before = len(df)
            df = df.drop_duplicates()
            removed = before - len(df)
            st.write(f"2. Deduplication completed: removed {removed:,} rows")
            logs.append(f"Deduplication removed {removed:,} duplicate rows")
            if enable_animation:
                time.sleep(0.25)

        if "Text Standardization" in steps:
            df, step_logs = standardize_known_columns(df)
            st.write("3. Text standardization completed")
            for item in step_logs:
                st.caption(item)
            logs.extend(step_logs)
            if enable_animation:
                time.sleep(0.25)

        if "Missing Value Treatment" in steps:
            df, step_logs = fill_missing_values(df)
            st.write("4. Missing value treatment completed")
            for item in step_logs[:8]:
                st.caption(item)
            if len(step_logs) > 8:
                st.caption(f"...and {len(step_logs) - 8} more columns")
            logs.extend(step_logs)
            if enable_animation:
                time.sleep(0.25)

        if "Business Logic Check" in steps:
            df, step_logs = apply_logic_checks(df)
            st.write("5. Business logic validation completed")
            for item in step_logs:
                st.caption(item)
            logs.extend(step_logs)
            if enable_animation:
                time.sleep(0.25)

        if "Outlier Profile" in steps:
            st.write("6. Outlier profile generated")
            logs.append("Outlier profile generated")
            if enable_animation:
                time.sleep(0.25)

        status.update(label="Pipeline completed successfully", state="complete", expanded=False)

    st.session_state.cleaned_df = df
    st.session_state.cleaning_logs = logs


cleaned_df = st.session_state.cleaned_df

if cleaned_df is not None:
    final_score, final_rates = build_quality_score(cleaned_df)
    delta_rows = len(cleaned_df) - len(df_raw)

    st.markdown('<div class="section-title"><h2>Cleaned Result</h2><span>After pipeline execution</span></div>', unsafe_allow_html=True)

    r1, r2, r3, r4 = st.columns(4)
    with r1:
        metric_card("Final Score", f"{final_score}%", f"+{final_score - quality_score} pts improved", "#10B981")
    with r2:
        metric_card("Final Records", f"{len(cleaned_df):,}", f"{delta_rows:+,} vs raw", "#0B3A75")
    with r3:
        metric_card("Final Missing", f"{int(cleaned_df.isna().sum().sum()):,}", f"{final_rates['missing_rate']:.1%} of all cells", "#FFC400")
    with r4:
        metric_card("Final Duplicates", f"{int(cleaned_df.duplicated().sum()):,}", f"{final_rates['duplicate_rate']:.1%} of records", "#E30613")

    result_left, result_right = st.columns([1.5, 1])
    with result_left:
        st.markdown('<div class="section-title"><h2>Cleaned Data Preview</h2><span>Ready for analytics</span></div>', unsafe_allow_html=True)
        st.dataframe(cleaned_df.head(preview_rows), use_container_width=True, height=390)

    with result_right:
        st.markdown('<div class="section-title"><h2>Delivery</h2><span>Export output</span></div>', unsafe_allow_html=True)
        st.download_button(
            label="Download Cleaned CSV",
            data=convert_df_to_csv(cleaned_df),
            file_name="redbull_cleaned_premium.csv",
            mime="text/csv",
            use_container_width=True,
        )

        st.markdown(
            """
            <div class="glass-card" style="margin-top:14px;">
                <h3 style="margin:0 0 10px 0; color:#061A33; letter-spacing:-.03em;">Cleaning Log</h3>
            """,
            unsafe_allow_html=True,
        )
        for log in st.session_state.cleaning_logs[:10]:
            st.markdown(f"<div class='quality-pill'>{log}</div>", unsafe_allow_html=True)
        if len(st.session_state.cleaning_logs) > 10:
            st.caption(f"...and {len(st.session_state.cleaning_logs) - 10} more actions")
        st.markdown("</div>", unsafe_allow_html=True)

    if "Outlier Profile" in steps:
        st.markdown('<div class="section-title"><h2>Final Diagnostics</h2><span>After cleaning</span></div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.pyplot(make_missing_chart(cleaned_df), use_container_width=True)
        with c2:
            st.pyplot(make_distribution_chart(cleaned_df), use_container_width=True)

st.markdown('<div class="footer-note">Built as a single Streamlit file · Modern executive dashboard design · Red Bull style theme</div>', unsafe_allow_html=True)
