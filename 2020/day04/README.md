# Advent of Code 2020 - Day 4: Passport Processing

## Problem Summary

Process passport data from a batch file where passports are separated by blank lines and contain key-value pairs. Validate passports based on required fields and field-specific rules.

## Solution

### Part 1: Field Presence Check

Count passports that contain all **7 required fields**:
- `byr` (Birth Year), `iyr` (Issue Year), `eyr` (Expiration Year)
- `hgt` (Height), `hcl` (Hair Color), `ecl` (Eye Color), `pid` (Passport ID)

*Note: `cid` (Country ID) is optional.*

### Part 2: Field Validation

Count passports where all required fields are present **and** have valid values:

| Field | Rule |
|-------|------|
| `byr` | 4 digits, 1920-2002 |
| `iyr` | 4 digits, 2010-2020 |
| `eyr` | 4 digits, 2020-2030 |
| `hgt` | Number + `cm` (150-193) or `in` (59-76) |
| `hcl` | `#` followed by 6 hex characters |
| `ecl` | One of: `amb`, `blu`, `brn`, `gry`, `grn`, `hzl`, `oth` |
| `pid` | 9-digit number (including leading zeros) |

## Approach

1. **Parsing**: Split input by blank lines, then parse each block into a dictionary
2. **Part 1**: Check for presence of all required keys
3. **Part 2**: Use dedicated validator functions for each field, mapped via a dictionary for clean iteration
