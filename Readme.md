# Tank Fill Calculation Tool

## Purpose

This project replaces the inherited `TANK_FILL_rev4.xlsx` spreadsheet calculation with a small Python program.

The goal is to make the tank-fill calculation easier to understand, test, maintain, and verify.

## Inherited Artifact

The original calculation came from the spreadsheet:

`TANK_FILL_rev4.xlsx`

The spreadsheet was manually reviewed before creating the Python version.

## Inputs

The Python function uses three inputs:

- `length_ft` = tank length in feet
- `width_ft` = tank width in feet
- `depth_in` = fill depth in inches

## Output

The function returns the calculated tank volume in U.S. gallons.

## Formula

The calculation used is:

```text
Volume (gallons) =
Length (ft) × Width (ft) × (Fill Depth (in) / 12) × 7.48052
