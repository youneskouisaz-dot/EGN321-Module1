# Defect Report

## Workbook Reviewed

`TANK_FILL_rev4.xlsx`

## Defect 1 - Incorrect R-108 Fill Depth

Record: `R-108`

Spreadsheet row: `13`

The fill depth was entered as:

`2.5 inches`

The corrected value is:

`25.0 inches`

The workbook formula was:

```text
=C13*D13*(E13/12)*7.48052

Using the incorrect value:

10 × 6 × (2.5 / 12) × 7.48052

produces approximately:

93.5065 gallons

Using the corrected value:

10 × 6 × (25.0 / 12) × 7.48052

produces approximately:

935.065 gallons

This defect caused the calculated volume to be approximately ten times too small.

The Python replacement includes a regression test for the corrected R-108 calculation.

Defect 2 - Incorrect Total Range

The spreadsheet total formula was:

=SUM(G6:G17)

However, tank records continued below row 17.

This means the total did not include all populated tank rows.

The Python replacement does not depend on this incorrect spreadsheet total formula.

Defect 3 - Output Unit Not Clearly Identified

The calculated volume column did not clearly identify the result as U.S. gallons.

The Python version clearly documents the output unit as U.S. gallons.

Verification

The defects were reviewed manually and then checked again using Python in Google Colab
