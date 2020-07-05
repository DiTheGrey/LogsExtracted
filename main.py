from pygrok import Grok
from dateutil.parser import parse
from typing import Dict, List

gp = Grok('%{TIMESTAMP_ISO8601:ts} TRACE \[%{WORD:name}\] .* \(%{WORD:service}\:%{NUMBER:req_id}\)')

service_stats: Dict[str, List[float]] = {}

d = {}


def process_request_for_service(begin: dict, end: dict):
    service = data.get('service')

    t1 = parse(begin.get('ts'))
    t2 = parse(data.get('ts'))

    result = t2 - t1
    service_stats.setdefault(service, [])
    service_stats[service].append(result)


with open('test.log') as fd:
    while True:
        line_contents = fd.readline()
        if not line_contents:
            # bail out on EOF
            break
        data = gp.match(line_contents)


        if not data:
            # skip line if no grok match
            continue

        key = (
            data.get('service'),
            data.get('req_id')
        )

        if key in d:
            begin = d.pop(key)
            process_request_for_service(begin=begin, end=data)
            print('processing of record: %s triggerred' % str(key))
        else:
            d[key] = data

print('')
print('RESULTS:')
for service, times in service_stats.items():
    print('service: %s | req_num: %s | max-time: %s' % (service, len(times), max(times)))
