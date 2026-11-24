# TraceMap UI

Install the dependencies with `pip install -r requirements.txt` and start the app
with `streamlit run app.py`.

Open **Color Palette** to browse 15 million swatches. Hover over a swatch or
focus it with Tab to see its alternate color.

Run `python -m components.palette` to export the complete `global.css` locally.
The export contains 30,000,000 rules and uses about 1.7 GB. The app reads one
page of rules at a time and generates those same rules on demand when the
export is absent.
