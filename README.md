# JSON Forger

A Python script to create or modify JSON files in the current working directory.

## Requirements

- Python 3.x

## Usage

> [!NOTE]
> Use `python` or `python3` depending on your OS.

### Create a JSON File

To create a new JSON file with a specified number of elements:

```sh
python json_forger.py create <file_name> <number_of_elements>
```

### Modify a JSON file

To modify the `name` field of a JSON element at a specified index:
```sh
python json_forger.py modify <file_name> <index> name=<new_value>
```

### Examples

Create a file named `data.json` with 10 elements:
```sh
python json_forger.py create data 10
```

Modify the `name` field of the element at index 2 in `data.json`:
```sh
python json_forger.py modify data 2 name=new_name
```

