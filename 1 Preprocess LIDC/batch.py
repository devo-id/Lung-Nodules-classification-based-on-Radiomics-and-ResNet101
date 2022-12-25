import os
for i in range(1,50): 
    os.system(f'cmd /c "python lidc2dicom.py --subjects {i} --log log.log --output-dir result --composite --images-dir LIDC-IDRI"')
