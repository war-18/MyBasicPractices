import os
import fetch_data as fd

print(os.listdir())
flist = fd.download("https://google.com/")

print(flist)

import fetch_data as fd
cat = fd.read_catalog(cat_fname)
flist = fd.download(**cat['entry_name'])