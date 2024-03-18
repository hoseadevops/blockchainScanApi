# Get contract source code for verified from https://etherscan.io by api key.(API calls per second: 5 calls for free)

### Reference

* etherscan
    * etherscan key : https://etherscan.io/myapikey
    * etherscan api doc : https://docs.etherscan.io/api-endpoints/contracts#get-contract-source-code-for-verified-contract-source-codes
    * python fire cli doc : https://github.com/google/python-fire/blob/master/docs/guide.md#argument-parsing
* bscscan
    * bscscan key (testnet only) : https://bscscan.com/myapikey


### Usage

```
# 导入 API KEY ( eth || eth )
export API_KEY=

# 多文件

python3 contract.py getsourcecode bsc '"renzoprotocol"' '"0x6921c63fcf9796c9733690804e116be3520ba468"'
python3 contract.py getsourcecode eth '"renzoprotocol"' '"0x6921c63fcf9796c9733690804e116be3520ba468"'


```