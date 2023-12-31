# %%
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tools.globals as globals

# %%
def fill_contract(option_code):
    """
    得到合約之指定CP資訊資訊

    :param: option_code (str)
    
    return: str
    """
    ret = globals.api.Contracts.Options[option_code]
    if ret is None:
        print("null contract")
    return ret