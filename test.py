from io import BufferedReader, BytesIO
import json
import orjson
import time

METRICS_KEYS = [
    "actor:{0}"
]

def parse_orjson(input: bytes) -> dict:
    line = BytesIO(input).readlines()
    # while data := line.read1():
    #     print(orjson.loads(data))
    # return data

def main():
    with open('data/large-file.json', 'rb') as filehandle:
        lines = filehandle.read()
        metrics = {}
        data = orjson.loads(lines)
        for line in data:
            # print(line['actor'])
            key = METRICS_KEYS[0].format(line['actor']['login'])
            try:
                metrics[key] += 1
            except KeyError as e:
                metrics[key] = 1
        print(len(metrics.keys()))
        exit()


if __name__ == '__main__':
    main()