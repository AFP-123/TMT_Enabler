import streamlit as st

# --- Title ---
st.title("UFR Logic Parameters Input")

# --- User Inputs ---

# Lookback list selection (only allow one)
lookback_list = st.multiselect(
    "Select lookback period(s):",
    options=[1, 3, 12],
    help="Choose one or more of Month (1), Quarter (3), or Year (12)."
)

# UFR Lookback list (optional)
lookback_list_UFR = st.multiselect(
    "Select UFR lookback period(s) (optional):",
    options=[1, 3, 12],
    help="Choose only if using UFR logic, else leave empty."
)

# Input amount selection
input_amount = st.selectbox(
    "Select input amount type:",
    options=["ARR", "MRR"]
)

# Run at levels
run_at_levels = st.multiselect(
    "Select run at levels:",
    options=["ARR", "MRR", "T3M", "TTM", "T3M (Annualized)"],
    default=["ARR", "MRR"]
)

# Retention levels
retention_levels = st.multiselect(
    "Select retention level(s):",
    options=[
        "Customer_level",
        "Customer_Product_level",
        "Customer_Product_RetentionType_level",
        "Level4"
    ],
    default=[
        "Customer_level",
        "Customer_Product_level",
        "Customer_Product_RetentionType_level"
    ]
)

# --- Check if all required inputs are provided ---
if (
    lookback_list
    and input_amount
    and run_at_levels
    and retention_levels
):
    st.success("All required inputs selected. Ready to run!")

    # --- Add your business logic or function call below ---
    st.write("### Selected Parameters:")
    st.write(f"Lookback List: {lookback_list}")
    st.write(f"UFR Lookback List: {lookback_list_UFR if lookback_list_UFR else 'Not using UFR logic'}")
    st.write(f"Input Amount: {input_amount}")
    st.write(f"Run At Levels: {run_at_levels}")
    st.write(f"Retention Levels: {retention_levels}")

    # You can now call your main function here
    # result = your_main_function(...)
    # st.write(result)

else:
    st.warning("Please select all required parameters to proceed.")