# filesync
A really simple file synchronisation routine

### ...but why?

This piece of code is really not meant to an environment where things are well planned.

I made it to distribute some files that were synchronised to an OneDrive folder
from a SharePoint page. A creative work around, some may say.

But well:
* It works;
* It saved me like 10 minutes/day.

### Details

To call sync when imported: 'sync(name, src, dst)'

Being:
* 'name': file name, purely cosmetic
* 'src': source path
* 'dst': destination path

'subs()' is only used inside 'sync()'

It gives a lot of text feedback, might annoy some.