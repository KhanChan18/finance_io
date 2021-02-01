# Virtual API System of Finance-I/O
import time
import yaml

from finance_io.vas import data_source

def getSector(date=None, sec_name=None):
    return data_source.getSector(
        date=date if date else time.strftime('%Y-%m-%d', time.localtime(time.time())),
        sec_name=sec_name if sec_name else 'sh-main'
    )
