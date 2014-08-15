# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

variable = 136123
string_variable = "foo bar"
dict_variable = {"foo": 123, "bar": 146}

# <codecell>

import ipykee
ipykee.create_project("tutorial_remote", internal_path="ipykee-storage", repository="git@github.com:anaderi/ipykee_test.git")
session = ipykee.Session(project_name="tutorial_remote")

# <codecell>

session.add(value=variable, key="variable")
session.add(value=string_variable, key="string")
session.add(value=dict_variable, key="dict")
session.show_added()

