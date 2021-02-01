import os

from finance_io.config import CONF
from finance_io.utils.loadtools import importObj
from finance_io.utils.io import readYAML
from finance_io.utils.misc import genPath
from finance_io.vas.backend import srcProxy
# from WindPy import w as wdb_conn

def getSector(date=None, sec_name=None):
    SEC_MAP = {}
    date = date if date else time.strftime('%Y-%m-%d', time.localtime(time.time())),
    sec_name = sec_name if sec_name else 'sh-main'
    res = w.wset(
        "sectorconstituent",
        "date={date};sectorid={sec_id}".format(date=date, sec_id=SEC_MAP[sec_name])
    )
    res_data = res.Data
    return dict(zip(res_data[1], res_data[2]))

def connInit():
    windConn = importObj(
        'wdb_conn',
        CONF['dataSource']['sdk']['name'],
        CONF['dataSource']['sdk']['path']
    )
    windConn.start()
    return windConn

def protoLoad():
    return readYAML(
        genPath(
            'rules/rules.yml',
            os.path.dirname(__file__)
        )
    )

def renderTemp(tempName, params):
    pass

class windProxy(srcProxy):
    
    def __init__(self):
        if CONF['dataSource']['mod'] == "dev":
            self.conn = None
        else:
            self.conn = connInit()
        self.protocols = protoLoad()

    def _execute(self, sec=None, func=None, **kwargs):
        pass

    def reqRend(self, **kwargs):
        import pdb;pdb.set_trace()
        return {
            "internal-module": sec,
            "params": [func]
        }


if __name__ == "__main__":
    #print(w.wsd(
    #   "688001.SH",
    #    "sec_name,mkt,trade_code,liststd,marginornot,total_shares,free_float_shares,float_a_shares,share_ntrd_prfshare,share_liqb,share_totala,share_restricteda,share_restrictedb,share_totalb,share_pledgeda,share_liqa_pledged,share_restricteda_pledged,pe_ttm,pb_mrq,val_pettm_high,val_pettm_low,val_pb_high,val_pb_low,eps_basic,eps_diluted,bps_adjust,bps_new,eps_adjust,grps,orps,roe_avg",
    #    "2021-01-01", "2021-01-30",
    #    "unit=1;currencyType="
    #))
    #import pdb;pdb.set_trace()
    #result = w.wset("sectorconstituent","date=2021-01-31;sectorid=1000033281000000")
    fw = open('sector_spec.yml', 'a', encoding='utf-8')
    for sec in SEC_MAP:
        res_dict = {
            "sec_name": sec,
            "sec_id": SEC_MAP[sec],
            "sec_comps": [
                {comp_id: comp_name} for comp_id, comp_name in tuple(wdb_show_sector(sec))
            ],
        }
        yaml.dump(res_dict, fw, allow_unicode=True)
    fw.close()
