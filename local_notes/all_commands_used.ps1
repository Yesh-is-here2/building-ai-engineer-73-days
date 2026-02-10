# ================================
# Building AI Engineer – All Commands Log
# Local reference only (NOT pushed to Git)
# ================================

# ---- Environment setup ----
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt

# ---- Run single day example ----
cd phase1_core_ml/01_python_basics
python main.py
cd ../../

# ---- Example commit flow ----
git add phase1_core_ml/01_python_basics
git commit -m "day 1: python basics"
git push

# ---- Run visualization example ----
cd phase5_data_systems_polish/62_seaborn_bar_chart
python main.py
cd ../../

# Add more commands here anytime.
