import iam_service
import logging
import webapp2

import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
 
        logger.info('>>>>> aaaaa')

        project_id = 'henry-dev'
        service_account_id = 'test123@henry-dev.iam.gserviceaccount.com'

        result = iam_service.list_keys(project_id, service_account_id)

        key_names = ''
        for key in result['keys']:
        	key_names += key['name'] + '<br>'

        self.response.out.write('helloaaaaa<br>' + key_names)


app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='8888')

if __name__ == '__main__':
    main()

