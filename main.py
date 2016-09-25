import iam_service
import logging
import webapp2


class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
 
        logging.info('>>>>> aaaaa')

        project_id = 'henry-dev'
        service_account_id = 'test123@henry-dev.iam.gserviceaccount.com'

        result = iam_service.list_keys(project_id, service_account_id)

        key_names = ''
        #for key in result['keys']:
        #	key_names += key['name'] + '<br>'

        self.response.out.write('helloaaaaa<br>' + key_names)


class ServiceAccountHandler(webapp2.RequestHandler):
    def get(self):
 
        service_account = iam_service.get_service_account()

        self.response.out.write('hello service account<br>' + service_account)





app = webapp2.WSGIApplication([
    ('/service_account', ServiceAccountHandler),
    ('/', HelloWebapp2),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='8888')

if __name__ == '__main__':
    main()

