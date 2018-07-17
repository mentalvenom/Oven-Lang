from ovenexec import run_code
from ovenenv import Env
from oventokenizer import tokenize as tok

# put code in code.oven

with open("code.oven") as f:
  code = f.read()

#print(tok(code).tokens)

env = Env()
run_code(env, code)
