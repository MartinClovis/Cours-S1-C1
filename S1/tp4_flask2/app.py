from flask import Flask, request, render_template, redirect, flash

app = Flask(__name__)
app.secret_key = 'une cle(token) : grain de sel(any random string)'
app.config["TEMPLATES_AUTO_RELOAD"] = True

liste_etudiants = [
    {'id':'1','nom':'tom', 'groupe_id':'1'},
    {'id':'2','nom':'enzo', 'groupe_id':'1'},
    {'id':'3','nom':'laurence', 'groupe_id':'2'},
    {'id':'4','nom':'theo', 'groupe_id':'2'},
    {'id':'5','nom':'mehdi', 'groupe_id':'3'}
]

liste_groupes = [
    {'id': '1', 'libelle': 'A1'},
    {'id': '2', 'libelle': 'A2'},
    {'id': '3', 'libelle': 'B1'},
    {'id': '4', 'libelle': 'B2'}
]


@app.route('/')
@app.route('/etudiant/show')
def show_etudiants():
    return render_template('etudiant/show_etudiant.html', etudiants=liste_etudiants )

@app.route('/etudiant/add', methods=['GET'])
def add_etudiant():
    print('''affichage du formulaire pour saisir un étudiant''')
    return render_template('etudiant/add_etudiant.html', groupes=liste_groupes)

@app.route('/etudiant/delete')
def delete_etudiant():
    print('''suppression d'un étudiant''')
    id = request.args.get('id')
    message = 'Suppression de  l\'étudiant d\'identifiant :' + id
    print(message)
    flash(message, 'alert-warning')
    return redirect('/etudiant/show')

@app.route('/etudiant/edit', methods=['GET'])
def edit_etudiant():
    print('''affichage du formulaire pour modifier un étudiant''')
    id=request.args.get('id')
    if id != None and id.isnumeric():
        indice = int(id)
        etudiant=liste_etudiants[indice-1]
    else:
        etudiant=[]
    return render_template('etudiant/edit_etudiant.html', etudiant=etudiant, groupes=liste_groupes)
@app.route('/etudiant/add', methods=['POST'])
def valid_add_etudiant():
    print('''ajout de l'étudiant dans le tableau''')
    nom = request.form.get('nom')
    id_groupe = request.form.get('id_groupe')
    message = 'Ajout d\'un étudiant de nom :' + nom + ' - id_groupe :' + id_groupe
    print(message)
    flash(message, 'alert-success')
    return redirect('/etudiant/show')

@app.route('/etudiant/edit', methods=['POST'])
def valid_edit_etudiant():
    print('''modification de l'étudiant dans le tableau''')
    id = request.form.get('id')
    nom = request.form.get('nom')
    id_groupe = request.form.get('id_groupe')
    message = 'Modification du nom :' + nom + ' - id_groupe :' + id_groupe + ' pour l\'étudiant d\'identifiant :' + id
    print(message)
    flash(message, 'alert-success')
    return redirect('/etudiant/show')

if __name__ == '__main__':
    app.run(debug=True, port=5000)