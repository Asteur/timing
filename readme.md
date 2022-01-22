### Timing

----

- Installation
`pip install git+https://github.com/Asteur/timing.git#egg=timing`

- `from timing import timing`
```
>>> @timing
    def test():
        return 1+1

>>> test()
test - 1.9150002117385156e-06
```
- copy logs
- `from timing import review_timing_logs`
```>>> review_timing_logs("test - 1.9150002117385156e-06")```

- think how to speed up your scripts
