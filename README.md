# mtqdm

Put tqdm on your menu bar.

## Usage

```bash
pip install mtqdm
```

My intentions for mtqdm is for it to be a *drop-in replacement* for **tqdm**.
So simply replace **tqdm** with **mtqdm** in your code.

```python
from mtqdm import mtqdm
for _ in mtqdm(range(100)):
    # ...
```

![mtqdm-0.1.3 in action](https://github.com/0oj/mtqdm/blob/main/examples/basic_usage.png?raw=true)

The progress bar from **tqdm** will still be displayed in the terminal. Additionally, a progress bar like the one above will appear in the menu bar. Clicking it will reveal metrics.

`100%|████████████████████| 100/100 [00:15<00:00,  6.50it/s]`