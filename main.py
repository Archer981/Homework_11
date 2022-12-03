from flask import Flask, render_template
from utils import *


app = Flask(__name__)


PATH = 'https://www.jsonkeeper.com/b/RQR9'
candidates = load_candidates_from_json(PATH)


@app.route('/')
def index_page():
    return render_template('index.html', candidates=candidates)


@app.route('/candidate/<int:pk>')
def single_page(pk):
    return render_template('single.html', candidate=get_candidate(pk, candidates))


@app.route('/search/<candidate_name>')
def search_page(candidate_name):
    search_results = get_candidates_by_name(candidate_name, candidates)
    quantity = len(search_results)
    return render_template('search.html', candidates=search_results, quantity=quantity)


@app.route('/skill/<skill_name>')
def skill_page(skill_name):
    search_results = get_candidates_by_skill(skill_name, candidates)
    quantity = len(search_results)
    return render_template('skill.html', candidates=search_results, quantity=quantity)


app.run()
