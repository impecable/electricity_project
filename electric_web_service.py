from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

products = []

class Device(Resource):
    def get(self,device_id):
        device = next(filter(lambda x: x['device_id'] == device_id, products), None)
        return {'device': device}, 200 if device else 404

    def post(self,device_id):
        device = {'device_name': 'sevket', 'device_id': device_id, 'status': False, 'alarm': False}
        products.append(device)
        return device, 201

    def put(self, device_id):
        request_data = request.get_json()
        alarm = request_data['alarm']
        status = request_data['status']
        device_name = request_data['device_name']
        device = next(filter(lambda x:x['device_id'] == device_id, products), None)
        products.remove(device)
        device = {'device_id': device_id, 'device_name': device_name, 'status': status, 'alarm': alarm}
        products.append(device)
        print(device)
        return device



class DeviceList(Resource):
    def get(self):
        return{'products':products}


api.add_resource(Device, '/products/<string:device_id>')
api.add_resource(DeviceList, '/devicesList')


app.run(port = 5000)
