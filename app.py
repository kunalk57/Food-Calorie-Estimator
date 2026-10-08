import streamlit as st
from PIL import Image

from src.estimator import FoodCalorieEstimator
from src.ml_pipeline import detect_food_items_from_image


st.set_page_config(page_title="AI Food Calorie Estimator", page_icon="🍱", layout="wide")


@st.cache_resource
def build_estimator():
    return FoodCalorieEstimator()


estimator = build_estimator()

st.title("🍱 AI-Based Food Calorie Estimator")
st.caption("Upload a meal image to estimate the food items, approximate portions, and total calories.")
st.info("Prototype status: this version uses a lightweight image heuristic plus user confirmation for food detection. Real YOLO/CNN detection can be added in the next stage.")

uploaded_image = st.file_uploader("Choose food image", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded meal image", use_column_width=True)
    detected = detect_food_items_from_image(image=image, filename=uploaded_image.name)
else:
    detected = detect_food_items_from_image(filename="rice_dal_roti.jpg")

if not detected:
    st.warning("No food items were detected from the image. Please select the foods manually from the list below.")
    detected = []

with st.container():
    st.subheader("Food selection")
    selected_items = st.multiselect(
        "Detected or predicted foods",
        options=estimator.food_list,
        default=detected,
        help="Choose the foods visible in the meal."
    )

    st.write("Estimated portion size is requested in grams per item.")

    item_weights = {}
    for item in selected_items:
        default_weight = 150.0 if item in {"rice", "dal", "roti", "biryani", "paneer"} else 100.0
        item_weights[item] = st.number_input(
            f"{item.title()} weight (g)",
            min_value=0.0,
            max_value=5000.0,
            value=float(default_weight),
            step=10.0,
            key=f"weight_{item}"
        )

    if selected_items:
        summary = estimator.estimate_meal(item_weights)

        st.subheader("Meal nutrition summary")
        total_calories = summary["total_calories"]
        total_protein = summary["total_protein"]
        total_carbs = summary["total_carbs"]
        total_fat = summary["total_fat"]

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Calories", f"{total_calories:.0f} kcal")
        col2.metric("Protein", f"{total_protein:.1f} g")
        col3.metric("Carbs", f"{total_carbs:.1f} g")
        col4.metric("Fat", f"{total_fat:.1f} g")

        st.write("Per-item breakdown:")
        for item, result in summary["items"].items():
            st.markdown(
                f"- **{item.title()}**: {result['grams']} g -> {result['calories']:.0f} kcal, "
                f"Protein {result['protein']:.1f} g | Carbs {result['carbs']:.1f} g | Fat {result['fat']:.1f} g"
            )

        st.info("These values are estimates based on a nutritional reference table and portion size input.")

st.sidebar.title("Project overview")
st.sidebar.markdown(
    """
    This project follows the full AI pipeline:
    1. Food image upload
    2. Detection / classification
    3. Portion estimation
    4. Calorie and nutrition estimation
    """
)
st.sidebar.markdown("Built as a 3rd-year AI/ML capstone project.")
