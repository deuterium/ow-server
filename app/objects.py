from ares import CVESearch
from flask_restful import Resource

class CVEVendor(Resource):
    def get(self):
        cve = CVESearch()
        return cve.browse('microsoft')

class CVEProduct(Resource):
    def get(self, product_id):
        cve = CVESearch()
        return cve.search("microsoft/{}".format(product_id))

class CVEID(Resource):
    def get(self, cve_id):
        cve = CVESearch()
        return cve.id("{}".format(cve_id))