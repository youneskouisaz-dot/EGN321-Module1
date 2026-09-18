# Tank Fill Calculation Tool

## Purpose

This project replaces the inherited `TANK_FILL_rev4.xlsx` spreadsheet calculation with a Python tool that is easier to understand, test, maintain, and verify.

## Inputs

The calculation uses:

- `length_ft` = tank length in feet
- `width_ft` = tank width in feet
- `depth_in` = fill depth in inches

## Output

The function returns tank volume in U.S. gallons.

## Formula

Volume = Length × Width × (Depth / 12) × 7.48052

The depth is divided by 12 to convert inches to feet.

`7.48052` is the conversion factor from cubic feet to U.S. gallons.

## Assumptions

- Length is entered in feet.
- Width is entered in feet.
- Fill depth is entered in inches.
- The tank is treated as a rectangular volume.
- All dimensions must be greater than zero.

## Rejected Inputs

The program raises a `ValueError` if:

- length is zero or negative
- width is zero or negative
- fill depth is zero or negative

## Known Limitations

The program assumes a rectangular tank shape.

It does not account for irregular tank shapes or internal equipment that may reduce usable volume.

## Verification

The Python calculation was checked against known-correct workbook cases R-101 and R-102.

A regression test was also created for the R-108 defect.

## Workbook Defects Addressed

The original workbook contained a data-entry defect in R-108 where the fill depth was entered as 2.5 inches instead of 25.0 inches.

The Python version includes a regression test for this issue.

See `DEFECTS.md` for the full defect report.

## Running Tests

Install the requirements:

```bash
pip install -r requirements.txt
