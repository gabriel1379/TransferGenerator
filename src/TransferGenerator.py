import xml.etree.ElementTree as ET

from Processors import Processors

from Transfers.FieldTransfer import FieldTransfer
from Transfers.TransferBlueprintTransfer import TransferBlueprintTransfer
from TransferCreator import TransferCreator


with open('../IN/sample.xml') as transfer_source_file:
    transfer_source_parsed = ET.parse(transfer_source_file)

root = transfer_source_parsed.getroot()
print(root.tag)
print(root.attrib)

transfer_blueprint = TransferBlueprintTransfer()
transfer_blueprint.set_name(root.attrib['name'])

for field_parsed in root:
    field_name = field_parsed.attrib['name']
    field_type = field_parsed.attrib['type']

    field = FieldTransfer()
    field.set_field_name(field_name)
    field.set_field_type(field_type)

    transfer_blueprint.add_field(field)

processors = Processors()
transfer_creator = TransferCreator(
    processors.get_processors()
)

with open('../OUT/SampleTransfer.py', mode='w') as transfer_target_file:
    transfer_target_file.write(transfer_creator.create_transfer(transfer_blueprint))

print('Done.')
