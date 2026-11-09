# Python Package Exercise

# Python Pet

A tiny pet python that lives in your terminal. It starts as an egg, and every
terminal command you run helps it grow: from egg, to cracking egg, to hatchling,
to young python, and finally to a full coiled python.

## Functions

### `create_egg(name, hatch_at=50)`

Creates a new pet egg.

- `name`: the pet's name. Leading and trailing spaces are removed.
- `hatch_at`: how many commands it takes to hatch. Must be a positive integer.

```python
from create_egg import create_egg

create_egg("Monty")
# {"name": "Monty", "hatch_at": 50, "commands_run": 0, "stage": "egg"}
```

Raises `TypeError` if `name` isn't a string or `hatch_at` isn't an integer, and
`ValueError` if `name` is empty or `hatch_at` is zero or negative.

### `get_stage(commands_run, hatch_at)`

Works out the growth stage from the numbers alone. It doesn't need a pet.

| `commands_run` (with `hatch_at=50`) | Stage |
|---|---|
| 0–24 | `"egg"` |
| 25–49 | `"cracking"` |
| 50–99 | `"hatchling"` |
| 100–199 | `"young python"` |
| 200+ | `"full python"` |

Stages scale with `hatch_at`: a pet hatches at exactly `hatch_at` commands,
becomes a young python at twice that, and a full python at four times that.

```python
from get_stage import get_stage

get_stage(0, 50)     # "egg"
get_stage(60, 50)    # "hatchling"
get_stage(40, 10)    # "full python"
```

Raises `TypeError` for non-integer arguments, and `ValueError` if
`commands_run` is negative or `hatch_at` is zero or negative.

## Running the tests

```bash
pip install pipenv
pipenv install --dev
pipenv run pytest
```

