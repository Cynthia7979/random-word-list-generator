# random-word-list-generator
Generate a random list of words for reciting. 

The source word list must be a `csv` file with two columns, the first column holding words and 
the second holding meanings.

When in `csv_mode`, `generate_list.py` generates two `csv` files, one containing only the words
and the other with meanings.

When `csv_mode` is set to `False`, `generate_list.py` generates two `txt` files.

This program *should* be compatible with Python 2.

## Usage: Generate Lists
Run file directly, or

`python generate_list.py <source_list> <output_directory> [number_of_words] [number_of_lists] [csv_mode]`

* **`source_list`** Path of the whole word list.  
Must be `csv` file - Use `process_excel.py` for conversions.
* **`output_directory`** Path of where to output the `txt` files.
* **`number_of_words`** Number of words to put in each list. Defaults to `30`. Not required.
* **`number_of_lists`** Number of word lists to randomly generate at one time.  
Note that for each list, two `txt` files will be generated, one containing only words
and the other with meanings. Defaults to `1`. Not required.
* **`csv_mode`** Whether or not to output `csv` files. Defaults to `True`.

Note that `generate_list.py` uses `sys.argv`, not `argparser`, which means no help 
messages will be shown if called with `-h` flag. Also, the non-required parameters are **positional**.


## Usage: `.xls` to `.csv`

`process_excel.py` can be used for converting differently formatted `.xls` files to `.csv` files.

Run the file directly for default settings, or

```
python process_excel.py workbook sheet_name [-h] [--wordscol WORDSCOL] [--meaningscol MEANINGSCOL]
                        [--end END] [--output OUTPUT]
```

* **`workbook`** Path of the excel workbook. The workbook *must* be an `xls` file.
* **`sheet_name`** Name of the work sheet. By Excel's default, this is "Sheet1".
* **`--wordscol WORDSCOL`** The number of the column holding the words. Indexes start at 0, which
means that A is 0, B is 1, etc.  
Currently reading words from rows is not supported.
* **`--meaningscol MEANINGSCOL`** The number of the column holding the meanings. Indexes start at 0, which
means that 1 is 0, 2 is 1, etc.  
Currently reading meanings from rows is not supported.
* **`--end END`** End Identifier: A lambda function that takes two arguments, `row` and `sheet`.
When the given `row` is the end of useful content, this function should return `True`.
You can use the `sheet` argument for getting specific cell values. Refer to the 
[xlrd documentation](https://xlrd.readthedocs.io/en/latest/) for more details.  
By default, the end identifier is `lambda row, sheet: sheet.cell_value(row, words_column) == ''`
* **`--out OUT`** The output directory.

Different to `generate_list.py`, `process_excel.py` uses `argparser` for more advanced argument
parsing. Running `python process_excel.py -h` will show an automatically generated help message.

