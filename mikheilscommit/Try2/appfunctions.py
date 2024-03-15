@app.route("/index"), methods=['GET','POST'])
def home():
    pass
    elif request.form.get('action').startswith('delete'):
            asset_id = request.form.get('action')[6:]
            response = deleteAsset(asset_id, path)
    


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template(
        'home.html',
        currentUser = currentUser
    )



#deletehero
#gethero
