# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "vega-datasets",
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.9.21"
app = marimo.App(width="medium", html_head_file="head.html")


@app.cell
def __():
    import marimo as mo
    from vega_datasets import data
    return data, mo


@app.cell
def __(data):
    data.cars()
    return


@app.cell
def __(mo):
    mo.callout(
        mo.md("""
    ## Callout

    This font should be styled
    """)
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        # heading

        Here is a paragraph
        """
    )
    return


if __name__ == "__main__":
    app.run()
