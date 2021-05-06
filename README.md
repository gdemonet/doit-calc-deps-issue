# Minimal reproducing example for `doit` "calc_dep" issue

To run this example, you will need to have `doit` installed (version 0.32 or
higher) with Python 3.6 (or higher).

Run the following:

```shell
$ python3 -m doit
.  get_dep:a
.  make_builddir
.  get_dep:b
.  get_dep:c
.  get_dep:f
.  get_dep:g
.  make_mod:c
.  make_mod:f
.  make_mod:g
.  make_mod:b
.  make_mod:a
$ echo $?
0
```
