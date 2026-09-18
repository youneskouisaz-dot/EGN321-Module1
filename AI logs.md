# AI Usage Log

## AI Tool Used

ChatGPT

## Use 1 - Python Function

### Prompt

I asked for help converting the verified tank-fill spreadsheet calculation into a pure Python function.

### AI Response

The AI suggested using named constants, input validation, unit conversion, and a function that returns the calculated tank volume.

### What I Changed

I used the actual formula, tank dimensions, and defect information verified from my workbook.

### Verification

I tested the function in Google Colab using workbook values and the corrected R-108 case.

## Use 2 - Automated Tests

### Prompt

I asked for help creating pytest tests for known-correct workbook rows, the R-108 defect, and invalid inputs.

### AI Response

The AI suggested using `pytest.approx()` for floating-point calculations and `pytest.raises(ValueError)` for invalid inputs.

### What I Changed

I used the workbook values from R-101, R-102, and R-108.

### Verification

I compared the Python results with the workbook evidence and ran the tests.

## Use 3 - Documentation

### Prompt

I asked for help organizing the README, defect report, and AI usage log.

### AI Response

The AI suggested documenting the formula, units, assumptions, rejected inputs, limitations, tests, and defects.

### Verification

I reviewed the documentation and made sure it matched the workbook and assignment requirements.
