import pandas as pd

def replace_pro(column):
    col = pd.DataFrame(column)
    return col.replace(pro_repl,'unknown')

def replace_cpu(column):
    col = pd.DataFrame(column)
    return col.replace(cpu_repl,'unknown')

def replace_os(column):
    col = pd.DataFrame(column)
    return col.replace(os_repl,'unknown')

def replace_band(column):
    col = pd.DataFrame(column)
    return col.replace(repl,'unknown')