# AI-Based Food Calorie Estimator

A practical AI/ML project prototype for estimating meal calories from food images and portion sizes.

## Project idea

The system accepts a meal image, suggests possible food items, allows the user to confirm the selection, and estimates calories and macronutrients based on weight input. The project is built as a foundation for a larger image-based nutrition recognition system.

Food Image -> Food Suggestion -> User Confirmation -> Portion Input -> Calorie Estimation -> Nutrition Summary

## Current status

This project is a working prototype with:

- a Streamlit-based user interface,
- a nutrition reference database,
- calorie and macro estimation logic,
- lightweight image-based item suggestion heuristics.

It is not yet a full YOLO/CNN-based food recognition pipeline, but it is a strong foundation for that next stage.

## Main features

- Upload food images
- Food suggestions based on filename and image colors
- Manual food selection
- Portion input in grams
- Per-item calorie and macro breakdown
- Total meal nutrition summary
- Clean demo interface

## Tech stack

- Python
- Streamlit
- OpenCV
- Pillow
- NumPy
- pandas
- scikit-learn
- PyTest

## Project structure

- `app.py` — Streamlit app
- `src/estimator.py` — calorie calculation logic
- `src/ml_pipeline.py` — image-based food suggestion heuristic
- `src/nutrition_db.py` — CSV nutrition database loader
- `data/food_nutrition.csv` — nutrition reference data
- `tests/test_estimator.py` — validation tests
- `docs/project_blueprint.md` — project blueprint

## Quick start

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```
4. Test the project:
   ```bash
   python -m pytest -q
   ```

## Example workflow

- Upload a meal image
- The app suggests likely foods using image and filename signals
- User confirms or edits the food list
- User enters portion size in grams for each item
- The app calculates total calories and macros

## Future upgrade path

This prototype can evolve into a stronger capstone project by adding:

- YOLO-based multi-object food detection
- CNN classification for food categories
- RGB-depth or reference object portion estimation
- User profiles and meal history
- Personalized nutrition recommendations

## Project blueprint

See the detailed proposal in [docs/project_blueprint.md](docs/project_blueprint.md).
