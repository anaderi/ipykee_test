# -*- coding: utf-8 -*-


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

# <codecell>

session.commit("Our first commit!")

# <codecell>

session.show_added()

# <codecell>

variable = 160
string_variable = "bar foo"

# <codecell>

session.add(value=variable, key="variable")
session.add(value=string_variable, key="string")

# <codecell>

session.commit("Second commit")