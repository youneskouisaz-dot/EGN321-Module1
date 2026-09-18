# Tank Fill Calculation Tool

## Purpose

This project replaces the inherited `TANK_FILL_rev4.xlsx` spreadsheet calculation with a small Python tool that is easier to understand, test, maintain, and verify.

## Inputs

The calculation uses:

- `length_ft` = tank length in feet
- `width_ft` = tank width in feet
- `depth_in` = fill depth in inches

## Output

The function returns tank volume in U.S. gallons.

## Formula

Volume = Length × Width × (Depth / 12) × 7.48052

The fill depth is divided by 12 to convert inches to feet.

`7.48052` is the conversion factor from cubic feet to U.S. gallons.

## Important Constants

The Python code uses:

```python
INCHES_PER_FOOT = 12.0
CUBIC_FEET_TO_GALLONS = 7.48052

These named constants make the calculation easier to understand and maintain.

Assumptions
Length is entered in feet.
Width is entered in feet.
Fill depth is entered in inches.
The tank is treated as a rectangular volume.
All dimensions must be greater than zero.
Rejected Inputs

The program raises a ValueError if:

length is zero or negative
width is zero or negative
fill depth is zero or negative
Known Limitations

The program assumes a rectangular tank shape.

It does not account for irregular tank shapes or internal equipment that may reduce usable volume.

Workbook Verification

The Python calculation was checked against known-correct workbook rows R-101 and R-102.

A regression test was also created for the R-108 defect found during Assignment 1.1.

Workbook Defects Addressed

The original workbook contained a data-entry defect in R-108 where the fill depth was entered as 2.5 inches instead of 25.0 inches.

The workbook also contained a total formula that did not include all populated rows.

The Python version includes a regression test for the R-108 issue.

See DEFECTS.md for the full defect report.

Project Structure
EGN321-Module1/
├── README.md
├── DEFECTS.md
├── AI_LOG.md
├── requirements.txt
├── src/
│   └── tank_fill.py
└── tests/
    └── test_tank_fill.py
How to Run the Tests

Install the requirements:

pip install -r requirements.txt

Run the tests:

pytest
AI Use

AI assistance used during development is documented in AI_LOG.md.
