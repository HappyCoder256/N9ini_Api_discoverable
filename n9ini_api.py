from flask import Flask, jsonify, request#, render_template_string
import pyodbc#, re
from flask_cors import CORS
#from bs4 import BeautifulSoup
#import threading#jsbeautifier, 
server = r'DESKTOP-IQTRCDN\SYLLABUS_RUTHORO'#"192.168.43.204"##"192.168.43.204""108.181.157.244"
database = 'Syllabus_Trans'
username = 'Syllabus_Origin'
password = 'client0'
driver= '{ODBC Driver 18 for SQL Server}'
#global conn
#conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';port=1433;MARS_Connection=yes;DATABASE='+database+';UID='+username+';PWD='+password+';Query Timeout=30;trustServerCertificate=yes;Encrypt=yes')
app = Flask(__name__)
CORS(app)
app.json.sort_keys = False
@app.route('/movie/featured', methods=['GET'])
def feauteds():
    try:
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';port=1433;MARS_Connection=yes;DATABASE='+database+';UID='+username+';PWD='+password+';Query Timeout=30;trustServerCertificate=yes;Encrypt=yes') as conn:
            with conn.cursor() as ludad1:
                query = """
                    SELECT id, movie_name, cover_poster, translator, year, poster
                    FROM featured_trans ORDER BY NEWID()
                """
                rum = ludad1.execute(query)
                movies = rum.fetchmany(25)
                dogi = []
                for movie in movies:
                    dogi.append({
                        "id":movie[0],
                        "movie_name":movie[1],
                        "cover_poster":movie[2],
                        "translator":movie[3],
                        "year":movie[4],
                        "main_poster":movie[5]
                    })
            return jsonify(dogi), 200
    except pyodbc.Error as numba1:
        ruty = []
        return ruty, 400
@app.route('/movie/latest_mov', methods=['GET'])
def latests_mov():
    try:
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';port=1433;MARS_Connection=yes;DATABASE='+database+';UID='+username+';PWD='+password+';Query Timeout=30;trustServerCertificate=yes;Encrypt=yes') as conn:
            with conn.cursor() as ludad2:
                query = """
                    SELECT id, movie_name, cover_poster, translator, year, poster
                    FROM all_translated WHERE year = 2024 ORDER BY NEWID()
                """
                try:
                    rum = ludad2.execute(query)
                except:
                    rum = ludad2.execute(query)
                movies = rum.fetchmany(25)
                dogi = []
                for movie in movies:
                    dogi.append({
                        "id":movie[0],
                        "movie_name":movie[1],
                        "cover_poster":movie[2],
                        "translator":movie[3],
                        "year":movie[4],
                        "main_poster":movie[5]
                    })
            return jsonify(dogi), 200
    except pyodbc.Error as numba1:
        ruty = []
        return ruty, 400
@app.route('/movie/latest_series', methods=['GET'])
def latests_series():
    try:
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';port=1433;MARS_Connection=yes;DATABASE='+database+';UID='+username+';PWD='+password+';Query Timeout=30;trustServerCertificate=yes;Encrypt=yes') as conn:
            with conn.cursor() as ludad3:
                query = """
                    SELECT id, movie_name, cover_poster, translator, year, poster
                    FROM all_series_translated WHERE year >= 2015 ORDER BY NEWID()
                """
                try:
                    rum = ludad3.execute(query)
                except:
                    rum = ludad3.execute(query)
                movies = rum.fetchmany(25)
                dogi = []
                for movie in movies:
                    dogi.append({
                        "id":movie[0],
                        "movie_name":movie[1],
                        "cover_poster":movie[2],
                        "translator":movie[3],
                        "year":movie[4],
                        "main_poster":movie[5]
                    })
            return jsonify(dogi), 200
    except pyodbc.Error as numba1:
        ruty = []
        return ruty, 400
@app.route('/movie/most_rated', methods=['GET'])
def most_rated():
    try:
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';port=1433;MARS_Connection=yes;DATABASE='+database+';UID='+username+';PWD='+password+';Query Timeout=30;trustServerCertificate=yes;Encrypt=yes') as conn:
            with conn.cursor() as ludad4:
                query = """
                    SELECT id, movie_name, cover_poster, translator, year, poster
                    FROM all_series_translated ORDER BY tmdb_id DESC
                """
                try:
                    rum = ludad4.execute(query)
                except:
                    rum = ludad4.execute(query)
                movies = rum.fetchmany(25)
                dogi = []
                for movie in movies:
                    dogi.append({
                        "id":movie[0],
                        "movie_name":movie[1],
                        "cover_poster":movie[2],
                        "translator":movie[3],
                        "year":movie[4],
                        "main_poster":movie[5]
                    })
            return jsonify(dogi), 200
    except pyodbc.Error as numba1:
        ruty = []
        return ruty, 400
@app.route('/movie/search/<string:luca>', methods=['GET'])
def searcher(luca):
    try:
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';port=1433;MARS_Connection=yes;DATABASE='+database+';UID='+username+';PWD='+password+';Query Timeout=30;trustServerCertificate=yes;Encrypt=yes') as conn:
            with conn.cursor() as ludad5:
                query = """
                    SELECT movie_name, poster, translator, year, id
                    FROM all_translated 
                    WHERE movie_name LIKE ? 
                    OR movie_name LIKE ? 
                    OR movie_name LIKE ? 
                    OR movie_name LIKE ?
                """
                
                # Format the parameter values for LIKE
                movie_q1 = f'%{luca} %'
                movie_q2 = f'% {luca} %'
                movie_q3 = f'% {luca}%'
                movie_q4 = f'%{luca}%'
                
                # Execute the query with parameters
                try:
                    rum = ludad5.execute(query, (movie_q1, movie_q2, movie_q3, movie_q4))
                except:
                    rum = ludad5.execute(query, (movie_q1, movie_q2, movie_q3, movie_q4))      
                if len(luca) <= 2:     
                    movies = rum.fetchmany(75)
                else:
                    movies = rum.fetchmany(100)
                dogi = []
                for movie in movies:
                    dogi.append({
                        "movie_name":movie[0],
                        "main_poster":movie[1],
                        "translator":movie[2],
                        "year":movie[3],
                        "Syllabus_id":movie[4]
                    })
            return jsonify(dogi), 200
    except pyodbc.Error as numba1:
        ruty = []
        return ruty, 400
@app.route('/movie/movies_load', methods=['GET'])
def movies_load():
    try:
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';port=1433;MARS_Connection=yes;DATABASE='+database+';UID='+username+';PWD='+password+';Query Timeout=30;trustServerCertificate=yes;Encrypt=yes') as conn:
            with conn.cursor() as ludad4:
                query = """
                    SELECT id, movie_name, cover_poster, translator, year, poster
                    FROM all_translated ORDER BY NEWID()
                """
                try:
                    rum = ludad4.execute(query)
                except:
                    rum = ludad4.execute(query)
                movies = rum.fetchmany(300)
                dogi = []
                for movie in movies:
                    dogi.append({
                        "id":movie[0],
                        "movie_name":movie[1],
                        "cover_poster":movie[2],
                        "translator":movie[3],
                        "year":movie[4],
                        "main_poster":movie[5]
                    })
            return jsonify(dogi), 200
    except pyodbc.Error as numba1:
        ruty = []
        return ruty, 400
@app.route('/movie/details/<int:mov_id>', methods=['GET'])
def movie_desc_load(mov_id):
    try:
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';port=1433;MARS_Connection=yes;DATABASE='+database+';UID='+username+';PWD='+password+';Query Timeout=30;trustServerCertificate=yes;Encrypt=yes') as conn:
            with conn.cursor() as ludad4:
                query = """
                    SELECT poster, file_id, sizes, title, Imdb_rate, all_genres, length, translator, budget, revenue, description, cast, main_genre, imdb_id, tmdb_id, year_of_release
                    FROM main_description_translated WHERE movie_id = ?
                """
                rum = ludad4.execute(query, mov_id)
                movi_det = rum.fetchmany(1)
                try:
                    tmdb_ider = movi_det[0][14]
                except IndexError as jdsk:
                    tmdb_ider = "Not_Available"
                try:
                    imdb_ider = movi_det[0][13]
                except IndexError as jdsk:
                    imdb_ider = "11111111111111"
                    
                #Lucana
                sql_query = """SELECT id, translator, movie_name, year, poster FROM all_translated WITH (READPAST) WHERE tmdb_id = ? OR imdb_id = ? ORDER BY NEWID()"""
                ludad4.execute(sql_query, tmdb_ider, imdb_ider)
                ruthoros = ludad4.fetchall()
                #Luthano
                sql_query = """SELECT sequel FROM all_translated WHERE id = ?"""
                ludad4.execute(sql_query, mov_id)
                ruthoros4 = ludad4.fetchall()
                #################
                dogi = {}
                for movie in movi_det:
                    scuta = ((str(movie[4])).replace(" ", ""))
                    try:
                        mufanne = int(movie[15])
                    except:
                        mufanne = (movie[15])[:4]
                    smav = (str(mufanne).replace(" ", ""))
                    sudo = (str(movie[2]).replace(" ", ""))
                    sudo1 = sudo.replace("\n", "")
                    sudo2 = sudo1.replace("\\", "")
                    dogi.update({
                        "poster":movie[0],
                        "file_code":movie[1],
                        "size":sudo2,
                        "title":movie[3],
                        "tmdb_id":"Not_Available",
                        "imdb_id":"Not_Available",
                        "imdb_rate":scuta,
                        "all_genres":movie[5],
                        "length":movie[6],
                        "translator":movie[7],
                        "year_of_release":int(smav),
                        "budget":movie[8],
                        "revenue":movie[9],
                        "description":movie[10],
                        "cast":movie[11],
                        "main_genre":movie[12],
                        "Alternatives":"Not_Available",
                        "Parts":"Not_Available"
                    })
                lugas = []
                dogi.update({
                    "tmdb_id":movi_det[0][14],
                    "imdb_id":movi_det[0][13]
                })
                #print(ruthoros)
                for movi in ruthoros:
                    id2 = movi[0]
                    trsnl = movi[1]
                    name_t = movi[2]
                    year = movi[3]
                    post = movi[4]
                    if id2 != mov_id:
                        lugas.append({
                            "Movie_id":id2,
                            "Translator":f"{trsnl}",
                            "Title":f"{name_t}",
                            "year":year,
                            "poster":post
                        })
                if lugas is not None:
                    dogi.update(
                        {"Alternatives":lugas}
                    )
                if ruthoros4 is not None:
                    bup = []
                    sql_query = """SELECT id, translator, movie_name, year, poster FROM all_translated WHERE sequel = ? ORDER BY NEWID()"""
                    ludad4.execute(sql_query, str(ruthoros4[0][0]))
                    ruthorosas = ludad4.fetchall()
                    for movie in ruthorosas:
                        id2 = movie[0]
                        trsnl = movie[1]
                        name_t = movie[2]
                        year = movie[3]
                        post = movie[4]
                        if id2 != mov_id:
                            bup.append({
                                "Movie_id":id2,
                                "Translator":f"{trsnl}",
                                "Title":f"{name_t}",
                                "year":year,
                                "poster":post
                            })
                    if bup is not None:
                        dogi.update(
                            {"Parts":bup}
                        )
            return jsonify(dogi), 200
    except pyodbc.Error as numba1:
        ruty = str(numba1)
        return ruty, 400
@app.route('/movie/genre/<string:genre_ide>', methods=['GET'])
def genre_load(genre_ide):
    mny = request.args.get('many', type=int)
    try:
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';port=1433;MARS_Connection=yes;DATABASE='+database+';UID='+username+';PWD='+password+';Query Timeout=30;trustServerCertificate=yes;Encrypt=yes') as conn:
            with conn.cursor() as ludad4:
                query = """
                    SELECT movie_id, title, backdrop, translator, tmdb_id, poster, year_of_release
                    FROM main_description_translated WHERE main_genre = ? ORDER BY NEWID()
                """
                rum = ludad4.execute(query, genre_ide)
                if mny >= 1:
                    movies = rum.fetchmany(100)
                else:
                    movies = rum.fetchmany(30)
                dogi = []
                for movie in movies:
                    try:
                        lupa = int(movie[6])
                    except:
                        lupa = (movie[6])[:4]
                    dogi.append({
                        "id":movie[0],
                        "movie_name":movie[1],
                        "cover_poster":movie[2],
                        "translator":movie[3],
                        "year":int(lupa),
                        "main_poster":movie[5]
                    })
            return jsonify(dogi), 200
    except pyodbc.Error as numba1:
        ruty = []
        return ruty, 400
@app.route('/movie/search/adv/<string:luca>', methods=['GET'])
def searcher2(luca):
    try:
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';port=1433;MARS_Connection=yes;DATABASE='+database+';UID='+username+';PWD='+password+';Query Timeout=30;trustServerCertificate=yes;Encrypt=yes') as conn:
            with conn.cursor() as ludad5:
                query = """
                    SELECT movie_name, translator, year, id
                    FROM all_translated 
                    WHERE movie_name LIKE ? 
                    OR movie_name LIKE ? 
                    OR movie_name LIKE ? 
                    OR movie_name LIKE ?
                """
                
                # Format the parameter values for LIKE
                movie_q1 = f'%{luca} %'
                movie_q2 = f'% {luca} %'
                movie_q3 = f'% {luca}%'
                movie_q4 = f'%{luca}%'
                
                # Execute the query with parameters
                try:
                    rum = ludad5.execute(query, (movie_q1, movie_q2, movie_q3, movie_q4))
                except:
                    rum = ludad5.execute(query, (movie_q1, movie_q2, movie_q3, movie_q4))      
                if len(luca) <= 2:     
                    movies = rum.fetchmany(12)
                else:
                    movies = rum.fetchmany(15)
                dogi = []
                for movie in movies:
                    dogi.append({
                        "movie_name":movie[0],
                        "translator":movie[1],
                        "year":movie[2],
                        "movie_id":movie[3]
                    })
            return jsonify(dogi), 200
    except pyodbc.Error as numba1:
        ruty = []
        return ruty, 400
@app.route('/vjs/list/', methods=['GET'])
def vjs_listing():
    try:
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';port=1433;MARS_Connection=yes;DATABASE='+database+';UID='+username+';PWD='+password+';Query Timeout=30;trustServerCertificate=yes;Encrypt=yes') as conn:
            with conn.cursor() as ludad5:
                ludad5.execute("SELECT DISTINCT translator FROM all_translated")
                vjson = ludad5.fetchmany(50)
                if not vjson:
                    messo = {
                        "message":"An error occurred while trying to respond to your request. Please use this format. (http://n9ini.vjs.com/all_vjs/list). If you repeatedly encounter error related to this, Please contact the Admin for more assistance",
                        "Status_code":"400 - No resource was supplied"
                    }
                    return jsonify(messo), 400
                else:
                    diban = []
                    for vj in vjson:
                        trsnl = vj[0]
                        rubra = f"{trsnl}".replace(" ","_")
                        diban.append({
                            "Name":f"{trsnl}",
                            "url":f"ttps://accurate-urchin-warm.ngrok-free.app/{rubra}/listmovies"
                        })
                    return jsonify(diban), 200
    except BaseException as lugemwa:
        diban = []
        diban.append({
            "Error":f"Database Error: {lugemwa}",
            "message":"Couldn't fetch results from main server. Contact the Happy Coders Team for more help"
        })
        return jsonify(diban), 200
@app.route('/genres/list/', methods=['GET'])
def genre_listing():
    try:
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';port=1433;MARS_Connection=yes;DATABASE='+database+';UID='+username+';PWD='+password+';Query Timeout=30;trustServerCertificate=yes;Encrypt=yes') as conn:
            with conn.cursor() as ludad5:
                ludad5.execute("SELECT DISTINCT main_genre FROM main_description_translated")
                vjson = ludad5.fetchmany(50)
                if not vjson:
                    messo = {
                        "message":"An error occurred while trying to respond to your request. Please use this format. (http://n9ini.vjs.com/all_vjs/list). If you repeatedly encounter error related to this, Please contact the Admin for more assistance",
                        "Status_code":"400 - No resource was supplied"
                    }
                    return jsonify(messo), 400
                else:
                    diban = []
                    for vj in vjson:
                        trsnl = vj[0]
                        rubra = f"{trsnl}".replace(" ","_")
                        diban.append({
                            "Genre":f"{trsnl}",
                            "url":f"ttps://accurate-urchin-warm.ngrok-free.app/genre/{rubra}/listmovies"
                        })
                    return jsonify(diban), 200
    except BaseException as lugemwa:
        diban = []
        diban.append({
            "Error":f"Database Error: {lugemwa}",
            "message":"Couldn't fetch results from main server. Contact the Happy Coders Team for more help"
        })
        return jsonify(diban), 200
@app.route('/<string:vj_name>/listmovies', methods=['GET'])
def listing_movies_vj(vj_name):
    try:
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';port=1433;MARS_Connection=yes;DATABASE='+database+';UID='+username+';PWD='+password+';Query Timeout=30;trustServerCertificate=yes;Encrypt=yes') as conn:
            with conn.cursor() as ludad4:
                vj_name = vj_name.replace("_", " ")
                query = """
                    SELECT id, movie_name, cover_poster, translator, year, poster
                    FROM all_translated WHERE translator = ? ORDER BY tmdb_id DESC
                """
                try:
                    rum = ludad4.execute(query, vj_name)
                except:
                    rum = ludad4.execute(query, vj_name)
                movies = rum.fetchmany(300)
                dogi = []
                for movie in movies:
                    dogi.append({
                        "id":movie[0],
                        "movie_name":movie[1],
                        "cover_poster":movie[2],
                        "translator":movie[3],
                        "year":movie[4],
                        "main_poster":movie[5]
                    })
            return jsonify(dogi), 200
    except pyodbc.Error as numba1:
        ruty = []
        return ruty, 400
@app.route('/genre/<string:genre_name>/listmovies', methods=['GET'])
def listing_movies_genres(genre_name):
    try:
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';port=1433;MARS_Connection=yes;DATABASE='+database+';UID='+username+';PWD='+password+';Query Timeout=30;trustServerCertificate=yes;Encrypt=yes') as conn:
            with conn.cursor() as ludad4:
                #vj_name = vj_name.replace("_", " ")
                query = """
                    SELECT movie_id, title, backdrop, translator, year_of_release, poster
                    FROM main_description_translated WHERE main_genre = ? ORDER BY tmdb_id DESC
                """
                try:
                    rum = ludad4.execute(query, genre_name)
                except:
                    rum = ludad4.execute(query, genre_name)
                movies = rum.fetchmany(400)
                dogi = []
                for movie in movies:
                    dogi.append({
                        "id":movie[0],
                        "movie_name":movie[1],
                        "cover_poster":movie[2],
                        "translator":movie[3],
                        "year":movie[4],
                        "main_poster":movie[5]
                    })
            return jsonify(dogi), 200
    except pyodbc.Error as numba1:
        ruty = []
        return ruty, 400
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)