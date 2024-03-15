from flask import Flask, render_template, jsonify, request

inmemorydataservice = [
    {'id': 12, 'name': 'Dr. Nice'},
    {'id': 13, 'name': 'Bombasto'},
    {'id': 14, 'name': 'Celeritas'},
    {'id': 15, 'name': 'Magneta'},
    {'id': 16, 'name': 'RubberMan'},
    {'id': 17, 'name': 'Dynama'},
    {'id': 18, 'name': 'Dr. IQ'},
    {'id': 19, 'name': 'Magma'},
    {'id': 20, 'name': 'Tornado'},
]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/heroes')
def get_heroes():
    return jsonify(inmemorydataservice)

@app.route('/api/heroes/<int:hero_id>')
def get_hero(hero_id):
    hero = next((hero for hero in inmemorydataservice if hero['id'] == hero_id), None)
    if hero is None:
        return jsonify({'error': 'Hero not found'}), 404
    return jsonify(hero)

@app.route('/api/heroes/<int:hero_id>', methods=['PUT'])
def update_hero(hero_id):
    data = request.get_json()
    hero = next((hero for hero in inmemorydataservice if hero['id'] == hero_id), None)
    if hero is None:
        return jsonify({'error': 'Hero not found'}), 404
    hero['name'] = data.get('name', hero['name'])
    return jsonify(hero)

@app.route('/api/heroes/<int:hero_id>', methods=['DELETE'])
def delete_hero(hero_id):
    global inmemorydataservice
    inmemorydataservice = [hero for hero in inmemorydataservice if hero['id'] != hero_id]
    return jsonify({'message': 'Hero deleted'})

@app.route('/api/heroes', methods=['POST'])
def add_hero():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    new_hero = {
        'id': max(hero['id'] for hero in inmemorydataservice) + 1,
        'name': data['name']
    }
    inmemorydataservice.append(new_hero)
    return jsonify(new_hero), 201

if __name__ == '__main__':
    app.run()
