# f1-data-analysis
Using Pandas in Python, I analyzed massive amounts of F1 race data to figure out the team with the highest average places gained from start to finish.

## Run with Docker

Build the image:

```bash
docker build -t f1-data-analysis .
```

Run the default analysis script (`main.py`):

```bash
docker run --rm -it -v "$(pwd):/app" f1-data-analysis
```

Run a different script if needed:

```bash
docker run --rm -it -v "$(pwd):/app" f1-data-analysis python scatter-plot.py
docker run --rm -it -v "$(pwd):/app" f1-data-analysis python interactive-scatter-plot.py
```
