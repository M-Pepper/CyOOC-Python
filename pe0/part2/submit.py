#!/usr/bin/env python3

from urllib.error import HTTPError
import json
import http.client

class Jobe:
    def __init__(self,server='10.50.30.236',filename='deliverable.py'):
        self.server = server
        self.resource = '/jobe/index.php/restapi/runs/'
        self.filename = filename
        self.runspec = {
            'language_id':'python3flag',
            'sourcefilename':self.filename,
            'sourcecode':None,
            'parameters':{'flagid':'check123456789'},
        }
        self.headers = {
            'Content-type':'application/json; charset=utf-8',
            'Accept':'application/json',
        }
        self.result = None

    def submit(self):
        with open(self.filename) as fp:
            source = fp.read()
        self.runspec['sourcecode'] = source

        try:
            connection = http.client.HTTPConnection(self.server)
            connection.request('POST',self.resource,json.dumps({'run_spec': self.runspec}),self.headers)
            response = connection.getresponse()
            if response.status != 204:
                content = response.read().decode('utf8')
                if content:
                    result = json.loads(content)
            connection.close()
        except (HTTPError, ValueError) as e:
                print('Exception occurred',e)
        else:
            self.result = result
            return result

    def __str__(self):
        return '{}\n{}\n{}'.format(self.result.get('cmpinfo'),self.result.get('stdout'),self.result.get('stderr'))
        

if __name__ == '__main__':
    job = Jobe()
    job.submit()
    print(job)


        



