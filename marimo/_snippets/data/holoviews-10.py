# Copyright 2024 Marimo. All rights reserved.
import marimo

__generated_with = "0.11.0"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # HoloViews: Error Analysis with `holoviews`

        Create visualizations with error bars and range overlays using `hv.ErrorBars` and `hv.VSpan`.
        Common usage: Uncertainty visualization, confidence intervals, data ranges.
        Commonly used in: Scientific research, statistical analysis, experimental data.
        """
    )
    return


@app.cell
def __():
    import holoviews as hv
    import numpy as np
    import pandas as pd
    
    hv.extension('bokeh')
    
    # Generate sample data with uncertainty
    x = np.linspace(0, 10, 30)
    y = np.sin(x) + 0.1
    yerr = np.random.uniform(0.1, 0.2, len(x))
    
    # Create error bars plot
    errorbars = hv.ErrorBars((x, y, yerr)).options(
        width=400, height=300,
        title='Measurement with Uncertainty'
    )
    
    curve = hv.Curve((x, y)).options(
        color='navy',
        xlabel='X',
        ylabel='Value'
    )
    error_plot = (curve * errorbars)
    
    # Create range visualization
    spans = []
    for i in range(3):
        x1, x2 = np.random.uniform(0, 10, 2)
        x1, x2 = min(x1, x2), max(x1, x2)
        spans.append(hv.VSpan(x1, x2).options(
            alpha=0.2, 
            fill_color=['blue', 'green', 'red'][i]
        ))
    
    range_plot = hv.Curve((x, y)) * hv.Overlay(spans).options(
        width=400, height=300,
        title='Regions of Interest'
    )
    
    # Combine visualizations
    layout = (error_plot + range_plot).cols(2)
    
    layout
    return (curve, error_plot, errorbars, hv, layout, np, pd, range_plot, spans,
            x, y, yerr)


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()
