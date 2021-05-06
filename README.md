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
Traceback (most recent call last):
  File "/home/gdemonet/repos/doit-calc-deps-issue/.venv/lib/python3.8/site-packages/doit/doit_cmd.py", line 190, in run
    return command.parse_execute(args)
  File "/home/gdemonet/repos/doit-calc-deps-issue/.venv/lib/python3.8/site-packages/doit/cmd_base.py", line 150, in parse_execute
    return self.execute(params, args)
  File "/home/gdemonet/repos/doit-calc-deps-issue/.venv/lib/python3.8/site-packages/doit/cmd_base.py", line 601, in execute
    return self._execute(**exec_params)
  File "/home/gdemonet/repos/doit-calc-deps-issue/.venv/lib/python3.8/site-packages/doit/cmd_run.py", line 264, in _execute
    return runner.run_all(self.control.task_dispatcher())
  File "/home/gdemonet/repos/doit-calc-deps-issue/.venv/lib/python3.8/site-packages/doit/runner.py", line 261, in run_all
    self.finish()
  File "/home/gdemonet/repos/doit-calc-deps-issue/.venv/lib/python3.8/site-packages/doit/runner.py", line 240, in finish
    self.dep_manager.close()
  File "/home/gdemonet/repos/doit-calc-deps-issue/.venv/lib/python3.8/site-packages/doit/dependency.py", line 514, in close
    self.backend.dump()
  File "/home/gdemonet/repos/doit-calc-deps-issue/.venv/lib/python3.8/site-packages/doit/dependency.py", line 179, in dump
    self._dbm[task_id] = self.codec.encode(self._db[task_id])
  File "/home/gdemonet/repos/doit-calc-deps-issue/.venv/lib/python3.8/site-packages/doit/dependency.py", line 57, in encode
    return self.encoder.encode(data)
  File "/home/gdemonet/.pyenv/versions/3.8.6/lib/python3.8/json/encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "/home/gdemonet/.pyenv/versions/3.8.6/lib/python3.8/json/encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "/home/gdemonet/.pyenv/versions/3.8.6/lib/python3.8/json/encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type PosixPath is not JSON serializable
$ echo $?
3
```
