

# Start app

```shell
granian --interface wsgi --workers 1 --backpressure 2 --reload main:app
```

```shell
uv pip install -e .
uv run app
```