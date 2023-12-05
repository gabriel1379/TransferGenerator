# TransferGenerator

Generates transfer classes based on definitions provided in `.xml` files, inspired by Symfony's transfer generator.

At present, the generated transfer classes provide:
  - Getters and setters for the fields
  - Adders for dicts and lists (although you can of course set them too)
  - A `modified` meta dict, with an individual `is_modified_...` methods for each field

## Usage:
  - Define the classes you need using `.xml` files, the names of which end in `..._transfers.xml`.
    - The structure these files should have is exemplified by the `IN/sample_transfers.xml` and `OUT/second_sample_transfers.xml` files.
  - You can either put these files in the `IN` directory, where the sample files are. The two sample files are considered as part of the repo but any other `_transfers.xml` files put there will be ignored.
  - OR you can provide custom input as well as custom output paths by using the `-i`/`--input_path` and the `-o`/`--output_path` command line arguments, respectively. If provided, they will be used, if not, the default paths (`IN/` and `OUT/` in the repo root) will be used.

`generate.py` - will run with the default values
`generate.py -i my_transfer_xmls -o my_generated_transfers` - will use the `my_transfer_xmls` input and the `my_generated_transfers` output paths, respectively.
  