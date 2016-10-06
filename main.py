import logging
import sys
import webapp2

import iam_service


# Setup stdout log handler for logging to stackdriver.
logger = logging.getLogger()
logger.setLevel(logging.INFO)

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
formatter = logging.Formatter('[%(levelname)s] %(message)s')
stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)


class ServiceAccountListHandler(webapp2.RequestHandler):
    def get(self):
        logger.info('Listing all service accounts.')
        project_id = name = self.request.get("project_id")
        result = iam_service.list_service_accounts(project_id)

        page = ''
        for accounts in result['accounts']:
            page += accounts['name'] + '<br>'
        self.response.out.write(page)


class ServiceAccountKeyListHandler(webapp2.RequestHandler):
    def get(self):
        logger.info('Listing all service account keys.')
        project_id = name = self.request.get('project_id')
        service_account_id = self.request.get("service_account_id")
        result = iam_service.list_keys(project_id, service_account_id)

        page = ''
        for key in result['keys']:
            page += key['name'] + '<br>'
        self.response.out.write(page)


class DefaultHandler(webapp2.RequestHandler):
    def get(self):
         self.response.out.write('Welcome to Simple GKE Server')


app = webapp2.WSGIApplication([
    ('/service_account/list', ServiceAccountListHandler),
    ('/service_account_key/list', ServiceAccountKeyListHandler),
    ('/', DefaultHandler),
], debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='8888')

if __name__ == '__main__':
    main()
