# `DateTime` and `DateTimeOffset`
- are immutable structs for representing a date and, optionally a time
- have a resolution of 100 ns and a range covering the years 0001 through 9999

## Differences
- `DateTime`
    - ignoresthe three-state flag in comparisons and considers two values equal if they hae the same year, month, day, hour, minute, and so on.
- `DateTimeOffset`
    - considers two values equal if they refer tothe same popint in time

Thus, DateTime considers the following two values <ins>**different**</ins>, whereas DateTimeOffset considers them <ins>**equal**</ins>:
```
July 01 2022 09:00:00 +00:00 (GMT)
July 01 2022 03:00:00 -06:00 (local time, Central America)
```
