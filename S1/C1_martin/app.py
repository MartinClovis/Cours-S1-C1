from flask import Flask, request, render_template, redirect, flash

app = Flask(__name__)
app.secret_key = 'une cle(token) : grain de sel(any random string)'
app.config["TEMPLATES_AUTO_RELOAD"] = True

typeCommercants = [
    {'id':1,'libelleType':'Boucherie'},
    {'id':2,'libelleType':'Boulangerie'},
    {'id':3,'libelleType':'Maraicher'},
    {'id':4,'libelleType':'Fromagerie'}
]
commercants=[
    {'id':1,'nomCommercant':'Boucherie Rousselet', 'dateInstallation':'2010-1-1','prixLocation':'500', 'adresse':'marché des vosges' ,'typeCommercant_id' :1,'image': 'boucherie_rousselet.jpg'},
    {'id':2,'nomCommercant':'Boulanger Peslier', 'dateInstallation':'2009-1-1','prixLocation':'600', 'adresse':'marché des vosges' ,'typeCommercant_id' :2,'image': 'boulanger_peslier.jpg'},
    {'id':3,'nomCommercant':'Patisserie Perez', 'dateInstallation':'2014-1-1','prixLocation':'600', 'adresse':'marché des vosges' ,'typeCommercant_id' :2,'image': 'patisserie_perez.jpg'},
    {'id':4,'nomCommercant':'Maraicher Ravier', 'dateInstallation':'2014-1-1','prixLocation':'600', 'adresse':'marché des vosges' ,'typeCommercant_id' :3,'image': 'maraicher_ravier.jpg'},
    {'id':5,'nomCommercant':'Bon Pain Woltz', 'dateInstallation':'2013-1-1','prixLocation':'700', 'adresse':'marché des vosges' ,'typeCommercant_id' :2,'image': 'bon_pain_woltz.jpg'},
    {'id':6,'nomCommercant':'Caly Maraicher', 'dateInstallation':'2014-1-1','prixLocation':'600', 'adresse':'marché des vosges' ,'typeCommercant_id' :3,'image': 'caly_maraicher.jpg'},
    {'id':7,'nomCommercant':'Boucherie Caly', 'dateInstallation':'2013-1-1','prixLocation':'600', 'adresse':'marché des vosges' ,'typeCommercant_id' :1,'image': 'boucherie_caly.jpg'},
    {'id':8,'nomCommercant':'Fromagerie mervant', 'dateInstallation':'2013-1-1','prixLocation':'600', 'adresse':'marché des vosges' ,'typeCommercant_id' :4,'image': 'fromagerie_mervant.jpg'},
    {'id':9,'nomCommercant':'Boulangerie Laure', 'dateInstallation':'2013-1-1','prixLocation':'800', 'adresse':'marché des vosges' ,'typeCommercant_id' :2,'image': 'boulangerie_laure.jpg'},
    {'id':10,'nomCommercant':'Boucherie Laurent', 'dateInstallation':'2013-1-1','prixLocation':'800', 'adresse':'marché des vosges' ,'typeCommercant_id' :1,'image': 'boucherie_laurent.jpg'},
    {'id':11,'nomCommercant':'Fromagerie dupuis', 'dateInstallation':'2014-1-1','prixLocation':'600', 'adresse':'marché des vosges' ,'typeCommercant_id' :4,'image': 'fromagerie_dupuis.jpg'}
]

types = typeCommercants.copy()
commercantsActifs = commercants.copy()


@app.route('/', methods=['GET'])
def show_layout():
    return render_template('layout.html')

@app.route('/type-commercant/show', methods=['GET'])
def show_type_commercant():
    return render_template('type_commercant/show_type_commercant.html', types=types)

@app.route('/type-commercant/add', methods=['GET'])
def add_type_commercant():
    return render_template('type_commercant/add_type_commercant.html')

@app.route('/type-commercant/add', methods=['POST'])
def valid_add_type_commercant():
    libelle = request.form.get('libelleType', '').strip()
    flash('Ajout type_commercant : ' + libelle, 'alert-success')
    return redirect('/type-commercant/show')

@app.route('/type-commercant/delete', methods=['GET'])
def delete_type_commercant():
    identifiant = request.args.get('id', type=int)
    libelle = types[identifiant - 1]['libelleType']
    flash('Suppression type_commercant : ' + libelle + ' - id : ' + str(identifiant), 'alert-warning')
    return redirect('/type-commercant/show')

@app.route('/type-commercant/edit', methods=['GET'])
def edit_type_commercant():
    identifiant = request.args.get('id', type=int)
    type_obj = types[identifiant - 1]
    return render_template('type_commercant/edit_type_commercant.html', type_obj=type_obj)

@app.route('/type-commercant/edit', methods=['POST'])
def valid_edit_type_commercant():
    identifiant = request.form.get('id', type=int)
    libelle = request.form.get('libelleType', '').strip()
    flash('Modification type_commercant : ' + libelle + ' - id : ' + str(identifiant), 'alert-success')
    return redirect('/type-commercant/show')

@app.route('/commercant/show', methods=['GET'])
def show_commercant():
    return render_template('commercant/show_commercant.html', commercants=commercantsActifs, types=types)

@app.route('/commercant/add', methods=['GET'])
def add_commercant():
    return render_template('commercant/add_commercant.html', types=types)

@app.route('/commercant/add', methods=['POST'])
def valid_add_commercant():
    nom = request.form.get('nomCommercant', '').strip()
    type_id = request.form.get('typeCommercant_id', type=int)
    flash('Ajout commercant : ' + nom + ' - typeCommercant_id : ' + str(type_id)
          + ' - dateInstallation : ' + request.form.get('dateInstallation', '')
          + ' - prixLocation : ' + request.form.get('prixLocation', '')
          + ' - adresse : ' + request.form.get('adresse', '')
          + ' - image : ' + request.form.get('image', ''), 'alert-success')
    return redirect('/commercant/show')

@app.route('/commercant/delete', methods=['GET'])
def delete_commercant():
    identifiant = request.args.get('id', type=int)
    commercant = commercantsActifs[identifiant - 1]
    message = ('Suppression commercant : ' + commercant['nomCommercant']
               + ' - typeCommercant_id : ' + str(commercant['typeCommercant_id'])
               + ' - dateInstallation : ' + commercant['dateInstallation']
               + ' - prixLocation : ' + commercant['prixLocation']
               + ' - adresse : ' + commercant['adresse']
               + ' - image : ' + commercant['image']
               + ' - id : ' + str(identifiant))
    flash(message, 'alert-warning')
    return redirect('/commercant/show')

@app.route('/commercant/edit', methods=['GET'])
def edit_commercant():
    identifiant = request.args.get('id', type=int)
    commercant = commercantsActifs[identifiant - 1]
    return render_template('commercant/edit_commercant.html', commercant=commercant, types=types)

@app.route('/commercant/edit', methods=['POST'])
def valid_edit_commercant():
    identifiant = request.form.get('id', type=int)
    nom = request.form.get('nomCommercant', '').strip()
    type_id = request.form.get('typeCommercant_id', type=int)
    date_installation = request.form.get('dateInstallation', '')
    prix_location = request.form.get('prixLocation', '')
    adresse = request.form.get('adresse', '')
    image = request.form.get('image', '')
    flash('Modification commercant : ' + nom + ' - typeCommercant_id : ' + str(type_id)
          + ' - dateInstallation : ' + date_installation
          + ' - prixLocation : ' + prix_location
          + ' - adresse : ' + adresse
          + ' - image : ' + image
          + ' - id : ' + str(identifiant), 'alert-success')
    return redirect('/commercant/show')

@app.route('/commercant/filtre', methods=['GET'])
def filtre_commercant():
    return render_template('commercant/filtre_commercant.html',
                           commercants=commercantsActifs, types=types)


@app.route('/commercant/filtre', methods=['POST'])
def valid_filtre_commercant():
    types_choisis = request.form.getlist('typeCommercant_id')
    prix = request.form.get('prixLocation', '')
    nom = request.form.get('nomCommercant', '')
    flash('Filtre commercant : typeCommercant_id : ' + ', '.join(types_choisis)
          + ' - prixLocation : ' + prix + ' - nomCommercant : ' + nom, 'alert-info')
    return redirect('/commercant/filtre')


