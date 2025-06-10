# LLMO ROI Calculator – Streamlit App

This repo contains a minimal Streamlit web application that helps sales teams quickly estimate
a client's return‑on‑investment (ROI) when adopting the **AIO Commerce Accelerator** service.

## Files
| File | Purpose |
|------|---------|
| `roi_calculator_app.py` | Main Streamlit script. |
| `requirements.txt` | Python dependencies (just Streamlit). |

## Quick Start (deploy via Streamlit Community Cloud)
1. **Fork or upload** this repo to your GitHub account.  
2. Go to [share.streamlit.io](https://share.streamlit.io) → sign in with GitHub.  
3. Click **“New app”** → select this repo & branch → `roi_calculator_app.py` as *Main file*.  
4. Deploy – the app builds automatically.  
5. Share the generated URL with prospects.

### Local Run
```bash
pip install -r requirements.txt
streamlit run roi_calculator_app.py
```

## Customisation
* Change default values in the `st.number_input` / `st.slider` widgets.
* Add more inputs (e.g. traffic, conversion‑rate) – keep formulas in sync.
* Adjust branding via `st.set_page_config(page_title, page_icon, layout)`.

Enjoy!