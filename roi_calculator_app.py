# -*- coding: utf-8 -*-

import math
import streamlit as st

st.set_page_config(page_title="LLMO ROI Calculator", page_icon="🔢", layout="centered")

st.title("🔢 LLMO ROI Calculator")
st.write(
    """Estimate the return on investment (ROI) a client could achieve by adopting the **AIO Commerce Accelerator** service.
    Enter the client’s key business numbers in the sidebar. The calculator uses a lightweight model
    (baseline revenue, expected uplift, contribution margin & service cost) to output ROI, payback period and net profit."
)

with st.sidebar:
    st.header("Client inputs")
    baseline_rev = st.number_input(
        "Baseline monthly e‑commerce revenue (EUR)",
        min_value=0.0,
        value=50_000.0,
        step=1_000.0,
        format="%.0f",
    )
    margin = st.slider(
        "Contribution margin (%% of revenue)",
        min_value=0,
        max_value=100,
        value=40,
        step=1,
    )
    uplift = st.slider(
        "Expected revenue uplift (%%)",
        min_value=0,
        max_value=100,
        value=15,
        step=1,
    )
    horizon = st.slider(
        "Evaluation horizon (months)",
        min_value=1,
        max_value=24,
        value=12,
        step=1,
    )
    st.markdown("---")
    st.header("Service pricing")
    setup_fee = st.number_input(
        "Setup fee (EUR)",
        min_value=0.0,
        value=8_000.0,
        step=1_000.0,
        format="%.0f",
    )
    retainer = st.number_input(
        "Monthly retainer (EUR)",
        min_value=0.0,
        value=4_000.0,
        step=500.0,
        format="%.0f",
    )

# --- Calculations -----------------------------------------------------------
# Incremental revenue over horizon
inc_rev = baseline_rev * (uplift / 100) * horizon
# Incremental profit (contribution margin)
inc_profit = inc_rev * (margin / 100)
# Total service cost
total_cost = setup_fee + (retainer * horizon)
# ROI
roi = None
if total_cost > 0:
    roi = (inc_profit - total_cost) / total_cost

# Payback period (months) ---------------------------------
monthly_inc_profit = baseline_rev * (uplift / 100) * (margin / 100)
net_monthly_benefit = monthly_inc_profit - retainer
if net_monthly_benefit <= 0:
    payback = "Not within horizon"
else:
    months_needed = math.ceil(setup_fee / net_monthly_benefit)
    payback = f"{months_needed} months"

# --- Output ---------------------------------------------------------------
st.markdown("## 📈 Results")
col1, col2, col3 = st.columns(3)

col1.metric("ROI", f"{roi*100:,.1f}%" if roi is not None else "N/A")
col2.metric("Net profit (EUR)", f"{inc_profit - total_cost:,.0f}")
col3.metric("Payback period", payback)

with st.expander("See calculation details"):
    st.write(f"**Incremental revenue (over {horizon} mo):** EUR{inc_rev:,.0f}")
    st.write(f"""**Incremental profit (margin {margin}%):** EUR{inc_profit:,.0f}
**Total service cost:** EUR{total_cost:,.0f}""")

st.caption("Model assumes incremental revenue uplift applies evenly across the evaluation horizon.")
