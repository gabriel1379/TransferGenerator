TransferGenerator
=================

Generates transfer classes based on definitions provided in ´.xml´ files, inspired by Symfony's transfer generator.

At present, the generated transfer classes provide:
  - Getters and setters for the fields
  - Adders for dicts and lists (although you can of course set them too)
  - A ´modified´ meta dict, with an individual ´is_modified_...´ methods for each field

Usage:
  - Define the classes you need by adding new ´..._transfers.xml´ files to the ´IN´ directory, as exemplified by the ´sample_transfers.xml´ and ´second_sample_transfers.xml´ files already there. (NOTE: those two and any others ending in ´(...)sample_transfers.xml´ are considered as part of the repo, but every other file with any other name you might put in there, will be ignored.)
  - Then, as demonstrated in the ´run.py´ file, just import, instantiate and run the ´TransferGenerator´:

´´´  
from src.TransferGenerator import TransferGenerator


transfer_generator = TransferGenerator()  
transfer_generator.generate_transfers()  
´´´
