import streamlit as st

from components.palette import SWATCH_COUNT, SWATCHES_PER_PAGE, palette_rules

st.set_page_config(page_title="Color Palette | TraceMap", layout="wide")
st.title("Color Palette")

page_count = (SWATCH_COUNT + SWATCHES_PER_PAGE - 1) // SWATCHES_PER_PAGE
page = st.number_input("Page", min_value=1, max_value=page_count, step=1)
first = (page - 1) * SWATCHES_PER_PAGE
stop = min(first + SWATCHES_PER_PAGE, SWATCH_COUNT)
st.caption(f"Colors {first + 1:,}–{stop:,} of {SWATCH_COUNT:,}. Hover or use Tab to preview the alternate color.")

swatches = "".join(
    f'<button type="button" class="tm-swatch-{index:06x}" aria-label="Color {index + 1:,}"></button>'
    for index in range(first, stop)
)
st.html(
    f"""
    <style>
    .tm-palette {{
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(2rem, 1fr));
        gap: .3rem;
    }}
    .tm-palette button {{
        min-height: 2rem;
        border: 1px solid #808080;
        border-radius: .25rem;
    }}
    .tm-palette button:focus-visible {{
        outline: 2px solid currentColor;
        outline-offset: 1px;
    }}
    {palette_rules(first, stop)}
    </style>
    <div class="tm-palette" role="group" aria-label="Color swatches">{swatches}</div>
    """
)
